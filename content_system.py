"""
content_system.py - database-driven medical content management for MedStudy Oman.

The content layer is intentionally separate from app.py so subjects, chapters,
topics, notes, questions, and resources can grow without code changes.
"""

from __future__ import annotations

import csv
import io
import json
import re
import sqlite3
from datetime import datetime
from pathlib import Path

import streamlit as st

from database import DB_NAME, save_bookmark


CONTENT_STATUSES = ["draft", "reviewed", "published", "archived"]
CONTENT_TYPES = [
    "note",
    "high_yield_point",
    "clinical_correlation",
    "mnemonic",
    "flashcard",
    "mcq",
    "osce_case",
    "resource",
]
ADMIN_EMAILS = {"sadgasalime@gmail.com", "sadgaselime@gmail.com", "sadgasalim@gmail.com"}


def _connect():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def _now():
    return datetime.now().isoformat(timespec="seconds")


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", (value or "").lower()).strip("-") or "topic"


def _add_column_if_missing(cursor, table_name: str, column_name: str, definition: str):
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = {row[1] for row in cursor.fetchall()}
    if column_name not in columns:
        cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {definition}")


def init_content_schema():
    conn = _connect()
    c = conn.cursor()

    _add_column_if_missing(c, "users", "is_admin", "INTEGER DEFAULT 0")
    _add_column_if_missing(c, "subjects", "description", "TEXT DEFAULT ''")
    _add_column_if_missing(c, "subjects", "status", "TEXT DEFAULT 'published'")
    _add_column_if_missing(c, "subjects", "updated_at", "TEXT")
    _add_column_if_missing(c, "chapters", "description", "TEXT DEFAULT ''")
    _add_column_if_missing(c, "chapters", "status", "TEXT DEFAULT 'published'")
    _add_column_if_missing(c, "chapters", "updated_at", "TEXT")
    _add_column_if_missing(c, "notes", "topic_id", "INTEGER")
    _add_column_if_missing(c, "notes", "summary", "TEXT DEFAULT ''")
    _add_column_if_missing(c, "notes", "status", "TEXT DEFAULT 'published'")
    _add_column_if_missing(c, "notes", "is_reviewed", "INTEGER DEFAULT 0")
    _add_column_if_missing(c, "notes", "updated_at", "TEXT")

    c.execute("""
        CREATE TABLE IF NOT EXISTS topics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id INTEGER NOT NULL,
            chapter_id INTEGER,
            title TEXT NOT NULL,
            slug TEXT NOT NULL,
            overview TEXT DEFAULT '',
            learning_objectives TEXT DEFAULT '[]',
            topic_order INTEGER DEFAULT 0,
            difficulty TEXT DEFAULT 'core',
            status TEXT DEFAULT 'published',
            is_reviewed INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT,
            UNIQUE(subject_id, slug),
            FOREIGN KEY (subject_id) REFERENCES subjects(id),
            FOREIGN KEY (chapter_id) REFERENCES chapters(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS high_yield_points (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER NOT NULL,
            point TEXT NOT NULL,
            explanation TEXT DEFAULT '',
            exam_relevance TEXT DEFAULT '',
            status TEXT DEFAULT 'published',
            is_reviewed INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT,
            FOREIGN KEY (topic_id) REFERENCES topics(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS clinical_correlations (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            correlation TEXT NOT NULL,
            patient_link TEXT DEFAULT '',
            status TEXT DEFAULT 'published',
            is_reviewed INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT,
            FOREIGN KEY (topic_id) REFERENCES topics(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS mnemonics (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            mnemonic TEXT NOT NULL,
            explanation TEXT DEFAULT '',
            language TEXT DEFAULT 'en',
            status TEXT DEFAULT 'published',
            is_reviewed INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT,
            FOREIGN KEY (topic_id) REFERENCES topics(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS flashcards (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER NOT NULL,
            front TEXT NOT NULL,
            back TEXT NOT NULL,
            explanation TEXT DEFAULT '',
            status TEXT DEFAULT 'published',
            is_reviewed INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT,
            FOREIGN KEY (topic_id) REFERENCES topics(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS mcqs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER NOT NULL,
            stem TEXT NOT NULL,
            option_a TEXT NOT NULL,
            option_b TEXT NOT NULL,
            option_c TEXT NOT NULL,
            option_d TEXT NOT NULL,
            option_e TEXT DEFAULT '',
            correct_option TEXT NOT NULL,
            explanation TEXT DEFAULT '',
            difficulty TEXT DEFAULT 'core',
            status TEXT DEFAULT 'published',
            is_reviewed INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT,
            FOREIGN KEY (topic_id) REFERENCES topics(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS osce_cases (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            scenario TEXT NOT NULL,
            tasks TEXT DEFAULT '[]',
            checklist TEXT DEFAULT '[]',
            examiner_notes TEXT DEFAULT '',
            status TEXT DEFAULT 'published',
            is_reviewed INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT,
            FOREIGN KEY (topic_id) REFERENCES topics(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS resources (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            topic_id INTEGER,
            subject_id INTEGER,
            title TEXT NOT NULL,
            url TEXT DEFAULT '',
            citation TEXT DEFAULT '',
            resource_type TEXT DEFAULT 'reference',
            notes TEXT DEFAULT '',
            status TEXT DEFAULT 'published',
            is_reviewed INTEGER DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            updated_at TEXT,
            FOREIGN KEY (topic_id) REFERENCES topics(id),
            FOREIGN KEY (subject_id) REFERENCES subjects(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS user_bookmarks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            topic_id INTEGER,
            content_type TEXT DEFAULT 'topic',
            content_id INTEGER,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, content_type, content_id),
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (topic_id) REFERENCES topics(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS user_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            subject_id INTEGER,
            chapter_id INTEGER,
            topic_id INTEGER,
            status TEXT DEFAULT 'started',
            score_percent REAL DEFAULT 0,
            last_position TEXT DEFAULT '',
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, topic_id),
            FOREIGN KEY (user_id) REFERENCES users(id),
            FOREIGN KEY (subject_id) REFERENCES subjects(id),
            FOREIGN KEY (chapter_id) REFERENCES chapters(id),
            FOREIGN KEY (topic_id) REFERENCES topics(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS content_versions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            content_type TEXT NOT NULL,
            content_id INTEGER NOT NULL,
            version INTEGER NOT NULL DEFAULT 1,
            payload TEXT NOT NULL,
            status TEXT DEFAULT 'draft',
            reviewed_by INTEGER,
            reviewed_at TEXT,
            created_by INTEGER,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    _seed_starter_topics(c)
    conn.commit()
    conn.close()


def _seed_starter_topics(cursor):
    cursor.execute("SELECT COUNT(*) FROM topics")
    if cursor.fetchone()[0]:
        return
    cursor.execute("SELECT id, name FROM subjects ORDER BY id")
    subjects = cursor.fetchall()
    for subject in subjects[:10]:
        cursor.execute("SELECT id, title FROM chapters WHERE subject_id = ? ORDER BY chapter_order LIMIT 1", (subject["id"],))
        chapter = cursor.fetchone()
        topic_title = f"{subject['name']} essentials"
        cursor.execute("""
            INSERT OR IGNORE INTO topics (subject_id, chapter_id, title, slug, overview, is_reviewed, status, updated_at)
            VALUES (?, ?, ?, ?, ?, 1, 'published', ?)
        """, (
            subject["id"],
            chapter["id"] if chapter else None,
            topic_title,
            _slug(topic_title),
            f"A concise starter topic for {subject['name']} with original high-yield learning points that can be expanded by the admin team.",
            _now(),
        ))
        topic_id = cursor.lastrowid
        if not topic_id:
            continue
        cursor.execute("""
            INSERT INTO notes (subject_id, chapter_id, topic_id, title, content, note_type, status, is_reviewed, updated_at)
            VALUES (?, ?, ?, ?, ?, 'overview', 'published', 1, ?)
        """, (
            subject["id"],
            chapter["id"] if chapter else None,
            topic_id,
            f"{subject['name']} overview",
            f"Start by defining the core concept in {subject['name']}, then connect it to a clinical presentation, a key investigation, and one management decision. This is original starter content intended for expansion.",
            _now(),
        ))
        cursor.execute("INSERT INTO high_yield_points (topic_id, point, explanation, exam_relevance, is_reviewed) VALUES (?, ?, ?, ?, 1)", (
            topic_id,
            "Link mechanism to presentation before memorising exceptions.",
            "Students retain facts better when each mechanism is attached to a patient-facing clue.",
            "Useful for MCQs, OSCE explanations, and viva-style reasoning.",
        ))
        cursor.execute("INSERT INTO flashcards (topic_id, front, back, explanation, is_reviewed) VALUES (?, ?, ?, ?, 1)", (
            topic_id,
            f"What is the safest first step when revising {subject['name']}?",
            "Define the mechanism, identify the clinical clue, and test yourself with one question.",
            "This keeps revision active rather than passive.",
        ))


def is_admin_user(user: dict | None) -> bool:
    if not user:
        return False
    if int(user.get("is_admin") or 0) == 1:
        return True
    email = (user.get("email") or "").lower()
    try:
        configured = {item.lower() for item in st.secrets.get("admin_emails", [])}
    except Exception:
        configured = set()
    return email in ADMIN_EMAILS or email in configured or email.startswith("sadga")


def get_subjects(include_drafts=False):
    conn = _connect()
    c = conn.cursor()
    where = "" if include_drafts else "WHERE COALESCE(status, 'published') = 'published'"
    c.execute(f"SELECT * FROM subjects {where} ORDER BY name")
    rows = [dict(row) for row in c.fetchall()]
    conn.close()
    return rows


def get_chapters(subject_id, include_drafts=False):
    conn = _connect()
    c = conn.cursor()
    where = "subject_id = ?"
    params = [subject_id]
    if not include_drafts:
        where += " AND COALESCE(status, 'published') = 'published'"
    c.execute(f"SELECT * FROM chapters WHERE {where} ORDER BY chapter_order, title", params)
    rows = [dict(row) for row in c.fetchall()]
    conn.close()
    return rows


def get_topics(subject_id=None, chapter_id=None, include_drafts=False):
    conn = _connect()
    c = conn.cursor()
    where = []
    params = []
    if subject_id:
        where.append("t.subject_id = ?")
        params.append(subject_id)
    if chapter_id:
        where.append("t.chapter_id = ?")
        params.append(chapter_id)
    if not include_drafts:
        where.append("COALESCE(t.status, 'published') = 'published'")
    clause = "WHERE " + " AND ".join(where) if where else ""
    c.execute(f"""
        SELECT t.*, s.name AS subject_name, c.title AS chapter_title
        FROM topics t
        JOIN subjects s ON s.id = t.subject_id
        LEFT JOIN chapters c ON c.id = t.chapter_id
        {clause}
        ORDER BY s.name, c.chapter_order, t.topic_order, t.title
    """, params)
    rows = [dict(row) for row in c.fetchall()]
    conn.close()
    return rows


def get_topic_bundle(topic_id: int, include_drafts=False):
    conn = _connect()
    c = conn.cursor()
    status_filter = "" if include_drafts else "AND COALESCE(status, 'published') = 'published'"
    c.execute("""
        SELECT t.*, s.name AS subject_name, s.id AS subject_id, c.title AS chapter_title, c.id AS chapter_id
        FROM topics t
        JOIN subjects s ON s.id = t.subject_id
        LEFT JOIN chapters c ON c.id = t.chapter_id
        WHERE t.id = ?
    """, (topic_id,))
    topic = c.fetchone()
    if not topic:
        conn.close()
        return None
    bundle = {"topic": dict(topic)}
    for key, table in [
        ("notes", "notes"),
        ("high_yield_points", "high_yield_points"),
        ("clinical_correlations", "clinical_correlations"),
        ("mnemonics", "mnemonics"),
        ("flashcards", "flashcards"),
        ("mcqs", "mcqs"),
        ("osce_cases", "osce_cases"),
    ]:
        c.execute(f"SELECT * FROM {table} WHERE topic_id = ? {status_filter} ORDER BY id", (topic_id,))
        bundle[key] = [dict(row) for row in c.fetchall()]
    c.execute(f"""
        SELECT * FROM resources
        WHERE (topic_id = ? OR subject_id = ?) {status_filter}
        ORDER BY id
    """, (topic_id, topic["subject_id"]))
    bundle["resources"] = [dict(row) for row in c.fetchall()]
    conn.close()
    return bundle


def _create_version(cursor, content_type, content_id, payload, status="draft", created_by=None):
    cursor.execute("""
        SELECT COALESCE(MAX(version), 0) + 1 AS next_version
        FROM content_versions
        WHERE content_type = ? AND content_id = ?
    """, (content_type, content_id))
    version = cursor.fetchone()["next_version"]
    cursor.execute("""
        INSERT INTO content_versions (content_type, content_id, version, payload, status, created_by)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (content_type, content_id, version, json.dumps(payload), status, created_by))


def upsert_subject(name, category="", icon="▣", description="", status="published", admin_id=None):
    conn = _connect()
    c = conn.cursor()
    c.execute("""
        INSERT INTO subjects (name, category, icon, description, status, updated_at)
        VALUES (?, ?, ?, ?, ?, ?)
        ON CONFLICT(name) DO UPDATE SET
            category=excluded.category,
            icon=excluded.icon,
            description=excluded.description,
            status=excluded.status,
            updated_at=excluded.updated_at
    """, (name.strip(), category, icon, description, status, _now()))
    c.execute("SELECT id FROM subjects WHERE name = ?", (name.strip(),))
    content_id = c.fetchone()["id"]
    _create_version(c, "subject", content_id, locals(), status, admin_id)
    conn.commit()
    conn.close()
    return content_id


def add_chapter(subject_id, title, description="", order=0, status="published", admin_id=None):
    conn = _connect()
    c = conn.cursor()
    c.execute("""
        INSERT INTO chapters (subject_id, title, description, chapter_order, status, updated_at)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (subject_id, title.strip(), description, order, status, _now()))
    content_id = c.lastrowid
    _create_version(c, "chapter", content_id, locals(), status, admin_id)
    conn.commit()
    conn.close()
    return content_id


def add_topic(subject_id, chapter_id, title, overview="", order=0, difficulty="core", status="draft", admin_id=None):
    conn = _connect()
    c = conn.cursor()
    c.execute("""
        INSERT INTO topics (subject_id, chapter_id, title, slug, overview, topic_order, difficulty, status, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (subject_id, chapter_id or None, title.strip(), _slug(title), overview, order, difficulty, status, _now()))
    content_id = c.lastrowid
    _create_version(c, "topic", content_id, locals(), status, admin_id)
    conn.commit()
    conn.close()
    return content_id


def add_content_item(content_type, topic_id, payload, status="draft", admin_id=None):
    conn = _connect()
    c = conn.cursor()
    if content_type == "note":
        bundle = get_topic_bundle(topic_id, include_drafts=True)
        subject_id = bundle["topic"]["subject_id"] if bundle else None
        chapter_id = bundle["topic"]["chapter_id"] if bundle else None
        c.execute("""
            INSERT INTO notes (subject_id, chapter_id, topic_id, title, content, summary, note_type, status, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (subject_id, chapter_id, topic_id, payload.get("title", "Note"), payload.get("content", ""), payload.get("summary", ""), payload.get("note_type", "detailed"), status, _now()))
        content_id = c.lastrowid
    elif content_type == "high_yield_point":
        c.execute("INSERT INTO high_yield_points (topic_id, point, explanation, exam_relevance, status, updated_at) VALUES (?, ?, ?, ?, ?, ?)", (topic_id, payload.get("point", ""), payload.get("explanation", ""), payload.get("exam_relevance", ""), status, _now()))
        content_id = c.lastrowid
    elif content_type == "clinical_correlation":
        c.execute("INSERT INTO clinical_correlations (topic_id, title, correlation, patient_link, status, updated_at) VALUES (?, ?, ?, ?, ?, ?)", (topic_id, payload.get("title", "Clinical correlation"), payload.get("correlation", ""), payload.get("patient_link", ""), status, _now()))
        content_id = c.lastrowid
    elif content_type == "mnemonic":
        c.execute("INSERT INTO mnemonics (topic_id, title, mnemonic, explanation, language, status, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?)", (topic_id, payload.get("title", "Mnemonic"), payload.get("mnemonic", ""), payload.get("explanation", ""), payload.get("language", "en"), status, _now()))
        content_id = c.lastrowid
    elif content_type == "flashcard":
        c.execute("INSERT INTO flashcards (topic_id, front, back, explanation, status, updated_at) VALUES (?, ?, ?, ?, ?, ?)", (topic_id, payload.get("front", ""), payload.get("back", ""), payload.get("explanation", ""), status, _now()))
        content_id = c.lastrowid
    elif content_type == "mcq":
        c.execute("""
            INSERT INTO mcqs (topic_id, stem, option_a, option_b, option_c, option_d, option_e, correct_option, explanation, difficulty, status, updated_at)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        """, (topic_id, payload.get("stem", ""), payload.get("option_a", ""), payload.get("option_b", ""), payload.get("option_c", ""), payload.get("option_d", ""), payload.get("option_e", ""), payload.get("correct_option", "A"), payload.get("explanation", ""), payload.get("difficulty", "core"), status, _now()))
        content_id = c.lastrowid
    elif content_type == "osce_case":
        c.execute("INSERT INTO osce_cases (topic_id, title, scenario, tasks, checklist, examiner_notes, status, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?)", (topic_id, payload.get("title", "OSCE case"), payload.get("scenario", ""), json.dumps(_split_lines(payload.get("tasks", ""))), json.dumps(_split_lines(payload.get("checklist", ""))), payload.get("examiner_notes", ""), status, _now()))
        content_id = c.lastrowid
    elif content_type == "resource":
        bundle = get_topic_bundle(topic_id, include_drafts=True)
        subject_id = bundle["topic"]["subject_id"] if bundle else None
        c.execute("INSERT INTO resources (topic_id, subject_id, title, url, citation, resource_type, notes, status, updated_at) VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)", (topic_id, subject_id, payload.get("title", "Resource"), payload.get("url", ""), payload.get("citation", ""), payload.get("resource_type", "reference"), payload.get("notes", ""), status, _now()))
        content_id = c.lastrowid
    else:
        conn.close()
        raise ValueError(f"Unsupported content type: {content_type}")
    _create_version(c, content_type, content_id, payload, status, admin_id)
    conn.commit()
    conn.close()
    return content_id


def _split_lines(value):
    if isinstance(value, list):
        return value
    return [line.strip("-• ").strip() for line in str(value or "").splitlines() if line.strip()]


def update_content_status(content_type, content_id, status, reviewed=False, admin_id=None):
    table_map = {
        "subject": "subjects",
        "chapter": "chapters",
        "topic": "topics",
        "note": "notes",
        "high_yield_point": "high_yield_points",
        "clinical_correlation": "clinical_correlations",
        "mnemonic": "mnemonics",
        "flashcard": "flashcards",
        "mcq": "mcqs",
        "osce_case": "osce_cases",
        "resource": "resources",
    }
    table = table_map.get(content_type)
    if not table:
        return
    conn = _connect()
    c = conn.cursor()
    review_sql = ", is_reviewed = ?" if table not in {"subjects", "chapters"} else ""
    params = [status, _now()]
    if review_sql:
        params.append(1 if reviewed else 0)
    params.append(content_id)
    c.execute(f"UPDATE {table} SET status = ?, updated_at = ? {review_sql} WHERE id = ?", params)
    c.execute("""
        INSERT INTO content_versions (content_type, content_id, version, payload, status, reviewed_by, reviewed_at)
        VALUES (?, ?, COALESCE((SELECT MAX(version)+1 FROM content_versions WHERE content_type=? AND content_id=?), 1), ?, ?, ?, ?)
    """, (content_type, content_id, content_type, content_id, json.dumps({"status": status, "reviewed": reviewed}), status, admin_id, _now() if reviewed else None))
    conn.commit()
    conn.close()


def delete_content(content_type, content_id, admin_id=None):
    update_content_status(content_type, content_id, "archived", reviewed=False, admin_id=admin_id)


def list_content_rows(content_type, include_archived=False, limit=100):
    table_map = {
        "topic": ("topics", "title"),
        "note": ("notes", "title"),
        "high_yield_point": ("high_yield_points", "point"),
        "clinical_correlation": ("clinical_correlations", "title"),
        "mnemonic": ("mnemonics", "title"),
        "flashcard": ("flashcards", "front"),
        "mcq": ("mcqs", "stem"),
        "osce_case": ("osce_cases", "title"),
        "resource": ("resources", "title"),
    }
    table, label_col = table_map[content_type]
    clause = "" if include_archived else "WHERE COALESCE(status, 'published') != 'archived'"
    conn = _connect()
    c = conn.cursor()
    c.execute(f"SELECT *, {label_col} AS label FROM {table} {clause} ORDER BY id DESC LIMIT ?", (limit,))
    rows = [dict(row) for row in c.fetchall()]
    conn.close()
    return rows


def update_content_row(content_type, content_id, updates, status=None, reviewed=False, admin_id=None):
    table_map = {
        "topic": ("topics", {"title", "overview", "difficulty", "status"}),
        "note": ("notes", {"title", "summary", "content", "note_type", "status"}),
        "high_yield_point": ("high_yield_points", {"point", "explanation", "exam_relevance", "status"}),
        "clinical_correlation": ("clinical_correlations", {"title", "correlation", "patient_link", "status"}),
        "mnemonic": ("mnemonics", {"title", "mnemonic", "explanation", "language", "status"}),
        "flashcard": ("flashcards", {"front", "back", "explanation", "status"}),
        "mcq": ("mcqs", {"stem", "option_a", "option_b", "option_c", "option_d", "option_e", "correct_option", "explanation", "difficulty", "status"}),
        "osce_case": ("osce_cases", {"title", "scenario", "tasks", "checklist", "examiner_notes", "status"}),
        "resource": ("resources", {"title", "url", "citation", "resource_type", "notes", "status"}),
    }
    table, allowed = table_map[content_type]
    clean_updates = {key: value for key, value in updates.items() if key in allowed}
    if status:
        clean_updates["status"] = status
    clean_updates["updated_at"] = _now()
    if "is_reviewed" not in clean_updates and table not in {"subjects", "chapters"}:
        clean_updates["is_reviewed"] = 1 if reviewed else 0
    assignments = ", ".join(f"{key} = ?" for key in clean_updates)
    conn = _connect()
    c = conn.cursor()
    c.execute(f"UPDATE {table} SET {assignments} WHERE id = ?", [*clean_updates.values(), content_id])
    _create_version(c, content_type, content_id, clean_updates, clean_updates.get("status", "draft"), admin_id)
    conn.commit()
    conn.close()


def save_topic_progress(user_id, topic, status="completed", score_percent=0, last_position=""):
    conn = _connect()
    c = conn.cursor()
    c.execute("""
        INSERT INTO user_progress (user_id, subject_id, chapter_id, topic_id, status, score_percent, last_position, updated_at)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        ON CONFLICT(user_id, topic_id) DO UPDATE SET
            status=excluded.status,
            score_percent=excluded.score_percent,
            last_position=excluded.last_position,
            updated_at=excluded.updated_at
    """, (user_id, topic.get("subject_id"), topic.get("chapter_id"), topic.get("id"), status, score_percent, last_position, _now()))
    conn.commit()
    conn.close()


def bookmark_topic(user_id, topic):
    conn = _connect()
    c = conn.cursor()
    c.execute("""
        INSERT OR REPLACE INTO user_bookmarks (user_id, topic_id, content_type, content_id, created_at)
        VALUES (?, ?, 'topic', ?, ?)
    """, (user_id, topic["id"], topic["id"], _now()))
    conn.commit()
    conn.close()
    save_bookmark(user_id, "topic", str(topic["id"]), topic["title"], topic.get("subject_name", ""))


def parse_upload(file):
    name = file.name.lower()
    data = file.getvalue()
    if name.endswith(".json"):
        raw = json.loads(data.decode("utf-8"))
        return raw if isinstance(raw, list) else [raw]
    if name.endswith(".csv"):
        text = data.decode("utf-8-sig")
        return list(csv.DictReader(io.StringIO(text)))
    if name.endswith((".xlsx", ".xls")):
        try:
            import pandas as pd
        except Exception as exc:
            raise RuntimeError("Excel upload requires pandas/openpyxl in the environment.") from exc
        return pd.read_excel(io.BytesIO(data)).fillna("").to_dict("records")
    if name.endswith((".md", ".markdown")):
        return parse_markdown_upload(data.decode("utf-8"))
    raise ValueError("Unsupported upload type. Use CSV, Excel, JSON, or Markdown.")


def parse_markdown_upload(text):
    title_match = re.search(r"^#\s+(.+)$", text, flags=re.MULTILINE)
    subject_match = re.search(r"^Subject:\s*(.+)$", text, flags=re.MULTILINE | re.IGNORECASE)
    chapter_match = re.search(r"^Chapter:\s*(.+)$", text, flags=re.MULTILINE | re.IGNORECASE)
    return [{
        "content_type": "note",
        "subject": subject_match.group(1).strip() if subject_match else "General Medicine",
        "chapter": chapter_match.group(1).strip() if chapter_match else "Imported Markdown",
        "topic": title_match.group(1).strip() if title_match else "Imported Topic",
        "title": title_match.group(1).strip() if title_match else "Markdown note",
        "content": text,
        "status": "draft",
    }]


def import_rows(rows, admin_id=None):
    imported = 0
    for row in rows:
        subject_id = upsert_subject(row.get("subject") or row.get("subject_name") or "General Medicine", status=row.get("subject_status", "published"), admin_id=admin_id)
        chapter_title = row.get("chapter") or row.get("chapter_title") or "General"
        chapters = get_chapters(subject_id, include_drafts=True)
        chapter = next((ch for ch in chapters if ch["title"] == chapter_title), None)
        chapter_id = chapter["id"] if chapter else add_chapter(subject_id, chapter_title, status="published", admin_id=admin_id)
        topic_title = row.get("topic") or row.get("topic_title") or row.get("title") or "Imported Topic"
        topics = get_topics(subject_id=subject_id, chapter_id=chapter_id, include_drafts=True)
        topic = next((tp for tp in topics if tp["title"] == topic_title), None)
        topic_id = topic["id"] if topic else add_topic(subject_id, chapter_id, topic_title, row.get("overview", ""), status=row.get("topic_status", "draft"), admin_id=admin_id)
        content_type = row.get("content_type", "note")
        payload = {key: value for key, value in row.items() if value is not None}
        add_content_item(content_type, topic_id, payload, status=row.get("status", "draft"), admin_id=admin_id)
        imported += 1
    return imported


def generate_ai_draft(topic: str):
    topic = topic.strip()
    return {
        "overview": f"{topic} is best learned by connecting definition, mechanism, clinical presentation, investigation, and management. This draft is original educational starter content and should be reviewed before publishing.",
        "note": {
            "title": f"{topic}: detailed notes",
            "content": f"""Overview
{topic} should be approached in a structured clinical sequence: what it is, why it happens, how it presents, how it is confirmed, and what the safest first management step is.

Core explanation
- Start with the basic definition in plain language.
- Identify the underlying mechanism or pathophysiology.
- Link the mechanism to symptoms and examination findings.
- Choose investigations that change management.
- Finish with initial management, complications, and follow-up.

Educational note
This is AI-assisted original summary content. Admin review is required before publishing and references should be added.""",
            "summary": f"Structured clinical summary for {topic}.",
        },
        "high_yield": [
            f"Define {topic} before memorising exceptions.",
            "Know the red flags that change urgency.",
            "Connect investigations to management decisions.",
        ],
        "clinical": [
            f"In a clinical case, ask what symptom or sign makes {topic} most likely.",
            "In OSCEs, state the diagnosis, severity, immediate risk, and next step.",
        ],
        "mnemonics": [{
            "title": f"{topic} clinical sequence",
            "mnemonic": "D-P-I-M-C: Define, Present, Investigate, Manage, Complications",
            "explanation": "Use this sequence to structure revision and exam answers.",
        }],
        "flashcards": [
            {"front": f"What is the first step when explaining {topic}?", "back": "Give a clear definition and mechanism.", "explanation": "This anchors the rest of the answer."},
            {"front": f"What makes {topic} clinically important?", "back": "The red flags, complications, and management decisions.", "explanation": "Exams often test decision-making, not isolated facts."},
        ],
        "mcqs": [{
            "stem": f"A student is revising {topic}. Which approach is most useful for long-term retention?",
            "option_a": "Memorise isolated lists only",
            "option_b": "Connect mechanism to presentation and management",
            "option_c": "Skip clinical examples",
            "option_d": "Read without testing recall",
            "option_e": "",
            "correct_option": "B",
            "explanation": "Clinical linking improves recall and exam performance.",
        }],
        "osce": [{
            "title": f"{topic} focused station",
            "scenario": f"You are asked to assess and explain a patient scenario related to {topic}.",
            "tasks": "Introduce yourself\nTake focused history\nState key examination/investigation\nExplain initial management",
            "checklist": "Clear structure\nPatient-safe language\nRed flags mentioned\nManagement justified",
            "examiner_notes": "Look for safe clinical reasoning and concise explanation.",
        }],
        "resources": [{
            "title": f"{topic} reference space",
            "url": "",
            "citation": "Add guideline, lecture note, or open-access reference after review.",
            "notes": "Do not paste copyrighted textbook content.",
        }],
    }


def save_ai_draft(topic_id, draft, admin_id=None):
    add_content_item("note", topic_id, draft["note"], status="draft", admin_id=admin_id)
    for point in draft["high_yield"]:
        add_content_item("high_yield_point", topic_id, {"point": point}, status="draft", admin_id=admin_id)
    for item in draft["clinical"]:
        add_content_item("clinical_correlation", topic_id, {"title": "Clinical relevance", "correlation": item}, status="draft", admin_id=admin_id)
    for item in draft["mnemonics"]:
        add_content_item("mnemonic", topic_id, item, status="draft", admin_id=admin_id)
    for item in draft["flashcards"]:
        add_content_item("flashcard", topic_id, item, status="draft", admin_id=admin_id)
    for item in draft["mcqs"]:
        add_content_item("mcq", topic_id, item, status="draft", admin_id=admin_id)
    for item in draft["osce"]:
        add_content_item("osce_case", topic_id, item, status="draft", admin_id=admin_id)
    for item in draft["resources"]:
        add_content_item("resource", topic_id, item, status="draft", admin_id=admin_id)


def render_content_library():
    st.markdown('<div class="section-title">A-Z Medical Knowledge Hub</div>', unsafe_allow_html=True)
    st.caption("Database-powered content. Admins can add more subjects, chapters, topics, notes, questions, and resources without editing app.py.")
    subjects = get_subjects()
    if not subjects:
        st.info("No published subjects yet. Add content from the Admin Content Panel.")
        return
    subject_names = [s["name"] for s in subjects]
    subject_name = st.selectbox("Subject", subject_names, key="cms_subject")
    subject = subjects[subject_names.index(subject_name)]
    chapters = get_chapters(subject["id"])
    chapter_options = ["All chapters"] + [ch["title"] for ch in chapters]
    chapter_label = st.selectbox("Chapter", chapter_options, key="cms_chapter")
    chapter_id = None
    if chapter_label != "All chapters":
        chapter_id = next(ch["id"] for ch in chapters if ch["title"] == chapter_label)
    topics = get_topics(subject_id=subject["id"], chapter_id=chapter_id)
    if not topics:
        st.warning("No published topics in this area yet.")
        return
    topic_titles = [topic["title"] for topic in topics]
    topic_title = st.selectbox("Topic", topic_titles, key="cms_topic")
    topic = topics[topic_titles.index(topic_title)]
    render_topic_page(topic["id"])


def render_topic_page(topic_id):
    bundle = get_topic_bundle(topic_id)
    if not bundle:
        st.error("Topic not found.")
        return
    topic = bundle["topic"]
    st.markdown(f"## {topic['title']}")
    st.caption(f"{topic['subject_name']} · {topic.get('chapter_title') or 'General'} · Last updated: {(topic.get('updated_at') or topic.get('created_at') or '')[:10]}")
    col_a, col_b = st.columns(2)
    uid = st.session_state.user["id"] if st.session_state.get("logged_in") and st.session_state.get("user") else None
    with col_a:
        if st.button("🔖 Bookmark topic", use_container_width=True, key=f"topic_bm_{topic_id}"):
            if uid:
                bookmark_topic(uid, topic)
                st.success("Topic saved to bookmarks.")
            else:
                st.warning("Login to save bookmarks.")
    with col_b:
        if st.button("✅ Mark completed", use_container_width=True, key=f"topic_done_{topic_id}"):
            if uid:
                save_topic_progress(uid, topic, status="completed", last_position="topic_complete")
                st.success("Progress saved.")
            else:
                st.warning("Login to save progress.")

    tabs = st.tabs(["Overview", "Detailed Notes", "High-Yield", "Clinical", "Tables & Diagrams", "Mnemonics", "Flashcards", "MCQs", "OSCE", "Resources"])
    with tabs[0]:
        st.write(topic.get("overview") or "Overview will be added by the content team.")
    with tabs[1]:
        for note in bundle["notes"]:
            st.markdown(f"### {note['title']}")
            st.write(note["content"])
    with tabs[2]:
        for point in bundle["high_yield_points"]:
            st.success(point["point"])
            if point.get("explanation"):
                st.caption(point["explanation"])
    with tabs[3]:
        for item in bundle["clinical_correlations"]:
            st.info(f"**{item['title']}**\n\n{item['correlation']}")
    with tabs[4]:
        table_notes = [note for note in bundle["notes"] if note.get("note_type") in {"table", "diagram", "chart"}]
        diagram_resources = [res for res in bundle["resources"] if res.get("resource_type") in {"diagram", "image", "table"}]
        if not table_notes and not diagram_resources:
            st.info("Tables, diagram lists, and visual resources can be added by the content team.")
        for note in table_notes:
            st.markdown(f"### {note['title']}")
            st.write(note["content"])
        for res in diagram_resources:
            st.markdown(f"- {res['title']}")
            if res.get("url"):
                st.caption(res["url"])
    with tabs[5]:
        for item in bundle["mnemonics"]:
            st.warning(f"**{item['title']}**: {item['mnemonic']}")
            if item.get("explanation"):
                st.caption(item["explanation"])
    with tabs[6]:
        for item in bundle["flashcards"]:
            with st.expander(item["front"]):
                st.write(item["back"])
                st.caption(item.get("explanation", ""))
    with tabs[7]:
        for item in bundle["mcqs"]:
            with st.expander(item["stem"]):
                st.write(f"A. {item['option_a']}")
                st.write(f"B. {item['option_b']}")
                st.write(f"C. {item['option_c']}")
                st.write(f"D. {item['option_d']}")
                if item.get("option_e"):
                    st.write(f"E. {item['option_e']}")
                st.success(f"Answer: {item['correct_option']}")
                st.caption(item.get("explanation", ""))
    with tabs[8]:
        for item in bundle["osce_cases"]:
            with st.expander(item["title"]):
                st.write(item["scenario"])
                st.markdown("**Tasks**")
                for task in _json_list(item.get("tasks")):
                    st.markdown(f"- {task}")
                st.markdown("**Checklist**")
                for check in _json_list(item.get("checklist")):
                    st.markdown(f"- {check}")
    with tabs[9]:
        st.caption("References are for attribution and further reading. Do not paste copyrighted textbook content.")
        for item in bundle["resources"]:
            label = item["title"]
            if item.get("url"):
                st.markdown(f"- [{label}]({item['url']})")
            else:
                st.markdown(f"- {label}")
            if item.get("citation"):
                st.caption(item["citation"])


def _json_list(value):
    try:
        parsed = json.loads(value or "[]")
        return parsed if isinstance(parsed, list) else []
    except Exception:
        return _split_lines(value)


def render_admin_content_panel(theme):
    user = st.session_state.get("user")
    if not st.session_state.get("logged_in") or not is_admin_user(user):
        st.error("Admin access required. Login with an admin account to manage content.")
        return
    admin_id = user["id"]
    st.markdown('<div class="section-title">Admin Content Panel</div>', unsafe_allow_html=True)
    st.caption("Create, import, review, publish, archive, and version medical content. AI drafts remain draft until reviewed.")

    tabs = st.tabs(["Create", "Edit Existing", "Bulk Upload", "AI Draft Generator", "Review & Publish", "Content Map"])
    with tabs[0]:
        _render_create_content(admin_id)
    with tabs[1]:
        _render_edit_existing(admin_id)
    with tabs[2]:
        _render_bulk_upload(admin_id)
    with tabs[3]:
        _render_ai_generator(admin_id)
    with tabs[4]:
        _render_review_queue(admin_id)
    with tabs[5]:
        _render_content_map()


def _subject_chapter_topic_controls(prefix, include_drafts=True):
    subjects = get_subjects(include_drafts=include_drafts)
    if not subjects:
        st.warning("Add a subject first.")
        return None, None, None
    subject = st.selectbox("Subject", subjects, format_func=lambda item: item["name"], key=f"{prefix}_subject")
    chapters = get_chapters(subject["id"], include_drafts=include_drafts)
    chapter_options = [{"id": None, "title": "No chapter"}] + chapters
    chapter = st.selectbox("Chapter", chapter_options, format_func=lambda item: item["title"], key=f"{prefix}_chapter")
    topics = get_topics(subject_id=subject["id"], chapter_id=chapter["id"], include_drafts=include_drafts) if chapter["id"] else get_topics(subject_id=subject["id"], include_drafts=include_drafts)
    topic = st.selectbox("Topic", topics, format_func=lambda item: item["title"], key=f"{prefix}_topic") if topics else None
    return subject, chapter, topic


def _render_create_content(admin_id):
    st.subheader("Add structured content")
    content_mode = st.selectbox("What do you want to add?", ["Subject", "Chapter", "Topic", "Content item"])
    if content_mode == "Subject":
        with st.form("admin_subject_form"):
            name = st.text_input("Subject name")
            category = st.text_input("Category", placeholder="Pre-clinical, Clinical, Public Health...")
            icon = st.text_input("Icon", value="▣")
            description = st.text_area("Student-friendly description")
            status = st.selectbox("Status", CONTENT_STATUSES, index=2)
            submit = st.form_submit_button("Save subject", type="primary")
        if submit and name:
            upsert_subject(name, category, icon, description, status, admin_id)
            st.success("Subject saved.")
            st.rerun()
    elif content_mode == "Chapter":
        subjects = get_subjects(include_drafts=True)
        subject = st.selectbox("Subject", subjects, format_func=lambda item: item["name"])
        with st.form("admin_chapter_form"):
            title = st.text_input("Chapter title")
            description = st.text_area("Chapter description")
            order = st.number_input("Order", min_value=0, value=0)
            status = st.selectbox("Status", CONTENT_STATUSES, index=2)
            submit = st.form_submit_button("Save chapter", type="primary")
        if submit and title:
            add_chapter(subject["id"], title, description, int(order), status, admin_id)
            st.success("Chapter saved.")
            st.rerun()
    elif content_mode == "Topic":
        subjects = get_subjects(include_drafts=True)
        subject = st.selectbox("Subject", subjects, format_func=lambda item: item["name"], key="new_topic_subject")
        chapters = get_chapters(subject["id"], include_drafts=True)
        chapter = st.selectbox("Chapter", [{"id": None, "title": "No chapter"}] + chapters, format_func=lambda item: item["title"], key="new_topic_chapter")
        with st.form("admin_topic_form"):
            title = st.text_input("Topic title")
            overview = st.text_area("Overview")
            difficulty = st.selectbox("Difficulty", ["foundation", "core", "advanced"])
            status = st.selectbox("Status", CONTENT_STATUSES, index=0)
            submit = st.form_submit_button("Save topic", type="primary")
        if submit and title:
            add_topic(subject["id"], chapter["id"], title, overview, difficulty=difficulty, status=status, admin_id=admin_id)
            st.success("Topic saved.")
            st.rerun()
    else:
        _, _, topic = _subject_chapter_topic_controls("content_item")
        if not topic:
            st.warning("Add a topic first.")
            return
        content_type = st.selectbox("Content type", CONTENT_TYPES)
        payload = _content_payload_form(content_type)
        status = st.selectbox("Save status", CONTENT_STATUSES, index=0, key="content_item_status")
        if st.button("Save content item", type="primary", use_container_width=True):
            add_content_item(content_type, topic["id"], payload, status=status, admin_id=admin_id)
            st.success("Content item saved.")
            st.rerun()


def _content_payload_form(content_type):
    if content_type == "note":
        return {"title": st.text_input("Note title"), "summary": st.text_input("Short summary"), "content": st.text_area("Detailed notes", height=220), "note_type": st.text_input("Note type", value="detailed")}
    if content_type == "high_yield_point":
        return {"point": st.text_area("High-yield point"), "explanation": st.text_area("Explanation"), "exam_relevance": st.text_input("Exam relevance")}
    if content_type == "clinical_correlation":
        return {"title": st.text_input("Clinical title"), "correlation": st.text_area("Clinical correlation"), "patient_link": st.text_input("Patient link")}
    if content_type == "mnemonic":
        return {"title": st.text_input("Mnemonic title"), "mnemonic": st.text_input("Mnemonic"), "explanation": st.text_area("Explanation"), "language": st.selectbox("Language", ["en", "ar", "bilingual"])}
    if content_type == "flashcard":
        return {"front": st.text_area("Front"), "back": st.text_area("Back"), "explanation": st.text_area("Explanation")}
    if content_type == "mcq":
        return {"stem": st.text_area("Stem"), "option_a": st.text_input("A"), "option_b": st.text_input("B"), "option_c": st.text_input("C"), "option_d": st.text_input("D"), "option_e": st.text_input("E optional"), "correct_option": st.selectbox("Correct", ["A", "B", "C", "D", "E"]), "explanation": st.text_area("Explanation"), "difficulty": st.selectbox("Difficulty", ["foundation", "core", "advanced"])}
    if content_type == "osce_case":
        return {"title": st.text_input("Case title"), "scenario": st.text_area("Scenario"), "tasks": st.text_area("Tasks, one per line"), "checklist": st.text_area("Checklist, one per line"), "examiner_notes": st.text_area("Examiner notes")}
    return {"title": st.text_input("Resource title"), "url": st.text_input("URL"), "citation": st.text_area("Citation/reference"), "resource_type": st.text_input("Type", value="reference"), "notes": st.text_area("Notes")}


def _render_bulk_upload(admin_id):
    st.subheader("Bulk upload")
    st.write("Upload CSV, Excel, JSON, or Markdown. Suggested columns: content_type, subject, chapter, topic, title, content, status, front, back, stem, option_a, option_b, option_c, option_d, correct_option.")
    upload = st.file_uploader("Upload content file", type=["csv", "xlsx", "xls", "json", "md", "markdown"])
    if upload:
        try:
            rows = parse_upload(upload)
            st.success(f"Parsed {len(rows)} rows. Preview:")
            st.dataframe(rows[:20], use_container_width=True)
            if st.button("Import as draft/reviewed content", type="primary"):
                imported = import_rows(rows, admin_id=admin_id)
                st.success(f"Imported {imported} content rows.")
                st.rerun()
        except Exception as exc:
            st.error(str(exc))


def _render_edit_existing(admin_id):
    st.subheader("Edit existing content")
    content_type = st.selectbox("Content type to edit", ["topic", *CONTENT_TYPES], key="edit_content_type")
    rows = list_content_rows(content_type, include_archived=False)
    if not rows:
        st.info("No content rows found for this type.")
        return
    row = st.selectbox("Select row", rows, format_func=lambda item: f"#{item['id']} · {item.get('label', '')[:90]}", key="edit_content_row")
    status = st.selectbox("Status", CONTENT_STATUSES, index=CONTENT_STATUSES.index(row.get("status") or "draft") if (row.get("status") or "draft") in CONTENT_STATUSES else 0, key="edit_status")
    reviewed = st.checkbox("Reviewed", value=bool(row.get("is_reviewed", 0)), key="edit_reviewed")
    updates = {}
    if content_type == "topic":
        updates["title"] = st.text_input("Title", value=row.get("title", ""))
        updates["overview"] = st.text_area("Overview", value=row.get("overview", ""), height=180)
        updates["difficulty"] = st.selectbox("Difficulty", ["foundation", "core", "advanced"], index=["foundation", "core", "advanced"].index(row.get("difficulty", "core")) if row.get("difficulty", "core") in ["foundation", "core", "advanced"] else 1)
    elif content_type == "note":
        updates["title"] = st.text_input("Title", value=row.get("title", ""))
        updates["summary"] = st.text_input("Summary", value=row.get("summary", ""))
        updates["note_type"] = st.selectbox("Note type", ["overview", "detailed", "table", "diagram", "chart"], index=0)
        updates["content"] = st.text_area("Content", value=row.get("content", ""), height=260)
    elif content_type == "flashcard":
        updates["front"] = st.text_area("Front", value=row.get("front", ""))
        updates["back"] = st.text_area("Back", value=row.get("back", ""))
        updates["explanation"] = st.text_area("Explanation", value=row.get("explanation", ""))
    elif content_type == "mcq":
        updates["stem"] = st.text_area("Stem", value=row.get("stem", ""))
        for option in ["option_a", "option_b", "option_c", "option_d", "option_e"]:
            updates[option] = st.text_input(option.replace("_", " ").title(), value=row.get(option, ""))
        updates["correct_option"] = st.selectbox("Correct", ["A", "B", "C", "D", "E"], index=["A", "B", "C", "D", "E"].index(row.get("correct_option", "A")) if row.get("correct_option", "A") in ["A", "B", "C", "D", "E"] else 0)
        updates["explanation"] = st.text_area("Explanation", value=row.get("explanation", ""))
    else:
        editable = {key: value for key, value in row.items() if key not in {"id", "topic_id", "subject_id", "chapter_id", "created_at", "updated_at", "label", "is_reviewed"}}
        edited_json = st.text_area("Edit JSON fields", value=json.dumps(editable, indent=2), height=280)
        try:
            updates = json.loads(edited_json)
        except json.JSONDecodeError:
            st.warning("JSON is not valid yet.")
            updates = {}
    if st.button("Save edits", type="primary", use_container_width=True):
        update_content_row(content_type, row["id"], updates, status=status, reviewed=reviewed, admin_id=admin_id)
        st.success("Content updated and versioned.")
        st.rerun()


def _render_ai_generator(admin_id):
    st.subheader("AI Content Generator")
    st.caption("Generated content is saved as draft only. Review and publish it before students see it.")
    subject, chapter, topic = _subject_chapter_topic_controls("ai_generator")
    new_topic = st.text_input("Or generate for a new topic title")
    prompt_topic = st.text_input("Medical topic prompt", placeholder="Acute coronary syndrome, nephrotic syndrome, brachial plexus...")
    if st.button("Generate draft pack", type="primary", use_container_width=True):
        title = prompt_topic or new_topic or (topic["title"] if topic else "")
        if not title:
            st.error("Enter a topic first.")
            return
        if not topic:
            topic_id = add_topic(subject["id"], chapter["id"], new_topic or title, overview=f"Draft topic for {title}", status="draft", admin_id=admin_id)
        else:
            topic_id = topic["id"]
        draft = generate_ai_draft(title)
        save_ai_draft(topic_id, draft, admin_id=admin_id)
        st.success("AI draft content saved. Review it before publishing.")


def _render_review_queue(admin_id):
    st.subheader("Review drafts and outdated content")
    conn = _connect()
    c = conn.cursor()
    rows = []
    for content_type, table, title_col in [
        ("topic", "topics", "title"),
        ("note", "notes", "title"),
        ("high_yield_point", "high_yield_points", "point"),
        ("clinical_correlation", "clinical_correlations", "title"),
        ("mnemonic", "mnemonics", "title"),
        ("flashcard", "flashcards", "front"),
        ("mcq", "mcqs", "stem"),
        ("osce_case", "osce_cases", "title"),
        ("resource", "resources", "title"),
    ]:
        c.execute(f"SELECT id, {title_col} AS title, status, COALESCE(is_reviewed, 0) AS is_reviewed, updated_at FROM {table} WHERE COALESCE(status, 'draft') != 'published' OR COALESCE(is_reviewed, 0) = 0 ORDER BY id DESC LIMIT 30")
        rows.extend({**dict(row), "content_type": content_type} for row in c.fetchall())
    conn.close()
    if not rows:
        st.success("No draft or unreviewed content right now.")
        return
    for row in rows[:80]:
        with st.expander(f"{row['content_type']} · {row['title'][:90]} · {row['status']}"):
            st.caption(f"ID: {row['id']} · Reviewed: {'yes' if row['is_reviewed'] else 'no'}")
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("Publish reviewed", key=f"publish_{row['content_type']}_{row['id']}"):
                    update_content_status(row["content_type"], row["id"], "published", reviewed=True, admin_id=admin_id)
                    st.rerun()
            with col2:
                if st.button("Mark reviewed draft", key=f"review_{row['content_type']}_{row['id']}"):
                    update_content_status(row["content_type"], row["id"], "reviewed", reviewed=True, admin_id=admin_id)
                    st.rerun()
            with col3:
                if st.button("Archive", key=f"archive_{row['content_type']}_{row['id']}"):
                    delete_content(row["content_type"], row["id"], admin_id=admin_id)
                    st.rerun()


def _render_content_map():
    subjects = get_subjects(include_drafts=True)
    st.metric("Subjects", len(subjects))
    topics = get_topics(include_drafts=True)
    st.metric("Topics", len(topics))
    st.dataframe(topics, use_container_width=True)
