
    @media (max-width: 768px) {{
        .home-hero {{
            grid-template-columns: 1fr;
            min-height: 0;
            padding: 1.35rem;
        }}
        .home-title {{ font-size: 2rem; }}
        .home-subtitle {{ font-size: 0.9rem; }}
        .home-eyebrow {{
            align-items: flex-start;
            gap: 4px 8px;
            line-height: 1.35;
        }}
        .home-eyebrow-sep {{ display: none; }}
        .home-hero-metrics {{ grid-template-columns: 1fr; }}
        .medical-stage {{ min-height: 310px; }}
        .dna {{ display: none; }}
    }}
    @media (prefers-reduced-motion: reduce) {{
        .home-hero::after,
        .medical-orbit,
        .ecg-svg,
        .scan-light,
        .dna,
        .float-chip,
        .home-stat-card {{
            animation: none !important;
        }}
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
    metrics_html = "".join(
        f'<div class="home-hero-metric"><b>{value}</b><small>{label}</small></div>'
        for value, label in [
            ("98%", "Focused clinical recall"),
            ("24/7", "AI study companion"),
            ("12", "OSCE station modes"),
        ]
    )
    dna_html = "".join(
        f'<i style="--n:{i};--i:{i * 0.75}rad;"></i>'
        for i in range(12)
    )

    st.markdown(
        f'<section class="home-hero">'
        f'<div class="home-hero-copy">'
        f'<div class="home-eyebrow">{ico} {greet}, Dr. {first}<span class="home-eyebrow-sep">·</span>{date}</div>'
        f'<div class="home-title">A living clinical cockpit for <span>medical mastery</span>.</div>'
        f'<div class="home-subtitle">Practice questions, flashcards, timers, AI tutoring, OSCE prep, analytics, and local Oman medical resources in one focused workspace with momentum built into every session.</div>'
        f'<div class="home-tags">{tags_html}</div>'
        f'<div class="home-hero-metrics">{metrics_html}</div>'
        f'</div>'
        f'<div class="medical-stage" aria-label="Animated clinical vitals monitor">'
        f'<div class="medical-orbit"></div>'
        f'<div class="float-chip chip-heart">❤️</div>'
        f'<div class="float-chip chip-lung">🫁</div>'
        f'<div class="float-chip chip-pill">💊</div>'
        f'<div class="float-chip chip-cross">⚕️</div>'
        f'<div class="dna">{dna_html}</div>'
        f'<div class="vitals-card">'
        f'<div class="vitals-top"><span>MedStudy Live Simulator</span><span class="status-dot"></span></div>'
        f'<div class="vitals-screen">'
        f'<svg class="ecg-svg" viewBox="0 0 900 160" preserveAspectRatio="none" aria-hidden="true">'
        f'<polyline points="0,86 72,86 94,70 116,98 138,86 224,86 248,26 276,138 310,86 426,86 452,76 478,100 506,86 620,86 642,62 664,92 690,86 760,86 784,38 814,130 846,86 900,86" />'
        f'<polyline points="900,86 972,86 994,70 1016,98 1038,86 1124,86 1148,26 1176,138 1210,86 1326,86 1352,76 1378,100 1406,86 1520,86 1542,62 1564,92 1590,86 1660,86 1684,38 1714,130 1746,86 1800,86" />'
        f'</svg><div class="scan-light"></div></div>'
        f'<div class="vitals-grid">'
        f'<div class="vital-stat"><span>HR</span><strong>72 bpm</strong></div>'
        f'<div class="vital-stat"><span>SpO2</span><strong>99%</strong></div>'
        f'<div class="vital-stat"><span>Focus</span><strong>Deep</strong></div>'
        f'</div></div>'
        f'</div>'
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
                
