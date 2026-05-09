"""
app.py — MedStudy Oman 🩺
PHASES 1–5  (complete)
ThemeManager · Auth · Bento Home · Subject Hub · OSCE Timer · Developer Portfolio
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

# ── Feature modules (existing files, imported unchanged) ──────────────────────
MODULES_LOADED = False
_MODULE_ERR    = ""
try:
    try:
        from timer_enhanced import get_timer_html, get_timer_completion_animation
    except ImportError:
        def get_timer_html(*a, **kw): return ""
        def get_timer_completion_animation(*a, **kw): return ""
    try:
        from ai_features import ai_tutor_page as _legacy_ai   # kept for compatibility
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
        "theme":              "🩺 Clinical Snow",
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
    """Translate a key."""
    return TRANSLATIONS[st.session_state.language].get(key, key)


# ─────────────────────────────────────────────────────────────────────────────
# INJECT THEME
# ─────────────────────────────────────────────────────────────────────────────
_tm    = ThemeManager(st.session_state.theme)
theme  = THEMES.get(st.session_state.theme, list(THEMES.values())[0])
st.markdown(_tm.inject(), unsafe_allow_html=True)
inject_mobile(theme)   # Phase 9 — responsive CSS + PWA meta

# ── Custom sidebar toggle arrow ───────────────────────────────────────────────
st.markdown("""
<button id="sidebar-toggle-btn" title="Toggle sidebar">&#9664;</button>
<script>
(function() {
    function clickNativeToggle() {
        var doc = window.parent.document;
        // Try the collapsed control button (arrow when sidebar is hidden)
        var btn = doc.querySelector('[data-testid="collapsedControl"] button')
                || doc.querySelector('[data-testid="stSidebarCollapsedControl"] button')
                || doc.querySelector('button[kind="header"]');
        if (btn) { btn.click(); return true; }
        return false;
    }

    function updateArrow() {
        var doc = window.parent.document;
        var sb  = doc.querySelector('[data-testid="stSidebar"]');
        var myBtn = doc.getElementById('sidebar-toggle-btn');
        if (!sb || !myBtn) return;
        var open = sb.getBoundingClientRect().left >= -10;
        myBtn.innerHTML = open ? '&#9664;' : '&#9654;';
    }

    document.getElementById('sidebar-toggle-btn').addEventListener('click', function() {
        // Find Streamlit's own sidebar toggle buttons and click whichever is visible
        var doc = window.parent.document;
        var candidates = [
            doc.querySelector('[data-testid="collapsedControl"] button'),
            doc.querySelector('[data-testid="stSidebarCollapsedControl"] button'),
            doc.querySelector('[data-testid="stSidebar"] button[aria-label]'),
        ];
        for (var i = 0; i < candidates.length; i++) {
            if (candidates[i]) { candidates[i].click(); break; }
        }
        setTimeout(updateArrow, 350);
    });

    // Set initial arrow direction after a short delay
    setTimeout(updateArrow, 500);
})();
</script>
""", unsafe_allow_html=True)

# Welcome toast on first login
if st.session_state.get("just_logged_in") and st.session_state.logged_in:
    _u = st.session_state.user
    st.toast(f"🩺 Welcome, Dr. {_u['name']}! Ready to study?", icon="✅")
    st.session_state.just_logged_in = False


# ─────────────────────────────────────────────────────────────────────────────
# HELPER: FLOATING AI BUBBLE
# ─────────────────────────────────────────────────────────────────────────────
def _render_ai_bubble():
    open_state = st.session_state.ai_bubble_open
    label = "✕" if open_state else "🤖"
    bg    = theme["secondary"] if open_state else ""
    st.markdown(
        f'<div class="ai-bubble" style="{"background:" + bg if bg else ""}" '
        f'title="{"Close" if open_state else "Open"} AI Medical Tutor">{label}</div>',
        unsafe_allow_html=True,
    )

_render_ai_bubble()


# ─────────────────────────────────────────────────────────────────────────────
# SIDEBAR NAV
# ─────────────────────────────────────────────────────────────────────────────
SIDEBAR_NAV = [
    ("🏠", "home",         "Home"),
    ("📚", "subjects",     "Subjects"),
    ("🃏", "flashcards",   "Flashcards"),
    ("💡", "mnemonics",    "Mnemonics"),
    ("📝", "mcq_quiz",     "MCQ Quiz"),
    ("📊", "dashboard",    "Dashboard"),
    ("⏱️", "pomodoro",     "Pomodoro Timer"),
    ("🩺", "osce_timer",   "OSCE Timer"),
    ("🤖", "ai_tutor",     "AI Tutor"),
    ("🎤", "voice_ai",     "Voice AI"),
    ("⚗️", "lab_game",     "Lab Game"),
    ("🫁", "anatomy_3d",   "3D Anatomy"),
    ("📖", "resources",    "Resources"),
    ("📈", "progress",     "Progress"),
    ("👥", "study_groups", "Study Groups"),
    ("💬", "discussion",   "Forums"),
    ("📋", "shared_notes", "Shared Notes"),
    ("🏆", "leaderboards", "Leaderboards"),
    ("💡", "tips",         "Study Tips"),
    ("👤", "profile",      "My Profile"),
    ("🏅", "about",        "About"),
]

# ── Sidebar — native Streamlit components only ─────────────────────────────
with st.sidebar:
    st.markdown(f"""<div style='padding:0.8rem 0 0.6rem;border-bottom:2px solid {theme["primary"]};margin-bottom:0.8rem;'>
<span style='font-family:Syne,sans-serif;font-size:1.1rem;font-weight:900;color:{theme["primary"]};'>MedStudy</span>
<span style='font-family:Syne,sans-serif;font-size:1.1rem;font-weight:400;color:{theme["text"]};'>Oman 🩺</span><br>
<span style='font-size:0.6rem;color:{theme["primary"]};letter-spacing:0.12em;text-transform:uppercase;font-weight:700;'>AI · CLINICAL · 2026</span>
</div>""", unsafe_allow_html=True)

    st.write("")

    # Language
    st.caption("🌍 LANGUAGE")
    lc1, lc2 = st.columns(2)
    with lc1:
        if st.button("🇬🇧 EN", use_container_width=True,
                     type="primary" if st.session_state.language == "en" else "secondary",
                     key="lang_en"):
            st.session_state.language = "en"; st.rerun()
    with lc2:
        if st.button("🇴🇲 AR", use_container_width=True,
                     type="primary" if st.session_state.language == "ar" else "secondary",
                     key="lang_ar"):
            st.session_state.language = "ar"; st.rerun()

    st.write("")

    # Theme
    st.caption("🎨 THEME")
    theme_keys = list(THEMES.keys())
    sel_theme  = st.selectbox(
        "Theme", theme_keys,
        index=theme_keys.index(st.session_state.theme),
        key="theme_sel",
    )
    if sel_theme != st.session_state.theme:
        st.session_state.theme = sel_theme
        if st.session_state.logged_in:
            update_theme(st.session_state.user["id"], sel_theme)
        st.rerun()

    st.divider()

    # Auth
    if st.session_state.logged_in:
        u = st.session_state.user
        st.success(f"Dr. {u['name']}")
        st.caption(u.get("university", "SQU College of Medicine"))
        if st.button("🚪  Logout", use_container_width=True, key="sb_logout"):
            st.session_state.logged_in = False
            st.session_state.user = None
            st.session_state.page = "home"
            st.rerun()
    else:
        if st.button("🔑  Login", type="primary",
                     use_container_width=True, key="sb_login"):
            st.session_state.page = "auth"
            st.session_state.auth_mode = "login"
            st.rerun()
        if st.button("📝  Sign Up", use_container_width=True, key="sb_signup"):
            st.session_state.page = "auth"
            st.session_state.auth_mode = "signup"
            st.rerun()


# ── Page navigation strip (shown on all pages except home) ─────────────────
if st.session_state.page != "home":
    _nav_items = [
        ("🏠","home","Home"), ("📚","subjects","Subjects"),
        ("📝","mcq_quiz","Quiz"), ("🃏","flashcards","Cards"),
        ("🤖","ai_tutor","AI Tutor"), ("📊","dashboard","Dashboard"),
        ("⏱️","pomodoro","Timer"), ("💡","mnemonics","Mnemonics"),
        ("📖","resources","Resources"),
    ]
    _cols = st.columns(len(_nav_items))
    for _col, (_ico, _pid, _lbl) in zip(_cols, _nav_items):
        with _col:
            _active = st.session_state.page == _pid
            if st.button(
                f"{_ico} {_lbl}",
                key=f"topnav_{_pid}",
                use_container_width=True,
                type="primary" if _active else "secondary",
            ):
                st.session_state.page = _pid; st.rerun()
    st.markdown(
        f"<div style='height:1px;background:{theme['card_border']};margin:0.5rem 0 1.2rem;'></div>",
        unsafe_allow_html=True,
    )


# ═════════════════════════════════════════════════════════════════════════════
# PAGE HELPERS
# ═════════════════════════════════════════════════════════════════════════════

def _require_login(redirect_page: str = "home"):
    _, mid, _ = st.columns([1, 2, 1])
    with mid:
        st.markdown(
            f'<div style="text-align:center;padding:3rem 2rem;'
            f'background:{theme["glass_bg"]};border:1.5px solid {theme["glass_border"]};'
            f'border-top:4px solid {theme["primary"]};border-radius:24px;margin:2rem auto;">'+
            f'<div style="font-size:3.5rem;margin-bottom:1rem;animation:float 3s ease-in-out infinite;">🔒</div>'+
            f'<div style="font-family:Syne,sans-serif;font-size:1.6rem;font-weight:900;'
            f'color:{theme["text"]};margin-bottom:0.5rem;">Login Required</div>'+
            f'<div style="font-size:0.9rem;color:{theme["subtext"]};margin-bottom:1.5rem;">'
            f'Create a free account to access this feature.</div>'+
            f'</div>',
            unsafe_allow_html=True,
        )
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


def _page_header(icon: str, title: str, subtitle: str = ""):
    st.markdown(
        f'<div style="display:flex;align-items:center;gap:14px;margin-bottom:1.2rem;">'+
        f'<div style="width:48px;height:48px;border-radius:14px;'
        f'background:{theme["gradient"]};display:flex;align-items:center;'
        f'justify-content:center;font-size:1.6rem;flex-shrink:0;'
        f'box-shadow:0 4px 16px {theme["primary_glow"]};">{icon}</div>'+
        f'<div><div style="font-family:Syne,sans-serif;font-size:1.7rem;'
        f'font-weight:900;color:{theme["text"]};letter-spacing:-0.03em;">{title}</div>'+
        (f'<div style="font-size:0.8rem;color:{theme["subtext"]};">{subtitle}</div>' if subtitle else "")+
        f'</div></div>',
        unsafe_allow_html=True,
    )


def _render_pomodoro():
    timer_page(theme)


def _render_profile():
    user = st.session_state.user
    import random as _r
    _page_header("👤", f"Dr. {user['name']}", f"{user.get('university','SQU')} · Year {user.get('year','')}")

    ptabs = st.tabs(["📊 Analytics", "🏦 My Vault", "🎯 Academic Identity"])

    with ptabs[0]:
        p = theme["primary"]
        levels = [theme["surface_raised"], f"{p}28", f"{p}55", f"{p}88", p]
        cells  = "".join(
            f'<div style="width:13px;height:13px;border-radius:3px;'
            f'background:{_r.choices(levels,[40,25,15,12,8])[0]};margin:1px;"></div>'
            for _ in range(364)
        )
        st.markdown(
            f'<div style="margin-bottom:1rem;"><div style="font-family:Syne,sans-serif;'
            f'font-size:0.9rem;font-weight:800;color:{theme["text"]};margin-bottom:0.6rem;">'
            f'📅 Knowledge Heatmap — Last 12 months</div>'
            f'<div style="display:flex;flex-wrap:wrap;max-width:560px;">{cells}</div></div>',
            unsafe_allow_html=True,
        )
        m1, m2, m3, m4 = st.columns(4)
        for col, (ico, lbl, val, clr) in zip([m1,m2,m3,m4], [
            ("🔥","Streak","12 days",theme["primary"]),
            ("⏱️","Hours","48 hrs","#10b981"),
            ("📝","MCQs Done","243","#8b5cf6"),
            ("🏆","Rank","#24","#f59e0b"),
        ]):
            with col:
                st.markdown(
                    f'<div style="background:{theme["card_bg"]};border:1px solid {theme["card_border"]};'
                    f'border-top:3px solid {clr};border-radius:16px;padding:1rem;text-align:center;">'
                    f'<div style="font-size:1.3rem;">{ico}</div>'
                    f'<div style="font-family:Syne,sans-serif;font-size:1.4rem;font-weight:900;'
                    f'color:{clr};">{val}</div>'
                    f'<div style="font-size:0.7rem;color:{theme["subtext"]};">{lbl}</div></div>',
                    unsafe_allow_html=True,
                )

    with ptabs[1]:
        vault = st.session_state.get("vault_items", [])
        if not vault:
            st.info("🏦 Your vault is empty. Save resources from the Subjects page.")
        else:
            for item in vault:
                st.markdown(
                    f'<div style="background:{theme["card_bg"]};border:1px solid {theme["card_border"]};'
                    f'border-radius:12px;padding:0.8rem;margin-bottom:0.5rem;">'
                    f'{item.get("icon","📌")} <strong>{item.get("title","Resource")}</strong></div>',
                    unsafe_allow_html=True,
                )

    with ptabs[2]:
        a1, a2 = st.columns(2)
        with a1:
            st.markdown(
                f'<div style="background:{theme["glass_bg"]};border:1px solid {theme["glass_border"]};'
                f'border-radius:18px;padding:1.4rem;backdrop-filter:blur(12px);">'
                f'<div style="font-size:0.65rem;font-weight:800;color:{theme["primary"]};'
                f'letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.5rem;">Current Score</div>'
                f'<div style="font-family:Syne,sans-serif;font-size:2.8rem;font-weight:900;'
                f'color:{theme["primary"]};line-height:1;">80.6%</div>'
                f'<div style="height:6px;background:{theme["card_border"]};border-radius:999px;'
                f'overflow:hidden;margin:0.5rem 0;">'
                f'<div style="height:100%;width:80.6%;background:{theme["gradient"]};border-radius:999px;"></div>'
                f'</div><div style="font-size:0.75rem;color:{theme["subtext"]};">Target: 90% for OMSB Part 1</div>'
                f'</div>',
                unsafe_allow_html=True,
            )
        with a2:
            exams = ["🎯 OMSB Part 1 (2025)","📚 USMLE Step 1 (2026)","🌍 IELTS Academic","🏥 MOH Oman License"]
            rows  = "".join(
                f'<div style="font-size:0.84rem;color:{theme["text"]};padding:0.4rem 0;'
                f'border-bottom:1px solid {theme["card_border"]};">● {e}</div>'
                for e in exams
            )
            st.markdown(
                f'<div style="background:{theme["glass_bg"]};border:1px solid {theme["glass_border"]};'
                f'border-radius:18px;padding:1.4rem;backdrop-filter:blur(12px);">'
                f'<div style="font-size:0.65rem;font-weight:800;color:{theme["primary"]};'
                f'letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.6rem;">Target Exams</div>'
                f'{rows}</div>',
                unsafe_allow_html=True,
            )

# ═════════════════════════════════════════════════════════════════════════════
# ROUTING
# ═════════════════════════════════════════════════════════════════════════════
page = st.session_state.page

if page == "auth":
    auth_page(theme, login_user, signup_user)

elif page == "home":
    home_page(theme, tr, MOTIVATIONAL_QUOTES)

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
    _render_pomodoro()

elif page == "osce_timer":
    if MODULES_LOADED: osce_timer_page(theme)
    else: timer_page(theme)


elif page == "ai_tutor":
    ai_chat_tutor_page(theme)


elif page == "voice_ai":
    _page_header("🎤", tr("voice_ai"), "Hands-free studying powered by speech recognition")
    st.info("🎤 Voice AI — coming soon!")

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
        _page_header("👤", tr("profile"),
                     f"Dr. {st.session_state.user['name']} · Academic Analytics")
        _render_profile()

elif page == "about":
    about_page(theme)

else:
    st.session_state.page = "home"
    st.rerun()
