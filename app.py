"""
app.py — MedStudy Oman 🩺 ✦ Next-Generation Premium Platform
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Glassmorphism · Bento Grid · 15 Medical Themes · AI-Powered
The future of medical education software.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

import streamlit as st
import time
import random

st.set_page_config(
    page_title="MedStudy Oman",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Core imports ────────────────────────────────────f───────────────────────────
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
from mobile          import inject_mobile, render_bottom_nav

try:
    from content import MOTIVATIONAL_QUOTES
except ImportError:
    MOTIVATIONAL_QUOTES = [{"quote": "The art of medicine is in comforting.", "author": "Hippocrates"}]

# ── Feature modules ────────────────────────────────────────────────────────────
MODULES_LOADED = False
_MODULE_ERR    = ""
try:
    try:
        from timer_enhanced import get_timer_html, get_timer_completion_animation
    except ImportError:
        def get_timer_html(*a, **kw): return ""
        def get_timer_completion_animation(*a, **kw): return ""
    try:
        from ai_features import ai_tutor_page as _legacy_ai
    except ImportError:
        pass
    from lab_game         import lab_game_page
    from osce_timer       import osce_timer_page
    from anatomy_3d       import anatomy_3d_page
    from progress_tracker import progress_tracker_page
    from study_groups     import study_groups_page
    from discussion       import discussion_page
    from shared_notes     import shared_notes_page
    from leaderboards     import leaderboards_page
    from subjects_page    import subjects_page, SUBJECTS_LIBRARY
    from mnemonics_page   import mnemonics_page
    from dashboard_page   import dashboard_page
    from tips_page        import tips_page
    from resources_page   import resources_page
    MODULES_LOADED = True
except Exception as _e:
    _MODULE_ERR = str(_e)

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
        "signup": "Sign Up",                 "logout": "Logout",
        "welcome": "Welcome, Doctor",        "choose_language": "Language",
        "study_smart": "Study Medicine the Smart Way",
        "complete_platform": "Complete AI-powered platform for Omani medical students",
        "theme_selector": "Theme",           "email": "Email",
        "password": "Password",              "full_name": "Full Name",
        "university": "University",          "year": "Year",
        "confirm_password": "Confirm Password",
        "cancel": "Cancel",                  "account_created": "Account created!",
        "please_login": "Please login to view your profile",
        "choose_timer": "Choose Timer Style", "mode": "Mode",
        "subject": "Subject",               "start": "Start",
        "pause": "Pause",                   "reset": "Reset",
        "coming_soon": "Coming soon!",      "sessions": "Sessions",
        "medical_subjects": "Medical Subjects", "total_mcqs": "Total MCQs",
        "ai_tools": "AI Tools",             "beautiful_themes": "Themes",
        "study_hours": "Study Hours",       "bookmarks": "Bookmarks",
        "progress": "Progress",             "no_bookmarks": "No bookmarks yet!",
    },
    "ar": {
        "app_title": "الدراسة الطبية عُمان", "tagline": "منصة التعليم الطبي بالذكاء الاصطناعي",
        "home": "الرئيسية",                  "subjects": "المواد",
        "flashcards": "البطاقات",            "pomodoro": "المؤقت",
        "mnemonics": "وسائل الحفظ",          "mcq_quiz": "الأسئلة",
        "dashboard": "لوحة التحكم",          "tips": "نصائح",
        "motivation": "تحفيز",               "ai_tutor": "المعلم الذكي",
        "voice_ai": "الذكاء الصوتي",         "resources": "المراجع",
        "profile": "الملف الشخصي",          "login": "تسجيل الدخول",
        "signup": "التسجيل",                "logout": "خروج",
        "welcome": "مرحباً، دكتور",          "choose_language": "اللغة",
        "study_smart": "ادرس الطب بذكاء",
        "complete_platform": "منصة كاملة بالذكاء الاصطناعي للطلاب العمانيين",
        "theme_selector": "الثيم",           "email": "البريد الإلكتروني",
        "password": "كلمة المرور",           "full_name": "الاسم الكامل",
        "university": "الجامعة",             "year": "السنة",
        "confirm_password": "تأكيد كلمة المرور",
        "cancel": "إلغاء",                  "account_created": "تم إنشاء الحساب!",
        "please_login": "يرجى تسجيل الدخول",
        "choose_timer": "اختر نمط المؤقت",   "mode": "الوضع",
        "subject": "المادة",                "start": "ابدأ",
        "pause": "إيقاف",                   "reset": "إعادة",
        "coming_soon": "قريباً!",            "sessions": "الجلسات",
        "medical_subjects": "المواد الطبية", "total_mcqs": "إجمالي الأسئلة",
        "ai_tools": "أدوات الذكاء",         "beautiful_themes": "ثيمات",
        "study_hours": "ساعات الدراسة",     "bookmarks": "الإشارات المرجعية",
        "progress": "التقدم",               "no_bookmarks": "لا توجد إشارات بعد!",
    },
}


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def init_session():
    defaults = {
        "theme":              "🌌 Midnight Rounds",
        "language":           "en",
        "logged_in":          False,
        "user":               None,
        "page":               "home",
        "bookmarks":          [],
        "timer_style":        "radial",
        "sessions_completed": 0,
        "pomodoro_running":   False,
        "pomo_duration":      25 * 60,
        "selected_subject":   None,
        "show_auth":          False,
        "auth_mode":          "login",
        "ai_bubble_open":     False,
        "ai_chat_history":    [],
        "active_tab":         0,
        "vault_items":        [],
        "pomo_start_time":    None,
        "pomo_last_mode":     None,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v

init_session()


def tr(key: str) -> str:
    return TRANSLATIONS[st.session_state.language].get(key, key)


# ─────────────────────────────────────────────────────────────────────────────
# INJECT THEME
# ─────────────────────────────────────────────────────────────────────────────
_tm   = ThemeManager(st.session_state.theme)
theme = THEMES.get(st.session_state.theme, list(THEMES.values())[0])
st.markdown(_tm.inject(), unsafe_allow_html=True)
inject_mobile(theme)

# Welcome toast
if st.session_state.get("just_logged_in") and st.session_state.logged_in:
    _u = st.session_state.user
    st.toast(f"🩺 Welcome, Dr. {_u['name']}! Ready to study?", icon="✅")
    st.session_state.just_logged_in = False


# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR NAVIGATION — PREMIUM REDESIGN
# ─────────────────────────────────────────────────────────────────────────────

# Grouped navigation structure
NAV_GROUPS = [
    {
        "label": "Core",
        "items": [
            ("🏠", "home",      "Home"),
            ("📊", "dashboard", "Dashboard"),
            ("👤", "profile",   "My Profile"),
        ]
    },
    {
        "label": "Study",
        "items": [
            ("📚", "subjects",  "Subjects"),
            ("🃏", "flashcards","Flashcards"),
            ("💡", "mnemonics", "Mnemonics"),
            ("📝", "mcq_quiz",  "MCQ Quiz"),
            ("📖", "resources", "Resources"),
            ("💡", "tips",      "Study Tips"),
        ]
    },
    {
        "label": "Tools",
        "items": [
            ("⏱️", "pomodoro",  "Pomodoro Timer"),
            ("🩺", "osce_timer","OSCE Timer"),
            ("🤖", "ai_tutor",  "AI Tutor"),
            ("🎤", "voice_ai",  "Voice AI"),
            ("⚗️", "lab_game",  "Lab Game"),
            ("🫁", "anatomy_3d","3D Anatomy"),
        ]
    },
    {
        "label": "Community",
        "items": [
            ("📈", "progress",     "Progress"),
            ("👥", "study_groups", "Study Groups"),
            ("💬", "discussion",   "Forums"),
            ("📋", "shared_notes", "Shared Notes"),
            ("🏆", "leaderboards", "Leaderboards"),
        ]
    },
    {
        "label": "More",
        "items": [
            ("🏅", "about", "About"),
        ]
    },
]

# Force sidebar open via JS
import streamlit.components.v1 as _components
_components.html("""
<script>
try {
    var p = window.parent.document;
    var sb = p.querySelector('section[data-testid="stSidebar"]');
    if (sb) {
        sb.style.setProperty('display','flex','important');
        sb.style.setProperty('visibility','visible','important');
        sb.style.setProperty('min-width','260px','important');
        sb.style.setProperty('transform','none','important');
    }
    var ctrl = p.querySelector('[data-testid="collapsedControl"]');
    if (ctrl) ctrl.style.setProperty('display','flex','important');
    var sidebar = p.querySelector('[data-testid="stSidebar"]');
    if (sidebar && sidebar.getAttribute('aria-expanded') === 'false') {
        ctrl && ctrl.click();
    }
} catch(e) {}
</script>
""", height=0, scrolling=False)

# ── Sidebar Content ────────────────────────────────────────────────────────────
p   = theme["primary"]
sb  = theme["sidebar_bg"]
txt = theme["text"]
is_dark = theme.get("family") == "dark"
sidebar_text  = "#e8f4ff" if is_dark else "#f0f4ff"
sidebar_sub   = "rgba(232,244,255,0.50)" if is_dark else "rgba(240,244,255,0.60)"
sidebar_group = "rgba(232,244,255,0.32)" if is_dark else "rgba(240,244,255,0.45)"
sa = theme.get("sidebar_accent", p)

with st.sidebar:

    # ── Branding ──────────────────────────────────────────────────────────────
    st.markdown(f"""
    <div style="padding:1.2rem 0.4rem 1rem;margin-bottom:0.2rem;">
        <div style="display:flex;align-items:center;gap:10px;margin-bottom:0.6rem;">
            <div style="width:38px;height:38px;border-radius:10px;
                background:linear-gradient(135deg,{sa},{p});
                display:flex;align-items:center;justify-content:center;
                font-size:1.3rem;box-shadow:0 4px 16px {theme['primary_glow']};">🩺</div>
            <div>
                <div style="font-family:'Bricolage Grotesque',sans-serif;
                    font-size:1.05rem;font-weight:900;
                    color:{sidebar_text};line-height:1.1;">MedStudy</div>
                <div style="font-family:'Bricolage Grotesque',sans-serif;
                    font-size:0.78rem;font-weight:400;
                    color:{sa};">Oman ✦ 2026</div>
            </div>
        </div>
        <div style="height:1px;background:linear-gradient(90deg,{sa}55,transparent);margin-top:0.4rem;"></div>
    </div>
    """, unsafe_allow_html=True)

    # ── User Card ─────────────────────────────────────────────────────────────
    if st.session_state.logged_in:
        u = st.session_state.user
        initials = "".join(w[0].upper() for w in u["name"].split()[:2])
        streak = st.session_state.get("sessions_completed", 0)
        st.markdown(f"""
        <div style="margin:0.4rem 0 0.8rem;padding:0.9rem;
            background:rgba(255,255,255,0.06);
            border:1px solid rgba(255,255,255,0.10);
            border-radius:14px;backdrop-filter:blur(12px);">
            <div style="display:flex;align-items:center;gap:10px;margin-bottom:0.5rem;">
                <div style="width:36px;height:36px;border-radius:10px;
                    background:{theme['gradient']};
                    display:flex;align-items:center;justify-content:center;
                    font-family:'Bricolage Grotesque',sans-serif;
                    font-size:0.9rem;font-weight:900;
                    color:{theme['text_inverse']};flex-shrink:0;">{initials}</div>
                <div style="overflow:hidden;">
                    <div style="font-family:'Bricolage Grotesque',sans-serif;
                        font-size:0.88rem;font-weight:800;
                        color:{sidebar_text};
                        white-space:nowrap;overflow:hidden;text-overflow:ellipsis;">
                        Dr. {u['name']}</div>
                    <div style="font-size:0.68rem;color:{sa};font-weight:600;
                        letter-spacing:0.06em;text-transform:uppercase;">
                        {u.get('university','SQU')}</div>
                </div>
            </div>
            <div style="display:flex;gap:6px;flex-wrap:wrap;">
                <span style="background:{sa}22;border:1px solid {sa}44;
                    border-radius:999px;padding:2px 8px;
                    font-size:0.68rem;font-weight:700;color:{sa};">
                    🔥 {streak} sessions</span>
                <span style="background:rgba(255,255,255,0.08);border:1px solid rgba(255,255,255,0.12);
                    border-radius:999px;padding:2px 8px;
                    font-size:0.68rem;font-weight:600;color:{sidebar_sub};">
                    Year {u.get('year','—')}</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
        <div style="margin:0.4rem 0 0.8rem;padding:0.85rem;
            background:rgba(255,255,255,0.05);
            border:1px solid rgba(255,255,255,0.10);
            border-radius:14px;text-align:center;">
            <div style="font-size:0.8rem;color:{sidebar_sub};margin-bottom:0.4rem;">
                Sign in to track your progress</div>
        </div>
        """, unsafe_allow_html=True)
        lc, rc = st.columns(2)
        with lc:
            if st.button("🔑 Login", use_container_width=True,
                         type="primary", key="sb_login"):
                st.session_state.page = "auth"
                st.session_state.auth_mode = "login"
                st.rerun()
        with rc:
            if st.button("📝 Sign Up", use_container_width=True, key="sb_signup"):
                st.session_state.page = "auth"
                st.session_state.auth_mode = "signup"
                st.rerun()

    # ── Navigation Groups ──────────────────────────────────────────────────────
    cur_page = st.session_state.page
    for group in NAV_GROUPS:
        st.markdown(f"""
        <div style="margin:0.7rem 0 0.25rem;
            font-size:0.6rem;font-weight:800;
            letter-spacing:0.14em;text-transform:uppercase;
            color:{sidebar_group};padding-left:4px;">{group['label']}</div>
        """, unsafe_allow_html=True)
        for ico, page_id, label in group["items"]:
            active = cur_page == page_id
            if active:
                st.markdown(f"""
                <div style="display:flex;align-items:center;gap:9px;
                    padding:0.55rem 0.9rem;margin-bottom:2px;
                    border-radius:12px;
                    background:{sa}18;
                    border-left:3px solid {sa};
                    padding-left:calc(0.9rem - 3px);">
                    <span style="font-size:1rem;">{ico}</span>
                    <span style="font-family:'Plus Jakarta Sans',sans-serif;
                        font-size:0.88rem;font-weight:700;
                        color:{sidebar_text};">{label}</span>
                    <div style="margin-left:auto;width:5px;height:5px;
                        border-radius:50%;background:{sa};
                        box-shadow:0 0 8px {sa};"></div>
                </div>
                """, unsafe_allow_html=True)
            else:
                if st.button(
                    f"{ico}  {label}",
                    key=f"nav_{page_id}",
                    use_container_width=True,
                ):
                    st.session_state.page = page_id
                    st.rerun()

    # ── Settings Area ──────────────────────────────────────────────────────────
    st.markdown(f"""
    <div style="height:1px;
        background:linear-gradient(90deg,transparent,{sa}44,transparent);
        margin:0.8rem 0 0.6rem;"></div>
    """, unsafe_allow_html=True)

    # Language
    st.markdown(f"""
    <div style="font-size:0.6rem;font-weight:800;letter-spacing:0.14em;
        text-transform:uppercase;color:{sidebar_group};
        margin-bottom:0.35rem;padding-left:4px;">Language</div>
    """, unsafe_allow_html=True)
    lc1, lc2 = st.columns(2)
    with lc1:
        if st.button(
            "🇬🇧 EN",
            use_container_width=True,
            type="primary" if st.session_state.language == "en" else "secondary",
            key="lang_en",
        ):
            st.session_state.language = "en"; st.rerun()
    with lc2:
        if st.button(
            "🇴🇲 AR",
            use_container_width=True,
            type="primary" if st.session_state.language == "ar" else "secondary",
            key="lang_ar",
        ):
            st.session_state.language = "ar"; st.rerun()

    st.write("")

    # Theme Selector — Premium with category labels
   # Theme Selector — Premium with category labels
st.markdown(f"""
<div style="font-size:0.6rem;font-weight:800;letter-spacing:0.14em;
    text-transform:uppercase;color:{sidebar_group};
    margin-bottom:0.35rem;padding-left:4px;">Aesthetic Theme</div>
""", unsafe_allow_html=True)

theme_keys = list(THEMES.keys())

# Safe theme initialization
if "theme" not in st.session_state:
    st.session_state.theme = theme_keys[0]

# Prevent invalid theme crash
if st.session_state.theme not in theme_keys:
    st.session_state.theme = theme_keys[0]

sel_theme = st.selectbox(
    "Aesthetic Theme",
    theme_keys,
    index=theme_keys.index(st.session_state.theme),
    key="theme_sel",
    label_visibility="collapsed",
)

if sel_theme != st.session_state.theme:
    st.session_state.theme = sel_theme

    if st.session_state.logged_in:
        try:
            update_theme(st.session_state.user["id"], sel_theme)
        except Exception:
            pass

    st.rerun()

    # Theme preview swatch
    _t = THEMES[sel_theme]
    _colors = [_t["primary"], _t.get("secondary", _t["primary"]),
               _t.get("success", "#10d982"), _t.get("warning", "#fbbf24")]
    _swatches = "".join(
        f'<div style="width:18px;height:18px;border-radius:5px;'
        f'background:{c};box-shadow:0 2px 8px {c}55;"></div>'
        for c in _colors
    )
    st.markdown(f"""
    <div style="display:flex;gap:6px;align-items:center;
        margin:0.4rem 0 0.6rem;padding:0.6rem 0.8rem;
        background:rgba(255,255,255,0.05);
        border:1px solid rgba(255,255,255,0.08);
        border-radius:10px;">
        {_swatches}
        <span style="font-size:0.7rem;color:{sidebar_sub};margin-left:4px;">
            {_t.get('name','Theme')}</span>
    </div>
    """, unsafe_allow_html=True)

    # Logout
    if st.session_state.logged_in:
        if st.button("🚪 Logout", use_container_width=True, key="sb_logout"):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.session_state.page = "home"
            st.rerun()

    # Version footer
    st.markdown(f"""
    <div style="text-align:center;padding:0.8rem 0 0.2rem;
        font-size:0.62rem;color:{sidebar_group};letter-spacing:0.08em;">
        MedStudy Oman v3.0 ✦ 2026
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# FLOATING AI BUBBLE
# ─────────────────────────────────────────────────────────────────────────────
def _render_ai_bubble():
    open_state = st.session_state.ai_bubble_open
    label = "✕" if open_state else "🤖"
    st.markdown(
        f'<div class="ai-bubble anim-glow-pulse" '
        f'title="{"Close" if open_state else "Open"} AI Medical Tutor">'
        f'{label}</div>',
        unsafe_allow_html=True,
    )

_render_ai_bubble()


# ─────────────────────────────────────────────────────────────────────────────
# QUICK NAV BAR — Shown on non-home pages
# ─────────────────────────────────────────────────────────────────────────────
if st.session_state.page != "home":
    _nav_items = [
        ("🏠","home","Home"),   ("📚","subjects","Subjects"),
        ("📝","mcq_quiz","Quiz"), ("🃏","flashcards","Cards"),
        ("🤖","ai_tutor","AI"),  ("📊","dashboard","Stats"),
        ("⏱️","pomodoro","Timer"),("🏆","leaderboards","Rank"),
    ]
    # Premium scrollable nav bar
    nav_btns_html = ""
    for ico, pid, lbl in _nav_items:
        is_active = st.session_state.page == pid
        active_style = (
            f"background:{theme['gradient']};color:{theme['text_inverse']};"
            f"box-shadow:{theme['glow']};"
            if is_active else
            f"background:{theme['glass_bg']};color:{theme['text_muted']};"
            f"border:1px solid {theme['card_border']};"
        )
        nav_btns_html += f"""
        <div style="{active_style}border-radius:12px;padding:0.45rem 0.9rem;
            white-space:nowrap;font-size:0.82rem;font-weight:700;
            cursor:pointer;transition:all 0.2s ease;
            backdrop-filter:blur(12px);display:inline-flex;align-items:center;gap:5px;"
            onclick="">{ico} {lbl}</div>"""

    st.markdown(f"""
    <div style="display:flex;gap:8px;overflow-x:auto;padding:0.5rem 0 0.8rem;
        scrollbar-width:none;-webkit-overflow-scrolling:touch;
        margin-bottom:0.5rem;">
        {nav_btns_html}
    </div>
    <div style="height:1px;background:linear-gradient(90deg,transparent,
        {theme['card_border']},transparent);margin-bottom:1.4rem;"></div>
    """, unsafe_allow_html=True)

    # Actual Streamlit buttons for nav (functional)
    _cols = st.columns(len(_nav_items))
    for _col, (_ico, _pid, _lbl) in zip(_cols, _nav_items):
        with _col:
            _active = st.session_state.page == _pid
            if st.button(
                f"{_ico}",
                key=f"topnav_{_pid}",
                use_container_width=True,
                type="primary" if _active else "secondary",
                help=_lbl,
            ):
                st.session_state.page = _pid; st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# PAGE HELPERS
# ─────────────────────────────────────────────────────────────────────────────

def _require_login(redirect_page: str = "home"):
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        st.markdown(f"""
        <div style="text-align:center;padding:3.5rem 2rem;
            background:{theme['glass_bg']};
            border:1px solid {theme['glass_border']};
            border-top:3px solid {theme['primary']};
            border-radius:24px;margin:2rem auto;
            backdrop-filter:blur(20px);">
            <div style="font-size:3.5rem;margin-bottom:1rem;">🔒</div>
            <div style="font-family:'Bricolage Grotesque',sans-serif;
                font-size:1.6rem;font-weight:900;
                color:{theme['text']};margin-bottom:0.5rem;">
                Login Required</div>
            <div style="font-size:0.9rem;color:{theme['subtext']};
                margin-bottom:1.5rem;line-height:1.6;">
                Create a free account to unlock all features<br>
                and track your medical journey.</div>
        </div>
        """, unsafe_allow_html=True)
        lc, rc = st.columns(2)
        with lc:
            if st.button("🔑  Sign In", type="primary", use_container_width=True,
                         key=f"rl_login_{redirect_page}"):
                st.session_state.page = "auth"
                st.session_state.auth_mode = "login"
                st.rerun()
        with rc:
            if st.button("📝  Sign Up", use_container_width=True,
                         key=f"rl_signup_{redirect_page}"):
                st.session_state.page = "auth"
                st.session_state.auth_mode = "signup"
                st.rerun()


def _page_header(icon: str, title: str, subtitle: str = "", badge: str = ""):
    badge_html = ""
    if badge:
        badge_html = f"""<span class="med-badge">{badge}</span>"""
    st.markdown(f"""
    <div class="anim-fade-up" style="display:flex;align-items:center;
        gap:16px;margin-bottom:1.6rem;">
        <div style="width:52px;height:52px;border-radius:16px;
            background:{theme['gradient']};
            display:flex;align-items:center;justify-content:center;
            font-size:1.7rem;flex-shrink:0;
            box-shadow:{theme['glow']},0 8px 24px rgba(0,0,0,0.25);">{icon}</div>
        <div>
            <div style="display:flex;align-items:center;gap:10px;flex-wrap:wrap;">
                <div style="font-family:'Bricolage Grotesque',sans-serif;
                    font-size:1.9rem;font-weight:900;
                    color:{theme['text']};letter-spacing:-0.04em;
                    line-height:1.1;">{title}</div>
                {badge_html}
            </div>
            {f'<div style="font-size:0.82rem;color:{theme["subtext"]};margin-top:2px;">{subtitle}</div>' if subtitle else ""}
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# PROFILE PAGE RENDERER
# ─────────────────────────────────────────────────────────────────────────────
def _render_profile():
    user = st.session_state.user
    import random as _r
    _page_header("👤", f"Dr. {user['name']}",
                 f"{user.get('university','SQU')} · Year {user.get('year','')}",
                 badge="✦ Medical Scholar")

    ptabs = st.tabs(["📊 Analytics", "🏦 My Vault", "🎯 Academic Identity"])

    with ptabs[0]:
        p = theme["primary"]
        levels = [theme["surface_raised"], f"{p}28", f"{p}55", f"{p}88", p]
        cells  = "".join(
            f'<div style="width:13px;height:13px;border-radius:3px;'
            f'background:{_r.choices(levels,[40,25,15,12,8])[0]};margin:1px;"></div>'
            for _ in range(364)
        )
        st.markdown(f"""
        <div class="med-card anim-fade-up" style="margin-bottom:1.4rem;">
            <div class="med-label">📅 Knowledge Heatmap — Last 12 months</div>
            <div style="display:flex;flex-wrap:wrap;max-width:560px;">{cells}</div>
        </div>
        """, unsafe_allow_html=True)

        m1, m2, m3, m4 = st.columns(4)
        for col, (ico, lbl, val, clr) in zip([m1,m2,m3,m4], [
            ("🔥","Streak","12 days",theme["primary"]),
            ("⏱️","Hours","48 hrs","#10d982"),
            ("📝","MCQs Done","243","#a855f7"),
            ("🏆","Rank","#24","#f59e0b"),
        ]):
            with col:
                st.markdown(f"""
                <div class="med-card med-card-glow" style="text-align:center;
                    border-top:3px solid {clr};">
                    <div style="font-size:1.4rem;">{ico}</div>
                    <div class="med-stat-value" style="color:{clr};">{val}</div>
                    <div style="font-size:0.72rem;color:{theme['subtext']};
                        font-weight:600;letter-spacing:0.08em;
                        text-transform:uppercase;">{lbl}</div>
                </div>
                """, unsafe_allow_html=True)

    with ptabs[1]:
        vault = st.session_state.get("vault_items", [])
        if not vault:
            st.markdown(f"""
            <div class="med-card" style="text-align:center;padding:2.5rem;">
                <div style="font-size:2.5rem;margin-bottom:0.8rem;">🏦</div>
                <div style="font-family:'Bricolage Grotesque',sans-serif;
                    font-size:1.1rem;font-weight:700;color:{theme['text']};">
                    Your vault is empty</div>
                <div style="color:{theme['subtext']};font-size:0.85rem;margin-top:0.4rem;">
                    Save resources from Subjects to build your collection.</div>
            </div>
            """, unsafe_allow_html=True)
        else:
            for item in vault:
                st.markdown(f"""
                <div class="med-card" style="margin-bottom:0.6rem;">
                    {item.get("icon","📌")}
                    <strong style="color:{theme['text']};">{item.get("title","Resource")}</strong>
                </div>
                """, unsafe_allow_html=True)

    with ptabs[2]:
        a1, a2 = st.columns(2)
        with a1:
            st.markdown(f"""
            <div class="med-card anim-scale-in">
                <div class="med-label">Current Score</div>
                <div class="med-stat-value">80.6%</div>
                <div style="height:6px;background:{theme['card_border']};
                    border-radius:999px;overflow:hidden;margin:0.6rem 0;">
                    <div style="height:100%;width:80.6%;
                        background:{theme['gradient']};border-radius:999px;
                        box-shadow:{theme['glow']};"></div>
                </div>
                <div style="font-size:0.75rem;color:{theme['subtext']};">
                    Target: 90% for OMSB Part 1</div>
            </div>
            """, unsafe_allow_html=True)
        with a2:
            exams = [
                ("🎯","OMSB Part 1 (2025)"),
                ("📚","USMLE Step 1 (2026)"),
                ("🌍","IELTS Academic"),
                ("🏥","MOH Oman License"),
            ]
            rows = "".join(f"""
            <div style="display:flex;align-items:center;gap:8px;
                padding:0.5rem 0;
                border-bottom:1px solid {theme['card_border']};">
                <span>{ico}</span>
                <span style="font-size:0.85rem;color:{theme['text']};">{name}</span>
            </div>
            """ for ico, name in exams)
            st.markdown(f"""
            <div class="med-card anim-scale-in delay-1">
                <div class="med-label">Target Exams</div>
                {rows}
            </div>
            """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# THEME SHOWCASE PAGE (accessible via URL param or future nav)
# ─────────────────────────────────────────────────────────────────────────────
def _render_theme_showcase():
    """Beautiful grid showing all 15 themes with previews."""
    _page_header("🎨", "Theme Gallery",
                 "Choose your medical aesthetic — 15 premium styles",
                 badge="✦ 15 Themes")

    # Categorize themes
    dark_themes  = {k: v for k, v in THEMES.items() if v.get("family") == "dark"}
    light_themes = {k: v for k, v in THEMES.items() if v.get("family") in ("light", "warm")}

    for cat_label, cat_themes in [("🌑 Dark Themes", dark_themes),
                                   ("☀️ Light Themes", light_themes)]:
        st.markdown(f"""
        <div style="margin:1.4rem 0 0.8rem;">
            <div class="med-label">{cat_label}</div>
        </div>
        """, unsafe_allow_html=True)

        cols = st.columns(3)
        for i, (tkey, tval) in enumerate(cat_themes.items()):
            with cols[i % 3]:
                tp   = tval["primary"]
                tbg  = tval["bg"]
                tsb  = tval["sidebar_bg"]
                tgrd = tval["gradient"]
                is_active = tkey == st.session_state.theme
                border = f"2px solid {tp}" if is_active else f"1px solid {tval['card_border']}"
                active_badge = '<span style="font-size:0.65rem;font-weight:800;color:#10d982;margin-left:6px;">✓ ACTIVE</span>' if is_active else ""

                st.markdown(f"""
                <div style="background:{tval['card_bg']};
                    border:{border};
                    border-radius:18px;padding:1.1rem;margin-bottom:0.8rem;
                    backdrop-filter:blur(12px);
                    transition:all 0.2s ease;overflow:hidden;position:relative;
                    {'box-shadow:' + tval['glow'] if is_active else ''}">
                    <div style="height:40px;border-radius:10px;
                        background:{tgrd};margin-bottom:0.7rem;
                        opacity:0.85;"></div>
                    <div style="display:flex;justify-content:space-between;
                        align-items:flex-start;">
                        <div>
                            <div style="font-family:'Bricolage Grotesque',sans-serif;
                                font-size:0.88rem;font-weight:800;
                                color:{tval['text']};">{tkey}{active_badge}</div>
                            <div style="font-size:0.68rem;
                                color:{tval['subtext']};margin-top:2px;
                                text-transform:uppercase;letter-spacing:0.08em;
                                font-weight:600;">{tval.get('family','').upper()}</div>
                        </div>
                        <div style="display:flex;gap:4px;margin-top:2px;">
                            {''.join(f'<div style="width:12px;height:12px;border-radius:3px;background:{c};"></div>'
                                for c in [tp, tval.get('secondary',tp),
                                          tval.get('success','#10d982'),
                                          tval.get('warning','#fbbf24')])}
                        </div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

                if st.button(
                    f"✓ Active" if is_active else f"Apply Theme",
                    key=f"apply_theme_{tkey}",
                    use_container_width=True,
                    type="primary" if is_active else "secondary",
                ):
                    st.session_state.theme = tkey
                    if st.session_state.logged_in:
                        update_theme(st.session_state.user["id"], tkey)
                    st.rerun()


# ═════════════════════════════════════════════════════════════════════════════
# ROUTING
# ═════════════════════════════════════════════════════════════════════════════
page = st.session_state.page

if page == "auth":
    auth_page(theme, login_user, signup_user)

elif page == "home":
    home_page(theme, tr, MOTIVATIONAL_QUOTES)

elif page == "themes":
    _render_theme_showcase()

elif page == "subjects":
    if MODULES_LOADED: subjects_page(theme)
    else: st.error(f"Module error: {_MODULE_ERR}")

elif page == "flashcards":
    flashcards_page(theme)

elif page == "mnemonics":
    if MODULES_LOADED: mnemonics_page(theme)

elif page == "mcq_quiz":
    mcq_quiz_page(theme)

elif page == "dashboard":
    db_stats = {}
    if st.session_state.logged_in:
        db_stats = get_user_stats(st.session_state.user["id"]) or {}
    else:
        st.info("📊 Showing demo data — login to see your personal analytics.")
    if MODULES_LOADED:
        dashboard_page(theme, db_stats)

elif page == "pomodoro":
    timer_page(theme)

elif page == "osce_timer":
    if MODULES_LOADED: osce_timer_page(theme)
    else: timer_page(theme)

elif page == "ai_tutor":
    ai_chat_tutor_page(theme)

elif page == "voice_ai":
    _page_header("🎤", tr("voice_ai"), "Hands-free studying powered by speech recognition",
                 badge="Coming Soon")
    st.info("🎤 Voice AI — launching soon!")

elif page == "lab_game":
    if MODULES_LOADED: lab_game_page(theme)

elif page == "anatomy_3d":
    if MODULES_LOADED: anatomy_3d_page(theme)

elif page == "resources":
    if MODULES_LOADED: resources_page(theme)

elif page == "progress":
    if not st.session_state.logged_in:
        _require_login("progress")
    elif MODULES_LOADED:
        progress_tracker_page(theme, get_user_stats(st.session_state.user["id"]))

elif page == "study_groups":
    if MODULES_LOADED:
        study_groups_page(theme,
            st.session_state.user if st.session_state.logged_in else None)

elif page == "discussion":
    if MODULES_LOADED:
        discussion_page(theme,
            st.session_state.user if st.session_state.logged_in else None)

elif page == "shared_notes":
    if MODULES_LOADED:
        shared_notes_page(theme,
            st.session_state.user if st.session_state.logged_in else None)

elif page == "leaderboards":
    if MODULES_LOADED:
        leaderboards_page(theme,
            st.session_state.user if st.session_state.logged_in else None)

elif page == "tips":
    if MODULES_LOADED: tips_page(theme)

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
