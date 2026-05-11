"""
app.py - MedStudy Oman premium AI medical learning platform.
"""

from __future__ import annotations

from importlib import import_module

import streamlit as st

st.set_page_config(
    page_title="MedStudy Oman",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

from database import get_profile_overview, get_user_preferences, init_db, login_user, reset_password, signup_user
from login_page import auth_page
from styles import THEMES, ThemeManager
from mobile import inject_mobile, render_bottom_nav
from timer_enhanced import timer_page
from mcq_quiz_page import mcq_quiz_page
from flashcards_page import flashcards_page
from ai_chat_page import ai_tutor_page as ai_chat_tutor_page
from about_page import about_page
from premium_platform import (
    apply_rtl_if_arabic,
    get_translation,
    inject_premium_css,
    render_bookmarks,
    render_dashboard,
    render_profile_dashboard,
    render_settings,
    render_sidebar,
    render_subject_page,
    render_topbar,
    render_ai_mnemonics,
)

try:
    from content import MOTIVATIONAL_QUOTES
except ImportError:
    MOTIVATIONAL_QUOTES = [{"quote": "The art of medicine is in comforting.", "author": "Hippocrates"}]


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


_optional_import("lab_game", "lab_game_page")
_optional_import("osce_timer", "osce_timer_page")
_optional_import("anatomy_3d", "anatomy_3d_page")
_optional_import("progress_tracker", "progress_tracker_page")
_optional_import("study_groups", "study_groups_page")
_optional_import("discussion", "discussion_page")
_optional_import("shared_notes", "shared_notes_page")
_optional_import("leaderboards", "leaderboards_page")
_optional_import("subjects_page", "subjects_page")
_optional_import("dashboard_page", "dashboard_page")
_optional_import("tips_page", "tips_page")
_optional_import("resources_page", "resources_page")


def init_session():
    defaults = {
        "theme": "🌸 Light Lavender",
        "language": "en",
        "logged_in": False,
        "user": None,
        "page": "dashboard",
        "auth_mode": "login",
        "selected_subject": None,
        "ai_chat_history": [],
        "daily_goal_minutes": 60,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


def _load_profile_preferences_once():
    if not st.session_state.get("logged_in") or not st.session_state.get("user"):
        return
    if st.session_state.get("preferences_loaded_for") == st.session_state.user["id"]:
        return
    prefs = get_user_preferences(st.session_state.user["id"])
    st.session_state.theme = prefs.get("theme", st.session_state.theme)
    st.session_state.language = prefs.get("language", st.session_state.language)
    if prefs.get("daily_goal_minutes"):
        try:
            st.session_state.daily_goal_minutes = int(prefs["daily_goal_minutes"])
        except ValueError:
            pass
    st.session_state.preferences_loaded_for = st.session_state.user["id"]


def _render_unavailable(label: str, module_name: str):
    reason = FEATURE_ERRORS.get(module_name, "This feature module did not load.")
    st.warning(f"{label} is unavailable right now.")
    st.caption(f"Module: {module_name} - {reason}")


def _demo_stats():
    return {
        "streak": 4,
        "study_hours": 18.5,
        "mcq_percent": 78.0,
        "overall_progress": 46,
        "weak_areas": ["Renal acid-base", "Antimicrobial coverage", "ECG rhythm recognition"],
        "strong_areas": ["Anatomy", "Pathology", "Clinical reasoning"],
        "activities": [
            {"time": "Today", "text": "Reviewed cardiovascular OSCE checklist"},
            {"time": "Yesterday", "text": "Completed 20 pharmacology MCQs"},
            {"time": "2 days ago", "text": "Saved brachial plexus high-yield notes"},
        ],
    }


init_db()
init_session()

query_page = st.query_params.get("page")
valid_pages = {
    "dashboard", "profile", "az_hub", "subjects", "mcq_quiz", "flashcards",
    "ai_tutor", "ai_mnemonics", "osce_timer", "pomodoro", "analytics",
    "resources", "shared_notes", "settings",
}
if query_page in valid_pages and query_page != st.session_state.get("page"):
    st.session_state.page = query_page

_load_profile_preferences_once()

if st.session_state.theme not in THEMES:
    st.session_state.theme = "🌸 Light Lavender"

theme_manager = ThemeManager(st.session_state.theme)
theme = THEMES.get(st.session_state.theme, THEMES["🌸 Light Lavender"])

st.markdown(theme_manager.inject(), unsafe_allow_html=True)
inject_mobile(theme)
inject_premium_css(theme)
apply_rtl_if_arabic()

render_topbar(theme, THEMES)
if st.session_state.page != "auth":
    render_sidebar()

page = st.session_state.page

if page == "auth":
    auth_page(theme, login_user, signup_user)
    with st.expander("Forgot password"):
        reset_email = st.text_input("Account email", key="reset_email")
        reset_pass = st.text_input("New password", type="password", key="reset_password")
        if st.button("Update password", type="primary", key="reset_password_submit"):
            ok, message = reset_password(reset_email, reset_pass)
            if ok:
                st.success(message)
            else:
                st.error(message)

elif page == "dashboard":
    stats = get_profile_overview(st.session_state.user["id"]) if st.session_state.get("logged_in") else _demo_stats()
    render_dashboard(stats)

elif page in {"subjects", "az_hub"}:
    render_subject_page()

elif page == "mcq_quiz":
    mcq_quiz_page(theme)

elif page == "flashcards":
    flashcards_page(theme)

elif page == "ai_tutor":
    ai_chat_tutor_page(theme)

elif page == "analytics":
    if st.session_state.get("logged_in") and "dashboard_page" in globals():
        dashboard_page(theme, get_profile_overview(st.session_state.user["id"]))
    elif st.session_state.get("logged_in"):
        render_profile_dashboard()
    else:
        st.info("Showing demo performance insights. Login to see private analytics.")
        render_dashboard(_demo_stats())

elif page == "pomodoro":
    timer_page(theme)

elif page == "osce_timer":
    if "osce_timer_page" in globals():
        osce_timer_page(theme)
    else:
        timer_page(theme)

elif page == "shared_notes":
    if "shared_notes_page" in globals():
        shared_notes_page(theme, st.session_state.user if st.session_state.get("logged_in") else None)
    else:
        render_bookmarks()

elif page == "resources":
    if "resources_page" in globals():
        resources_page(theme)
    else:
        _render_unavailable("Medical References", "resources_page")

elif page == "ai_mnemonics":
    render_ai_mnemonics()

elif page == "profile":
    render_profile_dashboard()
    render_bookmarks()

elif page == "settings":
    render_settings(THEMES)

elif page == "lab_game":
    if "lab_game_page" in globals():
        lab_game_page(theme)
    else:
        _render_unavailable("Lab Game", "lab_game")

elif page == "anatomy_3d":
    if "anatomy_3d_page" in globals():
        anatomy_3d_page(theme)
    else:
        _render_unavailable("3D Anatomy", "anatomy_3d")

elif page == "study_groups":
    if "study_groups_page" in globals():
        study_groups_page(theme, st.session_state.user if st.session_state.get("logged_in") else None)
    else:
        _render_unavailable("Study Groups", "study_groups")

elif page == "discussion":
    if "discussion_page" in globals():
        discussion_page(theme, st.session_state.user if st.session_state.get("logged_in") else None)
    else:
        _render_unavailable("Forums", "discussion")

elif page == "leaderboards":
    if "leaderboards_page" in globals():
        leaderboards_page(theme, st.session_state.user if st.session_state.get("logged_in") else None)
    else:
        _render_unavailable("Leaderboards", "leaderboards")

elif page == "tips":
    if "tips_page" in globals():
        tips_page(theme)
    else:
        _render_unavailable("Study Tips", "tips_page")

elif page == "about":
    about_page(theme)

else:
    st.session_state.page = "dashboard"
    st.rerun()

st.markdown(f'<div class="disclaimer">{get_translation("educational_only")}</div>', unsafe_allow_html=True)
render_bottom_nav(theme)
