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
    "🌿 Herbal Remedy": {
        "name": "Herbal Remedy",
        "family": "light",
        "bg": "#F4F7F5",
        "sidebar_bg": "#E3EBE6",
        "sidebar_accent": "#10B981",
        "card_bg": "rgba(255, 255, 255, 0.85)",
        "card_border": "rgba(16, 185, 129, 0.12)",
        "glass_bg": "rgba(227, 235, 230, 0.75)",
        "glass_border": "rgba(16, 185, 129, 0.08)",
        "surface_raised": "#D5E2D9",
        "primary": "#10B981",
        "primary_glow": "rgba(16, 185, 129, 0.2)",
        "text": "#0F2D20",
        "subtext": "#1E5E42",
        "text_inverse": "#F4F7F5",
        "gradient": "linear-gradient(135deg, #10B981 0%, #059669 100%)",
        "glow": "0 8px 24px rgba(16, 185, 129, 0.08)",
    },
    "🌋 Crimson Pulse": {
        "name": "Crimson Pulse",
        "family": "dark",
        "bg": "#110708",
        "sidebar_bg": "#1C0D0E",
        "sidebar_accent": "#EF4444",
        "card_bg": "rgba(35, 17, 19, 0.65)",
        "card_border": "rgba(239, 68, 68, 0.15)",
        "glass_bg": "rgba(28, 13, 14, 0.75)",
        "glass_border": "rgba(255, 255, 255, 0.05)",
        "surface_raised": "#2D1517",
        "primary": "#EF4444",
        "primary_glow": "rgba(239, 68, 68, 0.3)",
        "text": "#FEE2E2",
        "subtext": "#FCA5A5",
        "text_inverse": "#110708",
        "gradient": "linear-gradient(135deg, #EF4444 0%, #B91C1C 100%)",
        "glow": "0 8px 32px rgba(239, 68, 68, 0.15)",
    },
    "💤 Deep Sleep": {
        "name": "Deep Sleep",
        "family": "dark",
        "bg": "#09090B",
        "sidebar_bg": "#18181B",
        "sidebar_accent": "#A78BFA",
        "card_bg": "rgba(39, 39, 42, 0.6)",
        "card_border": "rgba(167, 139, 250, 0.15)",
        "glass_bg": "rgba(24, 24, 27, 0.75)",
        "glass_border": "rgba(255, 255, 255, 0.05)",
        "surface_raised": "#27272A",
        "primary": "#A78BFA",
        "primary_glow": "rgba(167, 139, 250, 0.35)",
        "text": "#FAFAFA",
        "subtext": "#A1A1AA",
        "text_inverse": "#09090B",
        "gradient": "linear-gradient(135deg, #A78BFA 0%, #6366F1 100%)",
        "glow": "0 8px 32px rgba(167, 139, 250, 0.15)",
    },
    "🫁 Pulmonary Mist": {
        "name": "Pulmonary Mist",
        "family": "light",
        "bg": "#F0F4F8",
        "sidebar_bg": "#D9E2EC",
        "sidebar_accent": "#1982C4",
        "card_bg": "rgba(255, 255, 255, 0.85)",
        "card_border": "rgba(25, 130, 196, 0.12)",
        "glass_bg": "rgba(217, 226, 236, 0.75)",
        "glass_border": "rgba(25, 130, 196, 0.08)",
        "surface_raised": "#BCCCDC",
        "primary": "#1982C4",
        "primary_glow": "rgba(25, 130, 196, 0.2)",
        "text": "#102A43",
        "subtext": "#334E68",
        "text_inverse": "#F0F4F8",
        "gradient": "linear-gradient(135deg, #1982C4 0%, #4299E1 100%)",
        "glow": "0 8px 24px rgba(25, 130, 196, 0.08)",
    },
    "🧠 Synaptic Glow": {
        "name": "Synaptic Glow",
        "family": "dark",
        "bg": "#0D0B14",
        "sidebar_bg": "#171226",
        "sidebar_accent": "#F43F5E",
        "card_bg": "rgba(36, 28, 56, 0.65)",
        "card_border": "rgba(244, 63, 94, 0.15)",
        "glass_bg": "rgba(23, 18, 38, 0.75)",
        "glass_border": "rgba(255, 255, 255, 0.06)",
        "surface_raised": "#2A2044",
        "primary": "#F43F5E",
        "primary_glow": "rgba(244, 63, 94, 0.35)",
        "text": "#FFF1F2",
        "subtext": "#FDA4AF",
        "text_inverse": "#0D0B14",
        "gradient": "linear-gradient(135deg, #F43F5E 0%, #D946EF 100%)",
        "glow": "0 8px 32px rgba(244, 63, 94, 0.15)",
    },
    "🧪 Bio-Hazard": {
        "name": "Bio-Hazard",
        "family": "dark",
        "bg": "#090D0A",
        "sidebar_bg": "#111A13",
        "sidebar_accent": "#84CC16",
        "card_bg": "rgba(24, 38, 28, 0.65)",
        "card_border": "rgba(132, 204, 22, 0.15)",
        "glass_bg": "rgba(17, 26, 19, 0.75)",
        "glass_border": "rgba(255, 255, 255, 0.05)",
        "surface_raised": "#1D2E22",
        "primary": "#84CC16",
        "primary_glow": "rgba(132, 204, 22, 0.3)",
        "text": "#F7FEE7",
        "subtext": "#BEF264",
        "text_inverse": "#090D0A",
        "gradient": "linear-gradient(135deg, #84CC16 0%, #10B981 100%)",
        "glow": "0 8px 32px rgba(132, 204, 22, 0.15)",
    },
    "🧊 Sterile Ward": {
        "name": "Sterile Ward",
        "family": "light",
        "bg": "#F8FAFC",
        "sidebar_bg": "#F1F5F9",
        "sidebar_accent": "#64748B",
        "card_bg": "rgba(255, 255, 255, 0.9)",
        "card_border": "rgba(100, 116, 139, 0.1)",
        "glass_bg": "rgba(241, 245, 249, 0.8)",
        "glass_border": "rgba(100, 116, 139, 0.05)",
        "surface_raised": "#E2E8F0",
        "primary": "#64748B",
        "primary_glow": "rgba(100, 116, 139, 0.15)",
        "text": "#0F172A",
        "subtext": "#475569",
        "text_inverse": "#F8FAFC",
        "gradient": "linear-gradient(135deg, #64748B 0%, #475569 100%)",
        "glow": "0 8px 24px rgba(100, 116, 139, 0.05)",
    },
    "💡 Neural Path": {
        "name": "Neural Path",
        "family": "dark",
        "bg": "#030712",
        "sidebar_bg": "#111827",
        "sidebar_accent": "#F59E0B",
        "card_bg": "rgba(31, 41, 55, 0.65)",
        "card_border": "rgba(245, 158, 11, 0.15)",
        "glass_bg": "rgba(17, 24, 39, 0.75)",
        "glass_border": "rgba(255, 255, 255, 0.05)",
        "surface_raised": "#374151",
        "primary": "#F59E0B",
        "primary_glow": "rgba(245, 158, 11, 0.3)",
        "text": "#FFFBEB",
        "subtext": "#FDE68A",
        "text_inverse": "#030712",
        "gradient": "linear-gradient(135deg, #F59E0B 0%, #EF4444 100%)",
        "glow": "0 8px 32px rgba(245, 158, 11, 0.15)",
    },
    "🩺 Cardiogram": {
        "name": "Cardiogram",
        "family": "dark",
        "bg": "#0D0202",
        "sidebar_bg": "#1B0505",
        "sidebar_accent": "#FF003C",
        "card_bg": "rgba(43, 8, 8, 0.65)",
        "card_border": "rgba(255, 0, 60, 0.15)",
        "glass_bg": "rgba(27, 5, 5, 0.75)",
        "glass_border": "rgba(255, 255, 255, 0.05)",
        "surface_raised": "#3F0D0D",
        "primary": "#FF003C",
        "primary_glow": "rgba(255, 0, 60, 0.35)",
        "text": "#FFF0F2",
        "subtext": "#FFB3C1",
        "text_inverse": "#0D0202",
        "gradient": "linear-gradient(135deg, #FF003C 0%, #9B0024 100%)",
        "glow": "0 8px 32px rgba(255, 0, 60, 0.15)",
    },
    "🧬 Helix Nebula": {
        "name": "Helix Nebula",
        "family": "dark",
        "bg": "#050B14",
        "sidebar_bg": "#0F1A2D",
        "sidebar_accent": "#00F5FF",
        "card_bg": "rgba(23, 39, 66, 0.65)",
        "card_border": "rgba(0, 245, 255, 0.15)",
        "glass_bg": "rgba(15, 26, 45, 0.75)",
        "glass_border": "rgba(255, 255, 255, 0.06)",
        "surface_raised": "#1F3454",
        "primary": "#00F5FF",
        "primary_glow": "rgba(0, 245, 255, 0.35)",
        "text": "#E0FBFC",
        "subtext": "#98F5F9",
        "text_inverse": "#050B14",
        "gradient": "linear-gradient(135deg, #00F5FF 0%, #0077FF 100%)",
        "glow": "0 8px 32px rgba(0, 245, 255, 0.15)",
    },
    "🧪 Placebo": {
        "name": "Placebo",
        "family": "light",
        "bg": "#FAFAFA",
        "sidebar_bg": "#F4F4F5",
        "sidebar_accent": "#18181B",
        "card_bg": "rgba(255, 255, 255, 0.9)",
        "card_border": "rgba(24, 24, 27, 0.08)",
        "glass_bg": "rgba(244, 244, 245, 0.8)",
        "glass_border": "rgba(24, 24, 27, 0.04)",
        "surface_raised": "#E4E4E7",
        "primary": "#18181B",
        "primary_glow": "rgba(24, 24, 27, 0.15)",
        "text": "#09090B",
        "subtext": "#71717A",
        "text_inverse": "#FAFAFA",
        "gradient": "linear-gradient(135deg, #18181B 0%, #3F3F46 100%)",
        "glow": "0 8px 24px rgba(24, 24, 27, 0.04)",
    },
    "🚨 Modern ER": {
        "name": "Modern ER",
        "family": "dark",
        "bg": "#0D0E12",
        "sidebar_bg": "#151821",
        "sidebar_accent": "#FF5722",
        "card_bg": "rgba(33, 37, 50, 0.65)",
        "card_border": "rgba(255, 87, 34, 0.15)",
        "glass_bg": "rgba(21, 24, 33, 0.75)",
        "glass_border": "rgba(255, 255, 255, 0.05)",
        "surface_raised": "#2D3244",
        "primary": "#FF5722",
        "primary_glow": "rgba(255, 87, 34, 0.35)",
        "text": "#FDF2EE",
        "subtext": "#FFCCBC",
        "text_inverse": "#0D0E12",
        "gradient": "linear-gradient(135deg, #FF5722 0%, #E64A19 100%)",
        "glow": "0 8px 32px rgba(255, 87, 34, 0.15)",
    }
}

class ThemeManager:
    def __init__(self, theme_key: str):
        # Fallback cleanly if an invalid key is ever passed
        self.theme = THEMES.get(theme_key, list(THEMES.values())[0])

    def inject(self) -> str:
        t = self.theme
        is_dark = t.get("family") == "dark"
        sb_accent = t.get("sidebar_accent", t["primary"])
        card_border_glow = t["primary"] + "22"  # ~13% opacity hex
        sb_text = "#e2e8f0" if is_dark else "#1e293b"
        
        # Using double braces {{ }} throughout to safely compile CSS inside python f-strings
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

            /* ── Keep Sidebar Solidly Styled and Visible (Stops Flashing/Hiding) ── */
            [data-testid="stSidebar"], 
            section[data-testid="stSidebar"], 
            div[data-testid="stSidebarCollapsedControl"] + section {{
                background-color: var(--sidebar-bg) !important;
                border-right: 1px solid var(--glass-border) !important;
                min-width: 290px !important;
                max-width: 320px !important;
                width: 290px !important;
                transform: none !important; /* Forces the sidebar to stay on screen */
                transition: none !important; /* Prevents sidebar slide animations on page reload */
                box-shadow: 4px 0 24px rgba(0, 0, 0, 0.15) !important;
                visibility: visible !important; /* Guarantees the sidebar is visible */
                display: flex !important;
            }}

            /* Forces internal container elements to respect the background color */
            [data-testid="stSidebar"] > div:first-child,
            [data-testid="stSidebar"] [data-testid="stSidebarUserContent"] {{
                background-color: var(--sidebar-bg) !important;
                background-image: none !important;
            }}

            /* Sidebar navigation list item spacing adjustment */
            [data-testid="stSidebar"] [data-testid="stElementContainer"] {{
                margin-bottom: 2px !important;
            }}

            /* Style standard buttons inside the sidebar beautifully */
            [data-testid="stSidebar"] .stButton > button {{
                background-color: rgba(255, 255, 255, 0.04) !important;
                border: 1px solid rgba(255, 255, 255, 0.08) !important;
                color: {sb_text} !important;
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
