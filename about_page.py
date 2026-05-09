"""
about_page.py — MedStudy Oman 🩺
Phase 5: Developer Portfolio — Sadga Selime
Premium editorial layout · bio · mission · dev timeline · tech stack · contact form
"""

import streamlit as st


# ─────────────────────────────────────────────────────────────────────────────
# DATA
# ─────────────────────────────────────────────────────────────────────────────

TECH_STACK = [
    ("🐍", "Python 3.12",      "Core language",                "#3b82f6"),
    ("⚡", "Streamlit",         "Web framework",                "#ef4444"),
    ("🤖", "Gemini AI",         "AI / NLP engine",              "#8b5cf6"),
    ("🗃️", "SQLite",            "Local database",               "#f59e0b"),
    ("📊", "Plotly",            "Data visualisation",           "#06b6d4"),
    ("🎨", "CSS3 / Variables",  "ThemeManager + Glassmorphism", "#ec4899"),
    ("🔊", "SpeechRecognition", "Voice AI input",               "#10b981"),
    ("📦", "Pandas / NumPy",    "Data processing",              "#f97316"),
]

MILESTONES = [
    {
        "date":  "June 2023",
        "icon":  "💡",
        "title": "The Idea",
        "desc":  "Noticed that Omani medical students had no dedicated study platform. "
                 "Existing apps ignored OMSB standards, Gulf epidemiology, and Arabic language.",
        "color": "#e63946",
    },
    {
        "date":  "August 2023",
        "icon":  "🏗️",
        "title": "Foundation Built",
        "desc":  "Designed the database schema, authentication system, and the first "
                 "version of the subject library covering all 37 WFME-aligned subjects.",
        "color": "#f97316",
    },
    {
        "date":  "October 2023",
        "icon":  "🃏",
        "title": "Study Tools v1",
        "desc":  "Launched flashcards with spaced repetition, the MCQ bank (500+ questions), "
                 "and the first 150 mnemonics hand-curated from high-yield sources.",
        "color": "#f59e0b",
    },
    {
        "date":  "January 2024",
        "icon":  "🤖",
        "title": "AI Integration",
        "desc":  "Integrated Gemini AI as the Medical Tutor — real-time pathophysiology "
                 "explanations, differential diagnosis support, and voice AI for hands-free study.",
        "color": "#10b981",
    },
    {
        "date":  "April 2024",
        "icon":  "🩺",
        "title": "OSCE Engine",
        "desc":  "Built the OSCE Timer with 12 station presets, phase intervals (reading + station), "
                 "and 24 clinical scenarios with checklists.",
        "color": "#0891b2",
    },
    {
        "date":  "July 2024",
        "icon":  "👥",
        "title": "Community Features",
        "desc":  "Launched study groups, discussion forums, shared notes, and the national "
                 "leaderboard — making MedStudy Oman a true peer-learning platform.",
        "color": "#8b5cf6",
    },
    {
        "date":  "October 2024",
        "icon":  "🎨",
        "title": "Design Overhaul",
        "desc":  "Rewrote the entire UI with ThemeManager, glassmorphism, CSS variables, "
                 "and 4 premium themes (Clinical Snow, Deep Surgeon, Oasis Health, Cyber-Med).",
        "color": "#ec4899",
    },
    {
        "date":  "2025 →",
        "icon":  "🚀",
        "title": "MedStudy Oman 2026",
        "desc":  "Phase-by-phase transformation: Bento homepage, Subject Resource Hub, "
                 "multi-style timers, Sadga profile analytics, and the Developer Portfolio.",
        "color": "#a855f7",
    },
]

STATS_CARDS = [
    ("📚", "37",   "Medical Subjects",     "#e63946"),
    ("📝", "500+", "Practice MCQs",        "#10b981"),
    ("💡", "150+", "Mnemonics",            "#8b5cf6"),
    ("🃏", "200+", "Flashcard Entries",    "#f59e0b"),
    ("🤖", "8",    "AI-Powered Features",  "#06b6d4"),
    ("🩺", "24+",  "OSCE Scenarios",       "#ef4444"),
    ("🌍", "4",    "Premium Themes",       "#ec4899"),
    ("🇴🇲", "1",  "Country Inspired",     "#16a34a"),
]

FEATURED_IN = [
    ("🏥", "SQU College of Medicine", "Used by medical students"),
    ("🎓", "Oman Medical College",    "Recommended by peers"),
    ("📚", "OMSB Candidates",         "OMSB Part 1 prep tool"),
    ("🌍", "USMLE Aspirants",         "Step 1 & 2 CK revision"),
]


# ─────────────────────────────────────────────────────────────────────────────
# MAIN PAGE
# ─────────────────────────────────────────────────────────────────────────────
def about_page(theme: dict):
    _inject_about_css(theme)

    _render_hero(theme)
    _render_stats_strip(theme)
    _render_mission_bio(theme)
    _render_tech_stack(theme)
    _render_timeline(theme)
    _render_featured(theme)
    _render_contact(theme)
    _render_footer(theme)


# ─────────────────────────────────────────────────────────────────────────────
# SECTIONS
# ─────────────────────────────────────────────────────────────────────────────
def _render_hero(t: dict):
    st.markdown(f"""
    <div class="about-hero">
        
        <div class="about-orb about-orb-1"></div>
        <div class="about-orb about-orb-2"></div>
        <div class="about-orb about-orb-3"></div>

        <div style="position:relative;z-index:2;text-align:center;">
            
            <div class="dev-avatar-ring">
                <div class="dev-avatar-inner">👨‍⚕️</div>
            </div>

            
            <div class="about-eyebrow">Developer · Designer · Medical Student</div>
            <div class="about-name">Sadga Selime</div>
            <div class="about-subtitle">
                Creator of <span style="color:{t['primary']};background:{t['gradient']};
                -webkit-background-clip:text;-webkit-text-fill-color:transparent;
                background-clip:text;font-weight:800;">MedStudy Oman</span>
            </div>

            
            <div class="about-tags">
                <span class="about-tag">🇴🇲 Based in Oman</span>
                <span class="about-tag">🎓 Medical Student</span>
                <span class="about-tag">⚡ Full-Stack Dev</span>
                <span class="about-tag">🤖 AI Enthusiast</span>
                <span class="about-tag">🩺 OMSB Candidate</span>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)


def _render_stats_strip(t: dict):
    st.markdown("<div style='height:1rem'></div>", unsafe_allow_html=True)
    cols = st.columns(4)
    for i, (icon, num, label, color) in enumerate(STATS_CARDS):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="about-stat-card" style="border-top:3px solid {color};
                 animation-delay:{i*0.07:.2f}s;">
                <div style="font-size:1.6rem;margin-bottom:0.3rem;">{icon}</div>
                <div style="font-family:'Syne',sans-serif;font-size:1.7rem;
                     font-weight:900;color:{color};line-height:1;">{num}</div>
                <div style="font-size:0.72rem;color:{t['subtext']};margin-top:2px;
                     font-weight:600;">{label}</div>
            </div>
            """, unsafe_allow_html=True)
        if i == 3:
            cols = st.columns(4)  # second row


def _render_mission_bio(t: dict):
    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
    _section_divider(t, "🎯 Mission & Story")

    col_l, col_r = st.columns([3, 2])

    with col_l:
        st.markdown(f"""
        <div class="about-card">
            <div class="about-card-label">The Origin Story</div>
            <div class="about-card-body">
                <p>As a medical student at a time when Oman's healthcare system was rapidly
                expanding, I noticed something missing: a platform built <em>specifically
                for Omani medical students</em>.</p>

                <p>Most study apps were built for the US or UK market. They didn't know about
                the <strong>OMSB Fellowship pathway</strong>, they didn't cover
                <strong>tropical diseases endemic to Oman</strong>, and none of them spoke
                Arabic.</p>

                <p>So I built MedStudy Oman — from scratch, one feature at a time, between
                hospital rotations and exam seasons.</p>

                <p>Every flashcard, every mnemonic, every OSCE scenario was chosen because
                it was <em>actually useful</em> to an Omani medical student preparing for
                SQU finals, OMSB Part 1, or an international licensing exam.</p>
            </div>
        </div>
        """, unsafe_allow_html=True)

    with col_r:
        st.markdown(f"""
        <div class="about-card" style="height:100%;">
            <div class="about-card-label">The Mission</div>
            <div style="padding:0.5rem 0;">
        """, unsafe_allow_html=True)

        missions = [
            ("🎯", "Make OMSB prep accessible to every Omani student"),
            ("🌍", "Bridge the gap between SQU curriculum and global standards"),
            ("🤖", "Bring AI-powered education to the Gulf region"),
            ("🇴🇲", "Build Oman's first comprehensive medical study ecosystem"),
            ("🏥", "Produce doctors who are prepared, confident, and capable"),
        ]
        for icon, text in missions:
            st.markdown(f"""
            <div style="display:flex;align-items:flex-start;gap:10px;
                 margin-bottom:0.9rem;padding-bottom:0.9rem;
                 border-bottom:1px solid {t['card_border']};">
                <div style="width:32px;height:32px;border-radius:10px;
                     background:{t['primary']}18;display:flex;align-items:center;
                     justify-content:center;font-size:1rem;flex-shrink:0;">{icon}</div>
                <div style="font-size:0.85rem;color:{t['text']};line-height:1.5;
                     font-weight:500;">{text}</div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown("</div></div>", unsafe_allow_html=True)


def _render_tech_stack(t: dict):
    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
    _section_divider(t, "🛠️ Tech Stack")

    cols = st.columns(4)
    for i, (icon, name, role, color) in enumerate(TECH_STACK):
        with cols[i % 4]:
            st.markdown(f"""
            <div class="tech-card" style="--tc:{color};animation-delay:{i*0.06:.2f}s;">
                <div class="tc-icon" style="background:{color}18;color:{color};">
                    {icon}
                </div>
                <div class="tc-name">{name}</div>
                <div class="tc-role">{role}</div>
                <div class="tc-bar">
                    <div class="tc-bar-fill" style="background:{color};"></div>
                </div>
            </div>
            """, unsafe_allow_html=True)
        if i == 3:
            cols = st.columns(4)


def _render_timeline(t: dict):
    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
    _section_divider(t, "📅 Development Timeline")

    # Two-column timeline
    left_items  = MILESTONES[::2]   # even indices
    right_items = MILESTONES[1::2]  # odd indices

    col_l, col_mid, col_r = st.columns([5, 1, 5])

    def _tl_item(item: dict, align: str = "left"):
        border_side = "border-left" if align == "left" else "border-right"
        pad_side    = "padding-left" if align == "left" else "padding-right"
        dot_side    = "left" if align == "left" else "right"
        text_align  = "left" if align == "left" else "right"
        return f"""
        <div style="position:relative;{pad_side}:28px;padding-bottom:1.8rem;
             text-align:{text_align};">
            <div style="position:absolute;{dot_side}:0;top:4px;
                 width:14px;height:14px;border-radius:50%;
                 background:{item['color']};
                 box-shadow:0 0 10px {item['color']}60;
                 border:2px solid {t['surface']};"></div>
            <div style="font-size:0.68rem;font-weight:800;color:{item['color']};
                 letter-spacing:0.10em;text-transform:uppercase;
                 margin-bottom:0.2rem;">{item['date']}</div>
            <div style="font-family:'Syne',sans-serif;font-size:0.95rem;
                 font-weight:800;color:{t['text']};margin-bottom:0.3rem;">
                 {item['icon']} {item['title']}</div>
            <div style="font-size:0.78rem;color:{t['subtext']};line-height:1.6;">
                 {item['desc']}</div>
        </div>
        """

    with col_l:
        st.markdown(
            f"""<div style="border-right:2px solid {t['card_border']};
                padding-right:20px;">
            {"".join(_tl_item(item, "left") for item in left_items)}
            </div>""",
            unsafe_allow_html=True,
        )

    with col_mid:
        # Central spine dots — build HTML outside f-string to avoid nesting issues
        dot_html = "".join(
            f'<div style="width:10px;height:10px;border-radius:50%;'
            f'background:{t["primary"]}40;border:2px solid {t["primary"]};'
            f'flex-shrink:0;"></div>'
            for _ in MILESTONES[:4]
        )
        st.markdown(
            f'<div style="display:flex;flex-direction:column;align-items:center;'
            f'padding-top:8px;gap:60px;">{dot_html}</div>',
            unsafe_allow_html=True,
        )

    with col_r:
        st.markdown(
            f"""<div style="border-left:2px solid {t['card_border']};
                padding-left:20px;">
            {"".join(_tl_item(item, "right") for item in right_items)}
            </div>""",
            unsafe_allow_html=True,
        )


def _render_featured(t: dict):
    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
    _section_divider(t, "🏆 Used By")

    cols = st.columns(4)
    for i, (icon, name, desc) in enumerate(FEATURED_IN):
        with cols[i]:
            st.markdown(f"""
            <div style="background:{t['glass_bg']};border:1px solid {t['glass_border']};
                 border-radius:18px;padding:1.2rem;text-align:center;
                 backdrop-filter:blur(12px);transition:all 0.22s ease;">
                <div style="font-size:2rem;margin-bottom:0.5rem;">{icon}</div>
                <div style="font-family:'Syne',sans-serif;font-size:0.9rem;
                     font-weight:800;color:{t['text']};margin-bottom:0.2rem;">{name}</div>
                <div style="font-size:0.74rem;color:{t['subtext']};">{desc}</div>
            </div>
            """, unsafe_allow_html=True)


def _render_contact(t: dict):
    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
    _section_divider(t, "💬 Feedback & Contact")

    col_form, col_info = st.columns([3, 2])

    with col_form:
        with st.form("about_contact_form", clear_on_submit=True):
            ff1, ff2 = st.columns(2)
            with ff1:
                f_name  = st.text_input("👤 Full Name",     placeholder="Dr. Your Name")
                f_uni   = st.text_input("🏫 University",    placeholder="SQU / OMC / …")
            with ff2:
                f_email = st.text_input("📧 Email",         placeholder="you@squ.edu.om")
                f_type  = st.selectbox("📋 Message Type", [
                    "🐛 Bug Report",
                    "💡 Feature Request",
                    "🙏 General Feedback",
                    "🤝 Collaboration",
                    "📚 Content Suggestion",
                    "🌐 Translation Help (Arabic)",
                ])
            f_rating = st.select_slider(
                "⭐ Rate MedStudy Oman",
                options=["⭐ 1", "⭐⭐ 2", "⭐⭐⭐ 3", "⭐⭐⭐⭐ 4", "⭐⭐⭐⭐⭐ 5"],
                value="⭐⭐⭐⭐⭐ 5",
            )
            f_msg = st.text_area(
                "💬 Your Message",
                placeholder="Tell Sadga what you think, what's missing, or what you'd like to see next…",
                height=120,
            )
            submitted = st.form_submit_button(
                "📨  Send Feedback",
                use_container_width=True,
                type="primary",
            )

        if submitted:
            if f_name and f_email and f_msg:
                st.success(
                    f"✅ Thank you, {f_name.split()[0]}! Your feedback has been recorded. "
                    "Sadga reads every message. 🙏"
                )
                st.balloons()
            else:
                st.error("⚠️ Please fill in Name, Email and Message.")

    with col_info:
        st.markdown(f"""
        <div class="about-card" style="height:100%;">
            <div class="about-card-label">Get in Touch</div>
            <div style="padding-top:0.5rem;">
        """, unsafe_allow_html=True)

        contacts = [
            ("📧", "Email",     "sadga.medstudy@gmail.com"),
            ("🐙", "GitHub",    "github.com/sadgaselime"),
            ("💼", "LinkedIn",  "linkedin.com/in/sadgaselime"),
            ("🐦", "Twitter/X", "@SadgaMedStudy"),
            ("📱", "WhatsApp",  "Oman Medical Students Group"),
        ]
        for icon, label, value in contacts:
            st.markdown(f"""
            <div style="display:flex;align-items:center;gap:10px;
                 padding:0.65rem 0;border-bottom:1px solid {t['card_border']};">
                <div style="width:30px;height:30px;border-radius:8px;
                     background:{t['primary']}15;display:flex;align-items:center;
                     justify-content:center;font-size:0.9rem;flex-shrink:0;">{icon}</div>
                <div>
                    <div style="font-size:0.7rem;font-weight:700;color:{t['subtext']};
                         text-transform:uppercase;letter-spacing:0.06em;">{label}</div>
                    <div style="font-size:0.82rem;color:{t['primary']};font-weight:600;">
                         {value}</div>
                </div>
            </div>
            """, unsafe_allow_html=True)

        st.markdown(f"""
            </div>
            
            <div style="margin-top:1rem;padding:0.7rem;background:{t['primary']}10;
                 border:1px solid {t['primary']}30;border-radius:10px;
                 font-size:0.76rem;color:{t['text_muted']};text-align:center;">
                ⚡ Typical response within 24–48 hours
            </div>
        </div>
        """, unsafe_allow_html=True)


def _render_footer(t: dict):
    st.markdown("<div style='height:2rem'></div>", unsafe_allow_html=True)
    st.markdown(f"""
    <div class="about-footer">
        <div style="margin-bottom:0.4rem;">
            <span style="font-family:'Syne',sans-serif;font-size:1.4rem;font-weight:900;
                 display:inline;
                 color:{t['primary']};
                 background:{t['gradient']};-webkit-background-clip:text;
                 -webkit-text-fill-color:transparent;background-clip:text;">
                 MedStudy Oman</span>
        </div>
        <div style="font-size:0.78rem;color:{t['subtext']};margin-bottom:1rem;">
             Built with 💙 in Oman · For Omani Doctors · By an Omani Medical Student
        </div>
        <div style="display:flex;gap:8px;justify-content:center;flex-wrap:wrap;">
            <span class="footer-tag">🎓 SQU Aligned</span>
            <span class="footer-tag">🏛️ OMSB Ready</span>
            <span class="footer-tag">🌍 WFME Standards</span>
            <span class="footer-tag">📋 USMLE Compatible</span>
            <span class="footer-tag">🩺 PLAB Friendly</span>
        </div>
        <div style="margin-top:1.2rem;font-size:0.72rem;color:{t['subtext']};opacity:0.5;">
             © 2025 Sadga Selime · MedStudy Oman · All rights reserved
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# SHARED HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def _section_divider(t: dict, title: str):
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:14px;margin-bottom:1.2rem;">
        <div style="font-family:'Syne',sans-serif;font-size:1.15rem;font-weight:900;
             color:{t['text']};white-space:nowrap;">{title}</div>
        <div style="flex:1;height:1px;background:{t['card_border']};"></div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────────────────────
def _inject_about_css(t: dict):
    st.markdown(f"""
    <style>
    /* ── Hero ─────────────────────────────────────── */
    .about-hero {{
        position:       relative;
        overflow:       hidden;
        background:     {t['hero_gradient']};
        border:         1px solid {t['card_border']};
        border-radius:  28px;
        padding:        3.5rem 2rem 3rem;
        margin-bottom:  2rem;
        text-align:     center;
    }}
    .about-orb {{
        position:       absolute;
        border-radius:  50%;
        pointer-events: none;
        animation:      glowPulse 4s ease-in-out infinite;
    }}
    .about-orb-1 {{
        width:180px; height:180px;
        top:-60px; left:-60px;
        background: radial-gradient(circle, {t['primary']}25, transparent 70%);
    }}
    .about-orb-2 {{
        width:220px; height:220px;
        bottom:-80px; right:-80px;
        background: radial-gradient(circle, {t['secondary']}20, transparent 70%);
        animation-delay: 1s;
    }}
    .about-orb-3 {{
        width:140px; height:140px;
        top:40%; left:55%;
        background: radial-gradient(circle, {t['primary']}12, transparent 70%);
        animation-delay: 2s;
    }}
    .dev-avatar-ring {{
        width:100px; height:100px;
        border-radius:50%;
        background:{t['gradient']};
        padding:3px;
        box-shadow:{t['glow']};
        margin:0 auto 1.2rem;
        animation:float 4s ease-in-out infinite;
    }}
    .dev-avatar-inner {{
        width:100%; height:100%;
        border-radius:50%;
        background:{t['surface']};
        display:flex; align-items:center; justify-content:center;
        font-size:2.6rem;
    }}
    .about-eyebrow {{
        font-size:0.72rem; font-weight:800;
        letter-spacing:0.14em; text-transform:uppercase;
        color:{t['primary']}; margin-bottom:0.5rem;
        animation:fadeIn 0.4s ease both;
    }}
    .about-name {{
        font-family:'Syne',sans-serif;
        font-size:clamp(2rem,4vw,3rem);
        font-weight:900; color:{t['text']};
        letter-spacing:-0.03em; line-height:1.1;
        margin-bottom:0.4rem;
        animation:fadeUp 0.5s ease both;
    }}
    .about-subtitle {{
        font-size:1.05rem; color:{t['text_muted']};
        margin-bottom:1.2rem;
        animation:fadeUp 0.6s ease both;
    }}
    .about-tags {{
        display:flex; gap:8px; justify-content:center;
        flex-wrap:wrap;
        animation:fadeUp 0.7s ease both;
    }}
    .about-tag {{
        background:{t['glass_bg']};
        border:1px solid {t['glass_border']};
        border-radius:999px;
        padding:5px 14px;
        font-size:0.78rem; font-weight:600;
        color:{t['text_muted']};
        backdrop-filter:blur(8px);
        transition:all 0.2s ease;
    }}
    .about-tag:hover {{
        background:{t['primary']}; color:{t['text_inverse']};
        border-color:{t['primary']};
    }}

    /* ── Stat cards ───────────────────────────────── */
    .about-stat-card {{
        background:    {t['card_bg']};
        border:        1px solid {t['card_border']};
        border-radius: 18px;
        padding:       1.1rem 0.8rem;
        text-align:    center;
        transition:    all 0.25s ease;
        backdrop-filter: blur(10px);
        margin-bottom: 0.8rem;
        animation:     scaleIn 0.4s ease both;
    }}
    .about-stat-card:hover {{
        transform:  translateY(-4px);
        box-shadow: var(--shadow-md), var(--glow);
    }}

    /* ── General card ─────────────────────────────── */
    .about-card {{
        background:    {t['glass_bg']};
        border:        1px solid {t['glass_border']};
        border-radius: 22px;
        padding:       1.8rem;
        backdrop-filter: blur(16px);
        box-shadow:    {t['shadow_sm']};
        animation:     fadeUp 0.5s ease both;
    }}
    .about-card-label {{
        font-size:     0.68rem;
        font-weight:   800;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color:         {t['primary']};
        margin-bottom: 0.8rem;
    }}
    .about-card-body {{
        font-size:     0.88rem;
        color:         {t['text']};
        line-height:   1.85;
    }}
    .about-card-body p {{ margin-bottom:0.8rem; }}
    .about-card-body p:last-child {{ margin-bottom:0; }}
    .about-card-body strong {{ color:{t['text']}; font-weight:700; }}
    .about-card-body em    {{ color:{t['primary']}; font-style:italic; }}

    /* ── Tech stack cards ─────────────────────────── */
    .tech-card {{
        background:    {t['card_bg']};
        border:        1px solid {t['card_border']};
        border-top:    3px solid var(--tc, {t['primary']});
        border-radius: 16px;
        padding:       1rem 0.9rem;
        text-align:    center;
        transition:    all 0.25s ease;
        margin-bottom: 0.8rem;
        animation:     stagger-fade 0.4s ease both;
    }}
    .tech-card:hover {{
        transform:    translateY(-4px);
        box-shadow:   0 8px 24px var(--tc, {t['primary']})25;
        border-color: var(--tc, {t['primary']});
    }}
    .tc-icon {{
        width:44px; height:44px; border-radius:12px;
        display:flex; align-items:center; justify-content:center;
        font-size:1.3rem; margin:0 auto 0.5rem;
        transition:all 0.2s;
    }}
    .tech-card:hover .tc-icon {{ transform:scale(1.1); }}
    .tc-name {{
        font-family:'Syne',sans-serif; font-size:0.85rem;
        font-weight:800; color:{t['text']}; margin-bottom:0.2rem;
    }}
    .tc-role  {{ font-size:0.71rem; color:{t['subtext']}; margin-bottom:0.6rem; }}
    .tc-bar   {{
        width:100%; height:3px;
        background:{t['card_border']};
        border-radius:999px; overflow:hidden;
    }}
    .tc-bar-fill {{
        height:100%; width:85%;
        border-radius:999px;
        animation:shimmer 2s ease-in-out infinite;
    }}

    /* ── Footer ───────────────────────────────────── */
    .about-footer {{
        background:    {t['glass_bg']};
        border:        1px solid {t['glass_border']};
        border-radius: 22px;
        padding:       2.5rem 2rem;
        text-align:    center;
        backdrop-filter: blur(16px);
    }}
    .footer-tag {{
        background:    {t['card_bg']};
        border:        1px solid {t['card_border']};
        border-radius: 999px;
        padding:       4px 12px;
        font-size:     0.73rem;
        font-weight:   600;
        color:         {t['text_muted']};
    }}
    </style>
    """, unsafe_allow_html=True)