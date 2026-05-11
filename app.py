"""
app.py — MedStudy Oman 🩺
PHASES 1–5  (complete)
ThemeManager · Auth · Bento Home · Subject Hub · OSCE Timer · Developer Portfolio
"""

import streamlit as st
import time
import random
from importlib import import_module

st.set_page_config(
    page_title="MedStudy Oman",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

# ── Core imports ──────────────────────────────────────────────────────────────
from database import (
    init_db, signup_user, login_user,
    update_theme, save_study_session, get_user_stats,
)
from styles          import ThemeManager, THEMES
from login_page      import auth_page
from home_page       import home_page
from timer_enhanced      import timer_page
from about_page      import about_page
from ai_chat_page    import ai_tutor_page as ai_chat_tutor_page
from mcq_quiz_page   import mcq_quiz_page
from flashcards_page import flashcards_page
from mobile          import inject_mobile, render_bottom_nav   # Phase 9

try:
    from content import MOTIVATIONAL_QUOTES
except ImportError:
    MOTIVATIONAL_QUOTES = [{"quote": "The art of medicine is in comforting.", "author": "Hippocrates"}]

# ── Feature modules ───────────────────────────────────────────────────────────
# Import optional pages one-by-one so a missing dependency in one feature does
# not disable unrelated parts of the medical study platform.
FEATURE_ERRORS = {}


def _optional_import(module_name: str, *attrs: str):
    try:
        module = import_module(module_name)
    except Exception as exc:
        FEATURE_ERRORS[module_name] = str(exc)
        return

    for attr in attrs:
        try:
            globals()[attr] = getattr(module, attr)
        except AttributeError as exc:
            FEATURE_ERRORS[f"{module_name}.{attr}"] = str(exc)


try:
    from timer_enhanced import get_timer_html, get_timer_completion_animation
except ImportError:
    def get_timer_html(*a, **kw): return ""
    def get_timer_completion_animation(*a, **kw): return ""

try:
    from ai_features import ai_tutor_page as _legacy_ai   # kept for compatibility
except Exception as _e:
    FEATURE_ERRORS["ai_features"] = str(_e)

_optional_import("lab_game", "lab_game_page")
_optional_import("osce_timer", "osce_timer_page")
_optional_import("anatomy_3d", "anatomy_3d_page")
_optional_import("progress_tracker", "progress_tracker_page")
_optional_import("study_groups", "study_groups_page")
_optional_import("discussion", "discussion_page")
_optional_import("shared_notes", "shared_notes_page")
_optional_import("leaderboards", "leaderboards_page")
_optional_import("subjects_page", "subjects_page", "SUBJECTS_LIBRARY")
_optional_import("mnemonics_page", "mnemonics_page")
_optional_import("dashboard_page", "dashboard_page")
_optional_import("tips_page", "tips_page")
_optional_import("resources_page", "resources_page")

MODULES_LOADED = not FEATURE_ERRORS

init_db()

# ─────────────────────────────────────────────────────────────────────────────
# TRANSLATIONS
# ─────────────────────────────────────────────────────────────────────────────
TRANSLATIONS = {
    "en": {
        "app_title": "MedStudy Oman",        "tagline": "AI-Powered Medical Education",
        "home": "Home",                       "subjects": "Subjects",
        "flashcards": "Flashcards",           "pomodoro": "Pomodoro",
        "mnemonics": "Mnemonics",             "mcq_quiz": "MCQ Quiz",
        "dashboard": "Dashboard",             "tips": "Tips",
        "motivation": "Motivation",           "ai_tutor": "AI Tutor",
        "voice_ai": "Voice AI",               "resources": "Resources",
        "profile": "My Profile",             "login": "Login",
