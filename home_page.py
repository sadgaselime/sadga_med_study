"""
home_page.py — MedStudy Oman 🩺
Phase 3 (v3) — Clean Redesign
Hero · Stats · Module Grid · Quick Subjects
"""

import streamlit as st
import datetime
import random

ALL_MODULES = [
    ("📚", "subjects",     "Subjects",     "37 subjects A-Z",        "#e63946"),
    ("🃏", "flashcards",   "Flashcards",   "200+ SM-2 cards",        "#f59e0b"),
    ("📝", "mcq_quiz",     "MCQ Quiz",     "500+ practice Qs",       "#10b981"),
    ("💡", "mnemonics",    "Mnemonics",    "150+ memory anchors",    "#8b5cf6"),
    ("🤖", "ai_tutor",     "AI Tutor",     "Gemini AI powered",      "#06b6d4"),
    ("🎤", "voice_ai",     "Voice AI",     "Hands-free study",       "#ec4899"),
    ("⏱️", "pomodoro",     "Timer",        "3 display styles",       "#ef4444"),
    ("🩺", "osce_timer",   "OSCE Timer",   "12 station presets",     "#dc2626"),
    ("⚗️", "lab_game",     "Lab Game",     "2-min speed challenge",  "#84cc16"),
    ("🫁", "anatomy_3d",   "3D Anatomy",   "Interactive atlas",      "#0891b2"),
    ("📖", "resources",    "Resources",    "Books · Apps · Videos",  "#7c3aed"),
    ("📊", "dashboard",    "Dashboard",    "Analytics & heatmap",    "#16a34a"),
    ("👥", "study_groups", "Study Groups", "Collaborate with peers", "#f97316"),
    ("💬", "discussion",   "Forums",       "Case discussions",       "#0d9488"),
    ("📋", "shared_notes", "Shared Notes", "Crowd-sourced revision", "#6366f1"),
    ("🏆", "leaderboards", "Leaderboard",  "National rankings",      "#d97706"),
    ("💡", "tips",         "Study Tips",   "High-yield strategies",  "#4f46e5"),
    ("🏅", "about",        "About",        "Meet the developer",     "#9ca3af"),
]

FEATURED_SUBJECTS = [
    ("❤️","Cardiology"), ("🧠","Neurology"), ("🫁","Pulmonology"),
    ("💊","Pharmacology"), ("🔬","Pathology"), ("🧬","Biochemistry"),
    ("🦴","Anatomy"), ("⚕️","Int. Medicine"), ("🔪","Surgery"),
    ("👶","Paediatrics"), ("🤰","Obs & Gynae"), ("🦠","Inf. Disease"),
]


def home_page(theme: dict, tr, motivational_quotes: list):
    _inject_home_css(theme)
    _hero(theme)
    _stats(theme)
    _cta_buttons()
    _module_grid(theme)
    _subject_strip(theme)


def _inject_home_css(t: dict):
    st.markdown(f"""
    <style>
    div[data-testid="stHorizontalBlock"] .stButton > button {{
        background:    {t["card_bg"]} !important;
        border:        1.5px solid {t["card_border"]} !important;
        border-radius: 16px !important;
        padding:       0.9rem 0.5rem 0.8rem !important;
        font-weight:   700 !important;
        font-size:     0.78rem !important;
        color:         {t["text"]} !important;
        text-align:    center !important;
        white-space:   pre-wrap !important;
        min-height:    74px !important;
        line-height:   1.4 !important;
        transition:    all 0.2s ease !important;
        backdrop-filter: blur(8px);
    }}
    div[data-testid="stHorizontalBlock"] .stButton > button:hover {{
        background:    {t["primary"]}12 !important;
        border-color:  {t["primary"]}70 !important;
        color:         {t["primary"]} !important;
        transform:     translateY(-3px) !important;
        box-shadow:    0 6px 20px {t["primary"]}18 !important;
    }}
    </style>
    """, unsafe_allow_html=True)


def _hero(t: dict):
    now   = datetime.datetime.now()
    hour  = now.hour
    if hour < 12:   greet, ico = "Good Morning",   "☀️"
    elif hour < 17: greet, ico = "Good Afternoon", "🌤️"
    elif hour < 21: greet, ico = "Good Evening",   "🌅"
    else:           greet, ico = "Night Session",  "🌙"

    user  = st.session_state.get("user") or {}
    first = (user.get("name") or "Doctor").split()[0]
    date  = now.strftime("%A, %d %B %Y")
    p     = t["primary"]
    op    = "0.07" if t["family"] != "dark" else "0.1
