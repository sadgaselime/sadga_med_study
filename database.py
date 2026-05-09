"""
database.py — Handles all user data, login, signup, and progress saving.
Think of this as the "memory" of your app.
"""

import sqlite3
import bcrypt
import json
from datetime import datetime

DB_NAME = "medstudy_oman.db"

# ─────────────────────────────────────────
# 1. INITIALISE DATABASE (runs on startup)
# ─────────────────────────────────────────
def init_db():
    """Creates all tables if they don't exist yet."""
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Users table
    c.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL,
            email TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL,
            university TEXT DEFAULT 'SQU',
            year_of_study INTEGER DEFAULT 1,
            theme TEXT DEFAULT 'Neural Purple',
            created_at TEXT DEFAULT CURRENT_TIMESTAMP,
            last_login TEXT
        )
    """)

    # Flashcard progress table
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

    # MCQ attempts table
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

    # Study sessions (Pomodoro)
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

    conn.commit()
    conn.close()


# ─────────────────────────────────────────
# 2. SIGNUP
# ─────────────────────────────────────────
def signup_user(name, email, password, university="SQU", year=1):
    """
    Creates a new user account.
    Returns (True, "Success") or (False, "Error message")
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()

        # Hash the password so it's never stored as plain text
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


# ─────────────────────────────────────────
# 3. LOGIN
# ─────────────────────────────────────────
def login_user(email, password):
    """
    Checks email + password.
    Returns (True, user_dict) or (False, "Error message")
    """
    try:
        conn = sqlite3.connect(DB_NAME)
        c = conn.cursor()

        c.execute("SELECT * FROM users WHERE email = ?", (email,))
        user = c.fetchone()

        if not user:
            conn.close()
            return False, "No account found with this email."

        # Check password against the stored hash
        stored_hash = user[3].encode("utf-8")
        if bcrypt.checkpw(password.encode("utf-8"), stored_hash):
            # Update last login time
            c.execute("UPDATE users SET last_login = ? WHERE id = ?",
                     (datetime.now().isoformat(), user[0]))
            conn.commit()
            conn.close()

            user_dict = {
                "id": user[0],
                "name": user[1],
                "email": user[2],
                "university": user[4],
                "year": user[5],
                "theme": user[6],
                "created_at": user[7],
                "last_login": user[8],
            }
            return True, user_dict
        else:
            conn.close()
            return False, "Incorrect password. Please try again."

    except Exception as e:
        return False, f"Error: {str(e)}"


# ─────────────────────────────────────────
# 4. UPDATE USER THEME
# ─────────────────────────────────────────
def update_theme(user_id, theme_name):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("UPDATE users SET theme = ? WHERE id = ?", (theme_name, user_id))
    conn.commit()
    conn.close()


# ─────────────────────────────────────────
# 5. SAVE STUDY SESSION
# ─────────────────────────────────────────
def save_study_session(user_id, subject, duration_minutes):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        INSERT INTO study_sessions (user_id, subject, duration_minutes)
        VALUES (?, ?, ?)
    """, (user_id, subject, duration_minutes))
    conn.commit()
    conn.close()


# ─────────────────────────────────────────
# 6. GET USER STATS
# ─────────────────────────────────────────
def get_user_stats(user_id):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()

    # Total study minutes
    c.execute("SELECT SUM(duration_minutes) FROM study_sessions WHERE user_id = ?", (user_id,))
    total_minutes = c.fetchone()[0] or 0

    # Total sessions
    c.execute("SELECT COUNT(*) FROM study_sessions WHERE user_id = ?", (user_id,))
    total_sessions = c.fetchone()[0] or 0

    # MCQ stats
    c.execute("SELECT SUM(correct), SUM(total) FROM mcq_attempts WHERE user_id = ?", (user_id,))
    mcq_row = c.fetchone()
    correct = mcq_row[0] or 0
    total_mcq = mcq_row[1] or 0

    conn.close()
    return {
        "study_hours": round(total_minutes / 60, 1),
        "sessions": total_sessions,
        "mcq_correct": correct,
        "mcq_total": total_mcq,
        "mcq_percent": round((correct / total_mcq * 100) if total_mcq > 0 else 0, 1)
    }


# ─────────────────────────────────────────
# 7. SAVE MCQ ATTEMPT
# ─────────────────────────────────────────
def save_mcq_attempt(user_id, subject, correct, total):
    conn = sqlite3.connect(DB_NAME)
    c = conn.cursor()
    c.execute("""
        INSERT INTO mcq_attempts (user_id, subject, correct, total)
        VALUES (?, ?, ?, ?)
    """, (user_id, subject, correct, total))
    conn.commit()
    conn.close()