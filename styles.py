"""
styles.py — MedStudy Oman ✦ Fixed Sidebar Edition
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Premium Medical UI System with Proper Sidebar Support
"""

# ═══════════════════════════════════════════════════════════════════════
# THEMES
# ═══════════════════════════════════════════════════════════════════════

THEMES = {

    "🌌 Midnight Rounds": {
        "name": "Midnight Rounds",
        "family": "dark",

        "primary": "#22d3ee",
        "primary_glow": "rgba(34,211,238,0.30)",
        "secondary": "#0891b2",
        "accent": "#164e63",

        "bg": "#020617",
        "surface": "#0a1628",
        "surface_raised": "#0f1f38",

        "card_bg": "rgba(10,22,40,0.80)",
        "card_border": "rgba(34,211,238,0.14)",

        "sidebar_bg": "#060f1e",

        "glass_bg": "rgba(34,211,238,0.045)",
        "glass_border": "rgba(34,211,238,0.18)",
        "glass_blur": "28px",

        "text": "#e2f4ff",
        "text_muted": "#7ab8d4",
        "subtext": "#3d6a88",
        "text_inverse": "#020617",

        "gradient": "linear-gradient(135deg,#22d3ee,#3b82f6)",
        "hero_gradient": "linear-gradient(160deg,#020617 0%,#061228 55%,#020a1a 100%)",

        "card_gradient": "linear-gradient(145deg,rgba(34,211,238,0.06),rgba(59,130,246,0.03))",

        "glow": "0 0 40px rgba(34,211,238,0.28)",
        "glow_lg": "0 0 80px rgba(34,211,238,0.15)",

        "shadow_sm": "0 2px 8px rgba(0,0,0,0.50)",
        "shadow_md": "0 8px 32px rgba(0,0,0,0.60)",
        "shadow_lg": "0 24px 64px rgba(0,0,0,0.70)",

        "hover_bg": "rgba(34,211,238,0.08)",
        "focus_ring": "0 0 0 3px rgba(34,211,238,0.32)",

        "success": "#10d982",
        "warning": "#fbbf24",
        "error": "#f43f5e",
        "info": "#22d3ee",

        "sidebar_accent": "#22d3ee",
        "nav_active_bg": "rgba(34,211,238,0.12)",
        "badge_bg": "rgba(34,211,238,0.15)",
        "streak_color": "#fbbf24",
    },

    "🩺 Clinical Precision": {
        "name": "Clinical Precision",
        "family": "light",

        "primary": "#0066cc",
        "primary_glow": "rgba(0,102,204,0.20)",
        "secondary": "#34c759",
        "accent": "#004a9f",

        "bg": "#f5f7fa",
        "surface": "#ffffff",
        "surface_raised": "#eef1f6",

        "card_bg": "rgba(255,255,255,0.92)",
        "card_border": "rgba(0,102,204,0.14)",

        "sidebar_bg": "#1c3557",

        "glass_bg": "rgba(255,255,255,0.75)",
        "glass_border": "rgba(0,102,204,0.22)",
        "glass_blur": "20px",

        "text": "#0d1f3c",
        "text_muted": "#3a5280",
        "subtext": "#6b82a8",
        "text_inverse": "#ffffff",

        "gradient": "linear-gradient(135deg,#0066cc,#34c759)",
        "hero_gradient": "linear-gradient(160deg,#f5f7fa 0%,#eaf0fb 55%,#e0eaf8 100%)",

        "card_gradient": "linear-gradient(145deg,rgba(255,255,255,0.97),rgba(238,241,246,0.88))",

        "glow": "0 0 28px rgba(0,102,204,0.18)",
        "glow_lg": "0 0 60px rgba(0,102,204,0.10)",

        "shadow_sm": "0 1px 6px rgba(13,31,60,0.07)",
        "shadow_md": "0 6px 24px rgba(13,31,60,0.10)",
        "shadow_lg": "0 16px 52px rgba(13,31,60,0.14)",

        "hover_bg": "rgba(0,102,204,0.06)",
        "focus_ring": "0 0 0 3px rgba(0,102,204,0.25)",

        "success": "#34c759",
        "warning": "#ff9500",
        "error": "#ff3b30",
        "info": "#0066cc",

        "sidebar_accent": "#22d3ee",
        "nav_active_bg": "rgba(255,255,255,0.15)",
        "badge_bg": "rgba(34,199,89,0.18)",
        "streak_color": "#ff9500",
    },
}


# ═══════════════════════════════════════════════════════════════════════
# THEME MANAGER
# ═══════════════════════════════════════════════════════════════════════

class ThemeManager:

    def __init__(self, theme_key: str):
        self.key = theme_key
        self.t = THEMES.get(theme_key, THEMES["🌌 Midnight Rounds"])

    def inject(self):

        t = self.t

        cs = "dark" if t["family"] == "dark" else "light"

        return f"""
<style>

/* ═══════════════════════════════════════════════════════════════
   ROOT VARIABLES
   ═══════════════════════════════════════════════════════════════ */

:root {{

    color-scheme: {cs};

    --primary: {t["primary"]};
    --primary-glow: {t["primary_glow"]};
    --secondary: {t["secondary"]};

    --bg: {t["bg"]};
    --surface: {t["surface"]};

    --card-bg: {t["card_bg"]};
    --card-border: {t["card_border"]};

    --sidebar-bg: {t["sidebar_bg"]};

    --glass-bg: {t["glass_bg"]};
    --glass-border: {t["glass_border"]};
    --blur: {t["glass_blur"]};

    --text: {t["text"]};
    --text-muted: {t["text_muted"]};
    --subtext: {t["subtext"]};
    --text-inverse: {t["text_inverse"]};

    --gradient: {t["gradient"]};
    --hero-gradient: {t["hero_gradient"]};

    --shadow-md: {t["shadow_md"]};
    --shadow-lg: {t["shadow_lg"]};

    --glow: {t["glow"]};
    --glow-lg: {t["glow_lg"]};

    --hover-bg: {t["hover_bg"]};
    --focus-ring: {t["focus_ring"]};

    --radius: 18px;
}}


/* ═══════════════════════════════════════════════════════════════
   GLOBAL
   ═══════════════════════════════════════════════════════════════ */

html,
body,
.stApp {{
    background: var(--hero-gradient) !important;
    color: var(--text) !important;
}

* {{
    font-family: 'Inter', sans-serif !important;
}}

h1,h2,h3,h4,h5,h6 {{
    color: var(--text) !important;
}}

p,span,label,div {{
    color: var(--text);
}}


/* ═══════════════════════════════════════════════════════════════
   FIXED SIDEBAR
   ═══════════════════════════════════════════════════════════════ */

section[data-testid="stSidebar"] {{
    background: var(--sidebar-bg) !important;

    border-right: 1px solid var(--glass-border) !important;

    width: 290px !important;
    min-width: 290px !important;

    box-shadow: 4px 0 40px rgba(0,0,0,0.35) !important;
}}

section[data-testid="stSidebar"] > div {{
    background: var(--sidebar-bg) !important;
}}

section[data-testid="stSidebar"] * {{
    color: var(--text) !important;
}}


/* FIX COLLAPSE ISSUE */
[data-testid="stSidebar"][aria-expanded="false"] {{
    min-width: 290px !important;
}}


/* TOGGLE BUTTON */
button[kind="header"] {{
    opacity: 1 !important;
    visibility: visible !important;
}}


/* ═══════════════════════════════════════════════════════════════
   MAIN CONTAINER
   ═══════════════════════════════════════════════════════════════ */

.block-container {{
    padding-top: 2rem !important;
    padding-bottom: 4rem !important;
    max-width: 1450px !important;
}}


/* ═══════════════════════════════════════════════════════════════
   BUTTONS
   ═══════════════════════════════════════════════════════════════ */

.stButton > button {{

    background: var(--glass-bg) !important;

    border: 1px solid var(--card-border) !important;

    border-radius: 14px !important;

    color: var(--text) !important;

    min-height: 45px !important;

    transition: all 0.25s ease !important;

    backdrop-filter: blur(var(--blur)) !important;
}}

.stButton > button:hover {{

    border-color: var(--primary) !important;

    transform: translateY(-2px);

    box-shadow: var(--glow), var(--shadow-md);
}}


/* ═══════════════════════════════════════════════════════════════
   INPUTS
   ═══════════════════════════════════════════════════════════════ */

.stTextInput input,
.stTextArea textarea,
.stSelectbox > div > div {{

    background: var(--glass-bg) !important;

    color: var(--text) !important;

    border: 1px solid var(--card-border) !important;

    border-radius: 14px !important;

    backdrop-filter: blur(var(--blur)) !important;
}}

.stTextInput input:focus,
.stTextArea textarea:focus {{

    border-color: var(--primary) !important;

    box-shadow: var(--focus-ring) !important;
}}


/* ═══════════════════════════════════════════════════════════════
   CARDS
   ═══════════════════════════════════════════════════════════════ */

.med-card {{

    background: var(--card-bg);

    border: 1px solid var(--card-border);

    border-radius: 24px;

    padding: 1.5rem;

    backdrop-filter: blur(var(--blur));

    transition: all 0.25s ease;
}}

.med-card:hover {{

    transform: translateY(-4px);

    border-color: var(--primary);

    box-shadow: var(--glow), var(--shadow-lg);
}}


/* ═══════════════════════════════════════════════════════════════
   METRICS
   ═══════════════════════════════════════════════════════════════ */

[data-testid="metric-container"] {{

    background: var(--card-bg) !important;

    border: 1px solid var(--card-border) !important;

    border-radius: 20px !important;

    padding: 1rem !important;

    backdrop-filter: blur(var(--blur)) !important;
}}

[data-testid="metric-container"]:hover {{

    transform: translateY(-3px);

    box-shadow: var(--shadow-md);
}}

[data-testid="stMetricValue"] {{

    color: var(--primary) !important;

    font-size: 2rem !important;

    font-weight: 800 !important;
}}


/* ═══════════════════════════════════════════════════════════════
   TABS
   ═══════════════════════════════════════════════════════════════ */

.stTabs [data-baseweb="tab-list"] {{

    background: var(--glass-bg) !important;

    border-radius: 999px !important;

    padding: 6px !important;

    border: 1px solid var(--card-border) !important;
}}

.stTabs [data-baseweb="tab"] {{

    border-radius: 999px !important;

    color: var(--text-muted) !important;
}}

.stTabs [aria-selected="true"] {{

    background: var(--gradient) !important;

    color: var(--text-inverse) !important;

    box-shadow: var(--glow);
}}


/* ═══════════════════════════════════════════════════════════════
   SCROLLBAR
   ═══════════════════════════════════════════════════════════════ */

::-webkit-scrollbar {{
    width: 5px;
}}

::-webkit-scrollbar-thumb {{

    background: var(--primary);

    border-radius: 999px;
}}


/* ═══════════════════════════════════════════════════════════════
   MOBILE
   ═══════════════════════════════════════════════════════════════ */

@media (max-width: 768px) {{

    .block-container {{
        padding: 1rem !important;
    }}

    section[data-testid="stSidebar"] {{
        width: 100% !important;
        min-width: 100% !important;
    }}
}}

</style>
"""


# ═══════════════════════════════════════════════════════════════════════
# GET CSS
# ═══════════════════════════════════════════════════════════════════════

def get_css(theme_key: str):

    return ThemeManager(theme_key).inject()


# ═══════════════════════════════════════════════════════════════════════
# THEME PREVIEW
# ═══════════════════════════════════════════════════════════════════════

def render_theme_preview(theme_key: str):

    t = THEMES.get(theme_key, {})

    return f'''
    <div style="
        display:flex;
        align-items:center;
        gap:8px;
    ">
        <div style="
            width:12px;
            height:12px;
            border-radius:50%;
            background:{t.get("primary","#fff")};
            box-shadow:0 0 10px {t.get("primary_glow","transparent")};
        "></div>

        <div style="
            width:12px;
            height:12px;
            border-radius:3px;
            background:{t.get("bg","#000")};
            border:1px solid rgba(255,255,255,0.15);
        "></div>
    </div>
    '''
