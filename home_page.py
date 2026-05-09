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
    op    = "0.07" if t["family"] != "dark" else "0.11"

    steth = f'<svg width="90" height="90" viewBox="0 0 24 24" fill="none" stroke="{p}" stroke-width="1.1" opacity="{op}"><path d="M4.8 2.3A.3.3 0 104.5 2v5a3 3 0 006 0v-5"/><path d="M7.5 7A6 6 0 0013.5 13v4.5a3.5 3.5 0 007 0V14"/><circle cx="20.5" cy="12" r="1.5"/></svg>'
    cap   = f'<svg width="80" height="80" viewBox="0 0 24 24" fill="none" stroke="{p}" stroke-width="1.1" opacity="{op}"><path d="M22 10v6M2 10l10-5 10 5-10 5z"/><path d="M6 12v5c3 3 9 3 12 0v-5"/></svg>'
    ecg   = f'<svg width="130" height="48" viewBox="0 0 130 48" fill="none" stroke="{p}" stroke-width="1.4" opacity="{op}"><polyline points="0,24 22,24 30,6 40,42 48,14 57,24 80,24 88,5 97,43 106,20 115,24 130,24" stroke-linecap="round"/></svg>'
    cross = f'<svg width="44" height="44" viewBox="0 0 24 24" fill="{p}" opacity="{op}"><path d="M9 2h6v6h6v6h-6v8H9v-8H3V8h6z"/></svg>'

    tags_html = "".join(
        f'<span style="background:{t["glass_bg"]};border:1px solid {t["glass_border"]};'
        f'border-radius:999px;padding:4px 12px;font-size:0.73rem;font-weight:600;'
        f'color:{t["subtext"]};">{tag}</span>'
        for tag in ["🇴🇲 SQU-COM","🏛 OMSB","🌍 WFME","📋 USMLE","🩺 PLAB"]
    )

    st.markdown(
        f'<div style="background:{t["hero_gradient"]};border:1px solid {t["card_border"]};'
        f'border-radius:24px;padding:2.6rem 3rem 2.2rem;margin-bottom:1rem;'
        f'position:relative;overflow:hidden;">'
        f'<div style="position:absolute;top:-10px;right:30px;pointer-events:none;">{steth}</div>'
        f'<div style="position:absolute;top:15px;right:130px;pointer-events:none;">{cap}</div>'
        f'<div style="position:absolute;bottom:20px;right:50px;pointer-events:none;">{ecg}</div>'
        f'<div style="position:absolute;top:20px;right:240px;pointer-events:none;">{cross}</div>'
        f'<div style="position:absolute;top:-40px;right:-40px;width:160px;height:160px;'
        f'border-radius:50%;background:radial-gradient(circle,{t["primary"]}18,transparent 70%);'
        f'pointer-events:none;"></div>'
        f'<div style="position:relative;z-index:1;">'
        f'<div style="display:inline-flex;align-items:center;gap:7px;padding:4px 14px;'
        f'background:{t["primary_glow"]};border:1px solid {t["primary"]}40;'
        f'border-radius:999px;font-size:0.7rem;font-weight:700;color:{t["primary"]};'
        f'letter-spacing:0.10em;text-transform:uppercase;margin-bottom:1rem;">'
        f'{ico} {greet}, Dr. {first}<span style="opacity:0.4;margin:0 3px;">·</span>{date}</div>'
        f'<div style="font-family:Syne,sans-serif;font-size:clamp(1.9rem,3.5vw,2.8rem);'
        f'font-weight:900;color:{t["text"]};letter-spacing:-0.04em;line-height:1.1;margin-bottom:0.8rem;">'
        f'Study Medicine the <span style="color:{t["primary"]};">Smart Way 🎓</span></div>'
        f'<div style="font-size:0.92rem;color:{t["text_muted"]};max-width:480px;'
        f'line-height:1.7;margin-bottom:1.5rem;">'
        f'AI-powered clinical education for Omani medical students — OMSB · USMLE · PLAB · SQU-COM aligned.</div>'
        f'<div style="display:flex;gap:6px;flex-wrap:wrap;">{tags_html}</div>'
        f'</div></div>',
        unsafe_allow_html=True,
    )


def _stats(t: dict):
    items = [
        ("📚","37",   "Medical Subjects", t["primary"]),
        ("📝","500+", "Practice MCQs",    "#10b981"),
        ("🤖","8",    "AI Tools",         "#8b5cf6"),
        ("🃏","200+", "Flashcards",       "#f59e0b"),
        ("🩺","12+",  "OSCE Stations",    "#ef4444"),
    ]
    cols = st.columns(5)
    for col, (ico, num, lbl, clr) in zip(cols, items):
        with col:
            st.markdown(
                f'<div style="background:{t["card_bg"]};border:1px solid {t["card_border"]};'
                f'border-top:3px solid {clr};border-radius:14px;'
                f'padding:0.8rem 0.5rem;text-align:center;margin-bottom:0.5rem;'
                f'backdrop-filter:blur(10px);">'
                f'<div style="font-size:1.1rem;margin-bottom:2px;">{ico}</div>'
                f'<div style="font-family:Syne,sans-serif;font-size:1.4rem;'
                f'font-weight:900;color:{clr};line-height:1;">{num}</div>'
                f'<div style="font-size:0.65rem;color:{t["subtext"]};'
                f'font-weight:600;margin-top:2px;">{lbl}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )


def _cta_buttons():
    c1, c2, c3, _ = st.columns([2, 2, 2, 1])
    with c1:
        if st.button("📚  Browse Subjects", type="primary",
                     use_container_width=True, key="cta_subj"):
            st.session_state.page = "subjects"; st.rerun()
    with c2:
        if st.button("🤖  Ask AI Tutor",
                     use_container_width=True, key="cta_ai"):
            st.session_state.page = "ai_tutor"; st.rerun()
    with c3:
        if st.button("📝  Take a Quiz",
                     use_container_width=True, key="cta_quiz"):
            st.session_state.page = "mcq_quiz"; st.rerun()
    st.markdown("<div style='height:0.3rem'></div>", unsafe_allow_html=True)


def _module_grid(t: dict):
    st.markdown(
        f'<div style="font-family:Syne,sans-serif;font-size:1rem;font-weight:900;'
        f'color:{t["text"]};margin:0.9rem 0 0.5rem;display:flex;align-items:center;gap:10px;">'
        f'🧩 All Modules'
        f'<div style="flex:1;height:1.5px;background:{t["card_border"]};border-radius:999px;"></div>'
        f'<span style="font-size:0.66rem;font-weight:500;color:{t["subtext"]};">{len(ALL_MODULES)} modules</span>'
        f'</div>',
        unsafe_allow_html=True,
    )
    rows = [ALL_MODULES[i:i+6] for i in range(0, len(ALL_MODULES), 6)]
    for row_idx, row in enumerate(rows):
        cols = st.columns(6)
        for col, (icon, page_id, name, desc, color) in zip(cols, row):
            with col:
                st.markdown(
                    f'<div style="height:3px;background:{color};'
                    f'border-radius:4px 4px 0 0;margin-bottom:-3px;'
                    f'position:relative;z-index:1;"></div>',
                    unsafe_allow_html=True,
                )
                if st.button(
                    f"{icon}\n{name}",
                    key=f"mod_{page_id}_{row_idx}",
                    use_container_width=True,
                ):
                    st.session_state.page = page_id; st.rerun()
        if row_idx < len(rows) - 1:
            st.markdown("<div style='height:3px'></div>", unsafe_allow_html=True)
    st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)


def _subject_strip(t: dict):
    st.markdown(
        f'<div style="font-family:Syne,sans-serif;font-size:1rem;font-weight:900;'
        f'color:{t["text"]};margin-bottom:0.5rem;display:flex;align-items:center;gap:10px;">'
        f'⚡ Quick Subject Access'
        f'<div style="flex:1;height:1.5px;background:{t["card_border"]};border-radius:999px;"></div>'
        f'</div>',
        unsafe_allow_html=True,
    )
    cols = st.columns(len(FEATURED_SUBJECTS))
    for col, (ico, name) in zip(cols, FEATURED_SUBJECTS):
        with col:
            if st.button(f"{ico} {name}", key=f"subj_{name}", use_container_width=True):
                st.session_state.page = "subjects"
                st.session_state.selected_subject = name
                st.rerun()
