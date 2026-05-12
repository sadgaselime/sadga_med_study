"""
premium_platform.py - luxury MedStudy Oman Streamlit components.
"""

from __future__ import annotations

import hashlib
import html
import re
from datetime import datetime

import streamlit as st

from medical_knowledge import AZ_MEDICAL_KNOWLEDGE, SUBJECT_ORDER
from database import (
    get_ai_mnemonic_history,
    get_bookmarks,
    get_profile_overview,
    remove_bookmark,
    save_ai_mnemonic,
    save_bookmark,
    save_completed_lesson,
    update_language,
    update_theme,
    update_user_setting,
)


TRANSLATIONS = {
    "en": {
        "dashboard": "Dashboard",
        "knowledge_library": "Knowledge Library",
        "question_bank": "Question Bank",
        "flashcard_vault": "Flashcard Vault",
        "ai_study_tutor": "AI Study Tutor",
        "performance_insights": "Performance Insights",
        "focus_mode": "Focus Mode",
        "clinical_skills_lab": "Clinical Skills Lab",
        "study_notes": "Study Notes",
        "medical_references": "Medical References",
        "ai_mnemonics_studio": "AI Mnemonics Studio",
        "study_pillars": "Study Pillars",
        "az_hub": "A-Z Medical Knowledge Hub",
        "settings": "Settings",
        "user_profile": "User Profile",
        "search": "Search medicine, notes, mnemonics...",
        "login": "Login",
        "logout": "Logout",
        "profile": "Profile",
        "notifications": "Notifications",
        "master_medicine": "Master Medicine with a Smarter Clinical Study System",
        "hero_sub": "Practice questions, flashcards, OSCE stations, AI tutoring, analytics, and medical references in one focused workspace.",
        "continue_studying": "Continue Studying",
        "todays_progress": "Today's Progress",
        "weak_areas": "Weak Areas",
        "strong_subjects": "Strong Subjects",
        "recommended_next_step": "Recommended Next Step",
        "daily_streak": "Daily Streak",
        "study_time": "Study Time",
        "recent_activity": "Recent Activity",
        "quick_actions": "Quick Actions",
        "topic_of_day": "Recommended Topic of the Day",
        "educational_only": "For educational purposes only. Not a substitute for professional medical advice.",
        "bookmark": "Bookmark",
        "completed": "Completed",
        "save": "Save",
        "workspace": "Student Workspace",
        "workspace_subtitle": "Your clinical study command center",
        "mnemonic_topic_label": "Topic, disease, anatomy structure, drug class, pathway, criteria, or list",
        "style": "Style",
        "generate_mnemonic": "Generate Mnemonic",
        "generated_memory_system": "Generated Memory System",
        "english_explanation": "English explanation",
        "arabic_explanation": "Arabic explanation",
        "recall_quiz": "Recall quiz",
        "subject": "Subject",
    },
    "ar": {
        "dashboard": "لوحة الدراسة",
        "knowledge_library": "مكتبة المعرفة",
        "question_bank": "بنك الأسئلة",
        "flashcard_vault": "خزنة البطاقات",
        "ai_study_tutor": "المعلم الذكي",
        "performance_insights": "تحليلات الأداء",
        "focus_mode": "وضع التركيز",
        "clinical_skills_lab": "مختبر المهارات السريرية",
        "study_notes": "ملاحظات الدراسة",
        "medical_references": "المراجع الطبية",
        "ai_mnemonics_studio": "استوديو وسائل الحفظ الذكية",
        "study_pillars": "ركائز الدراسة",
        "az_hub": "مركز المعرفة الطبية من الألف إلى الياء",
        "settings": "الإعدادات",
        "user_profile": "الملف الشخصي",
        "search": "ابحث في الطب والملاحظات ووسائل الحفظ...",
        "login": "تسجيل الدخول",
        "logout": "تسجيل الخروج",
        "profile": "الملف",
        "notifications": "الإشعارات",
        "master_medicine": "أتقن الطب بنظام دراسة سريري أكثر ذكاء",
        "hero_sub": "أسئلة تدريبية، بطاقات، محطات OSCE، معلم ذكي، تحليلات ومراجع طبية في مساحة واحدة مركزة.",
        "continue_studying": "تابع الدراسة",
        "todays_progress": "تقدم اليوم",
        "weak_areas": "نقاط تحتاج تقوية",
        "strong_subjects": "المواد القوية",
        "recommended_next_step": "الخطوة التالية المقترحة",
        "daily_streak": "سلسلة الأيام",
        "study_time": "وقت الدراسة",
        "recent_activity": "النشاط الأخير",
        "quick_actions": "إجراءات سريعة",
        "topic_of_day": "موضوع اليوم المقترح",
        "educational_only": "لأغراض تعليمية فقط. ليس بديلا عن الاستشارة الطبية المهنية.",
        "bookmark": "حفظ",
        "completed": "تم",
        "save": "حفظ",
        "workspace": "مساحة الطالب",
        "workspace_subtitle": "مركزك المنظم للدراسة السريرية",
        "mnemonic_topic_label": "موضوع أو مرض أو تركيب تشريحي أو فئة دوائية أو مسار أو قائمة",
        "style": "النمط",
        "generate_mnemonic": "إنشاء وسيلة حفظ",
        "generated_memory_system": "نظام الذاكرة الناتج",
        "english_explanation": "الشرح الإنجليزي",
        "arabic_explanation": "الشرح العربي",
        "recall_quiz": "اختبار الاسترجاع",
        "subject": "المادة",
    },
}


PRO_NAV_ITEMS = [
    ("dashboard", "dashboard", "⌂", "Home", "الرئيسية", "#8b5cf6"),
    ("user_profile", "profile", "👤", "Profile", "الملف", "#0ea5e9"),
    ("study_pillars", "study_pillars", "✚", "Pillars", "الركائز", "#06b6d4"),
    ("az_hub", "az_hub", "🧠", "Med Hub", "المركز", "#10b981"),
    ("knowledge_library", "subjects", "📚", "Library", "المكتبة", "#14b8a6"),
    ("question_bank", "mcq_quiz", "📝", "Q Bank", "الأسئلة", "#f97316"),
    ("flashcard_vault", "flashcards", "💎", "Cards", "البطاقات", "#ec4899"),
    ("ai_study_tutor", "ai_tutor", "🤖", "AI Tutor", "المعلم", "#6366f1"),
    ("ai_mnemonics_studio", "ai_mnemonics", "💡", "Mnemonics", "الحفظ", "#eab308"),
    ("clinical_skills_lab", "osce_timer", "🩺", "OSCE", "الأوسكي", "#ef4444"),
    ("focus_mode", "pomodoro", "⏱", "Focus", "التركيز", "#06b6d4"),
    ("performance_insights", "analytics", "📊", "Insights", "الأداء", "#22c55e"),
    ("medical_references", "resources", "📖", "Refs", "المراجع", "#a855f7"),
    ("study_notes", "shared_notes", "✍️", "Notes", "الملاحظات", "#f59e0b"),
    ("settings", "settings", "⚙️", "Settings", "الإعدادات", "#64748b"),
    ("admin_content", "admin_content", "🛠", "Admin", "الإدارة", "#4f46e5"),
    ("about", "about", "ℹ️", "About", "عن التطبيق", "#9ca3af"),
]


def get_translation(key: str, language: str | None = None) -> str:
    lang = language or st.session_state.get("language", "en")
    return TRANSLATIONS.get(lang, TRANSLATIONS["en"]).get(key, key)


def apply_rtl_if_arabic():
    if st.session_state.get("language") != "ar":
        return
    st.markdown(
        """
        <style>
        .stApp, .block-container, [data-testid="stMarkdownContainer"] {
            direction: rtl;
            text-align: right;
        }
        .med-topbar, .med-sidebar, .module-card, .hero-panel, .lux-card {
            direction: rtl;
            text-align: right;
        }
        .stTextInput input, .stTextArea textarea { direction: rtl; text-align: right; }
        </style>
        """,
        unsafe_allow_html=True,
    )


def inject_premium_css(theme):
    is_dark = theme.get("family") == "dark"
    shell_text = "#f8fbff" if is_dark else theme["text"]
    shell_muted = "#b7c9d8" if is_dark else theme["text_muted"]
    card_text = "#071827" if is_dark else theme["text"]
    card_body = "#40586b" if is_dark else theme["text_muted"]
    topbar_bg = (
        "linear-gradient(135deg, rgba(255,255,255,0.14), rgba(255,255,255,0.06))"
        if is_dark else
        "linear-gradient(135deg, rgba(255,255,255,0.82), rgba(255,255,255,0.58))"
    )
    soft_shadow = "0 18px 48px rgba(3,18,34,0.18)" if is_dark else theme["shadow_md"]
    nav_shadow = "0 24px 80px rgba(0,0,0,0.36)" if is_dark else theme["shadow_lg"]
    st.markdown(
        f"""
        <style>
        :root {{
            --cyan: {theme["primary"]};
            --emerald: {theme["secondary"]};
            --line: {theme["card_border"]};
            --panel: {theme["card_bg"]};
            --glass: {theme["glass_bg"]};
            --glass-strong: {theme["glass_border"]};
            --ink: {shell_text};
            --muted: {shell_muted};
            --premium-card-text: {card_text};
            --premium-card-body: {card_body};
            --navy-shadow: {nav_shadow};
            --soft-shadow: {soft_shadow};
        }}
        html, body, .stApp {{
            background:
                radial-gradient(circle at 12% 8%, {theme["primary_glow"]}, transparent 30%),
                radial-gradient(circle at 88% 12%, {theme["hover_bg"]}, transparent 28%),
                {theme["hero_gradient"]} !important;
        }}
        .block-container {{
            max-width: 1500px !important;
            padding-top: 1.1rem !important;
        }}
        .medical-animation-layer {{
            position: fixed;
            inset: 0;
            pointer-events: none;
            overflow: hidden;
            z-index: 0;
        }}
        .medical-float {{
            position: absolute;
            color: {theme["primary"]} !important;
            opacity: {"0.16" if is_dark else "0.13"};
            font-weight: 900;
            filter: drop-shadow(0 10px 24px {theme["primary_glow"]});
            animation: medFloat 13s ease-in-out infinite;
        }}
        .medical-float.instrument {{
            opacity: {"0.20" if is_dark else "0.16"};
            font-size: 1.6rem;
            animation: medDrift 18s ease-in-out infinite;
        }}
        .medical-float.wordmark {{
            font-size: 1.4rem;
            letter-spacing: 0.05em;
            opacity: {"0.14" if is_dark else "0.11"};
        }}
        .medical-float:nth-child(1) {{ top: 10%; left: 5%; font-size: 2rem; animation-delay: 0s; }}
        .medical-float:nth-child(2) {{ top: 16%; right: 9%; font-size: 2.4rem; animation-delay: -3s; }}
        .medical-float:nth-child(3) {{ top: 52%; left: 8%; animation-delay: -6s; }}
        .medical-float:nth-child(4) {{ top: 64%; right: 12%; animation-delay: -2s; }}
        .medical-float:nth-child(5) {{ top: 38%; left: 46%; animation-delay: -8s; }}
        .medical-float:nth-child(6) {{ bottom: 8%; left: 28%; animation-delay: -5s; }}
        .medical-float:nth-child(7) {{ top: 28%; left: 18%; animation-delay: -11s; }}
        .medical-float:nth-child(8) {{ top: 76%; right: 24%; animation-delay: -7s; }}
        .medical-float:nth-child(9) {{ top: 44%; right: 35%; animation-delay: -13s; }}
        .medical-float:nth-child(10) {{ top: 6%; left: 52%; animation-delay: -9s; }}
        .medical-float:nth-child(11) {{ bottom: 20%; right: 6%; animation-delay: -15s; }}
        .medical-float:nth-child(12) {{ top: 82%; left: 6%; animation-delay: -4s; }}
        .medical-float:nth-child(13) {{ top: 26%; right: 48%; animation-delay: -17s; }}
        .medical-float:nth-child(14) {{ bottom: 34%; left: 64%; animation-delay: -10s; }}
        .cinema-sweep {{
            position: absolute;
            inset: -20% auto auto -18%;
            width: 58vw;
            height: 130vh;
            transform: rotate(18deg);
            background: linear-gradient(90deg, transparent, {theme["primary_glow"]}, transparent);
            opacity: {"0.16" if is_dark else "0.12"};
            animation: sweepMove 22s ease-in-out infinite;
        }}
        @keyframes medFloat {{
            0%, 100% {{ transform: translate3d(0,0,0) rotate(0deg); }}
            35% {{ transform: translate3d(14px,-18px,0) rotate(5deg); }}
            70% {{ transform: translate3d(-12px,10px,0) rotate(-4deg); }}
        }}
        @keyframes medDrift {{
            0%, 100% {{ transform: translate3d(0,0,0) rotate(-3deg) scale(1); }}
            45% {{ transform: translate3d(22px,-22px,0) rotate(7deg) scale(1.04); }}
            72% {{ transform: translate3d(-18px,16px,0) rotate(-6deg) scale(.98); }}
        }}
        @keyframes sweepMove {{
            0%, 100% {{ transform: translateX(-18%) rotate(18deg); }}
            50% {{ transform: translateX(118vw) rotate(18deg); }}
        }}
        .stApp > *:not(.medical-animation-layer) {{
            position: relative;
            z-index: 1;
        }}
        .cinematic-page-strip {{
            display:grid;
            grid-template-columns: auto 1fr auto;
            gap:14px;
            align-items:center;
            margin: 0 0 18px;
            padding: 16px;
            border-radius: 24px;
            border: 1px solid var(--line);
            background:
                linear-gradient(135deg, var(--glass), rgba(255,255,255,0.10)),
                radial-gradient(circle at 85% 20%, {theme["primary_glow"]}, transparent 34%);
            box-shadow: var(--soft-shadow);
            backdrop-filter: blur(22px);
            overflow:hidden;
            position:relative;
        }}
        .cinematic-page-strip::after {{
            content:"";
            position:absolute;
            inset:0;
            background: linear-gradient(90deg, transparent, rgba(255,255,255,0.18), transparent);
            transform: translateX(-120%);
            animation: pageShimmer 9s ease-in-out infinite;
        }}
        @keyframes pageShimmer {{
            0%, 45% {{ transform: translateX(-120%); }}
            70%, 100% {{ transform: translateX(120%); }}
        }}
        .cinema-page-symbol {{
            width:52px;
            height:52px;
            border-radius:19px;
            display:grid;
            place-items:center;
            background: linear-gradient(135deg, var(--cyan), var(--emerald));
            color:{theme["text_inverse"]} !important;
            font-size:1.35rem;
            box-shadow: 0 14px 34px {theme["primary_glow"]};
            z-index:1;
        }}
        .cinema-page-title {{
            color:var(--ink) !important;
            font-weight:900;
            font-size:1.08rem;
            z-index:1;
        }}
        .cinema-page-sub {{
            color:var(--muted) !important;
            font-size:.84rem;
            margin-top:3px;
            z-index:1;
        }}
        .cinema-tool-row {{
            display:flex;
            gap:8px;
            flex-wrap:wrap;
            justify-content:flex-end;
            z-index:1;
        }}
        .cinema-tool-chip {{
            display:inline-flex;
            align-items:center;
            gap:5px;
            border-radius:999px;
            border:1px solid var(--line);
            background:rgba(255,255,255,0.42);
            color:var(--ink) !important;
            padding:7px 10px;
            font-size:.75rem;
            font-weight:850;
        }}
        .med-topbar {{
            position: sticky;
            top: 0;
            z-index: 50;
            display: grid;
            grid-template-columns: minmax(310px, 1.2fr) minmax(260px, 1.55fr) auto auto auto auto;
            gap: 12px;
            align-items: center;
            padding: 14px;
            margin-bottom: 18px;
            border: 1px solid var(--line);
            border-radius: 24px;
            background: {topbar_bg};
            box-shadow: var(--navy-shadow);
            backdrop-filter: blur(26px);
        }}
        .brand-lockup {{
            display:flex;
            align-items:center;
            gap:12px;
            min-width:0;
        }}
        .brand-mark {{
            width:56px;
            height:56px;
            display:grid;
            place-items:center;
            border-radius:21px;
            background: linear-gradient(135deg, var(--cyan), var(--emerald));
            color:{theme["text_inverse"]} !important;
            font-weight:900;
            font-size:1.1rem;
            box-shadow: 0 14px 36px rgba(56,213,255,0.22);
        }}
        .brand-title {{
            color: var(--ink) !important;
            font-weight: 950;
            font-size: clamp(1.5rem, 2.2vw, 2.15rem);
            line-height: .96;
            letter-spacing: 0 !important;
        }}
        .brand-sub {{
            color: var(--muted) !important;
            font-size: .78rem;
            letter-spacing: .08em;
            text-transform: uppercase;
            margin-top: 3px;
        }}
        .search-shell {{
            min-height:46px;
            border:1px solid var(--line);
            border-radius: 16px;
            background: var(--glass);
            color: var(--muted) !important;
            display:flex;
            align-items:center;
            padding:0 15px;
            gap:10px;
        }}
        .notification-dot {{
            width:46px;height:46px;border-radius:16px;
            border:1px solid var(--line);
            display:grid;place-items:center;
            background:var(--glass);
            color:var(--ink) !important;
        }}
        .language-chip {{
            display:flex;
            gap:6px;
            padding:4px;
            border-radius: 999px;
            border:1px solid var(--line);
            background:var(--glass);
        }}
        .hero-panel {{
            border: 1px solid rgba(146, 224, 255, .22);
            border-radius: 28px;
            padding: clamp(1.5rem, 3vw, 3.2rem);
            background:
                linear-gradient(120deg, var(--glass), rgba(255,255,255,0.08)),
                radial-gradient(circle at 82% 20%, {theme["primary_glow"]}, transparent 34%);
            box-shadow: var(--navy-shadow);
            overflow:hidden;
            position:relative;
        }}
        .hero-panel:after {{
            content:"";
            position:absolute;
            right:24px;
            bottom:-52px;
            width:260px;
            height:260px;
            border-radius:50%;
            border:1px solid rgba(56,213,255,0.20);
            background:radial-gradient(circle, rgba(56,213,255,0.12), transparent 64%);
        }}
        .eyebrow {{
            display:inline-flex;
            color:var(--ink) !important;
            border:1px solid var(--line);
            background:var(--glass);
            border-radius:999px;
            padding:7px 11px;
            font-size:.78rem;
            font-weight:800;
            margin-bottom:18px;
        }}
        .hero-title {{
            color:var(--ink) !important;
            font-size: clamp(2.25rem, 5vw, 5.2rem);
            line-height:.98;
            max-width: 980px;
            font-weight:900;
            letter-spacing:0 !important;
            margin:0;
        }}
        .hero-subtitle {{
            color:var(--muted) !important;
            max-width:760px;
            font-size:1.08rem;
            line-height:1.7;
            margin-top:18px;
        }}
        .badge-row {{ display:flex; flex-wrap:wrap; gap:10px; margin-top:24px; }}
        .exam-badge {{
            color:var(--ink) !important;
            border:1px solid var(--line);
            background:var(--glass);
            border-radius:999px;
            padding:8px 13px;
            font-weight:800;
            font-size:.8rem;
        }}
        .lux-grid {{
            display:grid;
            grid-template-columns: repeat(4, minmax(0,1fr));
            gap:14px;
            margin: 18px 0;
        }}
        .lux-card, .module-card {{
            border:1px solid var(--line);
            border-radius:24px;
            background:{theme["card_gradient"]};
            box-shadow: var(--soft-shadow);
            padding:18px;
            min-height:136px;
            transition: transform .18s ease, box-shadow .18s ease, border-color .18s ease;
            color:var(--premium-card-text) !important;
        }}
        .module-card:hover, .lux-card:hover {{
            transform: translateY(-3px);
            border-color: rgba(56,213,255,0.42);
            box-shadow: 0 24px 70px rgba(2,18,34,.25), 0 0 0 1px rgba(46,229,157,.12);
        }}
        .card-kicker {{ color:var(--muted) !important; font-size:.72rem; font-weight:900; text-transform:uppercase; letter-spacing:.08em; }}
        .card-title {{ color:var(--premium-card-text) !important; font-size:1.05rem; font-weight:900; margin:.25rem 0 .4rem; }}
        .card-body {{ color:var(--premium-card-body) !important; font-size:.88rem; line-height:1.5; }}
        .progress-line {{ height:8px; background:#dbeaf2; border-radius:999px; overflow:hidden; margin-top:14px; }}
        .progress-line span {{ display:block; height:100%; background:linear-gradient(90deg, var(--cyan), var(--emerald)); border-radius:999px; }}
        .stTabs [data-baseweb="tab-list"],
        .stTabs div[role="tablist"] {{
            background:
                linear-gradient(135deg, var(--glass), rgba(255,255,255,0.18)),
                radial-gradient(circle at 90% 10%, {theme["primary_glow"]}, transparent 34%) !important;
            border:1px solid var(--line) !important;
            border-radius:18px !important;
            padding:6px !important;
            box-shadow:var(--soft-shadow) !important;
            backdrop-filter:blur(22px) !important;
        }}
        .stTabs button[role="tab"],
        .stTabs [data-baseweb="tab"] {{
            border-radius:13px !important;
            color:var(--muted) !important;
            background:rgba(255,255,255,0.18) !important;
            border:1px solid transparent !important;
            min-height:40px !important;
            transition:all .18s ease !important;
        }}
        .stTabs button[role="tab"] *,
        .stTabs [data-baseweb="tab"] * {{
            color:inherit !important;
        }}
        .stTabs button[role="tab"]:hover,
        .stTabs [data-baseweb="tab"]:hover {{
            background:{theme["hover_bg"]} !important;
            color:var(--ink) !important;
        }}
        .stTabs button[role="tab"][aria-selected="true"],
        .stTabs [data-baseweb="tab"][aria-selected="true"],
        .stTabs [aria-selected="true"] {{
            background:linear-gradient(135deg, var(--cyan), var(--emerald)) !important;
            color:{theme["text_inverse"]} !important;
            border-color:rgba(255,255,255,.24) !important;
            box-shadow:0 14px 28px {theme["primary_glow"]} !important;
        }}
        .stTabs [data-baseweb="tab-highlight"] {{
            display:none !important;
        }}
        .stTabs div[role="tabpanel"],
        .stTabs [data-baseweb="tab-panel"] {{
            background:transparent !important;
            color:var(--ink) !important;
            border:0 !important;
        }}
        [data-baseweb="popover"] > div,
        [data-baseweb="menu"],
        [data-baseweb="select"] > div,
        [data-testid="stExpander"],
        [data-testid="stForm"],
        [data-testid="stAlert"] {{
            background:var(--glass) !important;
            color:var(--ink) !important;
            border-color:var(--line) !important;
            box-shadow:var(--soft-shadow) !important;
        }}
        [data-baseweb="menu"] *,
        [data-baseweb="popover"] *,
        [data-testid="stExpander"] *,
        [data-testid="stAlert"] * {{
            color:var(--ink) !important;
        }}
        .clinical-dashboard-shell {{
            position: relative;
            overflow: hidden;
            margin: 18px 0 20px;
            padding: clamp(16px, 2.2vw, 28px);
            border-radius: 30px;
            border: 1px solid rgba(129, 140, 248, 0.24);
            background:
                radial-gradient(circle at 12% 14%, rgba(110, 231, 183, 0.30), transparent 28%),
                radial-gradient(circle at 88% 8%, rgba(129, 140, 248, 0.28), transparent 26%),
                linear-gradient(135deg, rgba(250, 245, 255, 0.96), rgba(236, 253, 245, 0.86) 46%, rgba(255, 247, 237, 0.92));
            box-shadow: 0 28px 90px rgba(79, 70, 229, 0.16);
            color: #1f1b3d !important;
            isolation: isolate;
        }}
        .clinical-dashboard-shell::before {{
            content: "";
            position: absolute;
            inset: -42% -16% auto auto;
            width: 44vw;
            height: 44vw;
            min-width: 280px;
            min-height: 280px;
            border-radius: 999px;
            background: conic-gradient(from 120deg, rgba(16, 185, 129, 0.28), rgba(79, 70, 229, 0.22), rgba(34, 211, 238, 0.26), rgba(16, 185, 129, 0.28));
            filter: blur(16px);
            opacity: .7;
            animation: clinicalOrb 18s linear infinite;
            z-index: -1;
        }}
        .clinical-dashboard-shell::after {{
            content: "🩺   ECG   🎓   Rx   ⚕   DNA   💉";
            position: absolute;
            left: -8%;
            right: -8%;
            bottom: 10px;
            color: rgba(79, 70, 229, 0.12);
            font-size: clamp(1.6rem, 5vw, 4.8rem);
            font-weight: 900;
            white-space: nowrap;
            letter-spacing: .12em;
            animation: medTicker 28s linear infinite;
            z-index: -1;
        }}
        .clinical-headline {{
            display: grid;
            grid-template-columns: minmax(0, 1fr) auto;
            gap: 16px;
            align-items: start;
            margin-bottom: 18px;
        }}
        .clinical-kicker {{
            display: inline-flex;
            align-items: center;
            gap: 8px;
            width: fit-content;
            padding: 7px 11px;
            border-radius: 999px;
            border: 1px solid rgba(79, 70, 229, 0.18);
            background: rgba(255,255,255,0.58);
            color: #4f46e5 !important;
            font-size: .76rem;
            font-weight: 900;
            text-transform: uppercase;
            letter-spacing: .08em;
        }}
        .clinical-title {{
            color: #241b4d !important;
            font-size: clamp(1.45rem, 3vw, 2.55rem);
            line-height: 1.05;
            font-weight: 950;
            margin: 10px 0 8px;
        }}
        .clinical-subtitle {{
            color: #655f85 !important;
            max-width: 720px;
            line-height: 1.65;
            font-size: .98rem;
        }}
        .clinical-live-chip {{
            display: inline-flex;
            align-items: center;
            gap: 9px;
            padding: 10px 13px;
            border-radius: 16px;
            border: 1px solid rgba(16, 185, 129, 0.22);
            background: rgba(255,255,255,0.68);
            color: #064e3b !important;
            font-weight: 900;
            box-shadow: 0 14px 30px rgba(16,185,129,.13);
            white-space: nowrap;
        }}
        .status-dot {{
            width: 10px;
            height: 10px;
            border-radius: 999px;
            background: #10b981;
            box-shadow: 0 0 0 0 rgba(16,185,129,.46);
            animation: statusPulse 1.55s ease-out infinite;
        }}
        .telemetry-grid {{
            display: grid;
            grid-template-columns: 1.35fr .9fr .9fr;
            gap: 14px;
            align-items: stretch;
        }}
        .telemetry-panel, .progress-orbit-card, .clinical-flip-card {{
            border: 1px solid rgba(255,255,255,0.74);
            background: rgba(255,255,255,0.62);
            box-shadow: 0 18px 48px rgba(79, 70, 229, 0.12);
            backdrop-filter: blur(22px);
        }}
        .telemetry-panel {{
            border-radius: 26px;
            padding: 18px;
            min-height: 260px;
            position: relative;
            overflow: hidden;
        }}
        .telemetry-panel::after {{
            content: "";
            position: absolute;
            inset: auto -10% 0 -10%;
            height: 46%;
            background: linear-gradient(180deg, transparent, rgba(110,231,183,.18));
            pointer-events: none;
        }}
        .telemetry-label, .orbit-label, .flip-label {{
            color: #6d668a !important;
            font-size: .74rem;
            font-weight: 950;
            text-transform: uppercase;
            letter-spacing: .08em;
        }}
        .telemetry-value {{
            color: #1f1b3d !important;
            font-size: clamp(2.3rem, 5vw, 4.6rem);
            font-weight: 950;
            line-height: .94;
            margin-top: 10px;
            text-shadow: 0 0 26px rgba(16,185,129,.16);
        }}
        .telemetry-unit {{
            color: #655f85 !important;
            font-size: .88rem;
            margin: 7px 0 18px;
        }}
        .ecg-window {{
            position: relative;
            height: 108px;
            border-radius: 20px;
            overflow: hidden;
            border: 1px solid rgba(79,70,229,.12);
            background:
                linear-gradient(rgba(79,70,229,.07) 1px, transparent 1px),
                linear-gradient(90deg, rgba(79,70,229,.07) 1px, transparent 1px),
                rgba(250,245,255,.72);
            background-size: 22px 22px;
        }}
        .ecg-track {{
            width: 170%;
            height: 100%;
            animation: ecgSlide 5.4s linear infinite;
        }}
        .ecg-track polyline {{
            fill: none;
            stroke: #10b981;
            stroke-width: 4;
            stroke-linejoin: round;
            stroke-linecap: round;
            filter: drop-shadow(0 0 9px rgba(16,185,129,.55));
            stroke-dasharray: 1080;
            stroke-dashoffset: 1080;
            animation: ecgDraw 2.8s ease-in-out infinite;
        }}
        .orbit-grid {{
            display: grid;
            grid-template-columns: repeat(2, minmax(0, 1fr));
            gap: 14px;
        }}
        .progress-orbit-card {{
            min-height: 123px;
            border-radius: 24px;
            padding: 16px;
            display: grid;
            grid-template-columns: auto 1fr;
            gap: 13px;
            align-items: center;
            transition: transform .2s ease, box-shadow .2s ease;
        }}
        .progress-orbit-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 24px 62px rgba(79, 70, 229, 0.18);
        }}
        .progress-ring {{
            --value: 70;
            --ring-color: #10b981;
            width: 76px;
            height: 76px;
            border-radius: 50%;
            display: grid;
            place-items: center;
            background:
                radial-gradient(circle closest-side, rgba(255,255,255,.94) 71%, transparent 72%),
                conic-gradient(var(--ring-color) calc(var(--value) * 1%), rgba(226,232,240,.9) 0);
            box-shadow: inset 0 0 18px rgba(255,255,255,.85), 0 12px 26px rgba(79,70,229,.12);
        }}
        .progress-ring span {{
            color: #241b4d !important;
            font-size: .95rem;
            font-weight: 950;
        }}
        .orbit-title {{
            color: #241b4d !important;
            font-weight: 950;
            margin: 4px 0 3px;
        }}
        .orbit-copy {{
            color: #655f85 !important;
            font-size: .8rem;
            line-height: 1.35;
        }}
        .state-stable {{ --ring-color: #10b981; border-color: rgba(16,185,129,.24); }}
        .state-warn {{ --ring-color: #f59e0b; border-color: rgba(245,158,11,.28); }}
        .state-risk {{ --ring-color: #f43f5e; border-color: rgba(244,63,94,.24); }}
        .state-action {{ --ring-color: #4f46e5; border-color: rgba(79,70,229,.24); }}
        .flip-lab-grid {{
            display: grid;
            grid-template-columns: repeat(3, minmax(0, 1fr));
            gap: 14px;
            margin-top: 14px;
            perspective: 1200px;
        }}
        .clinical-flip-card {{
            min-height: 214px;
            border-radius: 26px;
            background: transparent;
            perspective: 1100px;
            box-shadow: none;
            border: 0;
        }}
        .clinical-flip-inner {{
            position: relative;
            width: 100%;
            min-height: 214px;
            transform-style: preserve-3d;
            transition: transform .7s cubic-bezier(.2,.8,.2,1);
        }}
        .clinical-flip-card:hover .clinical-flip-inner {{
            transform: rotateY(180deg) translateY(-3px);
        }}
        .clinical-flip-face {{
            position: absolute;
            inset: 0;
            display: flex;
            flex-direction: column;
            justify-content: space-between;
            border-radius: 26px;
            padding: 18px;
            border: 1px solid rgba(255,255,255,.76);
            backface-visibility: hidden;
            background:
                radial-gradient(circle at 86% 18%, rgba(110,231,183,.24), transparent 34%),
                rgba(255,255,255,.68);
            box-shadow: 0 18px 48px rgba(79, 70, 229, 0.13);
        }}
        .clinical-flip-back {{
            transform: rotateY(180deg);
            background:
                radial-gradient(circle at 16% 20%, rgba(34,211,238,.25), transparent 34%),
                linear-gradient(135deg, rgba(79,70,229,.90), rgba(67,56,202,.82));
        }}
        .flip-icon {{
            width: 48px;
            height: 48px;
            border-radius: 18px;
            display: grid;
            place-items: center;
            background: linear-gradient(135deg, #4f46e5, #10b981);
            color: #ffffff !important;
            font-size: 1.25rem;
            box-shadow: 0 14px 30px rgba(79,70,229,.25);
        }}
        .flip-title {{
            color: #241b4d !important;
            font-weight: 950;
            font-size: 1.08rem;
            margin-top: 12px;
        }}
        .flip-copy {{
            color: #655f85 !important;
            font-size: .86rem;
            line-height: 1.5;
            margin-top: 8px;
        }}
        .clinical-flip-back .flip-label,
        .clinical-flip-back .flip-title,
        .clinical-flip-back .flip-copy {{
            color: #f8fbff !important;
        }}
        .clinical-flip-back .flip-copy {{
            opacity: .88;
        }}
        .clinical-action-pill {{
            display: inline-flex;
            width: fit-content;
            align-items: center;
            gap: 7px;
            padding: 8px 11px;
            border-radius: 999px;
            color: #eef2ff !important;
            background: rgba(255,255,255,.16);
            border: 1px solid rgba(255,255,255,.24);
            font-size: .76rem;
            font-weight: 900;
        }}
        @keyframes clinicalOrb {{
            to {{ transform: rotate(360deg); }}
        }}
        @keyframes medTicker {{
            from {{ transform: translateX(-8%); }}
            to {{ transform: translateX(8%); }}
        }}
        @keyframes statusPulse {{
            0% {{ box-shadow: 0 0 0 0 rgba(16,185,129,.46); }}
            70% {{ box-shadow: 0 0 0 13px rgba(16,185,129,0); }}
            100% {{ box-shadow: 0 0 0 0 rgba(16,185,129,0); }}
        }}
        @keyframes ecgSlide {{
            from {{ transform: translateX(0); }}
            to {{ transform: translateX(-30%); }}
        }}
        @keyframes ecgDraw {{
            0% {{ stroke-dashoffset: 1080; opacity: .55; }}
            45% {{ stroke-dashoffset: 0; opacity: 1; }}
            100% {{ stroke-dashoffset: -1080; opacity: .72; }}
        }}
        .student-workspace {{
            display:grid;
            grid-template-columns: auto 1fr auto;
            gap:14px;
            align-items:center;
            margin: 18px 0 14px;
            padding: 16px;
            border-radius: 24px;
            border: 1px solid var(--line);
            background:
                linear-gradient(135deg, var(--glass), rgba(255,255,255,0.08)),
                radial-gradient(circle at 94% 18%, {theme["primary_glow"]}, transparent 34%);
            box-shadow: var(--soft-shadow);
            backdrop-filter: blur(22px);
        }}
        .student-symbol {{
            width: 54px;
            height: 54px;
            border-radius: 20px;
            display:grid;
            place-items:center;
            background: linear-gradient(135deg, var(--cyan), var(--emerald));
            color:{theme["text_inverse"]} !important;
            font-size:1.35rem;
            font-weight: 900;
            box-shadow: 0 16px 34px rgba(56,213,255,0.20);
        }}
        .student-workspace-title {{
            color:var(--ink) !important;
            font-weight: 900;
            font-size: 1.18rem;
            line-height: 1.15;
        }}
        .student-workspace-sub {{
            color:var(--muted) !important;
            font-size:.82rem;
            margin-top:4px;
        }}
        .student-badge {{
            border:1px solid var(--line);
            background:var(--glass);
            color:var(--ink) !important;
            border-radius:999px;
            padding:8px 12px;
            font-size:.72rem;
            font-weight:900;
            white-space:nowrap;
        }}
        .student-nav-grid div[data-testid="stHorizontalBlock"] {{
            gap: 0 !important;
            align-items: stretch !important;
        }}
        .student-nav-grid {{
            display: flex;
            align-items: center;
            gap: 7px;
            flex-wrap: wrap;
            background: rgba(255,255,255,0.91);
            border: 1px solid rgba(255,255,255,0.84);
            border-radius: 16px;
            padding: 8px 10px;
            box-shadow: 0 16px 42px rgba(31,41,55,0.10);
            backdrop-filter: blur(18px);
            margin-bottom: 18px;
            overflow-x: auto;
            scrollbar-width: none;
        }}
        .student-nav-grid::-webkit-scrollbar {{
            display: none;
        }}
        [data-testid="stSegmentedControl"] {{
            background: rgba(255,255,255,0.91);
            border: 1px solid rgba(255,255,255,0.84);
            border-radius: 16px;
            padding: 8px 10px;
            box-shadow: 0 16px 42px rgba(31,41,55,0.10);
            backdrop-filter: blur(18px);
            margin-bottom: 18px;
            overflow-x: auto;
            scrollbar-width: none;
        }}
        [data-testid="stSegmentedControl"]::-webkit-scrollbar {{
            display: none;
        }}
        [data-testid="stSegmentedControl"] [role="group"],
        [data-testid="stSegmentedControl"] [role="radiogroup"] {{
            display: flex !important;
            align-items: center !important;
            gap: 7px !important;
            flex-wrap: wrap !important;
        }}
        [role="radiogroup"] button,
        [data-testid="stSegmentedControl"] button {{
            display: inline-flex !important;
            align-items: center !important;
            min-height: 38px !important;
            border-radius: 10px !important;
            border: 1px solid transparent !important;
            background: rgba(255,255,255,0.92) !important;
            padding: 0 12px !important;
            color: {theme["text_muted"]} !important;
            transition: all 0.18s ease !important;
            box-shadow: 0 6px 18px rgba(31,41,55,0.06) !important;
        }}
        [role="radiogroup"] button p,
        [data-testid="stSegmentedControl"] button p {{
            color: inherit !important;
            font-weight: 850 !important;
            font-size: 0.86rem !important;
            white-space: nowrap !important;
        }}
        [role="radiogroup"] button:hover,
        [data-testid="stSegmentedControl"] button:hover {{
            background: {theme["hover_bg"]} !important;
            border-color: {theme["card_border"]} !important;
            color: {theme["text"]} !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 10px 24px rgba(31,41,55,0.08) !important;
        }}
        [role="radiogroup"] button[aria-pressed="true"],
        [role="radiogroup"] button[aria-checked="true"],
        [role="radiogroup"] button[data-checked="true"],
        [data-testid="stSegmentedControl"] button[aria-pressed="true"],
        [data-testid="stSegmentedControl"] button[aria-checked="true"] {{
            background: linear-gradient(135deg, #9a3412, #c2410c) !important;
            color: #fff7ed !important;
            border-color: rgba(154,52,18,0.32) !important;
            box-shadow: 0 12px 28px rgba(154,52,18,0.22) !important;
        }}
        .student-nav-grid [role="radiogroup"] {{
            display: flex;
            align-items: center;
            gap: 7px;
            flex-wrap: wrap;
        }}
        .student-nav-grid [data-testid="stRadio"] > label {{
            display: none !important;
        }}
        .student-nav-grid [data-testid="stRadio"] div[role="radio"] {{
            border-radius: 10px !important;
            border: 1px solid transparent !important;
            background: transparent !important;
            padding: 0 12px !important;
            min-height: 38px !important;
            color: {theme["text_muted"]} !important;
            transition: all 0.18s ease !important;
            box-shadow: none !important;
        }}
        .student-nav-grid [data-testid="stRadio"] div[role="radio"] > div:first-child {{
            display: none !important;
        }}
        .student-nav-grid [data-testid="stRadio"] div[role="radio"] p {{
            color: inherit !important;
            font-weight: 850 !important;
            font-size: 0.86rem !important;
            white-space: nowrap !important;
        }}
        .student-nav-grid [data-testid="stRadio"] div[role="radio"]:hover {{
            background: {theme["hover_bg"]} !important;
            border-color: {theme["card_border"]} !important;
            color: {theme["text"]} !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 10px 24px rgba(31,41,55,0.08) !important;
        }}
        .student-nav-grid [data-testid="stRadio"] div[role="radio"][aria-checked="true"] {{
            background: linear-gradient(135deg, #9a3412, #c2410c) !important;
            color: #fff7ed !important;
            border-color: rgba(154,52,18,0.32) !important;
            box-shadow: 0 12px 28px rgba(154,52,18,0.22) !important;
        }}
        .student-nav-link {{
            display: inline-flex;
            align-items: center;
            gap: 6px;
            min-height: 38px;
            padding: 0 12px;
            border-radius: 10px;
            border: 1px solid transparent;
            color: {theme["text_muted"]} !important;
            text-decoration: none !important;
            font-weight: 850 !important;
            letter-spacing: 0 !important;
            white-space: nowrap;
            transition: all 0.18s ease;
            font-size: 0.86rem;
        }}
        .student-nav-link:hover {{
            background: {theme["hover_bg"]} !important;
            border-color: {theme["card_border"]} !important;
            color: {theme["text"]} !important;
            transform: translateY(-1px) !important;
            box-shadow: 0 10px 24px rgba(31,41,55,0.08) !important;
        }}
        .student-nav-link.active {{
            background: linear-gradient(135deg, #9a3412, #c2410c) !important;
            color: #fff7ed !important;
            border-color: rgba(154,52,18,0.32) !important;
            box-shadow: 0 12px 28px rgba(154,52,18,0.22) !important;
        }}
        .student-nav-icon {{
            display:inline-flex;
            align-items:center;
            justify-content:center;
            font-size: 0.9rem;
            line-height: 1;
        }}
        .section-title {{
            color:var(--ink) !important;
            font-weight:900;
            font-size:1.25rem;
            margin: 1.3rem 0 .75rem;
        }}
        .az-pill {{
            display:inline-flex;
            margin: 0 8px 8px 0;
            padding:8px 12px;
            border-radius:999px;
            background:var(--glass);
            border:1px solid var(--line);
            color:var(--ink) !important;
            font-weight:800;
            font-size:.78rem;
        }}
        .disclaimer {{
            margin-top: 22px;
            color:var(--muted) !important;
            font-size:.82rem;
            border-top:1px solid var(--line);
            padding-top:14px;
        }}
        @media (max-width: 1100px) {{
            .med-topbar {{ grid-template-columns: 1fr; }}
            .lux-grid {{ grid-template-columns: repeat(2, minmax(0,1fr)); }}
            .clinical-headline {{ grid-template-columns: 1fr; }}
            .telemetry-grid {{ grid-template-columns: 1fr; }}
            .brand-title {{ font-size: clamp(1.38rem, 5vw, 1.82rem); }}
        }}
        @media (max-width: 680px) {{
            .lux-grid {{ grid-template-columns: 1fr; }}
            .hero-panel {{ border-radius:22px; }}
            .module-card, .lux-card {{ border-radius:20px; }}
            .student-workspace {{ grid-template-columns: auto 1fr; }}
            .student-badge {{ display:none; }}
            .clinical-dashboard-shell {{ border-radius: 24px; padding: 14px; }}
            .orbit-grid, .flip-lab-grid {{ grid-template-columns: 1fr; }}
            .progress-orbit-card {{ min-height: 106px; }}
            .clinical-live-chip {{ width: fit-content; }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="medical-animation-layer">
            <div class="cinema-sweep"></div>
            <span class="medical-float instrument">🩺</span>
            <span class="medical-float instrument">🎓</span>
            <span class="medical-float wordmark">ECG</span>
            <span class="medical-float wordmark">DNA</span>
            <span class="medical-float wordmark">Rx</span>
            <span class="medical-float wordmark">OSCE</span>
            <span class="medical-float instrument">💉</span>
            <span class="medical-float instrument">🔬</span>
            <span class="medical-float instrument">🧪</span>
            <span class="medical-float instrument">🧬</span>
            <span class="medical-float instrument">🩻</span>
            <span class="medical-float instrument">💊</span>
            <span class="medical-float instrument">🩹</span>
            <span class="medical-float instrument">📚</span>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_language_selector():
    active = st.session_state.get("language", "en")
    col_en, col_ar = st.columns(2)
    with col_en:
        if st.button("EN", type="primary" if active == "en" else "secondary", use_container_width=True, key="premium_lang_en"):
            st.session_state.language = "en"
            if st.session_state.get("logged_in"):
                update_language(st.session_state.user["id"], "en")
            st.rerun()
    with col_ar:
        if st.button("AR", type="primary" if active == "ar" else "secondary", use_container_width=True, key="premium_lang_ar"):
            st.session_state.language = "ar"
            if st.session_state.get("logged_in"):
                update_language(st.session_state.user["id"], "ar")
            st.rerun()


def render_topbar(theme, themes):
    st.markdown(
        f"""
        <div class="med-topbar">
            <div class="brand-lockup">
                <div class="brand-mark">MS</div>
                <div>
                    <div class="brand-title">MedStudy Oman</div>
                    <div class="brand-sub">Premium AI Clinical Workspace</div>
                </div>
            </div>
            <div class="search-shell">⌕ {get_translation("search")}</div>
            <div class="notification-dot" title="{get_translation("notifications")}">◌</div>
            <div></div>
            <div></div>
            <div></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    controls = st.columns([1.35, 0.75, 1.05, 1.05, 0.8])
    with controls[0]:
        theme_keys = list(themes.keys())
        current = st.session_state.get("theme", theme_keys[0])
        selected = st.selectbox("Theme", theme_keys, index=theme_keys.index(current) if current in theme_keys else 0, label_visibility="collapsed")
        if selected != current:
            st.session_state.theme = selected
            if st.session_state.get("logged_in"):
                update_theme(st.session_state.user["id"], selected)
            st.rerun()
    with controls[1]:
        if st.button("⌂ Home", use_container_width=True, key="home_top"):
            st.session_state.page = "dashboard"
            st.query_params["page"] = "dashboard"
            st.rerun()
    with controls[2]:
        render_language_selector()
    with controls[3]:
        if st.session_state.get("logged_in"):
            if st.button(get_translation("profile"), use_container_width=True, key="profile_top"):
                st.session_state.page = "profile"
                st.rerun()
        else:
            if st.button(get_translation("login"), type="primary", use_container_width=True, key="login_top"):
                st.session_state.page = "auth"
                st.session_state.auth_mode = "login"
                st.rerun()
    with controls[4]:
        if st.session_state.get("logged_in") and st.button(get_translation("logout"), use_container_width=True, key="logout_top"):
            for key in ["logged_in", "user"]:
                st.session_state[key] = False if key == "logged_in" else None
            st.session_state.page = "dashboard"
            st.rerun()


def render_sidebar():
    current_page = st.session_state.get("page", "dashboard")
    language = st.session_state.get("language", "en")
    nav_options = []
    option_to_page = {}
    for _, page_id, icon, label_en, label_ar, _ in PRO_NAV_ITEMS:
        if page_id == "admin_content":
            try:
                from content_system import is_admin_user
                if not is_admin_user(st.session_state.get("user")):
                    continue
            except Exception:
                continue
        label = label_ar if language == "ar" else label_en
        option = f"{icon} {label}"
        nav_options.append(option)
        option_to_page[option] = page_id
    page_to_option = {page_id: option for option, page_id in option_to_page.items()}
    current_option = page_to_option.get(current_page, nav_options[0])
    st.markdown(
        f"""
        <div class="student-workspace">
            <div class="student-symbol">⚕</div>
            <div>
                <div class="student-workspace-title">{get_translation("workspace")}</div>
                <div class="student-workspace-sub">{get_translation("workspace_subtitle")}</div>
            </div>
            <div class="student-badge">SQU-COM · OMSB · USMLE</div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    selected_option = st.segmented_control(
        "Workspace modules",
        nav_options,
        default=current_option,
        label_visibility="collapsed",
        key="workspace_module_selector",
    )
    selected_option = selected_option or current_option
    selected_page = option_to_page[selected_option]
    if current_page in page_to_option and selected_page != current_page:
        st.session_state.page = selected_page
        st.query_params["page"] = selected_page
        st.rerun()


PAGE_CINEMA = {
    "dashboard": ("⌂", "Student Command Center", "Your home base for today: continue studying, see what matters, and jump into the next useful task.", ["🎓 Graduation", "🩺 Clinical", "ECG"]),
    "profile": ("👤", "Professional Profile", "See your progress, saved work, and study identity in one private student dashboard.", ["📊 Progress", "🔖 Saved", "🎯 Goals"]),
    "study_pillars": ("✚", "Premium Study Pillars", "Use the permanent resource vault, generate AI study modules, craft mnemonics, and ask the clinical tutor.", ["📚 Vault", "AI", "💡 Memory"]),
    "az_hub": ("🧠", "A-Z Medical Knowledge Hub", "Pick any subject and revise it with notes, diseases, tables, skills, and exam points.", ["🧬 DNA", "🔬 Lab", "📚 Notes"]),
    "subjects": ("📚", "Knowledge Library", "Browse medicine in a simple student-friendly way when you need to understand before memorising.", ["📖 Chapters", "✎ Review", "💡 Recall"]),
    "mcq_quiz": ("📝", "Question Bank", "Practice exam-style questions, learn from mistakes, and build confidence one set at a time.", ["? MCQs", "⏱ Timed", "📈 Score"]),
    "flashcards": ("💎", "Flashcard Vault", "Use quick recall cards for facts that are easy to forget before exams and ward rounds.", ["⚡ Recall", "🔁 Review", "🎓 Mastery"]),
    "ai_tutor": ("🤖", "AI Study Tutor", "Ask for simple explanations, clinical examples, or a study plan when a topic feels confusing.", ["AI Tutor", "🩺 Cases", "💬 Explain"]),
    "ai_mnemonics": ("💡", "AI Mnemonics Studio", "Turn long lists, pathways, and criteria into memorable English or Arabic study tricks.", ["💡 Memory", "🎨 Visual", "🧠 Quiz"]),
    "osce_timer": ("🩺", "Clinical Skills Lab", "Practise stations like a real student exam: timing, structure, checklists, and closing summaries.", ["OSCE", "⏱ Timer", "✚ Skills"]),
    "pomodoro": ("⏱", "Focus Mode", "Start calm study blocks when you need to stop scrolling and finish one clear task.", ["⏱ Focus", "☕ Break", "✅ Session"]),
    "analytics": ("📊", "Performance Insights", "Find what is strong, what needs work, and what to study next without guessing.", ["📈 Trends", "🎯 Weak Areas", "🏆 Strong"]),
    "resources": ("📖", "Medical References", "Keep trusted references nearby when you want to check a guideline, source, or topic link.", ["⌘ Refs", "🔬 Evidence", "📚 Sources"]),
    "shared_notes": ("✍️", "Study Notes", "Write quick pearls, save useful thoughts, and keep revision notes for later.", ["✍️ Notes", "🔖 Bookmark", "🧾 Revision"]),
    "settings": ("⚙️", "Settings", "Change your language, theme, study goal, and exam track whenever your routine changes.", ["🎨 Themes", "🌍 Language", "🎯 Goal"]),
    "admin_content": ("🛠", "Admin Content Panel", "Add, import, draft, review, and publish medical content without changing app code.", ["CSV", "JSON", "Drafts"]),
    "about": ("ℹ️", "About MedStudy Oman", "Meet the developer and learn why this platform was built for medical students in Oman.", ["👩‍💻 Developer", "🇴🇲 Oman", "🩺 Mission"]),
}


def render_cinematic_page_banner(page_id: str):
    icon, title, subtitle, chips = PAGE_CINEMA.get(
        page_id,
        ("⚕", "MedStudy Workspace", "A cinematic clinical study space for modern medical learners.", ["🩺 Tools", "🎓 Study", "💊 Medicine"]),
    )
    chip_html = "".join(f'<span class="cinema-tool-chip">{chip}</span>' for chip in chips)
    st.markdown(
        f"""
        <div class="cinematic-page-strip">
            <div class="cinema-page-symbol">{icon}</div>
            <div>
                <div class="cinema-page-title">{title}</div>
                <div class="cinema-page-sub">{subtitle}</div>
            </div>
            <div class="cinema-tool-row">{chip_html}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def render_hero():
    st.markdown(
        f"""
        <section class="hero-panel">
            <div class="eyebrow">AI-powered clinical learning for Oman and global exams</div>
            <h1 class="hero-title">{get_translation("master_medicine")}</h1>
            <p class="hero-subtitle">{get_translation("hero_sub")}</p>
            <div class="badge-row">
                <span class="exam-badge">SQU-COM</span>
                <span class="exam-badge">OMSB</span>
                <span class="exam-badge">USMLE</span>
                <span class="exam-badge">PLAB</span>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_stat_cards(stats):
    cards = [
        (get_translation("daily_streak"), f"{stats.get('streak', 0)} days", "Consistency across recent study days", 72),
        (get_translation("study_time"), f"{stats.get('study_hours', 0)} hrs", "Total focused learning time", 54),
        ("Quiz Average", f"{stats.get('mcq_percent', 0)}%", "Weighted across saved attempts", int(stats.get("mcq_percent", 0) or 42)),
        ("Progress", f"{stats.get('overall_progress', 38)}%", "Estimated platform mastery", stats.get("overall_progress", 38)),
    ]
    st.markdown('<div class="lux-grid">', unsafe_allow_html=True)
    for title, value, body, progress in cards:
        st.markdown(
            f"""
            <div class="lux-card">
                <div class="card-kicker">{title}</div>
                <div class="card-title" style="font-size:1.75rem;">{value}</div>
                <div class="card-body">{body}</div>
                <div class="progress-line"><span style="width:{min(100, max(0, progress))}%"></span></div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown("</div>", unsafe_allow_html=True)


def render_module_card(icon, title, description, progress, page_id, cta="Open"):
    st.markdown(
        f"""
        <div class="module-card">
            <div class="card-kicker">{icon} Module</div>
            <div class="card-title">{title}</div>
            <div class="card-body">{description}</div>
            <div class="progress-line"><span style="width:{progress}%"></span></div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    if st.button(cta, key=f"open_{page_id}_{title}", use_container_width=True):
        st.session_state.page = page_id
        st.rerun()


def _clamp_percent(value, fallback=0):
    try:
        number = int(float(value))
    except (TypeError, ValueError):
        number = fallback
    return min(100, max(0, number))


def _clinical_state(value, stable=75, warn=50):
    value = _clamp_percent(value)
    if value >= stable:
        return "state-stable", "Stable", "Emerald learning momentum"
    if value >= warn:
        return "state-warn", "Watch", "Needs a focused revision pulse"
    return "state-risk", "Priority", "Schedule targeted recall today"


def render_clinical_dashboard_visuals(stats):
    progress = _clamp_percent(stats.get("overall_progress", 38), 38)
    quiz = _clamp_percent(stats.get("mcq_percent", 0), 42)
    streak = _clamp_percent(stats.get("streak", 0), 0)
    study_hours = _clamp_percent(stats.get("study_hours", 0), 0)
    retention = _clamp_percent(round((progress * 0.52) + (quiz * 0.38) + min(streak, 20) * 0.5), 62)
    readiness = _clamp_percent(round((quiz * 0.46) + (progress * 0.44) + min(study_hours, 40) * 0.25), 58)
    focus_score = _clamp_percent(max(34, min(96, 48 + (streak * 4) + (study_hours * 2))), 64)
    weak_area = (stats.get("weak_areas") or ["Pharmacology"])[0]
    strong_area = (stats.get("strong_areas") or ["Clinical reasoning"])[0]
    progress_class, progress_label, progress_copy = _clinical_state(progress)
    quiz_class, quiz_label, quiz_copy = _clinical_state(quiz)
    retention_class, retention_label, retention_copy = _clinical_state(retention)
    readiness_class, readiness_label, readiness_copy = _clinical_state(readiness)

    st.markdown(
        f"""
        <section class="clinical-dashboard-shell">
            <div class="clinical-headline">
                <div>
                    <div class="clinical-kicker"><span class="status-dot"></span> Live clinical workspace</div>
                    <div class="clinical-title">Immersive Study Telemetry</div>
                    <div class="clinical-subtitle">
                        A soft-lavender command center with animated vitals, glowing progress states,
                        and hover-reveal cards for rapid clinical recall.
                    </div>
                </div>
                <div class="clinical-live-chip"><span class="status-dot"></span> Synced dashboard active</div>
            </div>
            <div class="telemetry-grid">
                <div class="telemetry-panel">
                    <div class="telemetry-label">Today's learning rhythm</div>
                    <div class="telemetry-value">{focus_score}%</div>
                    <div class="telemetry-unit">Focus flow from streak, study time, and saved activity</div>
                    <div class="ecg-window">
                        <svg class="ecg-track" viewBox="0 0 920 120" preserveAspectRatio="none" aria-hidden="true">
                            <polyline points="0,68 50,68 70,54 88,84 112,16 145,98 172,68 230,68 250,58 272,76 302,68 372,68 392,48 414,88 442,28 470,96 502,68 570,68 590,54 612,80 644,68 708,68 730,45 756,90 782,22 812,98 842,68 920,68" />
                        </svg>
                    </div>
                </div>
                <div class="orbit-grid">
                    <div class="progress-orbit-card {progress_class}" style="--value:{progress};">
                        <div class="progress-ring"><span>{progress}%</span></div>
                        <div>
                            <div class="orbit-label">{progress_label}</div>
                            <div class="orbit-title">Platform progress</div>
                            <div class="orbit-copy">{progress_copy}</div>
                        </div>
                    </div>
                    <div class="progress-orbit-card {quiz_class}" style="--value:{quiz};">
                        <div class="progress-ring"><span>{quiz}%</span></div>
                        <div>
                            <div class="orbit-label">{quiz_label}</div>
                            <div class="orbit-title">Question accuracy</div>
                            <div class="orbit-copy">{quiz_copy}</div>
                        </div>
                    </div>
                    <div class="progress-orbit-card {retention_class}" style="--value:{retention};">
                        <div class="progress-ring"><span>{retention}%</span></div>
                        <div>
                            <div class="orbit-label">{retention_label}</div>
                            <div class="orbit-title">Recall retention</div>
                            <div class="orbit-copy">{retention_copy}</div>
                        </div>
                    </div>
                    <div class="progress-orbit-card {readiness_class}" style="--value:{readiness};">
                        <div class="progress-ring"><span>{readiness}%</span></div>
                        <div>
                            <div class="orbit-label">{readiness_label}</div>
                            <div class="orbit-title">Exam readiness</div>
                            <div class="orbit-copy">{readiness_copy}</div>
                        </div>
                    </div>
                </div>
                <div class="telemetry-panel">
                    <div class="telemetry-label">Clinical signal board</div>
                    <div class="telemetry-value" style="font-size:clamp(2rem, 4vw, 3.6rem);">Rx</div>
                    <div class="telemetry-unit">Weak signal: {weak_area}<br>Strong signal: {strong_area}</div>
                    <svg viewBox="0 0 280 112" width="100%" height="112" aria-hidden="true">
                        <defs>
                            <linearGradient id="clinicalBars" x1="0" x2="1">
                                <stop offset="0%" stop-color="#4f46e5"/>
                                <stop offset="100%" stop-color="#10b981"/>
                            </linearGradient>
                        </defs>
                        <rect x="12" y="68" width="32" height="32" rx="10" fill="url(#clinicalBars)" opacity=".84"/>
                        <rect x="58" y="42" width="32" height="58" rx="10" fill="url(#clinicalBars)" opacity=".72"/>
                        <rect x="104" y="24" width="32" height="76" rx="10" fill="url(#clinicalBars)" opacity=".9"/>
                        <rect x="150" y="54" width="32" height="46" rx="10" fill="url(#clinicalBars)" opacity=".7"/>
                        <rect x="196" y="18" width="32" height="82" rx="10" fill="url(#clinicalBars)" opacity=".92"/>
                        <path d="M15 31 C60 8, 84 56, 128 35 S206 14, 250 34" stroke="#10b981" stroke-width="5" fill="none" stroke-linecap="round" opacity=".75"/>
                    </svg>
                </div>
            </div>
            <div class="flip-lab-grid">
                <div class="clinical-flip-card">
                    <div class="clinical-flip-inner">
                        <div class="clinical-flip-face">
                            <div>
                                <div class="flip-icon">🧠</div>
                                <div class="flip-label">Flash recall</div>
                                <div class="flip-title">Mnemonic Capsule</div>
                                <div class="flip-copy">Hover to reveal a compact memory prompt for the next revision sprint.</div>
                            </div>
                            <div class="orbit-copy">3D hover reveal</div>
                        </div>
                        <div class="clinical-flip-face clinical-flip-back">
                            <div>
                                <div class="flip-label">Reveal</div>
                                <div class="flip-title">Think: definition, danger signs, decision.</div>
                                <div class="flip-copy">Convert every note into one clinical trigger, one investigation, and one management action.</div>
                            </div>
                            <span class="clinical-action-pill">Launch recall loop</span>
                        </div>
                    </div>
                </div>
                <div class="clinical-flip-card">
                    <div class="clinical-flip-inner">
                        <div class="clinical-flip-face">
                            <div>
                                <div class="flip-icon">🩺</div>
                                <div class="flip-label">OSCE station</div>
                                <div class="flip-title">Clinical Skills Pulse</div>
                                <div class="flip-copy">Practice a focused exam flow with timing, findings, and closing summary.</div>
                            </div>
                            <div class="orbit-copy">Hover for station brief</div>
                        </div>
                        <div class="clinical-flip-face clinical-flip-back">
                            <div>
                                <div class="flip-label">Reveal</div>
                                <div class="flip-title">Cardio exam: inspect, palpate, auscultate, summarize.</div>
                                <div class="flip-copy">End with likely diagnosis, severity, and immediate next step.</div>
                            </div>
                            <span class="clinical-action-pill">Start 8 min station</span>
                        </div>
                    </div>
                </div>
                <div class="clinical-flip-card">
                    <div class="clinical-flip-inner">
                        <div class="clinical-flip-face">
                            <div>
                                <div class="flip-icon">🎓</div>
                                <div class="flip-label">Exam track</div>
                                <div class="flip-title">Premium Study Sprint</div>
                                <div class="flip-copy">A student-friendly command card for SQU-COM, OMSB, USMLE, and PLAB prep.</div>
                            </div>
                            <div class="orbit-copy">Hover for next step</div>
                        </div>
                        <div class="clinical-flip-face clinical-flip-back">
                            <div>
                                <div class="flip-label">Reveal</div>
                                <div class="flip-title">Next best step: 15 MCQs plus 5 flashcards.</div>
                                <div class="flip-copy">Prioritize {weak_area}, then protect your strength in {strong_area}.</div>
                            </div>
                            <span class="clinical-action-pill">Begin sprint</span>
                        </div>
                    </div>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def render_dashboard(stats):
    render_hero()
    render_clinical_dashboard_visuals(stats)
    st.markdown(
        """
        <div class="lux-grid">
            <div class="lux-card">
                <div class="card-kicker">✚ Start Here</div>
                <div class="card-title">Pick one clinical goal</div>
                <div class="card-body">Choose one small task for now: read a topic, answer a few questions, or practise one OSCE skill.</div>
            </div>
            <div class="lux-card">
                <div class="card-kicker">◇ Study Flow</div>
                <div class="card-title">Learn → Recall → Test</div>
                <div class="card-body">Study the idea first, recall it without looking, then test yourself so the lesson actually sticks.</div>
            </div>
            <div class="lux-card">
                <div class="card-kicker">⚕ Clinical Mode</div>
                <div class="card-title">Think like a doctor</div>
                <div class="card-body">Connect facts to real patients: symptoms, investigations, management, and what to say in an OSCE.</div>
            </div>
            <div class="lux-card">
                <div class="card-kicker">↗ Exam Ready</div>
                <div class="card-title">Track your weak spots</div>
                <div class="card-body">See what needs revision before it becomes exam stress, then plan your next study move clearly.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_stat_cards(stats)
    st.markdown(f'<div class="section-title">{get_translation("quick_actions")}</div>', unsafe_allow_html=True)
    modules = [
        ("▦", get_translation("az_hub"), "Open a subject when you want notes, high-yield points, diseases, drugs, and skills in one place.", 64, "az_hub"),
        ("?", get_translation("question_bank"), "Do a short MCQ set, learn from the answer, and keep track of your score over time.", 48, "mcq_quiz"),
        ("M", get_translation("ai_mnemonics_studio"), "Make hard lists easier to remember with simple, funny, or exam-style mnemonics.", 38, "ai_mnemonics"),
        ("✚", get_translation("clinical_skills_lab"), "Practise OSCE stations with timing so your exam flow feels calm and organised.", 52, "osce_timer"),
    ]
    cols = st.columns(4)
    for col, module in zip(cols, modules):
        with col:
            render_module_card(*module, cta="Launch")

    left, mid, right = st.columns([1.1, 1, 1])
    with left:
        st.markdown(f'<div class="section-title">{get_translation("continue_studying")}</div>', unsafe_allow_html=True)
        st.info("Renal physiology: acid-base compensation and electrolyte emergencies.")
        st.markdown(f'<div class="section-title">{get_translation("topic_of_day")}</div>', unsafe_allow_html=True)
        st.success("Approach to acute chest pain: ACS, PE, aortic dissection, pneumothorax, esophageal rupture.")
    with mid:
        st.markdown(f'<div class="section-title">{get_translation("weak_areas")}</div>', unsafe_allow_html=True)
        for item in stats.get("weak_areas", ["Pharmacology", "Renal", "ECG"]):
            st.warning(item)
        st.markdown(f'<div class="section-title">OSCE Practice Reminder</div>', unsafe_allow_html=True)
        st.info("Run one focused 8-minute cardiovascular exam station today.")
    with right:
        st.markdown(f'<div class="section-title">{get_translation("strong_subjects")}</div>', unsafe_allow_html=True)
        for item in stats.get("strong_areas", ["Anatomy", "Pathology", "Clinical reasoning"]):
            st.success(item)
        st.markdown(f'<div class="section-title">{get_translation("recent_activity")}</div>', unsafe_allow_html=True)
        for activity in stats.get("activities", [])[:5]:
            st.caption(f"{activity.get('time', 'Recently')} - {activity.get('text', '')}")


def _slug(value):
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-")


def _user_id():
    return st.session_state.user["id"] if st.session_state.get("logged_in") and st.session_state.get("user") else None


def render_subject_page():
    st.markdown(f'<div class="section-title">{get_translation("az_hub")}</div>', unsafe_allow_html=True)
    st.markdown("".join(f'<span class="az-pill">{name}</span>' for name in SUBJECT_ORDER), unsafe_allow_html=True)
    subject = st.selectbox(get_translation("subject"), SUBJECT_ORDER, key="az_subject_select")
    data = AZ_MEDICAL_KNOWLEDGE[subject]
    st.markdown(f"### {subject}")
    tabs = st.tabs(["✎ Notes", "◆ High-Yield", "⚕ Clinical", "Rx Diseases & Drugs", "? Practice", "⌘ Resources"])
    with tabs[0]:
        for index, chapter in enumerate(data["chapters"], 1):
            with st.expander(f"Chapter {index}: {chapter}", expanded=index == 1):
                st.markdown("**Chapter-wise notes**")
                st.write(data["high_yield"][min(index - 1, len(data["high_yield"]) - 1)])
                st.markdown("**Quick revision notes**")
                for note in data["quick_revision_notes"]:
                    st.markdown(f"- {note}")
                uid = _user_id()
                cols = st.columns(2)
                with cols[0]:
                    if st.button(get_translation("bookmark"), key=f"bm_{subject}_{index}", use_container_width=True):
                        if uid:
                            save_bookmark(uid, "chapter", f"{_slug(subject)}-{index}", chapter, subject)
                            st.success("Saved to bookmarks.")
                        else:
                            st.warning("Login to persist bookmarks.")
                with cols[1]:
                    if st.button(get_translation("completed"), key=f"done_{subject}_{index}", use_container_width=True):
                        if uid:
                            save_completed_lesson(uid, subject, f"{_slug(subject)}-{index}", chapter)
                            st.success("Lesson marked complete.")
                        else:
                            st.warning("Login to save progress.")
    with tabs[1]:
        for item in data["high_yield"]:
            st.success(item)
        st.markdown("**High-yield summaries**")
        for item in data["high_yield_summaries"]:
            st.markdown(f"- {item}")
        st.markdown("**Important diagrams list**")
        st.write(", ".join(data["important_diagrams"]))
        st.markdown("**Tables**")
        st.write(", ".join(data["tables"]))
    with tabs[2]:
        for item in data["clinical_correlations"]:
            st.info(item)
        st.markdown("**OSCE/practical skills**")
        for skill in data["osce_practical_skills"]:
            st.markdown(f"- {skill}")
    with tabs[3]:
        st.markdown("**Common diseases**")
        st.write(", ".join(data["common_diseases"]))
        st.markdown("**Drug charts**")
        for drug in data["drug_charts"]:
            st.markdown(f"- {drug}")
    with tabs[4]:
        st.markdown("**Flashcards**")
        for card in data["flashcards"]:
            st.markdown(f"- {card}")
        st.markdown("**MCQ starter**")
        for mcq in data["mcqs"]:
            st.write(mcq["stem"])
            st.caption(f"Answer: {mcq['answer']}")
        st.markdown("**Important mnemonics**")
        for mnemonic in data["important_mnemonics"]:
            st.markdown(f"- {mnemonic}")
    with tabs[5]:
        for ref in data["references_resources"]:
            st.markdown(f"- {ref}")


def render_bookmarks():
    uid = _user_id()
    st.markdown('<div class="section-title">Saved Bookmarks</div>', unsafe_allow_html=True)
    if not uid:
        st.warning("Login to view saved bookmarks.")
        return
    bookmarks = get_bookmarks(uid)
    if not bookmarks:
        st.info("No bookmarks yet. Save chapters from the A-Z Medical Knowledge Hub.")
        return
    for item in bookmarks:
        cols = st.columns([4, 1])
        with cols[0]:
            st.markdown(f"**{item['title']}**")
            st.caption(f"{item['item_type']} · {item.get('subject', '')} · {item.get('created_at', '')[:10]}")
        with cols[1]:
            if st.button("Remove", key=f"remove_{item['item_type']}_{item['item_id']}"):
                remove_bookmark(uid, item["item_type"], item["item_id"])
                st.rerun()


def _make_mnemonic(topic, mode):
    words = [part for part in re.split(r"[\s,;:/()\-]+", topic.strip()) if part]
    letters = "".join(word[0].upper() for word in words[:8]) or "MEDIC"
    seed = int(hashlib.sha256(topic.encode("utf-8")).hexdigest(), 16)
    clinical_words = ["Monitor", "Examine", "Diagnose", "Interpret", "Correlate", "Stabilize", "Review", "Treat"]
    phrase = " ".join(clinical_words[(seed + i) % len(clinical_words)] for i, _ in enumerate(letters))
    return {
        "mnemonic_type": mode,
        "easy_mnemonic": f"{letters}: {phrase}",
        "funny_mnemonic": f"{letters}: My Exam Day Intern Carefully Saves Real Time",
        "exam_mnemonic": f"For {topic}, recall {letters}, then define mechanism, presentation, investigation, management, and complication.",
        "visual_story": f"Imagine a polished clinical dashboard where each letter of {letters} lights up as you move from anatomy to diagnosis to treatment.",
        "english_explanation": f"This mnemonic anchors {topic} to a clinical sequence: recognize the pattern, test the key discriminator, then choose safe management.",
        "arabic_explanation": f"تساعدك وسيلة الحفظ هذه على ربط موضوع {topic} بالتسلسل السريري: التعرف على النمط، اختيار الفحص المناسب، ثم العلاج الآمن.",
        "recall_quiz": [
            f"What does the first letter in {letters} remind you to check?",
            f"Name one dangerous complication related to {topic}.",
            f"How would you explain {topic} to a patient in one sentence?",
        ],
    }


def render_ai_mnemonics():
    st.markdown(f'<div class="section-title">{get_translation("ai_mnemonics_studio")}</div>', unsafe_allow_html=True)
    uid = _user_id()
    with st.form("ai_mnemonic_form"):
        topic = st.text_input(get_translation("mnemonic_topic_label"))
        mode = st.selectbox(get_translation("style"), ["exam", "easy", "funny", "visual", "arabic_english"])
        submitted = st.form_submit_button(get_translation("generate_mnemonic"), type="primary", use_container_width=True)
    if submitted:
        if not topic.strip():
            st.error("Enter a topic first.")
        else:
            result = _make_mnemonic(topic, mode)
            st.session_state.last_mnemonic = {"topic": topic, **result}
            if uid:
                save_ai_mnemonic(uid, topic, result)
            st.success("Mnemonic generated and saved." if uid else "Mnemonic generated. Login to save history.")
    result = st.session_state.get("last_mnemonic")
    if result:
        st.markdown(f"### {get_translation('generated_memory_system')}")
        st.info(result["easy_mnemonic"])
        st.warning(result["funny_mnemonic"])
        st.success(result["exam_mnemonic"])
        st.write(result["visual_story"])
        st.markdown(f"**{get_translation('english_explanation')}**")
        st.write(result["english_explanation"])
        st.markdown(f"**{get_translation('arabic_explanation')}**")
        st.write(result["arabic_explanation"])
        st.markdown(f"**{get_translation('recall_quiz')}**")
        for q in result["recall_quiz"]:
            st.markdown(f"- {q}")
    if uid:
        st.markdown("### Mnemonic History")
        for item in get_ai_mnemonic_history(uid):
            with st.expander(f"{item['topic']} · {item['created_at'][:10]}"):
                st.write(item["easy_mnemonic"])
                st.caption(item["exam_mnemonic"])


def render_profile_dashboard():
    uid = _user_id()
    if not uid:
        st.warning("Login to see your private profile dashboard.")
        return
    profile = get_profile_overview(uid)
    st.markdown(f'<div class="section-title">{get_translation("user_profile")}</div>', unsafe_allow_html=True)
    render_stat_cards(profile)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("### Subject-wise Progress")
        scores = profile.get("subject_scores") or {"Anatomy": 76, "Pathology": 69, "Pharmacology": 58}
        for subject, score in scores.items():
            st.progress(min(100, int(score)), text=f"{subject}: {score}%")
    with col2:
        st.markdown("### Saved Bookmarks")
        for item in profile.get("bookmarks", [])[:6]:
            st.markdown(f"- {item['title']}")
        st.markdown("### Recommended Lessons")
        for item in profile.get("recommended_lessons", []):
            st.markdown(f"- {item}")
    with col3:
        st.markdown("### Recent Activity")
        for item in profile.get("activities", [])[:8]:
            st.caption(f"{item.get('time', 'Recently')} - {item.get('text', '')}")
        st.markdown("### Weak / Strong Areas")
        st.warning(", ".join(profile.get("weak_areas", [])))
        st.success(", ".join(profile.get("strong_areas", [])))


def render_settings(themes):
    st.markdown(f'<div class="section-title">{get_translation("settings")}</div>', unsafe_allow_html=True)
    uid = _user_id()
    if not uid:
        st.info("Login to persist settings to your profile.")
    daily_goal = st.slider("Daily study goal", 15, 240, int(st.session_state.get("daily_goal_minutes", 60)), step=15)
    exam_track = st.selectbox("Default exam track", ["SQU-COM", "OMSB", "USMLE", "PLAB"])
    if st.button(get_translation("save"), type="primary"):
        st.session_state.daily_goal_minutes = daily_goal
        if uid:
            update_user_setting(uid, "daily_goal_minutes", daily_goal)
            update_user_setting(uid, "exam_track", exam_track)
        st.success("Settings saved.")
    st.caption(get_translation("educational_only"))


def render_quiz_system():
    st.info("Open the full Question Bank from the navigation. Your saved quiz attempts are persisted per user.")


def render_ai_mnemonics():
    """AI-backed mnemonic craftsman with a deterministic history fallback."""
    from ai_service import DEFAULT_ERROR, generate_mnemonic, get_ai_status

    st.markdown(f'<div class="section-title">{get_translation("ai_mnemonics_studio")}</div>', unsafe_allow_html=True)
    uid = _user_id()
    status = get_ai_status()
    if not status["ready"]:
        st.warning("Add GEMINI_API_KEY or OPENAI_API_KEY to Streamlit secrets to generate live mnemonics.")

    facts = st.text_area(
        "Complex medical facts or symptoms",
        placeholder="Paste a list, diagnostic criteria, symptoms, drug adverse effects, or pathway steps...",
        height=180,
        key="ai_mnemonic_facts",
    )
    style = st.selectbox(
        "Mnemonic Style",
        ["Professional Academic", "Creative/Story", "Humorous"],
        key="ai_mnemonic_style",
    )
    if st.button("Generate Mnemonic", type="primary", use_container_width=True, key="ai_mnemonic_generate"):
        if not facts.strip():
            st.error("Enter the facts you want to remember first.")
        else:
            with st.spinner("Designing a mapped acronym..."):
                result = generate_mnemonic(facts.strip(), style)
            st.session_state.last_mnemonic = {
                "topic": facts.strip()[:80],
                "style": style,
                "response": result,
            }
            if uid and result != DEFAULT_ERROR:
                save_ai_mnemonic(
                    uid,
                    facts.strip()[:120],
                    {
                        "mnemonic_type": style,
                        "easy_mnemonic": result[:500],
                        "funny_mnemonic": "",
                        "exam_mnemonic": "AI-generated mapped acronym mnemonic.",
                        "visual_story": result,
                        "english_explanation": result,
                        "arabic_explanation": "",
                        "recall_quiz": [],
                    },
                )
            st.rerun()

    result = st.session_state.get("last_mnemonic")
    if result:
        st.markdown("### Generated Memory System")
        if result.get("response") == DEFAULT_ERROR:
            st.error(result["response"])
        else:
            safe_response = html.escape(result.get("response", "")).replace(chr(10), "<br>")
            st.markdown(
                f"""
                <div class="glass-card" style="border-left:4px solid #eab308;">
                    {safe_response}
                </div>
                """,
                unsafe_allow_html=True,
            )

    if uid:
        st.markdown("### Mnemonic History")
        for item in get_ai_mnemonic_history(uid):
            with st.expander(f"{item['topic']} · {item['created_at'][:10]}"):
                st.write(item["easy_mnemonic"])
                st.caption(item["exam_mnemonic"])
