"""
database.py - persistent user data, authentication, and learning analytics.
"""

from __future__ import annotations

import json
import sqlite3
import bcrypt
from collections import defaultdict
from datetime import datetime, date, timedelta
from pathlib import Path

APP_DIR = Path(__file__).resolve().parent
DB_NAME = str(APP_DIR / "medstudy_oman.db")


def _connect():
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    return conn


def init_db():
    """Creates all tables if they do not exist yet."""
    conn = _connect()
    c = conn.cursor()

    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            university TEXT DEFAULT 'SQU',
            year_of_study INTEGER DEFAULT 1,
            theme TEXT DEFAULT '🩺 Clinical Snow',
            language TEXT DEFAULT 'en',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            last_login TEXT
        )
    """)

    _add_column_if_missing(c, "users", "language", "TEXT DEFAULT 'en'")

    c.execute("""
        CREATE TABLE IF NOT EXISTS flashcard_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            card_id TEXT NOT NULL,
            subject TEXT NOT NULL,
            ease_factor REAL DEFAULT 2.5,
            interval_days INTEGER DEFAULT 1,
            next_review TEXT,
            times_reviewed INTEGER DEFAULT 0,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS mcq_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            correct INTEGER DEFAULT 0,
            total INTEGER DEFAULT 0,
            date TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS study_sessions (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            subject TEXT,
            duration_minutes INTEGER,
            date TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS study_goals (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            label TEXT NOT NULL,
            target INTEGER NOT NULL,
            unit TEXT DEFAULT '',
            icon TEXT DEFAULT '🎯',
            color TEXT DEFAULT '#10b981',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS activity_log (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            icon TEXT DEFAULT '⚡',
            text TEXT NOT NULL,
            badge TEXT DEFAULT 'Done',
            badge_color TEXT DEFAULT '#10b981',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS user_profiles (
            user_id INTEGER PRIMARY KEY,
            display_name TEXT,
            exam_track TEXT DEFAULT 'SQU-COM',
            target_exam TEXT DEFAULT 'OMSB Part 1',
            daily_goal_minutes INTEGER DEFAULT 60,
            bio TEXT DEFAULT '',
            avatar_url TEXT DEFAULT '',
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS subjects (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE NOT NULL,
            category TEXT,
            icon TEXT DEFAULT '▣',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS chapters (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id INTEGER NOT NULL,
            title TEXT NOT NULL,
            chapter_order INTEGER DEFAULT 0,
            FOREIGN KEY (subject_id) REFERENCES subjects(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS notes (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            subject_id INTEGER,
            chapter_id INTEGER,
            title TEXT NOT NULL,
            content TEXT NOT NULL,
            note_type TEXT DEFAULT 'high_yield',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (subject_id) REFERENCES subjects(id),
            FOREIGN KEY (chapter_id) REFERENCES chapters(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS bookmarks (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            item_type TEXT NOT NULL,
            item_id TEXT NOT NULL,
            title TEXT NOT NULL,
            subject TEXT DEFAULT '',
            metadata TEXT DEFAULT '{}',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, item_type, item_id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS quiz_attempts (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            topic TEXT DEFAULT '',
            correct INTEGER DEFAULT 0,
            total INTEGER DEFAULT 0,
            score_percent REAL DEFAULT 0,
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS completed_lessons (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            subject TEXT NOT NULL,
            lesson_id TEXT NOT NULL,
            title TEXT NOT NULL,
            completed_at TEXT DEFAULT CURRENT_TIMESTAMP,
            UNIQUE(user_id, subject, lesson_id),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS osce_progress (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            station TEXT NOT NULL,
            skill_domain TEXT DEFAULT '',
            score INTEGER DEFAULT 0,
            notes TEXT DEFAULT '',
            practiced_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS ai_mnemonics_history (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            topic TEXT NOT NULL,
            mnemonic_type TEXT DEFAULT 'exam',
            easy_mnemonic TEXT NOT NULL,
            funny_mnemonic TEXT DEFAULT '',
            exam_mnemonic TEXT DEFAULT '',
            visual_story TEXT DEFAULT '',
            english_explanation TEXT DEFAULT '',
            arabic_explanation TEXT DEFAULT '',
            recall_quiz TEXT DEFAULT '[]',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS study_activity (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            user_id INTEGER NOT NULL,
            activity_type TEXT NOT NULL,
            subject TEXT DEFAULT '',
            title TEXT NOT NULL,
            metadata TEXT DEFAULT '{}',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    c.execute("""
        CREATE TABLE IF NOT EXISTS settings (
            user_id INTEGER NOT NULL,
            key TEXT NOT NULL,
            value TEXT NOT NULL,
            updated_at TEXT DEFAULT CURRENT_TIMESTAMP,
            PRIMARY KEY (user_id, key),
            FOREIGN KEY (user_id) REFERENCES users(id)
        )
    """)

    _seed_medical_content(c)

    conn.commit()
    conn.close()


def _add_column_if_missing(cursor, table_name: str, column_name: str, definition: str):
    cursor.execute(f"PRAGMA table_info({table_name})")
    columns = {row[1] for row in cursor.fetchall()}
    if column_name not in columns:
        cursor.execute(f"ALTER TABLE {table_name} ADD COLUMN {column_name} {definition}")


def _seed_medical_content(cursor):
    try:
        from medical_knowledge import AZ_MEDICAL_KNOWLEDGE
    except Exception:
        return

    for subject_name, data in AZ_MEDICAL_KNOWLEDGE.items():
        cursor.execute("""
            INSERT OR IGNORE INTO subjects (name, category, icon)
            VALUES (?, ?, ?)
        """, (subject_name, data.get("category", ""), "▣"))
        cursor.execute("SELECT id FROM subjects WHERE name = ?", (subject_name,))
        subject_row = cursor.fetchone()
        if not subject_row:
            continue
        subject_id = subject_row[0]
        for order, chapter_title in enumerate(data.get("chapters", []), start=1):
            cursor.execute("SELECT id FROM chapters WHERE subject_id = ? AND title = ?", (subject_id, chapter_title))
            chapter_row = cursor.fetchone()
            if not chapter_row:
                cursor.execute("""
                    INSERT INTO chapters (subject_id, title, chapter_order)
                    VALUES (?, ?, ?)
                """, (subject_id, chapter_title, order))
                chapter_id = cursor.lastrowid
            else:
                chapter_id = chapter_row[0]
            note_text = "\n".join([
                "High-yield points:",
                *[f"- {item}" for item in data.get("high_yield", [])],
                "",
                "Clinical correlations:",
                *[f"- {item}" for item in data.get("clinical_correlations", [])],
                "",
                "Quick revision:",
                *[f"- {item}" for item in data.get("quick_revision_notes", [])],
            ])
            cursor.execute("""
                SELECT id FROM notes
                WHERE subject_id = ? AND chapter_id = ? AND title = ? AND note_type = 'starter_curriculum'
            """, (subject_id, chapter_id, chapter_title))
            if not cursor.fetchone():
                cursor.execute("""
                    INSERT INTO notes (subject_id, chapter_id, title, content, note_type)
                    VALUES (?, ?, ?, ?, 'starter_curriculum')
                """, (subject_id, chapter_id, chapter_title, note_text))


def signup_user(name, email, password, university="SQU", year=1):
    try:
        conn = _connect()
        c = conn.cursor()
        password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        c.execute("""
            INSERT INTO users (name, email, password_hash, university, year_of_study)
            VALUES (?, ?, ?, ?, ?)
        """, (name, email, password_hash, university, year))
        user_id = c.lastrowid
        c.execute("""
            INSERT OR IGNORE INTO user_profiles (user_id, display_name)
            VALUES (?, ?)
        """, (user_id, name))
        conn.commit()
        conn.close()
        return True, "Account created successfully!"
    except sqlite3.IntegrityError:
        return False, "This email is already registered. Please log in."
    except Exception as e:
        return False, f"Error: {str(e)}"


def login_user(email, password):
    try:
        conn = _connect()
        c = conn.cursor()
        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = c.fetchone()
        if not user:
            conn.close()
            return False, "No account found with this email."

        stored_hash = user["password_hash"].encode("utf-8")
        if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
            c.execute("UPDATE users SET last_login = ? WHERE id = ?", (datetime.now().isoformat(), user["id"]))
            conn.commit()
            conn.close()
            return True, {
                "id": user["id"],
                "name": user["name"],
                "email": user["email"],
                "university": user["university"],
                "year": user["year_of_study"],
                "theme": user["theme"],
                "language": user["language"] if "language" in user.keys() else "en",
                "created_at": user["created_at"],
                "last_login": user["last_login"],
            }
        conn.close()
        return False, "Incorrect password. Please try again."
    except Exception as e:
        return False, f"Error: {str(e)}"


def reset_password(email, new_password):
    if len(new_password or "") < 8:
        return False, "Password must be at least 8 characters."
    conn = _connect()
    c = conn.cursor()
    c.execute("SELECT id FROM users WHERE email = ?", (email,))
    user = c.fetchone()
    if not user:
        conn.close()
        return False, "No account found with this email."
    password_hash = bcrypt.hashpw(new_password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
    c.execute("UPDATE users SET password_hash = ? WHERE id = ?", (password_hash, user["id"]))
    c.execute("""
        INSERT INTO study_activity (user_id, activity_type, title)
        VALUES (?, 'security', 'Password updated')
    """, (user["id"],))
    conn.commit()
    conn.close()
    return True, "Password updated. You can log in with the new password."


def update_theme(user_id, theme_name):
    conn = _connect()
    c = conn.cursor()
    c.execute("UPDATE users SET theme = ? WHERE id = ?", (theme_name, user_id))
    c.execute("""
        INSERT INTO settings (user_id, key, value, updated_at)
        VALUES (?, 'theme', ?, ?)
        ON CONFLICT(user_id, key) DO UPDATE SET value = excluded.value, updated_at = excluded.updated_at
    """, (user_id, theme_name, datetime.now().isoformat()))
    conn.commit()
    conn.close()


def update_language(user_id, language):
    conn = _connect()
    c = conn.cursor()
    c.execute("UPDATE users SET language = ? WHERE id = ?", (language, user_id))
    c.execute("""
        INSERT INTO settings (user_id, key, value, updated_at)
        VALUES (?, 'language', ?, ?)
        ON CONFLICT(user_id, key) DO UPDATE SET value = excluded.value, updated_at = excluded.updated_at
    """, (user_id, language, datetime.now().isoformat()))
    conn.commit()
    conn.close()


def update_user_setting(user_id, key, value):
    conn = _connect()
    c = conn.cursor()
    c.execute("""
        INSERT INTO settings (user_id, key, value, updated_at)
        VALUES (?, ?, ?, ?)
        ON CONFLICT(user_id, key) DO UPDATE SET value = excluded.value, updated_at = excluded.updated_at
    """, (user_id, key, str(value), datetime.now().isoformat()))
    conn.commit()
    conn.close()


def get_user_preferences(user_id):
    conn = _connect()
    c = conn.cursor()
    c.execute("SELECT theme, language FROM users WHERE id = ?", (user_id,))
    user = c.fetchone()
    c.execute("SELECT key, value FROM settings WHERE user_id = ?", (user_id,))
    settings = {row["key"]: row["value"] for row in c.fetchall()}
    conn.close()
    return {
        "theme": settings.get("theme") or (user["theme"] if user else "🌑 Deep Surgeon"),
        "language": settings.get("language") or (user["language"] if user else "en"),
        **settings,
    }


def save_study_session(user_id, subject, duration_minutes):
    conn = _connect()
    c = conn.cursor()
    c.execute("""
        INSERT INTO study_sessions (user_id, subject, duration_minutes)
        VALUES (?, ?, ?)
    """, (user_id, subject, duration_minutes))
    c.execute("""
        INSERT INTO activity_log (user_id, icon, text, badge, badge_color)
        VALUES (?, '⏱️', ?, 'Focus', '#ef4444')
    """, (user_id, f"Completed {duration_minutes}-minute {subject or 'study'} session"))
    conn.commit()
    conn.close()


def save_mcq_attempt(user_id, subject, correct, total):
    conn = _connect()
    c = conn.cursor()
    c.execute("""
        INSERT INTO mcq_attempts (user_id, subject, correct, total)
        VALUES (?, ?, ?, ?)
    """, (user_id, subject, correct, total))
    pct = round((correct / total * 100) if total else 0, 1)
    c.execute("""
        INSERT INTO quiz_attempts (user_id, subject, correct, total, score_percent)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, subject, correct, total, pct))
    c.execute("""
        INSERT INTO activity_log (user_id, icon, text, badge, badge_color)
        VALUES (?, '📝', ?, ?, '#10b981')
    """, (user_id, f"Completed {total}-question {subject} MCQ set", f"{pct}%"))
    conn.commit()
    conn.close()


def save_bookmark(user_id, item_type, item_id, title, subject="", metadata=None):
    conn = _connect()
    c = conn.cursor()
    c.execute("""
        INSERT OR REPLACE INTO bookmarks
        (user_id, item_type, item_id, title, subject, metadata, created_at)
        VALUES (?, ?, ?, ?, ?, ?, ?)
    """, (
        user_id, item_type, item_id, title, subject,
        json.dumps(metadata or {}), datetime.now().isoformat()
    ))
    c.execute("""
        INSERT INTO study_activity (user_id, activity_type, subject, title, metadata)
        VALUES (?, 'bookmark', ?, ?, ?)
    """, (user_id, subject, f"Bookmarked {title}", json.dumps({"item_type": item_type})))
    conn.commit()
    conn.close()


def remove_bookmark(user_id, item_type, item_id):
    conn = _connect()
    c = conn.cursor()
    c.execute("DELETE FROM bookmarks WHERE user_id = ? AND item_type = ? AND item_id = ?", (user_id, item_type, item_id))
    conn.commit()
    conn.close()


def get_bookmarks(user_id, limit=100):
    conn = _connect()
    c = conn.cursor()
    c.execute("""
        SELECT item_type, item_id, title, subject, metadata, created_at
        FROM bookmarks
        WHERE user_id = ?
        ORDER BY created_at DESC
        LIMIT ?
    """, (user_id, limit))
    rows = [dict(row) for row in c.fetchall()]
    conn.close()
    for row in rows:
        try:
            row["metadata"] = json.loads(row.get("metadata") or "{}")
        except json.JSONDecodeError:
            row["metadata"] = {}
    return rows


def save_completed_lesson(user_id, subject, lesson_id, title):
    conn = _connect()
    c = conn.cursor()
    c.execute("""
        INSERT OR IGNORE INTO completed_lessons (user_id, subject, lesson_id, title)
        VALUES (?, ?, ?, ?)
    """, (user_id, subject, lesson_id, title))
    c.execute("""
        INSERT INTO study_activity (user_id, activity_type, subject, title)
        VALUES (?, 'lesson', ?, ?)
    """, (user_id, subject, f"Completed {title}"))
    conn.commit()
    conn.close()


def save_ai_mnemonic(user_id, topic, data):
    conn = _connect()
    c = conn.cursor()
    c.execute("""
        INSERT INTO ai_mnemonics_history (
            user_id, topic, mnemonic_type, easy_mnemonic, funny_mnemonic,
            exam_mnemonic, visual_story, english_explanation,
            arabic_explanation, recall_quiz
        )
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        user_id,
        topic,
        data.get("mnemonic_type", "exam"),
        data.get("easy_mnemonic", ""),
        data.get("funny_mnemonic", ""),
        data.get("exam_mnemonic", ""),
        data.get("visual_story", ""),
        data.get("english_explanation", ""),
        data.get("arabic_explanation", ""),
        json.dumps(data.get("recall_quiz", [])),
    ))
    c.execute("""
        INSERT INTO study_activity (user_id, activity_type, subject, title, metadata)
        VALUES (?, 'ai_mnemonic', ?, ?, ?)
    """, (user_id, data.get("subject", ""), f"Generated mnemonic for {topic}", json.dumps({"topic": topic})))
    conn.commit()
    conn.close()


def get_ai_mnemonic_history(user_id, limit=20):
    conn = _connect()
    c = conn.cursor()
    c.execute("""
        SELECT topic, mnemonic_type, easy_mnemonic, funny_mnemonic, exam_mnemonic,
               visual_story, english_explanation, arabic_explanation, recall_quiz, created_at
        FROM ai_mnemonics_history
        WHERE user_id = ?
        ORDER BY created_at DESC
        LIMIT ?
    """, (user_id, limit))
    rows = [dict(row) for row in c.fetchall()]
    conn.close()
    for row in rows:
        try:
            row["recall_quiz"] = json.loads(row.get("recall_quiz") or "[]")
        except json.JSONDecodeError:
            row["recall_quiz"] = []
    return rows


def get_recent_activity(user_id, limit=12):
    conn = _connect()
    c = conn.cursor()
    rows = []
    c.execute("""
        SELECT activity_type AS icon, title AS text, activity_type AS badge, '#10b981' AS badge_color, created_at
        FROM study_activity
        WHERE user_id = ?
        ORDER BY created_at DESC
        LIMIT ?
    """, (user_id, limit))
    rows.extend(dict(row) for row in c.fetchall())
    if len(rows) < limit:
        c.execute("""
            SELECT icon, text, badge, badge_color, created_at
            FROM activity_log
            WHERE user_id = ?
            ORDER BY created_at DESC
            LIMIT ?
        """, (user_id, limit - len(rows)))
        rows.extend(dict(row) for row in c.fetchall())
    conn.close()
    return [
        {**row, "time": _relative_time(row.get("created_at"))}
        for row in rows[:limit]
    ]


def get_profile_overview(user_id):
    stats = get_user_stats(user_id)
    bookmarks = get_bookmarks(user_id, limit=8)
    mnemonics = get_ai_mnemonic_history(user_id, limit=5)
    activity = get_recent_activity(user_id, limit=10)
    subject_scores = stats.get("subject_scores", {})
    weak = sorted(subject_scores, key=subject_scores.get)[:4]
    strong = sorted(subject_scores, key=subject_scores.get, reverse=True)[:4]
    progress_seed = min(100, int((stats.get("study_hours", 0) * 3) + (stats.get("mcq_percent", 0) * 0.45) + len(bookmarks) * 2))
    return {
        **stats,
        "overall_progress": progress_seed,
        "bookmarks": bookmarks,
        "mnemonics": mnemonics,
        "activities": activity or stats.get("activities", []),
        "weak_areas": weak or ["Renal physiology", "Antimicrobial coverage", "ECG rhythm recognition"],
        "strong_areas": strong or ["Anatomy", "Pathology", "Clinical reasoning"],
        "recommended_lessons": ["Approach to chest pain", "Acid-base disorders", "Beta-lactam antibiotics"],
    }


def save_activity(user_id, icon, text, badge="Done", badge_color="#10b981"):
    conn = _connect()
    c = conn.cursor()
    c.execute("""
        INSERT INTO activity_log (user_id, icon, text, badge, badge_color)
        VALUES (?, ?, ?, ?, ?)
    """, (user_id, icon, text, badge, badge_color))
    conn.commit()
    conn.close()


def _iso_day(value: str | None) -> str:
    if not value:
        return date.today().isoformat()
    try:
        return datetime.fromisoformat(value.replace("Z", "+00:00")).date().isoformat()
    except Exception:
        return value[:10]


def _current_streak(daily_minutes: dict[str, int]) -> int:
    streak = 0
    today = date.today()
    for offset in range(365):
        day = (today - timedelta(days=offset)).isoformat()
        if daily_minutes.get(day, 0) > 0:
            streak += 1
        else:
            break
    return streak


def _default_goals(study_hours: float, mcqs_done: int, flashcards_due: int, subject_count: int):
    return [
        {"label": "Study Hours", "icon": "⏱️", "current": round(study_hours, 1), "target": 20, "unit": "hrs", "color": "#e63946"},
        {"label": "MCQs Practiced", "icon": "📝", "current": mcqs_done, "target": 100, "unit": "Qs", "color": "#10b981"},
        {"label": "Flashcards", "icon": "🃏", "current": flashcards_due, "target": 50, "unit": "", "color": "#8b5cf6"},
        {"label": "Subjects", "icon": "📚", "current": subject_count, "target": 5, "unit": "", "color": "#f59e0b"},
    ]


def get_user_stats(user_id):
    conn = _connect()
    c = conn.cursor()

    c.execute("SELECT COALESCE(SUM(duration_minutes), 0) AS total FROM study_sessions WHERE user_id = ?", (user_id,))
    total_minutes = int(c.fetchone()["total"] or 0)
    study_hours = round(total_minutes / 60, 1)

    c.execute("SELECT COUNT(*) AS total FROM study_sessions WHERE user_id = ?", (user_id,))
    total_sessions = int(c.fetchone()["total"] or 0)

    c.execute("SELECT COALESCE(SUM(correct), 0) AS correct, COALESCE(SUM(total), 0) AS total FROM mcq_attempts WHERE user_id = ?", (user_id,))
    mcq_row = c.fetchone()
    correct = int(mcq_row["correct"] or 0)
    total_mcq = int(mcq_row["total"] or 0)
    mcq_percent = round((correct / total_mcq * 100) if total_mcq else 0, 1)

    daily_minutes = defaultdict(int)
    c.execute("SELECT date, duration_minutes FROM study_sessions WHERE user_id = ?", (user_id,))
    for row in c.fetchall():
        daily_minutes[_iso_day(row["date"])] += int(row["duration_minutes"] or 0)

    today = date.today()
    for offset in range(365):
        daily_minutes.setdefault((today - timedelta(days=offset)).isoformat(), 0)

    c.execute("SELECT date, subject, correct, total FROM mcq_attempts WHERE user_id = ? ORDER BY date ASC", (user_id,))
    attempts = c.fetchall()
    mcq_sessions = []
    subject_totals = defaultdict(lambda: [0, 0])
    for row in attempts:
        total = int(row["total"] or 0)
        row_correct = int(row["correct"] or 0)
        accuracy = round((row_correct / total * 100) if total else 0, 1)
        mcq_sessions.append({"date": _iso_day(row["date"]), "accuracy": accuracy, "count": total})
        subject_totals[row["subject"] or "General"][0] += row_correct
        subject_totals[row["subject"] or "General"][1] += total

    subject_scores = {
        subject: round((vals[0] / vals[1] * 100) if vals[1] else 0, 1)
        for subject, vals in subject_totals.items()
    }

    c.execute("SELECT COUNT(*) AS total FROM flashcard_progress WHERE user_id = ?", (user_id,))
    flashcards_due = int(c.fetchone()["total"] or 0)

    c.execute("SELECT icon, text, badge, badge_color, created_at FROM activity_log WHERE user_id = ? ORDER BY created_at DESC LIMIT 8", (user_id,))
    activities = []
    for row in c.fetchall():
        activities.append({
            "time": _relative_time(row["created_at"]),
            "icon": row["icon"],
            "text": row["text"],
            "badge": row["badge"],
            "badge_color": row["badge_color"],
        })

    conn.close()

    if not mcq_sessions and total_mcq:
        mcq_sessions = [{"date": today.isoformat(), "accuracy": mcq_percent, "count": total_mcq}]

    return {
        "study_hours": study_hours,
        "sessions": total_sessions,
        "mcq_correct": correct,
        "mcq_total": total_mcq,
        "mcq_percent": mcq_percent,
        "streak": _current_streak(dict(daily_minutes)),
        "total_hours": study_hours,
        "mcqs_done": total_mcq,
        "current_score": mcq_percent or 72.0,
        "rank": 24,
        "daily_minutes": dict(daily_minutes),
        "mcq_sessions": mcq_sessions,
        "subject_scores": subject_scores,
        "goals": _default_goals(study_hours, total_mcq, flashcards_due, len(subject_scores)),
        "activities": activities,
        "target_score": 90.0,
        "target_exam": "OMSB Part 1",
    }


def _relative_time(value: str | None) -> str:
    try:
        then = datetime.fromisoformat((value or "").replace("Z", "+00:00"))
    except Exception:
        return "Recently"
    delta = datetime.now() - then.replace(tzinfo=None)
    if delta.days >= 1:
        return f"{delta.days} day{'s' if delta.days != 1 else ''} ago"
    hours = delta.seconds // 3600
    if hours:
        return f"{hours} hr ago"
    minutes = max(1, delta.seconds // 60)
    return f"{minutes} min ago"
