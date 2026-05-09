"""
app.py — MedStudy Oman 🩺
PHASE: Absolute UI Layout Alignment
"""

import streamlit as st
import time
import random

# 1. Page Config (Must be the first Streamlit command)
st.set_page_config(
    page_title="MedStudy Oman",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Core imports ──────────────────────────────────────────────────────────────
from database import (
    init_db, signup_user, login_user,
    update_theme, save_study_session, get_user_stats,
)
from styles          import ThemeManager, THEMES
from login_page      import auth_page
from home_page       import home_page
from timer_enhanced  import timer_page
from about_page      import about_page
from ai_chat_page    import ai_tutor_page as ai_chat_tutor_page
from mcq_quiz_page   import mcq_quiz_page
from flashcards_page import flashcards_page

# Safe imports for mobile helper
try:
    from mobile import inject_mobile, render_bottom_nav
    HAS_MOBILE = True
except ImportError:
    HAS_MOBILE = False

# ── Feature modules ──────────────────────────────────────────────────────────
MODULES_LOADED = False
_MODULE_ERR    = ""
try:
    from subjects_page    import subjects_page
    from mnemonics_page   import mnemonics_page
    from dashboard_page   import dashboard_page
    from resources_page   import resources_page
    from osce_timer       import osce_timer_page
    from anatomy_3d       import anatomy_3d_page
    from lab_game         import lab_game_page
    MODULES_LOADED = True
except Exception as e:
    _MODULE_ERR = str(e)

init_db()

# ── Session State ────────────────────────────────────────────────────────────
def init_session():
    defaults = {
        "theme": "🩺 Clinical Snow",
        "language": "en",
        "logged_in": False,
        "user": None,
        "page": "home",
        "bookmarks": [],
        "ai_bubble_open": False,
        "vault_items": [],
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_session()

# ── Theme & Layout Loading ──────────────────────────────────────────────────
_tm = ThemeManager(st.session_state.theme)
theme = THEMES.get(st.session_state.theme, list(THEMES.values())[0])

# Apply general theme styles
st.markdown(_tm.inject(), unsafe_allow_html=True)

# 🚨 THE TOTAL LAYOUT REPAIR OVERRIDE 🚨
# This overrides the structural containers Streamlit uses to render the sidebar.
st.markdown(f"""
    <style>
        /* 1. Force the absolute outer container to align properly */
        [data-testid="stAppViewContainer"] {{
            display: flex !important;
            flex-direction: row !important;
            width: 100vw !important;
        }}

        /* 2. Target the main sidebar section */
        section[data-testid="stSidebar"] {{
            display: flex !important;
            visibility: visible !important;
            min-width: 290px !important;
            max-width: 290px !important;
            transform: translate3d(0px, 0px, 0px) !important;
            background-color: {theme.get("card_bg", "#ffffff")} !important;
            border-right: 1.5px solid {theme.get("card_border", "#e2e8f0")} !important;
        }}

        /* 3. Target the inner element containing actual sidebar widgets */
        [data-testid="stSidebarContent"] {{
            display: block !important;
            visibility: visible !important;
            opacity: 1 !important;
            width: 100% !important;
        }}

        /* 4. Kill the duplicate "ghost border" elements that cause double vertical lines */
        [data-testid="collapsedControl"],
        .st-emotion-cache-6qob1r, 
        .st-emotion-cache-16idsys, 
        .st-emotion-cache-1dp5vir,
        .st-emotion-cache-16idxsn {{
            border-right: none !important;
            box-shadow: none !important;
            display: none !important;
        }}

        /* 5. Force the main layout content wrapper to make room for our sidebar */
        [data-testid="stMainViewContainer"] {{
            margin-left: 0px !important;
            width: calc(100% - 290px) !important;
        }}
    </style>
""", unsafe_allow_html=True)

# ── Sidebar Content ──────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown(f"""
        <div style='padding:0.8rem 0 0.6rem; border-bottom:2px solid {theme["primary"]}; margin-bottom:0.8rem;'>
            <span style='font-family:Syne,sans-serif; font-size:1.2rem; font-weight:900; color:{theme["primary"]};'>MedStudy</span>
            <span style='font-family:Syne,sans-serif; font-size:1.2rem; font-weight:400; color:{theme["text"]};'>Oman 🩺</span><br>
            <span style='font-size:0.6rem; color:{theme["primary"]}; letter-spacing:0.12em; text-transform:uppercase; font-weight:700;'>AI · CLINICAL · 2026</span>
        </div>
    """, unsafe_allow_html=True)

    st.write("")

    # Simple Navigation
    st.caption("🧭 NAVIGATION")
    if st.button("🏠 Home Dashboard", use_container_width=True): 
        st.session_state.page = "home"; st.rerun()
    if st.button("📚 Subjects Hub", use_container_width=True): 
        st.session_state.page = "subjects"; st.rerun()
    if st.button("🃏 Flashcards", use_container_width=True): 
        st.session_state.page = "flashcards"; st.rerun()
    if st.button("🤖 AI Study Partner", use_container_width=True): 
        st.session_state.page = "ai_tutor"; st.rerun()

    st.divider()

    # Preferences
    st.caption("🎨 THEMING")
    theme_keys = list(THEMES.keys())
    sel_theme = st.selectbox(
        "Theme Select", theme_keys,
        index=theme_keys.index(st.session_state.theme),
        label_visibility="collapsed"
    )
    if sel_theme != st.session_state.theme:
        st.session_state.theme = sel_theme
        st.rerun()

# ── Page Routing ─────────────────────────────────────────────────────────────
page = st.session_state.page

if page == "auth":
    auth_page(theme, login_user, signup_user)
elif page == "home":
    home_page(theme, lambda x: x, [])
elif page == "subjects":
    if MODULES_LOADED: subjects_page(theme)
    else: st.error(f"Error loading subjects module: {_MODULE_ERR}")
elif page == "flashcards":
    flashcards_page(theme)
elif page == "ai_tutor":
    ai_chat_tutor_page(theme)
else:
    st.session_state.page = "home"
    st.rerun()
