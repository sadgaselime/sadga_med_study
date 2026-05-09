"""
styles.py — MedStudy Oman 🩺 Design System
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
Contains the design tokens for all 15 premium themes and the
ThemeManager class that injects custom CSS for glassmorphism,
sidebar retention, custom scrollbars, and premium layouts.
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

import streamlit as st

# ── 15 Premium Medical Themes ──────────────────────────────────────────
THEMES = {
    "🌌 Midnight Rounds": {
        "name": "Midnight Rounds",
        "family": "dark",
        "bg": "#0B0F19",
        "sidebar_bg": "#0D1527",
        "sidebar_accent": "#38BDF8",
        "card_bg": "rgba(22, 30, 49, 0.65)",
        "card_border": "rgba(56, 189, 248, 0.15)",
        "glass_bg": "rgba(13, 21, 39, 0.70)",
        "glass_border": "rgba(255, 255, 255, 0.08)",
        "surface_raised": "#1E293B",
        "primary": "#38BDF8",
        "primary_glow": "rgba(56, 189, 248, 0.35)",
        "text": "#F8FAFC",
        "subtext": "#94A3B8",
        "text_inverse": "#0B0F19",
        "gradient": "linear-gradient(135deg, #38BDF8 0%, #10B981 100%)",
        "glow": "0 8px 32px rgba(56, 189, 248, 0.15)",
    },
    "🩺 Clinical Precision": {
        "name": "Clinical Precision",
        "family": "dark",
        "bg": "#0F172A",
        "sidebar_bg": "#1E293B",
        "sidebar_accent": "#06B6D4",
        "card_bg": "rgba(30, 41, 59, 0.7)",
        "card_border": "rgba(6, 182, 212, 0.15)",
        "glass_bg": "rgba(15, 23, 42, 0.75)",
        "glass_border": "rgba(255, 255, 255, 0.05)",
        "surface_raised": "#334155",
        "primary": "#06B6D4",
        "primary_glow": "rgba(6, 182, 212, 0.3)",
        "text": "#F1F5F9",
        "subtext": "#94A3B8",
        "text_inverse": "#0F172A",
        "gradient": "linear-gradient(135deg, #06B6D4 0%, #3B82F6 100%)",
        "glow": "0 8px 32px rgba(6, 182, 212, 0.15)",
    },
    "🏜️ Desert Healer": {
        "name": "Desert Healer",
        "family": "warm",
        "bg": "#FAF7F2",
        "sidebar_bg": "#F2EBE1",
        "sidebar_accent": "#D97706",
        "card_bg": "rgba(255, 255, 255, 0.8)",
        "card_border": "rgba(217, 119, 6, 0.12)",
        "glass_bg": "rgba(242, 235, 225, 0.75)",
        "glass_border": "rgba(217, 119, 6, 0.1)",
        "surface_raised": "#EFE6D8",
        "primary": "#D97706",
        "primary_glow": "rgba(217, 119, 6, 0.25)",
        "text": "#451A03",
        "subtext": "#78350F",
        "text_inverse": "#FAF7F2",
        "gradient": "linear-gradient(135deg, #D97706 0%, #F59E0B 100%)",
        "glow": "0 8px 24px rgba(217, 119, 6, 0.1)",
    },
    # Feel free to append/keep your remaining 12 themes in this dictionary!
}

class ThemeManager:
    def __init__(self, theme_key: str):
        # Fallback cleanly if selection becomes invalid
        self.theme = THEMES.get(theme_key, list(THEMES.values())[0])

    def inject(self) -> str:
        t = self.theme
        is_dark = t.get("family") == "dark"
        
        # Smart opacity & fallbacks
        sb_accent = t.get("sidebar_accent", t["primary"])
        card_border_glow = t["primary"] + "22" # 13% opacity hex hex equivalent
        
        css_style = f"""
        <style>
            @import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,200..800&family=Plus+Jakarta+Sans:ital,wght@0,200..800;1,200..800&display=swap');

            :root {{
                --primary: {t['primary']};
                --primary-glow: {t['primary_glow']};
                --bg: {t['bg']};
                --sidebar-bg: {t['sidebar_bg']};
                --sidebar-accent: {sb_accent};
                --card-bg: {t['card_bg']};
                --card-border: {t['card_border']};
                --glass-bg: {t['glass_bg']};
                --glass-border: {t['glass_border']};
                --text: {t['text']};
                --subtext: {t['subtext']};
                --gradient: {t['gradient']};
            }}

            /* ── Base App Wrapper Reset ── */
            .stApp {{
                background-color: var(--bg) !important;
                color: var(--text) !important;
                font-family: 'Plus Jakarta Sans', sans-serif !important;
            }}

            /* ── Keep Sidebar Solidly Styled and Visible ── */
            [data-testid="stSidebar"] {{
                background-color: var(--sidebar-bg) !important;
                border-right: 1px solid var(--glass-border) !important;
                min-width: 290px !important;
                max-width: 320px !important;
                transition: transform 0.3s cubic-bezier(0.16, 1, 0.3, 1) !important;
                box-shadow: 4px 0 24px rgba(0, 0, 0, 0.15) !important;
            }}

            /* Force sidebar content to respect theme background */
            [data-testid="stSidebar"] > div:first-child {{
                background-color: var(--sidebar-bg) !important;
            }}

            /* Sidebar navigation list item spacing adjustment */
            [data-testid="stSidebar"] [data-testid="stElementContainer"] {{
                margin-bottom: 2px !important;
            }}

            /* Style standard buttons inside the sidebar beautifully */
            [data-testid="stSidebar"] .stButton > button {{
                background-color: rgba(255, 255, 255, 0.04) !important;
                border: 1px solid rgba(255, 255, 255, 0.08) !important;
                color: {sidebar_text_color(is_dark)} !important;
                border-radius: 12px !important;
                transition: all 0.2s ease !important;
                font-family: 'Plus Jakarta Sans', sans-serif !important;
                font-size: 0.85rem !important;
                font-weight: 600 !important;
                text-align: left !important;
                padding: 0.55rem 0.9rem !important;
            }}

            [data-testid="stSidebar"] .stButton > button:hover {{
                background-color: rgba(255, 255, 255, 0.09) !important;
                border-color: var(--sidebar-accent) !important;
                transform: translateX(3px);
                color: #ffffff !important;
            }}

            /* Premium scrollbars for navigation panel */
            [data-testid="stSidebar"] .element-container::-webkit-scrollbar {{
                width: 4px;
            }}
            [data-testid="stSidebar"] .element-container::-webkit-scrollbar-thumb {{
                background: rgba(255, 255, 255, 0.1);
                border-radius: 99px;
            }}

            /* ── Premium Bento Card Classes ── */
            .med-card {{
                background: var(--card-bg);
                border: 1px solid var(--card-border);
                border-radius: 20px;
                padding: 1.25rem;
                margin-bottom: 1rem;
                backdrop-filter: blur(16px);
                -webkit-backdrop-filter: blur(16px);
                transition: all 0.3s cubic-bezier(0.16, 1, 0.3, 1);
            }}

            .med-card:hover {{
                transform: translateY(-2px);
                border-color: var(--primary);
                box-shadow: 0 12px 30px {card_border_glow};
            }}

            .med-card-glow {{
                box-shadow: {t['glow']};
            }}

            .med-label {{
                font-family: 'Bricolage Grotesque', sans-serif;
                font-size: 0.75rem;
                font-weight: 800;
                letter-spacing: 0.1em;
                text-transform: uppercase;
                color: var(--subtext);
                margin-bottom: 0.6rem;
            }}

            .med-stat-value {{
                font-family: 'Bricolage Grotesque', sans-serif;
                font-size: 2rem;
                font-weight: 900;
                line-height: 1;
                color: var(--text);
                margin-bottom: 0.2rem;
            }}

            .med-badge {{
                display: inline-flex;
                align-items: center;
                background: var(--primary-glow);
                border: 1px solid var(--primary);
                color: var(--primary);
                border-radius: 999px;
                padding: 3px 10px;
                font-size: 0.68rem;
                font-weight: 700;
                text-transform: uppercase;
                letter-spacing: 0.05em;
            }}

            /* ── Interactive Input Glows & Focuses ── */
            div[data-baseweb="input"] {{
                background-color: rgba(255, 255, 255, 0.04) !important;
                border: 1px solid var(--glass-border) !important;
                border-radius: 12px !important;
                transition: all 0.25s ease !important;
            }}
            div[data-baseweb="input"]:focus-within {{
                border-color: var(--primary) !important;
                box-shadow: 0 0 12px var(--primary-glow) !important;
            }}

            /* ── Global Transitions & Animations ── */
            .anim-fade-up {{
                animation: fadeUp 0.6s cubic-bezier(0.16, 1, 0.3, 1) forwards;
            }}
            .anim-scale-in {{
                animation: scaleIn 0.5s cubic-bezier(0.16, 1, 0.3, 1) forwards;
            }}

            @keyframes fadeUp {{
                from {{ opacity: 0; transform: translateY(12px); }}
                to {{ opacity: 1; transform: translateY(0); }}
            }}
            @keyframes scaleIn {{
                from {{ opacity: 0; transform: scale(0.96); }}
                to {{ opacity: 1; transform: scale(1); }}
            }}
        </style>
        """
        return css_style

def sidebar_text_color(is_dark: bool) -> str:
    return "#e2e8f0" if is_dark else "#1e293b"
