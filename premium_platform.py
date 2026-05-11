"""
premium_platform.py - luxury MedStudy Oman Streamlit components.
"""

from __future__ import annotations

import hashlib
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
        .medical-float:nth-child(1) {{ top: 12%; left: 5%; font-size: 2rem; animation-delay: 0s; }}
        .medical-float:nth-child(2) {{ top: 20%; right: 9%; font-size: 2.4rem; animation-delay: -3s; }}
        .medical-float:nth-child(3) {{ top: 55%; left: 8%; font-size: 1.7rem; animation-delay: -6s; }}
        .medical-float:nth-child(4) {{ top: 64%; right: 12%; font-size: 2rem; animation-delay: -2s; }}
        .medical-float:nth-child(5) {{ top: 38%; left: 46%; font-size: 1.55rem; animation-delay: -8s; }}
        .medical-float:nth-child(6) {{ bottom: 8%; left: 28%; font-size: 1.8rem; animation-delay: -5s; }}
        @keyframes medFloat {{
            0%, 100% {{ transform: translate3d(0,0,0) rotate(0deg); }}
            35% {{ transform: translate3d(14px,-18px,0) rotate(5deg); }}
            70% {{ transform: translate3d(-12px,10px,0) rotate(-4deg); }}
        }}
        .stApp > *:not(.medical-animation-layer) {{
            position: relative;
            z-index: 1;
        }}
        .med-topbar {{
            position: sticky;
            top: 0;
            z-index: 50;
            display: grid;
            grid-template-columns: minmax(230px, 1.15fr) minmax(260px, 1.6fr) auto auto auto auto;
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
            width:46px;
            height:46px;
            display:grid;
            place-items:center;
            border-radius:18px;
            background: linear-gradient(135deg, var(--cyan), var(--emerald));
            color:{theme["text_inverse"]} !important;
            font-weight:900;
            box-shadow: 0 14px 36px rgba(56,213,255,0.22);
        }}
        .brand-title {{
            color: var(--ink) !important;
            font-weight: 900;
            font-size: 1.02rem;
            line-height: 1.05;
        }}
        .brand-sub {{
            color: var(--muted) !important;
            font-size: .72rem;
            letter-spacing: .08em;
            text-transform: uppercase;
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
        }}
        @media (max-width: 680px) {{
            .lux-grid {{ grid-template-columns: 1fr; }}
            .hero-panel {{ border-radius:22px; }}
            .module-card, .lux-card {{ border-radius:20px; }}
            .student-workspace {{ grid-template-columns: auto 1fr; }}
            .student-badge {{ display:none; }}
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )
    st.markdown(
        """
        <div class="medical-animation-layer">
            <span class="medical-float">✚</span>
            <span class="medical-float">⚕</span>
            <span class="medical-float">ECG</span>
            <span class="medical-float">DNA</span>
            <span class="medical-float">Rx</span>
            <span class="medical-float">OSCE</span>
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
    controls = st.columns([1.4, 1.1, 1.1, 1])
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
        render_language_selector()
    with controls[2]:
        if st.session_state.get("logged_in"):
            if st.button(get_translation("profile"), use_container_width=True, key="profile_top"):
                st.session_state.page = "profile"
                st.rerun()
        else:
            if st.button(get_translation("login"), type="primary", use_container_width=True, key="login_top"):
                st.session_state.page = "auth"
                st.session_state.auth_mode = "login"
                st.rerun()
    with controls[3]:
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
    if selected_page != current_page:
        st.session_state.page = selected_page
        st.query_params["page"] = selected_page
        st.rerun()


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


def render_dashboard(stats):
    render_hero()
    st.markdown(
        """
        <div class="lux-grid">
            <div class="lux-card">
                <div class="card-kicker">✚ Start Here</div>
                <div class="card-title">Pick one clinical goal</div>
                <div class="card-body">Choose a topic, practice questions, review flashcards, or rehearse an OSCE station.</div>
            </div>
            <div class="lux-card">
                <div class="card-kicker">◇ Study Flow</div>
                <div class="card-title">Learn → Recall → Test</div>
                <div class="card-body">Read high-yield notes, generate a mnemonic, then finish with MCQs for feedback.</div>
            </div>
            <div class="lux-card">
                <div class="card-kicker">⚕ Clinical Mode</div>
                <div class="card-title">Think like a doctor</div>
                <div class="card-body">Every subject links facts to symptoms, investigations, management, and OSCE skills.</div>
            </div>
            <div class="lux-card">
                <div class="card-kicker">↗ Exam Ready</div>
                <div class="card-title">Track your weak spots</div>
                <div class="card-body">Use analytics, bookmarks, and progress history to decide what to study next.</div>
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )
    render_stat_cards(stats)
    st.markdown(f'<div class="section-title">{get_translation("quick_actions")}</div>', unsafe_allow_html=True)
    modules = [
        ("▦", get_translation("az_hub"), "Chapter notes, clinical correlations, exam tables, OSCE links.", 64, "az_hub"),
        ("?", get_translation("question_bank"), "Practice exam-style MCQs and preserve attempt history.", 48, "mcq_quiz"),
        ("M", get_translation("ai_mnemonics_studio"), "Generate English and Arabic memory systems with recall quizzes.", 38, "ai_mnemonics"),
        ("✚", get_translation("clinical_skills_lab"), "Time OSCE stations and rehearse structured clinical skills.", 52, "osce_timer"),
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
