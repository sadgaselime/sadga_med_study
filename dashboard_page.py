"""
dashboard_page.py — MedStudy Oman 🩺
Phase 6: Analytics & Dashboard Engine
KPI cards · Knowledge Heatmap · Study Streak · MCQ Trends
Subject Radar · Score Progression · Goals · Activity Feed
"""

import streamlit as st
try:
    import plotly.graph_objects as go
    import plotly.express as px
except ModuleNotFoundError:
    go = None
    px = None
import random
import datetime
from collections import defaultdict


# ─────────────────────────────────────────────────────────────────────────────
# DEMO DATA GENERATOR  (used when real DB stats are sparse)
# ─────────────────────────────────────────────────────────────────────────────
def _generate_demo_stats(user: dict) -> dict:
    """Produce realistic-looking demo analytics data."""
    random.seed(42)
    today     = datetime.date.today()
    days_back = 365

    # Daily study minutes — last 365 days
    daily_minutes = {}
    for i in range(days_back):
        d = today - datetime.timedelta(days=i)
        if random.random() > 0.25:  # ~75% days studied
            mins = random.randint(20, 180)
        else:
            mins = 0
        daily_minutes[d.isoformat()] = mins

    # MCQ sessions — accuracy per session last 60 days
    mcq_sessions = []
    base_accuracy = 55.0
    for i in range(60):
        d     = today - datetime.timedelta(days=59 - i)
        acc   = min(95, base_accuracy + i * 0.5 + random.uniform(-8, 8))
        count = random.randint(10, 40)
        mcq_sessions.append({"date": d.isoformat(), "accuracy": round(acc, 1),
                              "count": count})

    # Subject performance (0–100 per subject)
    subjects = [
        "Cardiology", "Neurology", "Pulmonology", "Nephrology",
        "Gastro", "Endocrine", "Haematology", "Pharmacology",
        "Pathology", "Anatomy", "Physiology", "Microbiology",
    ]
    subject_scores = {s: random.randint(40, 95) for s in subjects}
    subject_scores["Cardiology"]   = 82
    subject_scores["Pharmacology"] = 74
    subject_scores["Pathology"]    = 88
    subject_scores["Anatomy"]      = 69

    # Mock exam scores
    mock_scores = []
    score = 58.0
    for i in range(12):
        d     = today - datetime.timedelta(days=330 - i * 28)
        score = min(92, score + random.uniform(0.5, 3.5))
        mock_scores.append({"date": d.isoformat(), "score": round(score, 1),
                             "exam": f"Mock {i+1}"})

    # Weekly goals
    goals = [
        {"label": "Study Hours",    "icon": "⏱️", "current": 14, "target": 20,
         "unit": "hrs", "color": "#e63946"},
        {"label": "MCQs Practiced", "icon": "📝", "current": 87, "target": 100,
         "unit": "Qs",  "color": "#10b981"},
        {"label": "Flashcards",     "icon": "🃏", "current": 45, "target": 50,
         "unit": "",    "color": "#8b5cf6"},
        {"label": "Subjects",       "icon": "📚", "current": 3,  "target": 5,
         "unit": "",    "color": "#f59e0b"},
    ]

    # Recent activity
    activities = [
        {"time": "2 min ago",  "icon": "📝", "text": "Completed 25-question Cardiology MCQ",
         "badge": "+25 pts",  "badge_color": "#10b981"},
        {"time": "1 hr ago",   "icon": "⏱️", "text": "Finished 25-min Pomodoro — Pharmacology",
         "badge": "🍅 ×1",   "badge_color": "#ef4444"},
        {"time": "3 hrs ago",  "icon": "🃏", "text": "Reviewed 30 Neurology flashcards",
         "badge": "SRS +1d",  "badge_color": "#8b5cf6"},
        {"time": "Yesterday",  "icon": "🩺", "text": "Completed OSCE — History Taking station",
         "badge": "✅ Done",  "badge_color": "#0891b2"},
        {"time": "Yesterday",  "icon": "💡", "text": "Added 3 mnemonics to Personal Vault",
         "badge": "🏦 Saved", "badge_color": "#f59e0b"},
        {"time": "2 days ago", "icon": "📖", "text": "Studied Pathology — Neoplasia chapter",
         "badge": "90 min",   "badge_color": "#7c3aed"},
        {"time": "3 days ago", "icon": "🤖", "text": "AI Tutor session — DKA pathophysiology",
         "badge": "Session",  "badge_color": "#ec4899"},
    ]

    # Streak calculation
