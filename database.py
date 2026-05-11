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
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            last_login TEXT
        )
    """)

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

    conn.commit()
    conn.close()


def signup_user(name, email, password, university="SQU", year=1):
    try:
        conn = _connect()
        c = conn.cursor()
        password_hash = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt()).decode("utf-8")
        c.execute("""
            INSERT INTO users (name, email, password_hash, university, year_of_study)
            VALUES (?, ?, ?, ?, ?)
        """, (name, email, password_hash, university, year))
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
                "created_at": user["created_at"],
                "last_login": user["last_login"],
            }
        conn.close()
        return False, "Incorrect password. Please try again."
    except Exception as e:
        return False, f"Error: {str(e)}"


def update_theme(user_id, theme_name):
    conn = _connect()
    c = conn.cursor()
    c.execute("UPDATE users SET theme = ? WHERE id = ?", (theme_name, user_id))
    conn.commit()
    conn.close()


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
        INSERT INTO activity_log (user_id, icon, text, badge, badge_color)
        VALUES (?, '📝', ?, ?, '#10b981')
    """, (user_id, f"Completed {total}-question {subject} MCQ set", f"{pct}%"))
    conn.commit()
    conn.close()


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
