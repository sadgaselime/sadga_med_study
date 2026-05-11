# File: app.py

"""
app.py — MedStudy Oman
ThemeManager · Auth · Animated Medical Home · Subject Hub · Dashboard · OSCE Timer
"""

import streamlit as st
from importlib import import_module

st.set_page_config(
    page_title="MedStudy Oman",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed",
)

from database import (
    init_db, signup_user, login_user,
    update_theme, get_user_stats,
)
from styles import ThemeManager, THEMES
from login_page import auth_page
from home_page import home_page
from timer_enhanced import timer_page
from about_page import about_page
from ai_chat_page import ai_tutor_page as ai_chat_tutor_page
from mcq_quiz_page import mcq_quiz_page
from flashcards_page import flashcards_page
from mobile import inject_mobile, render_bottom_nav

try:
    from content import MOTIVATIONAL_QUOTES
except ImportError:
    MOTIVATIONAL_QUOTES = [
        {"quote": "The art of medicine is in comforting.", "author": "Hippocrates"}
    ]

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
_optional_import("subjects_page", "subjects_page", "SUBJECTS_LIBRARY")
_optional_import("mnemonics_page", "mnemonics_page")
_optional_import("dashboard_page", "dashboard_page")
_optional_import("tips_page", "tips_page")
_optional_import("resources_page", "resources_page")

init_db()

TRANSLATIONS = {
    "en": {
        "app_title": "MedStudy Oman",
        "home": "Home",
        "subjects": "Subjects",
        "flashcards": "Flashcards",
        "pomodoro": "Pomodoro",
        "mnemonics": "Mnemonics",
        "mcq_quiz": "MCQ Quiz",
        "dashboard": "Dashboard",
        "tips": "Tips",
        "ai_tutor": "AI Tutor",
        "voice_ai": "Voice AI",
        "resources": "Resources",
        "profile": "My Profile",
        "login": "Login",
    },
    "ar": {
        "app_title": "الدراسة الطبية عُمان",
        "home": "الرئيسية",
        "subjects": "المواد",
        "flashcards": "البطاقات",
        "pomodoro": "المؤقت",
        "mnemonics": "وسائل الحفظ",
        "mcq_quiz": "الأسئلة",
        "dashboard": "لوحة التحكم",
        "tips": "نصائح",
        "ai_tutor": "المعلم الذكي",
        "voice_ai": "الذكاء الصوتي",
        "resources": "المراجع",
        "profile": "الملف الشخصي",
        "login": "تسجيل الدخول",
    },
}


def init_session():
    defaults = {
        "theme": "🩺 Clinical Snow",
        "language": "en",
        "logged_in": False,
        "user": None,
        "page": "home",
        "bookmarks": [],
        "timer_style": "radial",
        "sessions_completed": 0,
        "pomodoro_running": False,
        "pomo_duration": 25 * 60,
        "selected_subject": None,
        "show_auth": False,
        "auth_mode": "login",
        "ai_bubble_open": False,
        "ai_chat_history": [],
        "active_tab": 0,
        "vault_items": [],
        "pomo_start_time": None,
        "pomo_last_mode": None,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value


init_session()


def tr(key: str) -> str:
    return TRANSLATIONS[st.session_state.language].get(key, key)


if st.session_state.theme not in THEMES:
    st.session_state.theme = "🩺 Clinical Snow"

theme_manager = ThemeManager(st.session_state.theme)
theme = THEMES.get(st.session_state.theme, list(THEMES.values())[0])

st.markdown(theme_manager.inject(), unsafe_allow_html=True)
inject_mobile(theme)


def _render_ai_bubble():
    open_state = st.session_state.ai_bubble_open
    label = "✕" if open_state else "🤖"
    bg = theme["secondary"] if open_state else ""
    st.markdown(
        f'<div class="ai-bubble" style="{"background:" + bg if bg else ""}" '
        f'title="{"Close" if open_state else "Open"} AI Medical Tutor">{label}</div>',
        unsafe_allow_html=True,
    )


_render_ai_bubble()


brand_col, theme_col, lang_col, auth_col = st.columns([4, 2.5, 1.5, 1.6])

with brand_col:
    st.markdown(
        f"""
        <div style="font-family:Syne,sans-serif;font-size:1.15rem;font-weight:900;color:{theme['text']};">
            <span style="color:{theme['primary']};">MedStudy</span> Oman
            <span style="font-family:DM Sans,sans-serif;font-size:0.72rem;font-weight:800;color:{theme['subtext']};margin-left:10px;">
                AI Clinical Study Platform
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

with theme_col:
    theme_keys = list(THEMES.keys())
    selected_theme = st.selectbox(
        "Theme",
        theme_keys,
        index=theme_keys.index(st.session_state.theme),
        key="theme_sel_top",
        label_visibility="collapsed",
    )
    if selected_theme != st.session_state.theme:
        st.session_state.theme = selected_theme
        if st.session_state.logged_in:
            update_theme(st.session_state.user["id"], selected_theme)
        st.rerun()

with lang_col:
    lang_left, lang_right = st.columns(2)
    with lang_left:
        if st.button(
            "EN",
            use_container_width=True,
            type="primary" if st.session_state.language == "en" else "secondary",
            key="lang_en_top",
        ):
            st.session_state.language = "en"
            st.rerun()
    with lang_right:
        if st.button(
            "AR",
            use_container_width=True,
            type="primary" if st.session_state.language == "ar" else "secondary",
            key="lang_ar_top",
        ):
            st.session_state.language = "ar"
            st.rerun()

with auth_col:
    if st.session_state.logged_in:
        if st.button("Logout", use_container_width=True, key="top_logout"):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.session_state.page = "home"
            st.rerun()
    else:
        if st.button("Login", type="primary", use_container_width=True, key="top_login"):
            st.session_state.page = "auth"
            st.session_state.auth_mode = "login"
            st.rerun()


NAV_ITEMS = [
    ("🏠", "home", "Home"),
    ("📚", "subjects", "Library"),
    ("📝", "mcq_quiz", "MCQ"),
    ("🃏", "flashcards", "Cards"),
    ("🤖", "ai_tutor", "AI"),
    ("📊", "dashboard", "Analytics"),
    ("⏱️", "pomodoro", "Focus"),
    ("🩺", "osce_timer", "OSCE"),
    ("💡", "mnemonics", "Memos"),
    ("📖", "resources", "Refs"),
]

nav_cols = st.columns(len(NAV_ITEMS))

for col, (icon, page_id, label) in zip(nav_cols, NAV_ITEMS):
    with col:
        active = st.session_state.page == page_id
        if st.button(
            f"{icon} {label}",
            key=f"topnav_{page_id}",
            use_container_width=True,
            type="primary" if active else "secondary",
        ):
            st.session_state.page = page_id
            st.rerun()

st.markdown(
    f"<div style='height:1px;background:{theme['card_border']};margin:0.5rem 0 1.2rem;'></div>",
    unsafe_allow_html=True,
)


def _page_header(icon: str, title: str, subtitle: str = ""):
    st.markdown(
        f"""
        <div style="display:flex;align-items:center;gap:14px;margin-bottom:1.2rem;">
            <div style="width:48px;height:48px;border-radius:14px;background:{theme['gradient']};
                        display:flex;align-items:center;justify-content:center;font-size:1.6rem;
                        box-shadow:0 4px 16px {theme['primary_glow']};">
                {icon}
            </div>
            <div>
                <div style="font-family:Syne,sans-serif;font-size:1.7rem;font-weight:900;color:{theme['text']};">
                    {title}
                </div>
                <div style="font-size:0.8rem;color:{theme['subtext']};">
                    {subtitle}
                </div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_unavailable(label: str, module_name: str):
    reason = FEATURE_ERRORS.get(module_name, "This feature module did not load.")
    st.warning(f"{label} is unavailable right now.")
    st.caption(f"Module: {module_name} · {reason}")


def _require_login(redirect_page: str = "home"):
    st.warning("Login required.")
    if st.button("Sign In", type="primary", key=f"login_required_{redirect_page}"):
        st.session_state.page = "auth"
        st.session_state.auth_mode = "login"
        st.rerun()


def _render_profile():
    user = st.session_state.user
    _page_header("👤", f"Dr. {user['name']}", "Academic Analytics")
    st.info("Profile analytics and saved resources will appear here.")


page = st.session_state.page

if page == "auth":
    auth_page(theme, login_user, signup_user)

elif page == "home":
    home_page(theme, tr, MOTIVATIONAL_QUOTES)

elif page == "subjects":
    if "subjects_page" in globals():
        subjects_page(theme)
    else:
        _render_unavailable("Subjects", "subjects_page")

elif page == "flashcards":
    flashcards_page(theme)

elif page == "mnemonics":
    if "mnemonics_page" in globals():
        mnemonics_page(theme)
    else:
        _render_unavailable("Mnemonics", "mnemonics_page")

elif page == "mcq_quiz":
    mcq_quiz_page(theme)

elif page == "dashboard":
    db_stats = {}
    if st.session_state.logged_in:
        db_stats = get_user_stats(st.session_state.user["id"]) or {}
    else:
        st.info("📊 Showing demo data — login to see your personal analytics.")

    if "dashboard_page" in globals():
        dashboard_page(theme, db_stats)
    else:
        _render_unavailable("Dashboard", "dashboard_page")

elif page == "pomodoro":
    timer_page(theme)

elif page == "osce_timer":
    if "osce_timer_page" in globals():
        osce_timer_page(theme)
    else:
        timer_page(theme)

elif page == "ai_tutor":
    ai_chat_tutor_page(theme)

elif page == "voice_ai":
    _page_header("🎤", tr("voice_ai"), "Hands-free studying powered by speech recognition")
    st.info("Voice AI — coming soon.")

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

elif page == "resources":
    if "resources_page" in globals():
        resources_page(theme)
    else:
        _render_unavailable("Resources", "resources_page")

elif page == "progress":
    if not st.session_state.logged_in:
        _require_login("progress")
    elif "progress_tracker_page" in globals():
        progress_tracker_page(theme, get_user_stats(st.session_state.user["id"]))
    else:
        _render_unavailable("Progress", "progress_tracker")

elif page == "study_groups":
    if "study_groups_page" in globals():
        study_groups_page(
            theme,
            st.session_state.user if st.session_state.logged_in else None,
        )
    else:
        _render_unavailable("Study Groups", "study_groups")

elif page == "discussion":
    if "discussion_page" in globals():
        discussion_page(
            theme,
            st.session_state.user if st.session_state.logged_in else None,
        )
    else:
        _render_unavailable("Forums", "discussion")

elif page == "shared_notes":
    if "shared_notes_page" in globals():
        shared_notes_page(
            theme,
            st.session_state.user if st.session_state.logged_in else None,
        )
    else:
        _render_unavailable("Shared Notes", "shared_notes")

elif page == "leaderboards":
    if "leaderboards_page" in globals():
        leaderboards_page(
            theme,
            st.session_state.user if st.session_state.logged_in else None,
        )
    else:
        _render_unavailable("Leaderboards", "leaderboards")

elif page == "tips":
    if "tips_page" in globals():
        tips_page(theme)
    else:
        _render_unavailable("Study Tips", "tips_page")

elif page == "profile":
    if not st.session_state.logged_in:
        _require_login("profile")
    else:
        _render_profile()

elif page == "about":
    about_page(theme)

else:
    st.session_state.page = "home"
    st.rerun()

render_bottom_nav(theme)
