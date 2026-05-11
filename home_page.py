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
    .home-hero {{
        background:
            linear-gradient(135deg, {t["primary"]}16, transparent 42%),
            linear-gradient(160deg, {t["surface"]}, {t["surface_raised"]});
        border: 1px solid {t["card_border"]};
        border-radius: 8px;
        padding: 2rem;
        margin-bottom: 1rem;
        box-shadow: {t["shadow_md"]};
        position: relative;
        overflow: hidden;
    }}
    .home-hero::after {{
        content: "";
        position: absolute;
        inset: auto -80px -90px auto;
        width: 280px;
        height: 180px;
        border: 1px solid {t["primary"]}35;
        transform: rotate(-12deg);
        border-radius: 8px;
    }}
    .home-eyebrow {{
        display: inline-flex;
        align-items: center;
        gap: 8px;
        padding: 5px 10px;
        border: 1px solid {t["primary"]}40;
        border-radius: 8px;
        background: {t["primary_glow"]};
        color: {t["primary"]} !important;
        font-size: 0.68rem;
        font-weight: 800;
        text-transform: uppercase;
        letter-spacing: 0;
        margin-bottom: 0.85rem;
    }}
    .home-title {{
        font-family: Syne, sans-serif;
        font-size: clamp(2rem, 4vw, 3.15rem);
        line-height: 1.04;
        font-weight: 900;
        color: {t["text"]};
        letter-spacing: 0;
        max-width: 720px;
        margin-bottom: 0.8rem;
    }}
    .home-subtitle {{
        max-width: 680px;
        color: {t["text_muted"]};
        font-size: 1rem;
        line-height: 1.7;
        margin-bottom: 1.25rem;
    }}
    .home-tags {{
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
    }}
    .home-tag {{
        border: 1px solid {t["card_border"]};
        background: {t["glass_bg"]};
        border-radius: 8px;
        padding: 6px 10px;
        color: {t["text_muted"]};
        font-size: 0.74rem;
        font-weight: 700;
    }}
    .home-section-title {{
        font-family: Syne, sans-serif;
        font-size: 1rem;
        font-weight: 900;
        color: {t["text"]};
        margin: 1rem 0 0.55rem;
        display: flex;
        align-items: center;
        gap: 10px;
        letter-spacing: 0;
    }}
    .home-section-title::after {{
        content: "";
        flex: 1;
        height: 1px;
        background: {t["card_border"]};
    }}
    .home-stat-card {{
        background: {t["card_bg"]};
        border: 1px solid {t["card_border"]};
        border-radius: 8px;
        padding: 0.85rem 0.7rem;
        text-align: left;
        min-height: 96px;
        box-shadow: {t["shadow_sm"]};
    }}
    .home-stat-icon {{
        width: 32px;
        height: 32px;
        border-radius: 8px;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-bottom: 0.45rem;
    }}
    .home-stat-number {{
        font-family: Syne, sans-serif;
        font-size: 1.45rem;
        line-height: 1;
        font-weight: 900;
        letter-spacing: 0;
    }}
    .home-stat-label {{
        margin-top: 0.25rem;
        font-size: 0.72rem;
        color: {t["subtext"]};
        font-weight: 700;
    }}
    div[data-testid="stHorizontalBlock"] .stButton > button {{
        background:    {t["card_bg"]} !important;
        border:        1.5px solid {t["card_border"]} !important;
        border-radius: 8px !important;
        padding:       0.65rem 0.45rem !important;
        font-weight:   700 !important;
        font-size:     0.82rem !important;
        color:         {t["text"]} !important;
        text-align:    center !important;
        white-space:   pre-wrap !important;
        min-height:    54px !important;
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
    @media (max-width: 768px) {{
        .home-hero {{ padding: 1.35rem; }}
        .home-title {{ font-size: 2rem; }}
        .home-subtitle {{ font-size: 0.9rem; }}
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
    tags_html = "".join(
        f'<span class="home-tag">{tag}</span>'
        for tag in ["🇴🇲 SQU-COM","🏛 OMSB","🌍 WFME","📋 USMLE","🩺 PLAB"]
    )

    st.markdown(
        f'<section class="home-hero">'
        f'<div style="position:relative;z-index:1;">'
        f'<div class="home-eyebrow">{ico} {greet}, Dr. {first}<span style="opacity:0.45;">·</span>{date}</div>'
        f'<div class="home-title">Your command center for medical school in Oman.</div>'
        f'<div class="home-subtitle">Practice questions, flashcards, timers, AI tutoring, OSCE prep, analytics, and local Oman medical resources in one focused workspace.</div>'
        f'<div class="home-tags">{tags_html}</div>'
        f'</div></section>',
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
                f'<div class="home-stat-card">'
                f'<div class="home-stat-icon" style="background:{clr}18;color:{clr};">{ico}</div>'
                f'<div class="home-stat-number" style="color:{clr};">{num}</div>'
                f'<div class="home-stat-label">{lbl}</div>'
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
        f'<div class="home-section-title">All Modules <span style="font-size:0.68rem;font-family:DM Sans,sans-serif;font-weight:700;color:{t["subtext"]};">{len(ALL_MODULES)} tools</span></div>',
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
        f'<div class="home-section-title">Quick Subject Access</div>',
        unsafe_allow_html=True,
    )
    cols = st.columns(len(FEATURED_SUBJECTS))
    for col, (ico, name) in zip(cols, FEATURED_SUBJECTS):
        with col:
            if st.button(f"{ico} {name}", key=f"subj_{name}", use_container_width=True):
                st.session_state.page = "subjects"
                st.session_state.selected_subject = name
                st.rerun()
