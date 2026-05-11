"""
mobile.py — MedStudy Oman 🩺
Phase 9: Mobile & PWA Polish
Responsive breakpoints · Bottom navigation · Touch targets · PWA meta tags
"""

import streamlit as st

# ─────────────────────────────────────────────────────────────────────────────
# BOTTOM NAV PAGES  (5 most-used)
# ─────────────────────────────────────────────────────────────────────────────
BOTTOM_NAV = [
    ("◆", "dashboard", "Dashboard", "لوحة الدراسة"),
    ("▦", "az_hub",    "Knowledge", "المعرفة"),
    ("?", "mcq_quiz",  "Questions", "الأسئلة"),
    ("AI", "ai_tutor", "AI Tutor", "المعلم"),
    ("◎", "profile",   "Profile", "الملف"),
]


# ─────────────────────────────────────────────────────────────────────────────
# ENTRY POINTS — call both from app.py on every render
# ─────────────────────────────────────────────────────────────────────────────
def inject_mobile(theme: dict):
    """Inject responsive CSS + PWA meta tags. Call once per render, before sidebar."""
    _pwa_meta(theme)
    _mobile_css(theme)


def render_bottom_nav(theme: dict):
    """Render fixed bottom navigation bar. Call at the very end of every page."""
    _bottom_nav_css(theme)
    _bottom_nav_buttons(theme)


# ─────────────────────────────────────────────────────────────────────────────
# PWA META TAGS
# ─────────────────────────────────────────────────────────────────────────────
def _pwa_meta(t: dict):
    theme_color = t["primary"]
    bg_color    = t["bg"]
    st.markdown(f"""
    <head>
        <meta name="viewport" content="width=device-width, initial-scale=1.0,
              maximum-scale=1.0, user-scalable=no, viewport-fit=cover">
        <meta name="theme-color" content="{theme_color}">
        <meta name="mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-capable" content="yes">
        <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
        <meta name="apple-mobile-web-app-title" content="MedStudy">
        <meta name="application-name" content="MedStudy Oman">
        <meta name="msapplication-TileColor" content="{theme_color}">
        <meta name="description"
              content="AI-powered medical education for Omani medical students.
                       OMSB · USMLE · SQU-COM · WFME aligned.">
        <link rel="manifest" href="/app/static/manifest.json">
        <link rel="apple-touch-icon" href="/app/static/icon-192.png">
    </head>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# RESPONSIVE CSS
# ─────────────────────────────────────────────────────────────────────────────
def _mobile_css(t: dict):
    st.markdown(f"""
    <style>
    /* ═══════════════════════════════════════════════════════════════
       GLOBAL TOUCH & TYPOGRAPHY FIXES  (all screen sizes)
    ═══════════════════════════════════════════════════════════════ */

    /* Prevent iOS font-size zoom on input focus (needs ≥16px) */
    input, textarea, select {{
        font-size: 16px !important;
    }}

    /* Minimum touch target — Apple HIG & Material recommends 44px */
    .stButton > button {{
        min-height:    44px     !important;
        padding:       0.55rem 0.9rem !important;
        touch-action:  manipulation;
        -webkit-tap-highlight-color: {t['primary']}30;
    }}
    .stButton > button:active {{
        transform:     scale(0.97) !important;
        opacity:       0.9 !important;
    }}

    /* Remove tap delay on links/buttons */
    *, *::before, *::after {{
        touch-action: manipulation;
    }}

    /* Smooth scrolling everywhere */
    html {{ scroll-behavior: smooth; }}

    /* Remove iOS input shadow */
    input, textarea {{
        -webkit-appearance: none;
        border-radius: 12px !important;
    }}

    /* ═══════════════════════════════════════════════════════════════
       TABLET  (max-width: 1024px)
    ═══════════════════════════════════════════════════════════════ */
    @media (max-width: 1024px) {{
        .block-container {{
            padding-left:  1rem !important;
            padding-right: 1rem !important;
        }}
        /* Reduce hero title size */
        [data-testid="stMarkdownContainer"] div[style*="3.4rem"],
        [data-testid="stMarkdownContainer"] div[style*="3.6rem"] {{
            font-size: 2.4rem !important;
        }}
    }}

    /* ═══════════════════════════════════════════════════════════════
       MOBILE  (max-width: 768px)
    ═══════════════════════════════════════════════════════════════ */
    @media (max-width: 768px) {{

        /* ── Block container ─────────────────────────────────────── */
        .block-container {{
            padding-left:   0.6rem  !important;
            padding-right:  0.6rem  !important;
            padding-top:    0.8rem  !important;
            padding-bottom: 90px    !important;   /* space for bottom nav */
        }}

        /* ── Sidebar — auto-collapse on mobile ───────────────────── */
        [data-testid="stSidebar"] {{
            min-width:  260px !important;
            max-width:  280px !important;
        }}

        /* ── Top bar — compact ───────────────────────────────────── */
        [data-testid="stMarkdownContainer"] div[style*="2.1rem"],
        [data-testid="stMarkdownContainer"] span[style*="2.1rem"],
        [data-testid="stMarkdownContainer"] span[style*="2.2rem"] {{
            font-size:     1.5rem !important;
        }}

        /* ── Hero card ───────────────────────────────────────────── */
        [data-testid="stMarkdownContainer"] div[style*="3rem 3rem"] {{
            padding:       1.5rem 1.2rem !important;
        }}
        /* Hero title */
        [data-testid="stMarkdownContainer"] div[style*="3.4rem"],
        [data-testid="stMarkdownContainer"] div[style*="3.6rem"] {{
            font-size:     2rem !important;
            line-height:   1.1 !important;
        }}
        /* Hero subtitle */
        [data-testid="stMarkdownContainer"] div[style*="1.05rem"],
        [data-testid="stMarkdownContainer"] div[style*="1rem;color"] {{
            font-size:     0.88rem !important;
        }}
        /* Hide decorative SVG icons on mobile (too crowded) */
        [data-testid="stMarkdownContainer"] div[style*="position:absolute"][style*="pointer-events:none"] {{
            display: none !important;
        }}

        /* ── Stats row — 2-col wrap ──────────────────────────────── */
        .stat-pill {{
            min-width:     140px !important;
            padding:       0.8rem !important;
        }}
        .stat-num {{ font-size: 1.3rem !important; }}

        /* ── Module grid buttons — 3 per row ─────────────────────── */
        div[data-testid="stHorizontalBlock"] {{
            flex-wrap:     wrap !important;
            gap:           6px  !important;
        }}
        div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {{
            min-width:     calc(33.33% - 6px) !important;
            flex:          1 1 calc(33.33% - 6px) !important;
        }}

        /* ── Cards — reduce padding ──────────────────────────────── */
        .dash-card, .glass-card, .about-card {{
            padding:       0.9rem !important;
            border-radius: 14px !important;
        }}

        /* ── Tabs — scrollable ───────────────────────────────────── */
        .stTabs [data-baseweb="tab-list"] {{
            overflow-x:    auto !important;
            flex-wrap:     nowrap !important;
        }}
        .stTabs [data-baseweb="tab"] {{
            white-space:   nowrap !important;
            padding:       7px 12px !important;
            font-size:     0.78rem !important;
        }}

        /* ── Metric cards — 2 per row ────────────────────────────── */
        .kpi-card {{ min-width: 130px !important; }}
        .kpi-value {{ font-size: 1.4rem !important; }}

        /* ── Heatmap — hide on very small ───────────────────────── */
        .hmap-grid {{ gap: 2px !important; }}
        .hmap-cell {{
            width:  11px !important;
            height: 11px !important;
        }}

        /* ── Chat area — full height ─────────────────────────────── */
        #chat-container {{ max-height: 380px !important; }}

        /* ── Section titles — smaller ────────────────────────────── */
        .home-section-title {{
            font-size: 1rem !important;
        }}

        /* ── Remove hover transforms (feel wrong on touch) ─────── */
        .smart-tile:hover, .subj-card:hover,
        .bento-tile:hover, .mod-tile:hover {{
            transform: none !important;
        }}
        .stButton > button:hover {{
            transform: none !important;
        }}

        /* ── MCQ option cards — full width ───────────────────────── */
        div[data-testid="stHorizontalBlock"]:has(.stButton) > div {{
            min-width: calc(50% - 6px) !important;
            flex: 1 1 calc(50% - 6px) !important;
        }}
    }}

    /* ═══════════════════════════════════════════════════════════════
       SMALL PHONE  (max-width: 480px)
    ═══════════════════════════════════════════════════════════════ */
    @media (max-width: 480px) {{
        .block-container {{
            padding-left:  0.4rem !important;
            padding-right: 0.4rem !important;
        }}

        /* Module grid → 2 per row on small phones */
        div[data-testid="stHorizontalBlock"] > div[data-testid="column"] {{
            min-width:     calc(50% - 4px) !important;
            flex:          1 1 calc(50% - 4px) !important;
        }}

        /* Hero title */
        [data-testid="stMarkdownContainer"] div[style*="3.4rem"],
        [data-testid="stMarkdownContainer"] div[style*="3.6rem"] {{
            font-size: 1.7rem !important;
        }}

        /* Top bar title */
        [data-testid="stMarkdownContainer"] span[style*="2.1rem"],
        [data-testid="stMarkdownContainer"] span[style*="2.2rem"] {{
            font-size: 1.3rem !important;
        }}

        /* Stats → wrap freely */
        .stat-pill {{ min-width: 120px !important; }}

        /* Bottom nav labels — smaller */
        .bnav-label {{ font-size: 0.6rem !important; }}

        /* Reduce all border radii for denser feel */
        .dash-card, .glass-card, .about-card,
        [data-testid="stForm"] {{
            border-radius: 12px !important;
        }}
    }}

    /* ═══════════════════════════════════════════════════════════════
       LANDSCAPE PHONE  (short + wide)
    ═══════════════════════════════════════════════════════════════ */
    @media (max-height: 500px) and (orientation: landscape) {{
        .block-container {{
            padding-bottom: 70px !important;
        }}
        .mobile-bottom-nav {{
            height: 56px !important;
        }}
    }}

    /* ═══════════════════════════════════════════════════════════════
       SAFE AREA (iPhone X+ notch / Dynamic Island)
    ═══════════════════════════════════════════════════════════════ */
    @supports (padding-bottom: env(safe-area-inset-bottom)) {{
        .mobile-bottom-nav {{
            padding-bottom: calc(8px + env(safe-area-inset-bottom)) !important;
            height:         calc(68px + env(safe-area-inset-bottom)) !important;
        }}
        .block-container {{
            padding-bottom: calc(90px + env(safe-area-inset-bottom)) !important;
        }}
    }}

    </style>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# BOTTOM NAVIGATION BAR
# ─────────────────────────────────────────────────────────────────────────────
def _bottom_nav_css(t: dict):
    st.markdown(f"""
    <style>
    /* ── Visual nav bar (fixed, visual only) ──────────────────────── */
    .mobile-bottom-nav {{
        display:         none;    /* hidden on desktop */
    }}
    @media (max-width: 768px) {{
        .mobile-bottom-nav {{
            display:         flex !important;
            position:        fixed;
            bottom:          0;
            left:            0;
            right:           0;
            height:          68px;
            background:      {t['sidebar_bg']};
            border-top:      1px solid {t['card_border']};
            align-items:     center;
            justify-content: space-around;
            z-index:         8000;
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            padding:         0 4px;
            box-shadow:      0 -4px 20px rgba(0,0,0,0.12);
        }}
        .bnav-item {{
            display:         flex;
            flex-direction:  column;
            align-items:     center;
            justify-content: center;
            gap:             2px;
            padding:         6px 10px;
            border-radius:   12px;
            cursor:          pointer;
            transition:      all 0.18s ease;
            min-width:       52px;
            flex:            1;
        }}
        .bnav-item:active {{ transform: scale(0.92); }}
        .bnav-icon  {{
            font-size:   1.3rem;
            line-height: 1;
        }}
        .bnav-label {{
            font-size:   0.62rem;
            font-weight: 700;
            letter-spacing: 0.02em;
            color:       {t['subtext']};
            white-space: nowrap;
        }}
        .bnav-item.bnav-active .bnav-label {{
            color: {t['primary']};
        }}
        .bnav-active-dot {{
            width:        4px;
            height:       4px;
            border-radius: 50%;
            background:   {t['primary']};
            margin-top:   1px;
        }}

        /* ── Real Streamlit nav buttons (invisible, same position) ── */
        .bnav-buttons-container {{
            position:    fixed;
            bottom:      0;
            left:        0;
            right:       0;
            height:      68px;
            z-index:     8001;
            display:     flex;
            align-items: stretch;
        }}
        .bnav-buttons-container .stButton > button {{
            background:    transparent !important;
            border:        none !important;
            border-radius: 0 !important;
            opacity:       0 !important;
            height:        100% !important;
            min-height:    68px !important;
            width:         100% !important;
            cursor:        pointer !important;
        }}
        /* Hide bottom nav buttons on desktop */
        .bnav-buttons-container {{
            display: none;
        }}
    }}

    /* Show on mobile */
    @media (max-width: 768px) {{
        .bnav-buttons-container {{
            display: flex !important;
        }}
    }}
    </style>
    """, unsafe_allow_html=True)


def _bottom_nav_buttons(t: dict):
    """Render the visual bar + invisible Streamlit button overlay."""
    current = st.session_state.get("page", "home")

    # ── Visual bar (HTML — fixed position, always visible) ────────────────
    items_html = ""
    is_arabic = st.session_state.get("language") == "ar"
    for icon, page_id, label, ar_label in BOTTOM_NAV:
        label = ar_label if is_arabic else label
        is_active   = current == page_id
        item_style  = " bnav-active" if is_active else ""
        dot         = '<div class="bnav-active-dot"></div>' if is_active else ""
        icon_style  = (f"color:{t['primary']};filter:drop-shadow(0 0 6px {t['primary']}60);"
                       if is_active else "")
        items_html += (
            f'<div class="bnav-item{item_style}">'
            f'<div class="bnav-icon" style="{icon_style}">{icon}</div>'
            f'<div class="bnav-label">{label}</div>'
            f'{dot}</div>'
        )

    st.markdown(
        f'<div class="mobile-bottom-nav">{items_html}</div>',
        unsafe_allow_html=True,
    )

    # ── Invisible Streamlit button overlay ────────────────────────────────
    st.markdown(
        '<div class="bnav-buttons-container">',
        unsafe_allow_html=True,
    )
    cols = st.columns(len(BOTTOM_NAV))
    is_arabic = st.session_state.get("language") == "ar"
    for col, (icon, page_id, label, ar_label) in zip(cols, BOTTOM_NAV):
        label = ar_label if is_arabic else label
        with col:
            if st.button(
                f"{icon} {label}",
                key=f"bnav_{page_id}",
                use_container_width=True,
            ):
                st.session_state.page = page_id
                st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# INSTALL PROMPT  (shown once, dismissible)
# ─────────────────────────────────────────────────────────────────────────────
def render_install_prompt(t: dict):
    """Show 'Add to Home Screen' tip — only on first visit."""
    if st.session_state.get("pwa_prompt_dismissed"):
        return

    st.markdown(f"""
    <div style="position:fixed;bottom:80px;left:50%;transform:translateX(-50%);
         background:{t['card_bg']};border:1.5px solid {t['primary']}50;
         border-radius:16px;padding:0.9rem 1.2rem;
         backdrop-filter:blur(20px);z-index:7000;
         box-shadow:{t['shadow_lg']};max-width:320px;width:90%;
         display:flex;align-items:center;gap:12px;
         animation:slideUp 0.4s ease both;"
         id="pwa-prompt">
        <div style="font-size:1.8rem;flex-shrink:0;">📲</div>
        <div>
            <div style="font-size:0.82rem;font-weight:800;color:{t['text']};
                 margin-bottom:2px;">Install MedStudy</div>
            <div style="font-size:0.72rem;color:{t['subtext']};">
                Tap <strong>Share → Add to Home Screen</strong> for the app experience</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if st.button("✕ Dismiss", key="pwa_dismiss"):
        st.session_state.pwa_prompt_dismissed = True
        st.rerun()
