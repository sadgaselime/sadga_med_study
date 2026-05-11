import streamlit as st
import datetime

ALL_MODULES = [
    ("📚", "subjects", "Subjects", "37 subjects A-Z", "#e63946"),
    ("🃏", "flashcards", "Flashcards", "200+ SM-2 cards", "#f59e0b"),
    ("📝", "mcq_quiz", "MCQ Quiz", "500+ practice Qs", "#10b981"),
    ("💡", "mnemonics", "Mnemonics", "150+ memory anchors", "#8b5cf6"),
    ("🤖", "ai_tutor", "AI Tutor", "AI powered help", "#06b6d4"),
    ("🎤", "voice_ai", "Voice AI", "Hands-free study", "#ec4899"),
    ("⏱️", "pomodoro", "Timer", "Focus sessions", "#ef4444"),
    ("🩺", "osce_timer", "OSCE Timer", "Station practice", "#dc2626"),
    ("⚗️", "lab_game", "Lab Game", "Speed challenge", "#84cc16"),
    ("🫁", "anatomy_3d", "3D Anatomy", "Interactive atlas", "#0891b2"),
    ("📖", "resources", "Resources", "Books and videos", "#7c3aed"),
    ("📊", "dashboard", "Dashboard", "Analytics", "#16a34a"),
    ("👥", "study_groups", "Study Groups", "Collaborate", "#f97316"),
    ("💬", "discussion", "Forums", "Case discussions", "#0d9488"),
    ("📋", "shared_notes", "Shared Notes", "Revision notes", "#6366f1"),
    ("🏆", "leaderboards", "Leaderboard", "Rankings", "#d97706"),
    ("💡", "tips", "Study Tips", "High-yield strategy", "#4f46e5"),
    ("🏅", "about", "About", "Developer info", "#9ca3af"),
]

FEATURED_SUBJECTS = [
    ("❤️", "Cardiology"),
    ("🧠", "Neurology"),
    ("🫁", "Pulmonology"),
    ("💊", "Pharmacology"),
    ("🔬", "Pathology"),
    ("🧬", "Biochemistry"),
    ("🦴", "Anatomy"),
    ("⚕️", "Int. Medicine"),
    ("🔪", "Surgery"),
    ("👶", "Paediatrics"),
    ("🤰", "Obs & Gynae"),
    ("🦠", "Inf. Disease"),
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
        display: grid;
        grid-template-columns: minmax(0, 1.05fr) minmax(320px, 0.95fr);
        align-items: center;
        gap: 1.5rem;
        background:
            radial-gradient(circle at 82% 18%, {t["primary"]}28, transparent 30%),
            radial-gradient(circle at 12% 88%, #10b98120, transparent 28%),
            linear-gradient(135deg, {t["primary"]}14, transparent 45%),
            linear-gradient(160deg, {t["surface"]}, {t["surface_raised"]});
        border: 1px solid {t["card_border"]};
        border-radius: 8px;
        padding: clamp(1.15rem, 3vw, 2.4rem);
        margin-bottom: 1rem;
        box-shadow: {t["shadow_md"]};
        position: relative;
        overflow: hidden;
        min-height: 430px;
        isolation: isolate;
    }}
    .home-hero::before {{
        content: "";
        position: absolute;
        inset: 0;
        background-image:
            linear-gradient({t["card_border"]}55 1px, transparent 1px),
            linear-gradient(90deg, {t["card_border"]}55 1px, transparent 1px);
        background-size: 48px 48px;
        opacity: 0.4;
        z-index: -2;
    }}
    .home-hero::after {{
        content: "";
        position: absolute;
        width: 420px;
        height: 420px;
        right: -150px;
        top: -145px;
        border: 1px solid {t["primary"]}30;
        border-radius: 50%;
        box-shadow: inset 0 0 80px {t["primary"]}16;
        animation: med-spin 28s linear infinite;
        z-index: -1;
    }}
    .home-hero-copy {{
        position: relative;
        z-index: 2;
    }}
    .home-eyebrow {{
        display: inline-flex;
        align-items: center;
        flex-wrap: wrap;
        gap: 8px;
        padding: 5px 10px;
        border: 1px solid {t["primary"]}40;
        border-radius: 8px;
        background: {t["primary_glow"]};
        color: {t["primary"]} !important;
        font-size: 0.68rem;
        font-weight: 800;
        text-transform: uppercase;
        margin-bottom: 0.85rem;
    }}
    .home-eyebrow-sep {{
        opacity: 0.45;
    }}
    .home-title {{
        font-family: Syne, sans-serif;
        font-size: clamp(2.15rem, 4.7vw, 4.35rem);
        line-height: 1.04;
        font-weight: 900;
        color: {t["text"]};
        max-width: 760px;
        margin-bottom: 0.8rem;
    }}
    .home-title span {{
        color: {t["primary"]} !important;
    }}
    .home-subtitle {{
        max-width: 680px;
        color: {t["text_muted"]};
        font-size: 1.02rem;
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
    .home-hero-metrics {{
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 0.55rem;
        max-width: 620px;
        margin-top: 1.15rem;
    }}
    .home-hero-metric {{
        background: {t["glass_bg"]};
        border: 1px solid {t["card_border"]};
        border-radius: 8px;
        padding: 0.7rem;
        min-height: 74px;
        backdrop-filter: blur(12px);
    }}
    .home-hero-metric b {{
        display: block;
        font-family: Syne, sans-serif;
        font-size: 1.18rem;
        color: {t["text"]} !important;
    }}
    .home-hero-metric small {{
        display: block;
        margin-top: 0.35rem;
        font-size: 0.68rem;
        color: {t["subtext"]} !important;
        font-weight: 800;
    }}
    .medical-stage {{
        position: relative;
        min-height: 360px;
        border-radius: 8px;
        border: 1px solid {t["card_border"]};
        background:
            radial-gradient(circle at 50% 38%, {t["primary"]}20, transparent 36%),
            linear-gradient(145deg, {t["glass_bg"]}, transparent);
        box-shadow: inset 0 0 48px {t["primary"]}10, {t["shadow_sm"]};
        overflow: hidden;
    }}
    .medical-orbit {{
        position: absolute;
        inset: 34px;
        border: 1px dashed {t["primary"]}42;
        border-radius: 50%;
        animation: med-spin 20s linear infinite;
    }}
    .medical-orbit::before,
    .medical-orbit::after {{
        content: "";
        position: absolute;
        width: 18px;
        height: 18px;
        border-radius: 50%;
        background: {t["primary"]};
        box-shadow: 0 0 22px {t["primary"]};
    }}
    .medical-orbit::before {{
        left: 17%;
        top: 5%;
    }}
    .medical-orbit::after {{
        right: 8%;
        bottom: 20%;
        background: #10b981;
        box-shadow: 0 0 22px #10b981;
    }}
    .vitals-card {{
        position: absolute;
        left: 9%;
        right: 9%;
        top: 50%;
        transform: translateY(-50%);
        border: 1px solid {t["card_border"]};
        border-radius: 8px;
        background: {t["surface"]};
        box-shadow: {t["shadow_lg"]};
        overflow: hidden;
    }}
    .vitals-top {{
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.72rem 0.9rem;
        border-bottom: 1px solid {t["card_border"]};
        font-size: 0.68rem;
        font-weight: 900;
        color: {t["subtext"]} !important;
        text-transform: uppercase;
    }}
    .status-dot {{
        width: 9px;
        height: 9px;
        border-radius: 50%;
        background: #10b981;
        box-shadow: 0 0 14px #10b981;
        animation: blink 1.5s ease-in-out infinite;
    }}
    .vitals-screen {{
        position: relative;
        height: 158px;
        background:
            linear-gradient({t["card_border"]}35 1px, transparent 1px),
            linear-gradient(90deg, {t["card_border"]}35 1px, transparent 1px),
            linear-gradient(180deg, rgba(0,0,0,0.12), transparent);
        background-size: 28px 28px, 28px 28px, 100% 100%;
        overflow: hidden;
    }}
    .ecg-svg {{
        position: absolute;
        left: 0;
        top: 0;
        width: 200%;
        height: 100%;
        animation: ecg-pan 3.2s linear infinite;
    }}
    .ecg-svg polyline {{
        fill: none;
        stroke: #10b981;
        stroke-width: 5;
        stroke-linecap: round;
        stroke-linejoin: round;
        filter: drop-shadow(0 0 7px #10b981);
    }}
    .scan-light {{
        position: absolute;
        inset: 0;
        background: linear-gradient(90deg, transparent, {t["primary"]}18, transparent);
        transform: translateX(-100%);
        animation: scan 4.8s ease-in-out infinite;
    }}
    .vitals-grid {{
        display: grid;
        grid-template-columns: repeat(3, 1fr);
        gap: 1px;
        background: {t["card_border"]};
    }}
    .vital-stat {{
        background: {t["surface"]};
        padding: 0.7rem;
    }}
    .vital-stat span {{
        display: block;
        font-size: 0.62rem;
        color: {t["subtext"]} !important;
        font-weight: 900;
        text-transform: uppercase;
    }}
    .vital-stat strong {{
        display: block;
        margin-top: 0.2rem;
        font-family: Syne, sans-serif;
        font-size: 1.1rem;
        color: {t["text"]} !important;
    }}
    .float-chip {{
        position: absolute;
        display: grid;
        place-items: center;
        width: 46px;
        height: 46px;
        border-radius: 8px;
        background: {t["card_bg"]};
        border: 1px solid {t["card_border"]};
        box-shadow: {t["shadow_sm"]};
        font-size: 1.35rem;
        animation: clinical-float 4.5s ease-in-out infinite;
    }}
    .chip-heart {{
        left: 10%;
        top: 13%;
    }}
    .chip-lung {{
        right: 12%;
        bottom: 10%;
        animation-delay: -2s;
    }}
    .chip-pill {{
        left: 16%;
        bottom: 14%;
        animation-delay: -1.4s;
    }}
    .chip-cross {{
        right: 28%;
        top: 7%;
        animation-delay: -2.8s;
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
        min-height: 96px;
        box-shadow: {t["shadow_sm"]};
        transition: all 0.2s ease;
    }}
    .home-stat-card:hover {{
        transform: translateY(-4px);
        border-color: {t["primary"]}70;
        box-shadow: {t["shadow_md"]};
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
        font-weight: 900;
    }}
    .home-stat-label {{
        margin-top: 0.25rem;
        font-size: 0.72rem;
        color: {t["subtext"]};
        font-weight: 700;
    }}
    div[data-testid="stHorizontalBlock"] .stButton > button {{
        background: {t["card_bg"]} !important;
        border: 1.5px solid {t["card_border"]} !important;
        border-radius: 8px !important;
        padding: 0.65rem 0.45rem !important;
        font-weight: 700 !important;
        font-size: 0.82rem !important;
        color: {t["text"]} !important;
        text-align: center !important;
        white-space: pre-wrap !important;
        min-height: 54px !important;
        line-height: 1.4 !important;
        transition: all 0.2s ease !important;
    }}
    div[data-testid="stHorizontalBlock"] .stButton > button:hover {{
        background: {t["primary"]}12 !important;
        border-color: {t["primary"]}70 !important;
        color: {t["primary"]} !important;
        transform: translateY(-3px) !important;
        box-shadow: 0 6px 20px {t["primary"]}18 !important;
    }}
    @keyframes med-spin {{
        from {{ transform: rotate(0deg); }}
        to {{ transform: rotate(360deg); }}
    }}
    @keyframes ecg-pan {{
        from {{ transform: translateX(-50%); }}
        to {{ transform: translateX(0); }}
    }}
    @keyframes scan {{
        0%, 18% {{ transform: translateX(-110%); opacity: 0; }}
        24%, 74% {{ opacity: 1; }}
        100% {{ transform: translateX(110%); opacity: 0; }}
    }}
    @keyframes blink {{
        0%, 100% {{ opacity: 0.45; transform: scale(0.85); }}
        50% {{ opacity: 1; transform: scale(1.1); }}
    }}
    @keyframes clinical-float {{
        0%, 100% {{ transform: translateY(0) rotate(0deg); }}
        50% {{ transform: translateY(-14px) rotate(3deg); }}
    }}
    @media (max-width: 768px) {{
        .home-hero {{
            grid-template-columns: 1fr;
            min-height: 0;
            padding: 1.35rem;
        }}
        .home-title {{
            font-size: 2rem;
        }}
        .home-subtitle {{
            font-size: 0.9rem;
        }}
        .home-eyebrow-sep {{
            display: none;
        }}
        .home-hero-metrics {{
            grid-template-columns: 1fr;
        }}
        .medical-stage {{
            min-height: 310px;
        }}
    }}
    @media (prefers-reduced-motion: reduce) {{
        .home-hero::after,
        .medical-orbit,
        .ecg-svg,
        .scan-light,
        .float-chip,
        .home-stat-card {{
            animation: none !important;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)


def _hero(t: dict):
    now = datetime.datetime.now()
    hour = now.hour

    if hour < 12:
        greet, ico = "Good Morning", "☀️"
    elif hour < 17:
        greet, ico = "Good Afternoon", "🌤️"
    elif hour < 21:
        greet, ico = "Good Evening", "🌅"
    else:
        greet, ico = "Night Session", "🌙"

    user = st.session_state.get("user") or {}
    first = (user.get("name") or "Doctor").split()[0]
    date = now.strftime("%A, %d %B %Y")

    tags_html = "".join(
        f'<span class="home-tag">{tag}</span>'
        for tag in ["🇴🇲 SQU-COM", "🏛 OMSB", "🌍 WFME", "📋 USMLE", "🩺 PLAB"]
    )

    metrics_html = "".join(
        f'<div class="home-hero-metric"><b>{value}</b><small>{label}</small></div>'
        for value, label in [
            ("98%", "Focused clinical recall"),
            ("24/7", "AI study companion"),
            ("12", "OSCE station modes"),
        ]
    )

    st.markdown(
        f"""
        <section class="home-hero">
            <div class="home-hero-copy">
                <div class="home-eyebrow">
                    {ico} {greet}, Dr. {first}
                    <span class="home-eyebrow-sep">·</span>
                    {date}
                </div>
                <div class="home-title">
                    A living clinical cockpit for <span>medical mastery</span>.
                </div>
                <div class="home-subtitle">
                    Practice questions, flashcards, timers, AI tutoring, OSCE prep,
                    analytics, and local Oman medical resources in one focused workspace
                    with momentum built into every session.
                </div>
                <div class="home-tags">{tags_html}</div>
                <div class="home-hero-metrics">{metrics_html}</div>
            </div>

            <div class="medical-stage" aria-label="Animated clinical vitals monitor">
                <div class="medical-orbit"></div>
                <div class="float-chip chip-heart">❤️</div>
                <div class="float-chip chip-lung">🫁</div>
                <div class="float-chip chip-pill">💊</div>
                <div class="float-chip chip-cross">⚕️</div>

                <div class="vitals-card">
                    <div class="vitals-top">
                        <span>MedStudy Live Simulator</span>
                        <span class="status-dot"></span>
                    </div>
                    <div class="vitals-screen">
                        <svg class="ecg-svg" viewBox="0 0 900 160" preserveAspectRatio="none" aria-hidden="true">
                            <polyline points="0,86 72,86 94,70 116,98 138,86 224,86 248,26 276,138 310,86 426,86 452,76 478,100 506,86 620,86 642,62 664,92 690,86 760,86 784,38 814,130 846,86 900,86" />
                            <polyline points="900,86 972,86 994,70 1016,98 1038,86 1124,86 1148,26 1176,138 1210,86 1326,86 1352,76 1378,100 1406,86 1520,86 1542,62 1564,92 1590,86 1660,86 1684,38 1714,130 1746,86 1800,86" />
                        </svg>
                        <div class="scan-light"></div>
                    </div>
                    <div class="vitals-grid">
                        <div class="vital-stat"><span>HR</span><strong>72 bpm</strong></div>
                        <div class="vital-stat"><span>SpO2</span><strong>99%</strong></div>
                        <div class="vital-stat"><span>Focus</span><strong>Deep</strong></div>
                    </div>
                </div>
            </div>
        </section>
        """,
        unsafe_allow_html=True,
    )


def _stats(t: dict):
    items = [
        ("📚", "37", "Medical Subjects", t["primary"]),
        ("📝", "500+", "Practice MCQs", "#10b981"),
        ("🤖", "8", "AI Tools", "#8b5cf6"),
        ("🃏", "200+", "Flashcards", "#f59e0b"),
        ("🩺", "12+", "OSCE Stations", "#ef4444"),
    ]

    cols = st.columns(5)
    for col, (ico, num, label, color) in zip(cols, items):
        with col:
            st.markdown(
                f"""
                <div class="home-stat-card">
                    <div class="home-stat-icon" style="background:{color}18;color:{color};">{ico}</div>
                    <div class="home-stat-number" style="color:{color};">{num}</div>
                    <div class="home-stat-label">{label}</div>
                </div>
                """,
                unsafe_allow_html=True,
            )


def _cta_buttons():
    c1, c2, c3, _ = st.columns([2, 2, 2, 1])

    with c1:
        if st.button("📚  Browse Subjects", type="primary", use_container_width=True, key="cta_subj"):
            st.session_state.page = "subjects"
            st.rerun()

    with c2:
        if st.button("🤖  Ask AI Tutor", use_container_width=True, key="cta_ai"):
            st.session_state.page = "ai_tutor"
            st.rerun()

    with c3:
        if st.button("📝  Take a Quiz", use_container_width=True, key="cta_quiz"):
            st.session_state.page = "mcq_quiz"
            st.rerun()


def _module_grid(t: dict):
    st.markdown(
        f"""
        <div class="home-section-title">
            All Modules
            <span style="font-size:0.68rem;font-family:DM Sans,sans-serif;font-weight:700;color:{t["subtext"]};">
                {len(ALL_MODULES)} tools
            </span>
        </div>
        """,
        unsafe_allow_html=True,
    )

    rows = [ALL_MODULES[i:i + 6] for i in range(0, len(ALL_MODULES), 6)]
    for row_index, row in enumerate(rows):
        cols = st.columns(6)

        for col, (icon, page_id, name, desc, color) in zip(cols, row):
            with col:
                st.markdown(
                    f"""
                    <div style="height:3px;background:{color};border-radius:4px 4px 0 0;
                                margin-bottom:-3px;position:relative;z-index:1;"></div>
                    """,
                    unsafe_allow_html=True,
                )

                if st.button(
                    f"{icon}\n{name}",
                    key=f"mod_{page_id}_{row_index}",
                    use_container_width=True,
                ):
                    st.session_state.page = page_id
                    st.rerun()


def _subject_strip(t: dict):
    st.markdown('<div class="home-section-title">Quick Subject Access</div>', unsafe_allow_html=True)

    cols = st.columns(len(FEATURED_SUBJECTS))
    for col, (icon, name) in zip(cols, FEATURED_SUBJECTS):
        with col:
            if st.button(f"{icon} {name}", key=f"subj_{name}", use_container_width=True):
                st.session_state.page = "subjects"
                st.session_state.selected_subject = name
                st.rerun()
