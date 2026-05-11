"""
styles.py — MedStudy Oman 🩺
Phase 1: Dynamic ThemeManager Engine
4 Themes: Clinical Snow · Deep Surgeon · Oasis Health · Cyber-Med
"""

# ─────────────────────────────────────────────────────────────────────────────
# THEME DEFINITIONS — CSS Variable Maps
# ─────────────────────────────────────────────────────────────────────────────

THEMES = {

    # ── 1. CLINICAL SNOW — Crisp white, surgical red, deep navy ──────────────
    "🩺 Clinical Snow": {
        "name":           "Clinical Snow",
        "family":         "light",
        "primary":        "#c8102e",          # NHS red — bold, clinical
        "primary_glow":   "rgba(200,16,46,0.22)",
        "secondary":      "#003087",           # deep royal blue
        "accent":         "#005eb8",
        "bg":             "#f4f6f9",
        "surface":        "#ffffff",
        "surface_raised": "#edf0f5",
        "card_bg":        "rgba(255,255,255,0.88)",
        "card_border":    "rgba(200,210,228,0.85)",
        "sidebar_bg":     "rgba(244,246,249,0.97)",
        "glass_bg":       "rgba(255,255,255,0.70)",
        "glass_border":   "rgba(255,255,255,0.95)",
        "glass_blur":     "20px",
        "text":           "#0d1117",
        "text_muted":     "#4a5568",
        "subtext":        "#718096",
        "text_inverse":   "#ffffff",
        "gradient":       "linear-gradient(135deg,#c8102e 0%,#003087 100%)",
        "hero_gradient":  "linear-gradient(160deg,#f4f6f9 0%,#eaf0fb 60%,#e2eaf8 100%)",
        "card_gradient":  "linear-gradient(145deg,rgba(255,255,255,0.95),rgba(237,240,245,0.75))",
        "glow":           "0 0 24px rgba(200,16,46,0.18), 0 0 64px rgba(200,16,46,0.07)",
        "shadow_sm":      "0 2px 8px rgba(13,17,23,0.07)",
        "shadow_md":      "0 8px 32px rgba(13,17,23,0.11)",
        "shadow_lg":      "0 20px 60px rgba(13,17,23,0.16)",
        "hover_bg":       "rgba(200,16,46,0.06)",
        "focus_ring":     "0 0 0 3px rgba(200,16,46,0.28)",
        "success":        "#15803d",
        "warning":        "#b45309",
        "error":          "#c8102e",
        "info":           "#0369a1",
        "chart_1": "#c8102e", "chart_2": "#003087",
        "chart_3": "#15803d", "chart_4": "#b45309",
    },

    # ── 2. DEEP SURGEON — Midnight navy, electric cyan, ICU monitor feel ─────
    "🌑 Deep Surgeon": {
        "name":           "Deep Surgeon",
        "family":         "dark",
        "primary":        "#00e5ff",           # electric cyan — monitor glow
        "primary_glow":   "rgba(0,229,255,0.28)",
        "secondary":      "#00b8d4",
        "accent":         "#006064",
        "bg":             "#080d1a",
        "surface":        "#0f1829",
        "surface_raised": "#162035",
        "card_bg":        "rgba(15,24,41,0.85)",
        "card_border":    "rgba(0,229,255,0.13)",
        "sidebar_bg":     "rgba(8,13,26,0.98)",
        "glass_bg":       "rgba(0,229,255,0.04)",
        "glass_border":   "rgba(0,229,255,0.18)",
        "glass_blur":     "24px",
        "text":           "#ddf4ff",
        "text_muted":     "#7db8cc",
        "subtext":        "#4a7a90",
        "text_inverse":   "#080d1a",
        "gradient":       "linear-gradient(135deg,#00e5ff 0%,#0050ef 100%)",
        "hero_gradient":  "linear-gradient(160deg,#080d1a 0%,#0c1530 55%,#080d20 100%)",
        "card_gradient":  "linear-gradient(145deg,rgba(0,229,255,0.07),rgba(0,80,239,0.04))",
        "glow":           "0 0 36px rgba(0,229,255,0.28), 0 0 90px rgba(0,229,255,0.09)",
        "shadow_sm":      "0 2px 8px rgba(0,0,0,0.45)",
        "shadow_md":      "0 8px 32px rgba(0,0,0,0.55)",
        "shadow_lg":      "0 20px 60px rgba(0,0,0,0.65)",
        "hover_bg":       "rgba(0,229,255,0.07)",
        "focus_ring":     "0 0 0 3px rgba(0,229,255,0.32)",
        "success":        "#00e676",
        "warning":        "#ffd740",
        "error":          "#ff5252",
        "info":           "#40c4ff",
        "chart_1": "#00e5ff", "chart_2": "#7c4dff",
        "chart_3": "#00e676", "chart_4": "#ffd740",
    },

    # ── 3. OASIS HEALTH — Oman-inspired: deep teal, warm gold, desert sand ──
    "🌿 Oasis Health": {
        "name":           "Oasis Health",
        "family":         "warm",
        "primary":        "#00695c",           # deep Omani teal
        "primary_glow":   "rgba(0,105,92,0.24)",
        "secondary":      "#e6a817",           # desert gold
        "accent":         "#bf360c",           # terracotta
        "bg":             "#f9f5ee",
        "surface":        "#ffffff",
        "surface_raised": "#f3ede1",
        "card_bg":        "rgba(255,252,242,0.90)",
        "card_border":    "rgba(180,145,60,0.28)",
        "sidebar_bg":     "rgba(249,245,238,0.97)",
        "glass_bg":       "rgba(255,252,242,0.72)",
        "glass_border":   "rgba(230,168,23,0.36)",
        "glass_blur":     "18px",
        "text":           "#1a2418",
        "text_muted":     "#3d5239",
        "subtext":        "#6b7d65",
        "text_inverse":   "#ffffff",
        "gradient":       "linear-gradient(135deg,#00695c 0%,#e6a817 100%)",
        "hero_gradient":  "linear-gradient(160deg,#f9f5ee 0%,#f3ede1 55%,#ede5d3 100%)",
        "card_gradient":  "linear-gradient(145deg,rgba(255,252,242,0.96),rgba(243,237,225,0.82))",
        "glow":           "0 0 24px rgba(0,105,92,0.20), 0 0 64px rgba(230,168,23,0.12)",
        "shadow_sm":      "0 2px 8px rgba(26,36,24,0.09)",
        "shadow_md":      "0 8px 32px rgba(26,36,24,0.13)",
        "shadow_lg":      "0 20px 60px rgba(26,36,24,0.18)",
        "hover_bg":       "rgba(0,105,92,0.07)",
        "focus_ring":     "0 0 0 3px rgba(0,105,92,0.28)",
        "success":        "#00695c",
        "warning":        "#e6a817",
        "error":          "#bf360c",
        "info":           "#1565c0",
        "chart_1": "#00695c", "chart_2": "#e6a817",
        "chart_3": "#bf360c", "chart_4": "#4caf50",
    },

    # ── 4. CYBER-MED — Absolute black, vivid violet, neon, glassmorphism ─────
    "⚡ Cyber-Med": {
        "name":           "Cyber-Med",
        "family":         "dark",
        "primary":        "#b84aff",           # vivid violet
        "primary_glow":   "rgba(184,74,255,0.32)",
        "secondary":      "#ff2d78",           # neon pink accent
        "accent":         "#5a00cc",
        "bg":             "#030006",
        "surface":        "#0a000f",
        "surface_raised": "#120018",
        "card_bg":        "rgba(10,0,15,0.80)",
        "card_border":    "rgba(184,74,255,0.18)",
        "sidebar_bg":     "rgba(3,0,6,0.99)",
        "glass_bg":       "rgba(184,74,255,0.055)",
        "glass_border":   "rgba(184,74,255,0.22)",
        "glass_blur":     "32px",
        "text":           "#f3e8ff",
        "text_muted":     "#a87dcc",
        "subtext":        "#6d4a90",
        "text_inverse":   "#030006",
        "gradient":       "linear-gradient(135deg,#b84aff 0%,#ff2d78 100%)",
        "hero_gradient":  "linear-gradient(160deg,#030006 0%,#0c0018 55%,#060010 100%)",
        "card_gradient":  "linear-gradient(145deg,rgba(184,74,255,0.09),rgba(255,45,120,0.04))",
        "glow":           "0 0 40px rgba(184,74,255,0.32), 0 0 100px rgba(184,74,255,0.10)",
        "shadow_sm":      "0 2px 8px rgba(0,0,0,0.65)",
        "shadow_md":      "0 8px 32px rgba(0,0,0,0.72)",
        "shadow_lg":      "0 20px 60px rgba(0,0,0,0.82)",
        "hover_bg":       "rgba(184,74,255,0.09)",
        "focus_ring":     "0 0 0 3px rgba(184,74,255,0.38)",
        "success":        "#39ff7c",
        "warning":        "#ffe03a",
        "error":          "#ff3a5e",
        "info":           "#38d9ff",
        "chart_1": "#b84aff", "chart_2": "#ff2d78",
        "chart_3": "#39ff7c", "chart_4": "#ffe03a",
    },

    "🏥 Hospital White": {
        "name":"Hospital White","family":"light",
        "primary":"#005eb8","primary_glow":"rgba(0,94,184,0.20)",
        "secondary":"#00a86b","accent":"#0041a8",
        "bg":"#ffffff","surface":"#ffffff","surface_raised":"#f5f7fa",
        "card_bg":"rgba(255,255,255,0.95)","card_border":"rgba(200,210,230,0.80)",
        "sidebar_bg":"rgba(250,252,255,0.98)",
        "glass_bg":"rgba(255,255,255,0.80)","glass_border":"rgba(220,230,245,0.90)","glass_blur":"16px",
        "text":"#0d1b2a","text_muted":"#3a4a5c","subtext":"#6b7a8d","text_inverse":"#ffffff",
        "gradient":"linear-gradient(135deg,#005eb8,#00a86b)",
        "hero_gradient":"linear-gradient(160deg,#ffffff 0%,#f0f5ff 50%,#e8f2ff 100%)",
        "card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.98),rgba(240,245,255,0.85))",
        "glow":"0 0 24px rgba(0,94,184,0.16)","shadow_sm":"0 1px 6px rgba(13,27,42,0.08)",
        "shadow_md":"0 4px 24px rgba(13,27,42,0.10)","shadow_lg":"0 12px 48px rgba(13,27,42,0.14)",
        "hover_bg":"rgba(0,94,184,0.05)","focus_ring":"0 0 0 3px rgba(0,94,184,0.25)",
        "success":"#00a86b","warning":"#f59e0b","error":"#dc2626","info":"#0066cc",
        "chart_1":"#005eb8","chart_2":"#00a86b","chart_3":"#f59e0b","chart_4":"#dc2626",
    },
    "🚨 Code Red": {
        "name":"Code Red","family":"dark",
        "primary":"#ff3333","primary_glow":"rgba(255,51,51,0.32)",
        "secondary":"#ff6b35","accent":"#8b0000",
        "bg":"#0d0000","surface":"#1a0000","surface_raised":"#250000",
        "card_bg":"rgba(26,0,0,0.88)","card_border":"rgba(255,51,51,0.18)",
        "sidebar_bg":"rgba(13,0,0,0.98)",
        "glass_bg":"rgba(255,51,51,0.06)","glass_border":"rgba(255,51,51,0.22)","glass_blur":"20px",
        "text":"#ffe8e8","text_muted":"#cc9999","subtext":"#886666","text_inverse":"#0d0000",
        "gradient":"linear-gradient(135deg,#ff3333,#ff6b35)",
        "hero_gradient":"linear-gradient(160deg,#0d0000 0%,#1a0500 50%,#0d0000 100%)",
        "card_gradient":"linear-gradient(145deg,rgba(255,51,51,0.10),rgba(139,0,0,0.06))",
        "glow":"0 0 40px rgba(255,51,51,0.30)","shadow_sm":"0 2px 8px rgba(0,0,0,0.55)",
        "shadow_md":"0 8px 32px rgba(0,0,0,0.65)","shadow_lg":"0 20px 60px rgba(0,0,0,0.75)",
        "hover_bg":"rgba(255,51,51,0.09)","focus_ring":"0 0 0 3px rgba(255,51,51,0.35)",
        "success":"#00ff88","warning":"#ffd700","error":"#ff3333","info":"#ff6b35",
        "chart_1":"#ff3333","chart_2":"#ff6b35","chart_3":"#ffd700","chart_4":"#00ff88",
    },
    "💚 OR Suite": {
        "name":"OR Suite","family":"light",
        "primary":"#1a6b3c","primary_glow":"rgba(26,107,60,0.22)",
        "secondary":"#2e8b57","accent":"#0d4a2a",
        "bg":"#f0f7f2","surface":"#ffffff","surface_raised":"#e8f5ec",
        "card_bg":"rgba(255,255,255,0.90)","card_border":"rgba(46,139,87,0.25)",
        "sidebar_bg":"rgba(240,247,242,0.98)",
        "glass_bg":"rgba(240,247,242,0.75)","glass_border":"rgba(46,139,87,0.35)","glass_blur":"18px",
        "text":"#0d2e1a","text_muted":"#2d5a3d","subtext":"#5a8c6a","text_inverse":"#ffffff",
        "gradient":"linear-gradient(135deg,#1a6b3c,#2e8b57)",
        "hero_gradient":"linear-gradient(160deg,#f0f7f2 0%,#e0f0e6 50%,#d4ead9 100%)",
        "card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.95),rgba(232,245,236,0.85))",
        "glow":"0 0 24px rgba(26,107,60,0.20)","shadow_sm":"0 2px 8px rgba(13,46,26,0.08)",
        "shadow_md":"0 8px 28px rgba(13,46,26,0.12)","shadow_lg":"0 16px 52px rgba(13,46,26,0.16)",
        "hover_bg":"rgba(26,107,60,0.06)","focus_ring":"0 0 0 3px rgba(26,107,60,0.28)",
        "success":"#1a6b3c","warning":"#d97706","error":"#c0392b","info":"#0077b6",
        "chart_1":"#1a6b3c","chart_2":"#2e8b57","chart_3":"#d97706","chart_4":"#0077b6",
    },
    "🌊 ICU Blue": {
        "name":"ICU Blue","family":"light",
        "primary":"#1d4ed8","primary_glow":"rgba(29,78,216,0.22)",
        "secondary":"#0ea5e9","accent":"#0c3474",
        "bg":"#f0f4ff","surface":"#ffffff","surface_raised":"#e8efff",
        "card_bg":"rgba(255,255,255,0.90)","card_border":"rgba(29,78,216,0.20)",
        "sidebar_bg":"rgba(240,244,255,0.98)",
        "glass_bg":"rgba(255,255,255,0.72)","glass_border":"rgba(29,78,216,0.28)","glass_blur":"18px",
        "text":"#0c1445","text_muted":"#2c4a8c","subtext":"#5470b0","text_inverse":"#ffffff",
        "gradient":"linear-gradient(135deg,#1d4ed8,#0ea5e9)",
        "hero_gradient":"linear-gradient(160deg,#f0f4ff 0%,#dde8ff 50%,#d0e2ff 100%)",
        "card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.95),rgba(221,232,255,0.85))",
        "glow":"0 0 24px rgba(29,78,216,0.20)","shadow_sm":"0 2px 8px rgba(12,20,69,0.08)",
        "shadow_md":"0 8px 28px rgba(12,20,69,0.12)","shadow_lg":"0 16px 52px rgba(12,20,69,0.16)",
        "hover_bg":"rgba(29,78,216,0.06)","focus_ring":"0 0 0 3px rgba(29,78,216,0.28)",
        "success":"#059669","warning":"#d97706","error":"#dc2626","info":"#0ea5e9",
        "chart_1":"#1d4ed8","chart_2":"#0ea5e9","chart_3":"#059669","chart_4":"#f59e0b",
    },
    "🌸 Paediatric Ward": {
        "name":"Paediatric Ward","family":"light",
        "primary":"#e91e8c","primary_glow":"rgba(233,30,140,0.22)",
        "secondary":"#ff9a3c","accent":"#9c1060",
        "bg":"#fff5f8","surface":"#ffffff","surface_raised":"#ffedf4",
        "card_bg":"rgba(255,255,255,0.90)","card_border":"rgba(233,30,140,0.20)",
        "sidebar_bg":"rgba(255,245,248,0.98)",
        "glass_bg":"rgba(255,255,255,0.72)","glass_border":"rgba(233,30,140,0.28)","glass_blur":"16px",
        "text":"#2a0a18","text_muted":"#7a2a50","subtext":"#aa6080","text_inverse":"#ffffff",
        "gradient":"linear-gradient(135deg,#e91e8c,#ff9a3c)",
        "hero_gradient":"linear-gradient(160deg,#fff5f8 0%,#ffe0ed 50%,#ffd6e7 100%)",
        "card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.96),rgba(255,224,237,0.85))",
        "glow":"0 0 24px rgba(233,30,140,0.22)","shadow_sm":"0 2px 8px rgba(42,10,24,0.08)",
        "shadow_md":"0 8px 28px rgba(42,10,24,0.12)","shadow_lg":"0 16px 52px rgba(42,10,24,0.16)",
        "hover_bg":"rgba(233,30,140,0.06)","focus_ring":"0 0 0 3px rgba(233,30,140,0.28)",
        "success":"#10b981","warning":"#f59e0b","error":"#ef4444","info":"#6366f1",
        "chart_1":"#e91e8c","chart_2":"#ff9a3c","chart_3":"#10b981","chart_4":"#6366f1",
    },
    "📟 ECG Monitor": {
        "name":"ECG Monitor","family":"dark",
        "primary":"#00ff41","primary_glow":"rgba(0,255,65,0.30)",
        "secondary":"#00cc33","accent":"#005c14",
        "bg":"#000a00","surface":"#001400","surface_raised":"#001e00",
        "card_bg":"rgba(0,20,0,0.88)","card_border":"rgba(0,255,65,0.15)",
        "sidebar_bg":"rgba(0,10,0,0.98)",
        "glass_bg":"rgba(0,255,65,0.04)","glass_border":"rgba(0,255,65,0.18)","glass_blur":"20px",
        "text":"#ccffcc","text_muted":"#66cc66","subtext":"#33883a","text_inverse":"#000a00",
        "gradient":"linear-gradient(135deg,#00ff41,#00cc33)",
        "hero_gradient":"linear-gradient(160deg,#000a00 0%,#001800 50%,#000a00 100%)",
        "card_gradient":"linear-gradient(145deg,rgba(0,255,65,0.06),rgba(0,204,51,0.03))",
        "glow":"0 0 40px rgba(0,255,65,0.28)","shadow_sm":"0 2px 8px rgba(0,0,0,0.55)",
        "shadow_md":"0 8px 32px rgba(0,0,0,0.65)","shadow_lg":"0 20px 60px rgba(0,0,0,0.75)",
        "hover_bg":"rgba(0,255,65,0.07)","focus_ring":"0 0 0 3px rgba(0,255,65,0.35)",
        "success":"#00ff41","warning":"#ccff00","error":"#ff4141","info":"#00ccff",
        "chart_1":"#00ff41","chart_2":"#ccff00","chart_3":"#00ccff","chart_4":"#ff9900",
    },
    "🔬 Lab Dark": {
        "name":"Lab Dark","family":"dark",
        "primary":"#7c3aff","primary_glow":"rgba(124,58,255,0.30)",
        "secondary":"#00d4ff","accent":"#4a00cc",
        "bg":"#050510","surface":"#0a0a1e","surface_raised":"#0f0f28",
        "card_bg":"rgba(10,10,30,0.88)","card_border":"rgba(124,58,255,0.18)",
        "sidebar_bg":"rgba(5,5,16,0.99)",
        "glass_bg":"rgba(124,58,255,0.05)","glass_border":"rgba(124,58,255,0.20)","glass_blur":"24px",
        "text":"#e8e0ff","text_muted":"#9988cc","subtext":"#665588","text_inverse":"#050510",
        "gradient":"linear-gradient(135deg,#7c3aff,#00d4ff)",
        "hero_gradient":"linear-gradient(160deg,#050510 0%,#0a0820 50%,#050510 100%)",
        "card_gradient":"linear-gradient(145deg,rgba(124,58,255,0.08),rgba(0,212,255,0.04))",
        "glow":"0 0 36px rgba(124,58,255,0.28)","shadow_sm":"0 2px 8px rgba(0,0,0,0.55)",
        "shadow_md":"0 8px 32px rgba(0,0,0,0.65)","shadow_lg":"0 20px 60px rgba(0,0,0,0.75)",
        "hover_bg":"rgba(124,58,255,0.08)","focus_ring":"0 0 0 3px rgba(124,58,255,0.35)",
        "success":"#00ff88","warning":"#ffcc00","error":"#ff4466","info":"#00d4ff",
        "chart_1":"#7c3aff","chart_2":"#00d4ff","chart_3":"#00ff88","chart_4":"#ffcc00",
    },
    "🎓 Ivory Hall": {
        "name":"Ivory Hall","family":"light",
        "primary":"#8b5e0a","primary_glow":"rgba(139,94,10,0.22)",
        "secondary":"#2c4a7c","accent":"#5c3a00",
        "bg":"#fafaf0","surface":"#ffffff","surface_raised":"#f5f5e8",
        "card_bg":"rgba(255,255,248,0.90)","card_border":"rgba(139,94,10,0.22)",
        "sidebar_bg":"rgba(250,250,240,0.98)",
        "glass_bg":"rgba(255,255,248,0.75)","glass_border":"rgba(139,94,10,0.32)","glass_blur":"16px",
        "text":"#1a1408","text_muted":"#4a3a18","subtext":"#7a6840","text_inverse":"#ffffff",
        "gradient":"linear-gradient(135deg,#8b5e0a,#2c4a7c)",
        "hero_gradient":"linear-gradient(160deg,#fafaf0 0%,#f5f0d8 50%,#ede8cc 100%)",
        "card_gradient":"linear-gradient(145deg,rgba(255,255,248,0.96),rgba(245,240,216,0.85))",
        "glow":"0 0 24px rgba(139,94,10,0.20)","shadow_sm":"0 2px 8px rgba(26,20,8,0.10)",
        "shadow_md":"0 8px 28px rgba(26,20,8,0.14)","shadow_lg":"0 16px 52px rgba(26,20,8,0.18)",
        "hover_bg":"rgba(139,94,10,0.06)","focus_ring":"0 0 0 3px rgba(139,94,10,0.28)",
        "success":"#2d6a2d","warning":"#c87941","error":"#c0392b","info":"#2c4a7c",
        "chart_1":"#8b5e0a","chart_2":"#2c4a7c","chart_3":"#2d6a2d","chart_4":"#c87941",
    },
    "🏛️ Royal College": {
        "name":"Royal College","family":"dark",
        "primary":"#ffd700","primary_glow":"rgba(255,215,0,0.28)",
        "secondary":"#c0a000","accent":"#806800",
        "bg":"#050510","surface":"#080820","surface_raised":"#0c0c2a",
        "card_bg":"rgba(8,8,32,0.88)","card_border":"rgba(255,215,0,0.16)",
        "sidebar_bg":"rgba(5,5,16,0.99)",
        "glass_bg":"rgba(255,215,0,0.04)","glass_border":"rgba(255,215,0,0.20)","glass_blur":"22px",
        "text":"#fff8e0","text_muted":"#cca820","subtext":"#886c00","text_inverse":"#050510",
        "gradient":"linear-gradient(135deg,#ffd700,#c0a000)",
        "hero_gradient":"linear-gradient(160deg,#050510 0%,#0a0820 50%,#05050a 100%)",
        "card_gradient":"linear-gradient(145deg,rgba(255,215,0,0.07),rgba(192,160,0,0.03))",
        "glow":"0 0 40px rgba(255,215,0,0.26)","shadow_sm":"0 2px 8px rgba(0,0,0,0.55)",
        "shadow_md":"0 8px 32px rgba(0,0,0,0.65)","shadow_lg":"0 20px 60px rgba(0,0,0,0.75)",
        "hover_bg":"rgba(255,215,0,0.07)","focus_ring":"0 0 0 3px rgba(255,215,0,0.32)",
        "success":"#00e676","warning":"#ffd700","error":"#ff5252","info":"#40c4ff",
        "chart_1":"#ffd700","chart_2":"#40c4ff","chart_3":"#00e676","chart_4":"#ff5252",
    },
    "🌅 Desert Gold": {
        "name":"Desert Gold","family":"warm",
        "primary":"#c9861a","primary_glow":"rgba(201,134,26,0.25)",
        "secondary":"#8b4513","accent":"#6b3000",
        "bg":"#fdf6e3","surface":"#ffffff","surface_raised":"#f8edd0",
        "card_bg":"rgba(255,252,240,0.90)","card_border":"rgba(201,134,26,0.28)",
        "sidebar_bg":"rgba(253,246,227,0.98)",
        "glass_bg":"rgba(255,252,240,0.72)","glass_border":"rgba(201,134,26,0.36)","glass_blur":"18px",
        "text":"#2a1800","text_muted":"#6a4010","subtext":"#9a7040","text_inverse":"#ffffff",
        "gradient":"linear-gradient(135deg,#c9861a,#8b4513)",
        "hero_gradient":"linear-gradient(160deg,#fdf6e3 0%,#f8edd0 50%,#f2e2b4 100%)",
        "card_gradient":"linear-gradient(145deg,rgba(255,252,240,0.96),rgba(248,237,208,0.85))",
        "glow":"0 0 24px rgba(201,134,26,0.24)","shadow_sm":"0 2px 8px rgba(42,24,0,0.10)",
        "shadow_md":"0 8px 28px rgba(42,24,0,0.14)","shadow_lg":"0 16px 52px rgba(42,24,0,0.18)",
        "hover_bg":"rgba(201,134,26,0.07)","focus_ring":"0 0 0 3px rgba(201,134,26,0.30)",
        "success":"#2d6a2d","warning":"#c9861a","error":"#c0392b","info":"#2563eb",
        "chart_1":"#c9861a","chart_2":"#8b4513","chart_3":"#2d6a2d","chart_4":"#2563eb",
    },
    "🌙 Night Shift": {
        "name":"Night Shift","family":"dark",
        "primary":"#4facfe","primary_glow":"rgba(79,172,254,0.28)",
        "secondary":"#00f2fe","accent":"#0044aa",
        "bg":"#000814","surface":"#001020","surface_raised":"#001828",
        "card_bg":"rgba(0,16,32,0.88)","card_border":"rgba(79,172,254,0.16)",
        "sidebar_bg":"rgba(0,8,20,0.99)",
        "glass_bg":"rgba(79,172,254,0.05)","glass_border":"rgba(79,172,254,0.20)","glass_blur":"22px",
        "text":"#ddeeff","text_muted":"#7799cc","subtext":"#446688","text_inverse":"#000814",
        "gradient":"linear-gradient(135deg,#4facfe,#00f2fe)",
        "hero_gradient":"linear-gradient(160deg,#000814 0%,#001428 50%,#000814 100%)",
        "card_gradient":"linear-gradient(145deg,rgba(79,172,254,0.08),rgba(0,242,254,0.04))",
        "glow":"0 0 36px rgba(79,172,254,0.26)","shadow_sm":"0 2px 8px rgba(0,0,0,0.55)",
        "shadow_md":"0 8px 32px rgba(0,0,0,0.65)","shadow_lg":"0 20px 60px rgba(0,0,0,0.75)",
        "hover_bg":"rgba(79,172,254,0.08)","focus_ring":"0 0 0 3px rgba(79,172,254,0.32)",
        "success":"#00e676","warning":"#ffd740","error":"#ff5252","info":"#00f2fe",
        "chart_1":"#4facfe","chart_2":"#00f2fe","chart_3":"#00e676","chart_4":"#ffd740",
    },
    "🌿 Botanic Heal": {
        "name":"Botanic Heal","family":"light",
        "primary":"#2d6a2d","primary_glow":"rgba(45,106,45,0.22)",
        "secondary":"#8bc34a","accent":"#1a4020",
        "bg":"#f1f8f0","surface":"#ffffff","surface_raised":"#e4f4e2",
        "card_bg":"rgba(255,255,255,0.90)","card_border":"rgba(45,106,45,0.22)",
        "sidebar_bg":"rgba(241,248,240,0.98)",
        "glass_bg":"rgba(241,248,240,0.75)","glass_border":"rgba(139,195,74,0.35)","glass_blur":"16px",
        "text":"#0d2010","text_muted":"#2d522d","subtext":"#5a845a","text_inverse":"#ffffff",
        "gradient":"linear-gradient(135deg,#2d6a2d,#8bc34a)",
        "hero_gradient":"linear-gradient(160deg,#f1f8f0 0%,#e0f0dc 50%,#d0e8cc 100%)",
        "card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.96),rgba(228,244,226,0.85))",
        "glow":"0 0 24px rgba(45,106,45,0.20)","shadow_sm":"0 2px 8px rgba(13,32,16,0.09)",
        "shadow_md":"0 8px 28px rgba(13,32,16,0.13)","shadow_lg":"0 16px 52px rgba(13,32,16,0.17)",
        "hover_bg":"rgba(45,106,45,0.06)","focus_ring":"0 0 0 3px rgba(45,106,45,0.28)",
        "success":"#2d6a2d","warning":"#f59e0b","error":"#c0392b","info":"#0277bd",
        "chart_1":"#2d6a2d","chart_2":"#8bc34a","chart_3":"#f59e0b","chart_4":"#0277bd",
    },
    "🫀 Cardiac Arrest": {
        "name":"Cardiac Arrest","family":"dark",
        "primary":"#ff2d55","primary_glow":"rgba(255,45,85,0.35)",
        "secondary":"#ff9f0a","accent":"#8b0030",
        "bg":"#08000a","surface":"#100015","surface_raised":"#180020",
        "card_bg":"rgba(16,0,21,0.88)","card_border":"rgba(255,45,85,0.20)",
        "sidebar_bg":"rgba(8,0,10,0.99)",
        "glass_bg":"rgba(255,45,85,0.06)","glass_border":"rgba(255,45,85,0.24)","glass_blur":"22px",
        "text":"#ffe8ec","text_muted":"#cc7788","subtext":"#884455","text_inverse":"#08000a",
        "gradient":"linear-gradient(135deg,#ff2d55,#ff9f0a)",
        "hero_gradient":"linear-gradient(160deg,#08000a 0%,#14000a 50%,#08000a 100%)",
        "card_gradient":"linear-gradient(145deg,rgba(255,45,85,0.09),rgba(255,159,10,0.04))",
        "glow":"0 0 44px rgba(255,45,85,0.32)","shadow_sm":"0 2px 8px rgba(0,0,0,0.60)",
        "shadow_md":"0 8px 32px rgba(0,0,0,0.70)","shadow_lg":"0 20px 60px rgba(0,0,0,0.80)",
        "hover_bg":"rgba(255,45,85,0.09)","focus_ring":"0 0 0 3px rgba(255,45,85,0.38)",
        "success":"#30d158","warning":"#ff9f0a","error":"#ff2d55","info":"#64d2ff",
        "chart_1":"#ff2d55","chart_2":"#ff9f0a","chart_3":"#30d158","chart_4":"#64d2ff",
    },
    "🩻 Radiology": {
        "name":"Radiology","family":"dark",
        "primary":"#ddeeff","primary_glow":"rgba(221,238,255,0.20)",
        "secondary":"#90a8c0","accent":"#506070",
        "bg":"#000000","surface":"#050505","surface_raised":"#0a0a0a",
        "card_bg":"rgba(5,5,5,0.88)","card_border":"rgba(221,238,255,0.14)",
        "sidebar_bg":"rgba(0,0,0,0.99)",
        "glass_bg":"rgba(221,238,255,0.04)","glass_border":"rgba(221,238,255,0.16)","glass_blur":"20px",
        "text":"#ddeeff","text_muted":"#8899aa","subtext":"#445566","text_inverse":"#000000",
        "gradient":"linear-gradient(135deg,#ddeeff,#90a8c0)",
        "hero_gradient":"linear-gradient(160deg,#000000 0%,#050a10 50%,#000000 100%)",
        "card_gradient":"linear-gradient(145deg,rgba(221,238,255,0.06),rgba(144,168,192,0.03))",
        "glow":"0 0 30px rgba(221,238,255,0.18)","shadow_sm":"0 2px 8px rgba(0,0,0,0.70)",
        "shadow_md":"0 8px 32px rgba(0,0,0,0.80)","shadow_lg":"0 20px 60px rgba(0,0,0,0.90)",
        "hover_bg":"rgba(221,238,255,0.06)","focus_ring":"0 0 0 3px rgba(221,238,255,0.25)",
        "success":"#30d158","warning":"#ffd60a","error":"#ff453a","info":"#64d2ff",
        "chart_1":"#ddeeff","chart_2":"#64d2ff","chart_3":"#30d158","chart_4":"#ffd60a",
    },
    "🎨 Soft Rounds": {
        "name":"Soft Rounds","family":"light",
        "primary":"#f06a35","primary_glow":"rgba(240,106,53,0.22)",
        "secondary":"#7c4dff","accent":"#b03800",
        "bg":"#fef9f5","surface":"#ffffff","surface_raised":"#fdeee6",
        "card_bg":"rgba(255,255,255,0.90)","card_border":"rgba(240,106,53,0.22)",
        "sidebar_bg":"rgba(254,249,245,0.98)",
        "glass_bg":"rgba(255,255,255,0.75)","glass_border":"rgba(240,106,53,0.30)","glass_blur":"16px",
        "text":"#2a1008","text_muted":"#6a3a20","subtext":"#9a6a50","text_inverse":"#ffffff",
        "gradient":"linear-gradient(135deg,#f06a35,#7c4dff)",
        "hero_gradient":"linear-gradient(160deg,#fef9f5 0%,#fdeee6 50%,#fae0d4 100%)",
        "card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.96),rgba(253,238,230,0.85))",
        "glow":"0 0 24px rgba(240,106,53,0.22)","shadow_sm":"0 2px 8px rgba(42,16,8,0.09)",
        "shadow_md":"0 8px 28px rgba(42,16,8,0.13)","shadow_lg":"0 16px 52px rgba(42,16,8,0.17)",
        "hover_bg":"rgba(240,106,53,0.06)","focus_ring":"0 0 0 3px rgba(240,106,53,0.28)",
        "success":"#10b981","warning":"#f59e0b","error":"#ef4444","info":"#7c4dff",
        "chart_1":"#f06a35","chart_2":"#7c4dff","chart_3":"#10b981","chart_4":"#f59e0b",
    },
}


class ThemeManager:
    """
    Injects CSS custom properties and global styles into Streamlit.
    Call ThemeManager(theme_key).inject() once per render.
    """

    def __init__(self, theme_key: str):
        self.key = theme_key
        self.t = THEMES.get(theme_key, THEMES["🩺 Clinical Snow"])

    # ── public API ──────────────────────────────────────────────────────────
    def inject(self):
        """Return complete <style> block to pass to st.markdown(unsafe_allow_html=True)"""
        return f"<style>\n{self._css_vars()}\n{self._global_reset()}\n{self._components()}\n{self._animations()}\n</style>"

    def get(self, key: str, fallback: str = ""):
        return self.t.get(key, fallback)

    # ── internal builders ───────────────────────────────────────────────────
    def _css_vars(self) -> str:
        t = self.t
        return f"""
        :root {{
            /* ── Core palette ─────────────────────────── */
            --primary:          {t['primary']};
            --primary-glow:     {t['primary_glow']};
            --secondary:        {t['secondary']};
            --accent:           {t['accent']};

            /* ── Surfaces ─────────────────────────────── */
            --bg:               {t['bg']};
            --surface:          {t['surface']};
            --surface-raised:   {t['surface_raised']};
            --card-bg:          {t['card_bg']};
            --card-border:      {t['card_border']};
            --sidebar-bg:       {t['sidebar_bg']};

            /* ── Glass ────────────────────────────────── */
            --glass-bg:         {t['glass_bg']};
            --glass-border:     {t['glass_border']};
            --glass-blur:       {t['glass_blur']};

            /* ── Typography ───────────────────────────── */
            --text:             {t['text']};
            --text-muted:       {t['text_muted']};
            --subtext:          {t['subtext']};
            --text-inverse:     {t['text_inverse']};

            /* ── Gradients ────────────────────────────── */
            --gradient:         {t['gradient']};
            --hero-gradient:    {t['hero_gradient']};
            --card-gradient:    {t['card_gradient']};

            /* ── Glow & Shadow ────────────────────────── */
            --glow:             {t['glow']};
            --shadow-sm:        {t['shadow_sm']};
            --shadow-md:        {t['shadow_md']};
            --shadow-lg:        {t['shadow_lg']};

            /* ── Interactive ──────────────────────────── */
            --hover-bg:         {t['hover_bg']};
            --focus-ring:       {t['focus_ring']};

            /* ── Status ───────────────────────────────── */
            --success:          {t['success']};
            --warning:          {t['warning']};
            --error:            {t['error']};
            --info:             {t['info']};

            /* ── Spacing & Geometry ───────────────────── */
            --radius-sm:        8px;
            --radius-md:        16px;
            --radius-lg:        25px;
            --radius-xl:        32px;
            --radius-full:      9999px;
        }}
        """

    def _global_reset(self) -> str:
        t = self.t
        # colour-scheme hint tells the browser to render native controls correctly
        color_scheme = "dark" if t["family"] == "dark" else "light"
        return f"""
        /* ═══════════════════════════════════════════════════════════════
           GOOGLE FONTS
        ═══════════════════════════════════════════════════════════════ */
        @import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=DM+Mono:wght@400;500&display=swap');

        /* ═══════════════════════════════════════════════════════════════
           ROOT — VARIABLES + COLOUR SCHEME
           All rules below use var(--x) so a single :root update is enough
        ═══════════════════════════════════════════════════════════════ */
        :root {{
            color-scheme: {color_scheme};
        }}

        /* ── Page & app background ──────────────────── */
        html {{
            background-color: var(--bg) !important;
            color:            var(--text) !important;
        }}
        body {{
            background-color: var(--bg) !important;
            color:            var(--text) !important;
        }}
        .stApp {{
            background: var(--hero-gradient) !important;
            color:      var(--text) !important;
        }}
        /* Every Streamlit container — transparent so .stApp bg shows through */
        .main,
        .main .block-container,
        [data-testid="stAppViewContainer"],
        [data-testid="stAppViewContainer"] > .main,
        [data-testid="stMain"],
        [data-testid="stMainBlockContainer"],
        [data-testid="stVerticalBlock"],
        [data-testid="stVerticalBlockBorderWrapper"],
        [data-testid="column"],
        .element-container,
        .row-widget {{
            background: transparent !important;
            color:      var(--text) !important;
        }}

        /* ── Fonts everywhere ───────────────────────── */
        *, *::before, *::after {{
            font-family:            'DM Sans', system-ui, sans-serif !important;
            -webkit-font-smoothing: antialiased;
            box-sizing:             border-box;
        }}
        h1, h2, h3, h4, h5, h6 {{
            font-family:   'Syne', sans-serif !important;
            font-weight:   800 !important;
            letter-spacing: -0.02em;
            color:         var(--text) !important;
        }}

        /* ═══════════════════════════════════════════════════════════════
           SIDEBAR
        ═══════════════════════════════════════════════════════════════ */
        [data-testid="stSidebar"],
        [data-testid="stSidebar"] > div,
        [data-testid="stSidebar"] > div:first-child,
        section[data-testid="stSidebar"] {{
            background:      var(--sidebar-bg) !important;
            border-right:    1px solid var(--card-border) !important;
            backdrop-filter: blur(20px);
        }}
        /* All text inside sidebar */
        [data-testid="stSidebar"] p,
        [data-testid="stSidebar"] span,
        [data-testid="stSidebar"] div,
        [data-testid="stSidebar"] label,
        [data-testid="stSidebar"] li {{
            color: var(--text) !important;
        }}
        [data-testid="stSidebar"] .stSelectbox > div > div {{
            background: var(--glass-bg)     !important;
            color:      var(--text)         !important;
            border:     1px solid var(--card-border) !important;
        }}
        [data-testid="stSidebar"] svg {{ fill: var(--text-muted) !important; }}

        /* ═══════════════════════════════════════════════════════════════
           ALL TEXT — every Streamlit text container, all versions
        ═══════════════════════════════════════════════════════════════ */
        p, li, span, label, td, th, caption, figcaption,
        .stMarkdown, .stMarkdown *,
        [data-testid="stMarkdownContainer"],
        [data-testid="stMarkdownContainer"] *,
        [data-testid="stText"],
        [data-testid="stText"] *,
        [data-testid="stCaptionContainer"],
        [data-testid="stCaptionContainer"] *,
        .stAlert p, .stAlert span,
        .stInfo p,  .stSuccess p, .stWarning p, .stError p {{
            color: var(--text) !important;
        }}
        /* Captions & sub-text */
        small, .stCaption, .caption,
        [data-testid="stCaptionContainer"] p {{
            color: var(--subtext) !important;
        }}

        /* ═══════════════════════════════════════════════════════════════
           WIDGET LABELS — all input labels
        ═══════════════════════════════════════════════════════════════ */
        .stTextInput    > label,
        .stTextArea     > label,
        .stSelectbox    > label,
        .stMultiSelect  > label,
        .stRadio        > label,
        .stCheckbox     > label,
        .stSlider       > label,
        .stNumberInput  > label,
        .stDateInput    > label,
        .stTimeInput    > label,
        .stFileUploader > label,
        .stColorPicker  > label,
        /* Newer Streamlit label wrappers */
        [data-testid="stWidgetLabel"],
        [data-testid="stWidgetLabel"] *,
        [data-testid="InputInstructions"] {{
            color: var(--text-muted) !important;
        }}

        /* ═══════════════════════════════════════════════════════════════
           TEXT INPUTS
        ═══════════════════════════════════════════════════════════════ */
        .stTextInput > div > div > input,
        .stTextArea  > div > div > textarea,
        .stNumberInput > div > div > input {{
            background:    var(--glass-bg)    !important;
            color:         var(--text)        !important;
            border:        1.5px solid var(--card-border) !important;
            border-radius: 12px              !important;
            caret-color:   var(--primary)    !important;
        }}
        .stTextInput > div > div > input:focus,
        .stTextArea  > div > div > textarea:focus,
        .stNumberInput > div > div > input:focus {{
            border-color: var(--primary)   !important;
            box-shadow:   var(--focus-ring) !important;
            outline:      none             !important;
        }}
        .stTextInput > div > div > input::placeholder,
        .stTextArea  > div > div > textarea::placeholder {{
            color:   var(--subtext) !important;
            opacity: 0.7;
        }}

        /* ═══════════════════════════════════════════════════════════════
           SELECTBOX / MULTISELECT
        ═══════════════════════════════════════════════════════════════ */
        .stSelectbox    > div > div,
        .stSelectbox    > div > div > div,
        .stMultiSelect  > div > div,
        .stMultiSelect  > div > div > div {{
            background:    var(--glass-bg)    !important;
            color:         var(--text)        !important;
            border:        1.5px solid var(--card-border) !important;
            border-radius: 12px              !important;
        }}
        /* Selected tags in multiselect */
        .stMultiSelect span[data-baseweb="tag"] {{
            background: var(--primary-glow)  !important;
            color:      var(--primary)       !important;
        }}
        /* Dropdown popover list */
        [data-baseweb="popover"] > div,
        [data-baseweb="menu"],
        [data-baseweb="list"] {{
            background: var(--surface)       !important;
            border:     1px solid var(--card-border) !important;
            border-radius: 12px             !important;
        }}
        [data-baseweb="menu"]    li,
        [data-baseweb="list"]    li,
        [role="option"],
        [role="option"] *,
        [data-baseweb="option"],
        [data-baseweb="option"] * {{
            color:      var(--text)          !important;
            background: transparent         !important;
        }}
        [role="option"]:hover,
        [data-baseweb="option"]:hover {{
            background: var(--hover-bg)      !important;
        }}
        .stSelectbox svg,
        .stMultiSelect svg {{
            fill: var(--text-muted)          !important;
        }}

        /* ═══════════════════════════════════════════════════════════════
           RADIO & CHECKBOX
        ═══════════════════════════════════════════════════════════════ */
        .stRadio    > div,
        .stRadio    > div > label,
        .stRadio    > div > label > div,
        .stCheckbox > label,
        .stCheckbox > label > span {{
            color: var(--text) !important;
        }}
        /* Radio circle */
        .stRadio input[type="radio"]:checked + div {{
            background: var(--primary) !important;
            border-color: var(--primary) !important;
        }}

        /* ═══════════════════════════════════════════════════════════════
           SLIDER
        ═══════════════════════════════════════════════════════════════ */
        .stSlider [data-testid="stSlider"] div[role="slider"] {{
            background: var(--primary) !important;
        }}
        .stSlider .stMarkdown p {{ color: var(--subtext) !important; }}

        /* ═══════════════════════════════════════════════════════════════
           EXPANDER
        ═══════════════════════════════════════════════════════════════ */
        [data-testid="stExpander"],
        [data-testid="stExpander"] > div {{
            background:    var(--glass-bg)    !important;
            border:        1px solid var(--card-border) !important;
            border-radius: 14px              !important;
        }}
        .streamlit-expanderHeader,
        [data-testid="stExpander"] summary,
        [data-testid="stExpander"] summary *,
        [data-testid="stExpanderToggleIcon"] {{
            background: transparent          !important;
            color:      var(--text)          !important;
        }}
        .streamlit-expanderContent,
        [data-testid="stExpanderDetails"],
        [data-testid="stExpanderDetails"] * {{
            background: var(--glass-bg)      !important;
            color:      var(--text)          !important;
        }}

        /* ═══════════════════════════════════════════════════════════════
           TABS
        ═══════════════════════════════════════════════════════════════ */
        .stTabs [data-baseweb="tab-list"] {{
            background:    var(--glass-bg)    !important;
            border:        1px solid var(--card-border) !important;
            border-radius: 999px             !important;
            padding:       5px              !important;
            gap:           4px              !important;
        }}
        .stTabs [data-baseweb="tab"] {{
            color:         var(--text-muted) !important;
            background:    transparent       !important;
            border:        none             !important;
            border-radius: 999px            !important;
        }}
        .stTabs [data-baseweb="tab"]:hover {{
            background: var(--hover-bg)      !important;
            color:      var(--primary)       !important;
        }}
        .stTabs [aria-selected="true"] {{
            background: var(--gradient)      !important;
            color:      var(--text-inverse)  !important;
        }}
        /* Tab panel content */
        [data-baseweb="tab-panel"] {{
            background: transparent          !important;
            padding-top: 1rem               !important;
        }}

        /* ═══════════════════════════════════════════════════════════════
           METRIC WIDGET
        ═══════════════════════════════════════════════════════════════ */
        [data-testid="metric-container"] {{
            background:    var(--card-bg)     !important;
            border:        1px solid var(--card-border) !important;
            border-radius: 16px              !important;
            padding:       1rem             !important;
        }}
        [data-testid="stMetricLabel"],
        [data-testid="stMetricLabel"] * {{
            color: var(--subtext)  !important;
        }}
        [data-testid="stMetricValue"],
        [data-testid="stMetricValue"] * {{
            color: var(--primary)  !important;
        }}
        [data-testid="stMetricDelta"] {{
            color: var(--success)  !important;
        }}

        /* ═══════════════════════════════════════════════════════════════
           FORM
        ═══════════════════════════════════════════════════════════════ */
        [data-testid="stForm"] {{
            background:    var(--glass-bg)    !important;
            border:        1px solid var(--card-border) !important;
            border-radius: 16px              !important;
            padding:       1rem             !important;
        }}
        [data-testid="stForm"] * {{
            color: var(--text) !important;
        }}

        /* ═══════════════════════════════════════════════════════════════
           ALERT BOXES (info / success / warning / error)
        ═══════════════════════════════════════════════════════════════ */
        [data-testid="stAlert"] {{
            border-radius: 12px             !important;
            border:        1px solid var(--card-border) !important;
        }}
        [data-testid="stAlert"] p,
        [data-testid="stAlert"] span {{
            color: var(--text) !important;
        }}

        /* ═══════════════════════════════════════════════════════════════
           DIVIDER
        ═══════════════════════════════════════════════════════════════ */
        hr {{ border-color: var(--card-border) !important; }}

        /* ═══════════════════════════════════════════════════════════════
           SCROLLBAR
        ═══════════════════════════════════════════════════════════════ */
        ::-webkit-scrollbar       {{ width: 5px; height: 5px; }}
        ::-webkit-scrollbar-track {{ background: transparent; }}
        ::-webkit-scrollbar-thumb {{
            background:    var(--primary)60; border-radius: 999px;
        }}
        ::-webkit-scrollbar-thumb:hover {{ background: var(--primary); }}

        /* ═══════════════════════════════════════════════════════════════
           HIDE ALL STREAMLIT CHROME
           Covers all known Streamlit 1.x versions
        ═══════════════════════════════════════════════════════════════ */
        header,
        header[data-testid="stHeader"],
        [data-testid="stHeader"],
        [data-testid="stToolbar"],
        [data-testid="stDecoration"],
        [data-testid="stStatusWidget"],
        [data-testid="stDeployButton"],
        [data-testid="collapsedControl"],
        .stApp > header,
        #MainMenu,
        footer,
        footer a,
        .reportview-container .main footer,
        .viewerBadge_link__qRIco,
        .viewerBadge_container__r5tak {{
            display: none !important;
        }}

        /* ═══════════════════════════════════════════════════════════════
           BLOCK CONTAINER
        ═══════════════════════════════════════════════════════════════ */
        .block-container {{
            padding-top:    1.5rem !important;
            padding-bottom: 3rem  !important;
            max-width:      100%  !important;
        }}
        """

    def _components(self) -> str:
        t = self.t
        return f"""
        /* ═══════════════════════════════════════════════
           GLASS CARD — base reusable
        ═══════════════════════════════════════════════ */
        .glass-card {{
            background:     var(--glass-bg);
            border:         1px solid var(--glass-border);
            border-radius:  var(--radius-lg);
            backdrop-filter: blur(var(--glass-blur));
            -webkit-backdrop-filter: blur(var(--glass-blur));
            box-shadow:     var(--shadow-md);
            padding:        1.75rem;
            transition:     transform 0.25s ease, box-shadow 0.25s ease;
        }}
        .glass-card:hover {{
            transform:      translateY(-3px);
            box-shadow:     var(--shadow-lg), var(--glow);
        }}

        /* ═══════════════════════════════════════════════
           BENTO TILE
        ═══════════════════════════════════════════════ */
        .bento-tile {{
            background:     var(--card-gradient);
            border:         1px solid var(--card-border);
            border-radius:  var(--radius-lg);
            padding:        1.5rem;
            backdrop-filter: blur(12px);
            box-shadow:     var(--shadow-sm);
            cursor:         pointer;
            transition:     all 0.30s cubic-bezier(0.34,1.56,0.64,1);
            position:       relative;
            overflow:       hidden;
        }}
        .bento-tile::before {{
            content: '';
            position: absolute;
            inset: 0;
            background: var(--gradient);
            opacity: 0;
            transition: opacity 0.30s ease;
            border-radius: inherit;
        }}
        .bento-tile:hover {{
            transform:      translateY(-6px) scale(1.02);
            box-shadow:     var(--shadow-lg), var(--glow);
            border-color:   var(--primary);
        }}
        .bento-tile:hover::before {{ opacity: 0.06; }}

        /* ═══════════════════════════════════════════════
           BUTTONS
        ═══════════════════════════════════════════════ */
        .stButton > button {{
            background:     var(--glass-bg) !important;
            border:         1.5px solid var(--card-border) !important;
            border-radius:  var(--radius-md) !important;
            color:          var(--text) !important;
            font-weight:    600 !important;
            padding:        0.6rem 1.2rem !important;
            transition:     all 0.22s ease !important;
            backdrop-filter: blur(8px);
            font-family:    'DM Sans', sans-serif !important;
            letter-spacing: 0.01em;
        }}
        .stButton > button:hover {{
            background:     var(--primary) !important;
            border-color:   var(--primary) !important;
            color:          var(--text-inverse) !important;
            transform:      translateY(-2px) !important;
            box-shadow:     var(--shadow-md), 0 0 20px var(--primary-glow) !important;
        }}
        .stButton > button[kind="primary"] {{
            background:     var(--gradient) !important;
            border:         none !important;
            color:          var(--text-inverse) !important;
            box-shadow:     var(--shadow-sm), 0 0 16px var(--primary-glow);
        }}
        .stButton > button[kind="primary"]:hover {{
            filter:         brightness(1.12) !important;
            transform:      translateY(-2px) !important;
            box-shadow:     var(--shadow-md), 0 0 30px var(--primary-glow) !important;
        }}

        /* ═══════════════════════════════════════════════
           INPUTS — floating label aesthetic
        ═══════════════════════════════════════════════ */
        .stTextInput > div > div > input,
        .stTextArea > div > div > textarea,
        .stSelectbox > div > div > div {{
            background:     var(--glass-bg) !important;
            border:         1.5px solid var(--card-border) !important;
            border-radius:  var(--radius-md) !important;
            color:          var(--text) !important;
            backdrop-filter: blur(8px);
            transition:     border-color 0.2s, box-shadow 0.2s;
            font-family:    'DM Sans', sans-serif !important;
        }}
        .stTextInput > div > div > input:focus,
        .stTextArea > div > div > textarea:focus {{
            border-color:   var(--primary) !important;
            box-shadow:     var(--focus-ring) !important;
            outline:        none !important;
        }}
        .stTextInput label, .stTextArea label,
        .stSelectbox label, .stRadio label {{
            color:          var(--text-muted) !important;
            font-weight:    600 !important;
            font-size:      0.87rem !important;
            letter-spacing: 0.04em !important;
            text-transform: uppercase !important;
        }}

        /* ═══════════════════════════════════════════════
           TABS — glass pill style
        ═══════════════════════════════════════════════ */
        .stTabs [data-baseweb="tab-list"] {{
            gap:              6px !important;
            background:       var(--glass-bg) !important;
            border:           1px solid var(--card-border) !important;
            border-radius:    var(--radius-xl) !important;
            padding:          6px !important;
            backdrop-filter:  blur(12px);
            flex-wrap:        wrap !important;
        }}
        .stTabs [data-baseweb="tab"] {{
            background:       transparent !important;
            border:           none !important;
            border-radius:    var(--radius-lg) !important;
            padding:          9px 18px !important;
            font-size:        0.88rem !important;
            font-weight:      600 !important;
            color:            var(--text-muted) !important;
            transition:       all 0.22s ease !important;
            white-space:      nowrap;
        }}
        .stTabs [data-baseweb="tab"]:hover {{
            background:       var(--hover-bg) !important;
            color:            var(--primary) !important;
        }}
        .stTabs [aria-selected="true"] {{
            background:       var(--gradient) !important;
            color:            var(--text-inverse) !important;
            box-shadow:       0 4px 16px var(--primary-glow) !important;
        }}

        /* ═══════════════════════════════════════════════
           SIDEBAR ITEMS
        ═══════════════════════════════════════════════ */
        .sidebar-nav-item {{
            display:        flex;
            align-items:    center;
            gap:            12px;
            padding:        10px 16px;
            border-radius:  var(--radius-md);
            cursor:         pointer;
            transition:     all 0.2s ease;
            color:          var(--text-muted);
            font-weight:    500;
            font-size:      0.9rem;
            margin-bottom:  2px;
        }}
        .sidebar-nav-item:hover {{
            background:     var(--hover-bg);
            color:          var(--primary);
            transform:      translateX(4px);
        }}
        .sidebar-nav-item.active {{
            background:     var(--glass-bg);
            border:         1px solid var(--glass-border);
            color:          var(--primary);
            font-weight:    700;
            box-shadow:     var(--shadow-sm);
        }}

        /* ═══════════════════════════════════════════════
           METRIC / STAT CARD
        ═══════════════════════════════════════════════ */
        .stat-card {{
            background:    var(--card-bg);
            border:        1px solid var(--card-border);
            border-radius: var(--radius-lg);
            padding:       1.5rem;
            text-align:    center;
            transition:    all 0.25s ease;
            position:      relative;
            overflow:      hidden;
        }}
        .stat-card::after {{
            content: '';
            position: absolute;
            bottom: 0; left: 0; right: 0;
            height: 3px;
            background: var(--gradient);
            border-radius: 0 0 var(--radius-lg) var(--radius-lg);
        }}
        .stat-card:hover {{
            transform: translateY(-4px);
            box-shadow: var(--shadow-md), var(--glow);
        }}

        /* ═══════════════════════════════════════════════
           BADGE
        ═══════════════════════════════════════════════ */
        .badge {{
            display:        inline-flex;
            align-items:    center;
            gap:            4px;
            padding:        3px 10px;
            border-radius:  var(--radius-full);
            font-size:      0.72rem;
            font-weight:    700;
            letter-spacing: 0.04em;
            text-transform: uppercase;
        }}
        .badge-primary {{
            background: var(--primary-glow);
            color: var(--primary);
            border: 1px solid var(--primary-glow);
        }}

        /* ═══════════════════════════════════════════════
           PROGRESS BAR (custom)
        ═══════════════════════════════════════════════ */
        .med-progress-bar {{
            width: 100%;
            height: 8px;
            background: var(--card-border);
            border-radius: var(--radius-full);
            overflow: hidden;
        }}
        .med-progress-fill {{
            height: 100%;
            background: var(--gradient);
            border-radius: var(--radius-full);
            transition: width 0.6s cubic-bezier(0.4,0,0.2,1);
        }}

        /* ═══════════════════════════════════════════════
           DIVIDER
        ═══════════════════════════════════════════════ */
        hr, .stDivider {{
            border: none !important;
            border-top: 1px solid var(--card-border) !important;
            margin: 1.5rem 0 !important;
        }}

        /* ═══════════════════════════════════════════════
           STREAMLIT METRIC
        ═══════════════════════════════════════════════ */
        [data-testid="metric-container"] {{
            background:    var(--card-bg) !important;
            border:        1px solid var(--card-border) !important;
            border-radius: var(--radius-lg) !important;
            padding:       1rem 1.25rem !important;
            backdrop-filter: blur(12px);
        }}
        [data-testid="metric-container"] label {{
            color: var(--text-muted) !important;
            font-size: 0.8rem !important;
            font-weight: 600 !important;
            text-transform: uppercase !important;
            letter-spacing: 0.06em !important;
        }}
        [data-testid="metric-container"] [data-testid="stMetricValue"] {{
            color: var(--primary) !important;
            font-family: 'Syne', sans-serif !important;
            font-size: 1.8rem !important;
            font-weight: 800 !important;
        }}

        /* ═══════════════════════════════════════════════
           ALERT / INFO BOXES
        ═══════════════════════════════════════════════ */
        [data-testid="stAlert"] {{
            border-radius: var(--radius-md) !important;
            border: none !important;
            backdrop-filter: blur(8px);
        }}

        /* ═══════════════════════════════════════════════
           EXPANDER
        ═══════════════════════════════════════════════ */
        .streamlit-expanderHeader {{
            background:    var(--glass-bg) !important;
            border:        1px solid var(--card-border) !important;
            border-radius: var(--radius-md) !important;
            color:         var(--text) !important;
            font-weight:   600 !important;
        }}

        /* ═══════════════════════════════════════════════
           FLOATING AI BUBBLE
        ═══════════════════════════════════════════════ */
        .ai-bubble {{
            position:      fixed;
            bottom:        28px;
            right:         28px;
            width:         62px;
            height:        62px;
            border-radius: 50%;
            background:    var(--gradient);
            display:       flex;
            align-items:   center;
            justify-content: center;
            font-size:     1.6rem;
            cursor:        pointer;
            box-shadow:    var(--shadow-lg), 0 0 30px var(--primary-glow);
            transition:    all 0.3s cubic-bezier(0.34,1.56,0.64,1);
            z-index:       9999;
            animation:     bubblePulse 3s ease-in-out infinite;
            border:        2px solid rgba(255,255,255,0.25);
        }}
        .ai-bubble:hover {{
            transform:     scale(1.15);
            box-shadow:    var(--shadow-lg), 0 0 50px var(--primary-glow);
        }}
        .ai-bubble-panel {{
            position:      fixed;
            bottom:        104px;
            right:         28px;
            width:         340px;
            max-height:    480px;
            background:    var(--card-bg);
            border:        1px solid var(--glass-border);
            border-radius: var(--radius-xl);
            backdrop-filter: blur(var(--glass-blur));
            box-shadow:    var(--shadow-lg), var(--glow);
            overflow:      hidden;
            z-index:       9998;
            animation:     slideUp 0.35s cubic-bezier(0.34,1.56,0.64,1);
        }}

        /* ═══════════════════════════════════════════════
           LOGIN CARD
        ═══════════════════════════════════════════════ */
        .login-card {{
            background:    var(--glass-bg);
            border:        1px solid var(--glass-border);
            border-radius: var(--radius-xl);
            backdrop-filter: blur(var(--glass-blur));
            box-shadow:    var(--shadow-lg), var(--glow);
            padding:       3rem 2.5rem;
            max-width:     460px;
            margin:        0 auto;
            animation:     fadeUp 0.5s cubic-bezier(0.34,1.56,0.64,1);
        }}
        .login-card .field-wrapper {{
            position:      relative;
            margin-bottom: 1.4rem;
        }}
        .login-card .field-wrapper label {{
            position:      absolute;
            top:           -10px;
            left:          14px;
            background:    var(--surface);
            padding:       0 6px;
            font-size:     0.75rem;
            font-weight:   700;
            color:         var(--primary);
            letter-spacing: 0.06em;
            text-transform: uppercase;
            z-index:       1;
            border-radius: 4px;
        }}

        /* ═══════════════════════════════════════════════
           KNOWLEDGE HEATMAP CELL
        ═══════════════════════════════════════════════ */
        .heatmap-cell {{
            width:         14px;
            height:        14px;
            border-radius: 3px;
            transition:    all 0.2s ease;
        }}
        .heatmap-cell:hover {{
            transform:     scale(1.4);
            z-index:       10;
        }}

        /* ═══════════════════════════════════════════════
           TIMER RING (Phase 4)
        ═══════════════════════════════════════════════ */
        .timer-ring-container {{
            position: relative;
            display: flex;
            align-items: center;
            justify-content: center;
        }}
        .timer-ring-container svg circle {{
            transition: stroke-dashoffset 1s linear;
            transform: rotate(-90deg);
            transform-origin: 50% 50%;
        }}
        .timer-lcd {{
            font-family:    'DM Mono', monospace !important;
            font-size:      4.5rem;
            font-weight:    500;
            color:          var(--primary);
            text-shadow:    0 0 20px var(--primary-glow), 0 0 40px var(--primary-glow);
            letter-spacing: 0.08em;
        }}
        .timer-bar-track {{
            position: fixed;
            top: 0; left: 0; right: 0;
            height: 4px;
            z-index: 9000;
            background: var(--card-border);
        }}
        .timer-bar-fill {{
            height: 100%;
            transition: width 1s linear, background 1s ease;
        }}

        /* ═══════════════════════════════════════════════
           VAULT / BENTO GRID
        ═══════════════════════════════════════════════ */
        .vault-grid {{
            display:               grid;
            grid-template-columns: repeat(auto-fill, minmax(200px, 1fr));
            gap:                   16px;
        }}
        .vault-item {{
            background:    var(--card-bg);
            border:        1px solid var(--card-border);
            border-radius: var(--radius-md);
            padding:       1.2rem;
            transition:    all 0.25s ease;
            cursor:        pointer;
            position:      relative;
        }}
        .vault-item:hover {{
            border-color:  var(--primary);
            box-shadow:    var(--shadow-sm), 0 0 12px var(--primary-glow);
            transform:     translateY(-2px);
        }}

        /* ═══════════════════════════════════════════════
           RESOURCE CARD (Phase 3)
        ═══════════════════════════════════════════════ */
        .resource-card {{
            background:    var(--card-bg);
            border:        1px solid var(--card-border);
            border-radius: var(--radius-lg);
            overflow:      hidden;
            transition:    all 0.28s ease;
        }}
        .resource-card:hover {{
            transform:     translateY(-4px);
            box-shadow:    var(--shadow-md), var(--glow);
        }}
        .resource-card .rc-header {{
            padding:       1rem 1.25rem;
            display:       flex;
            align-items:   center;
            gap:           10px;
            border-bottom: 1px solid var(--card-border);
        }}
        .resource-card .rc-body {{
            padding:       1rem 1.25rem;
        }}
        .resource-card .rc-actions {{
            padding:       0.75rem 1.25rem;
            display:       flex;
            gap:           8px;
            border-top:    1px solid var(--card-border);
            background:    var(--hover-bg);
        }}

        /* ═══════════════════════════════════════════════
           SAVE TO VAULT BUTTON
        ═══════════════════════════════════════════════ */
        .btn-vault {{
            background:    transparent;
            border:        1.5px solid var(--card-border);
            border-radius: var(--radius-sm);
            padding:       5px 12px;
            font-size:     0.78rem;
            font-weight:   600;
            color:         var(--text-muted);
            cursor:        pointer;
            transition:    all 0.2s;
            display:       inline-flex;
            align-items:   center;
            gap:           5px;
        }}
        .btn-vault:hover {{
            background:    var(--primary);
            border-color:  var(--primary);
            color:         var(--text-inverse);
        }}

        /* ═══════════════════════════════════════════════
           PROFILE — ACADEMIC IDENTITY
        ═══════════════════════════════════════════════ */
        .profile-avatar-ring {{
            width:         100px;
            height:        100px;
            border-radius: 50%;
            background:    var(--gradient);
            padding:       3px;
            box-shadow:    var(--glow);
        }}
        .profile-avatar-inner {{
            width:         100%;
            height:        100%;
            border-radius: 50%;
            background:    var(--surface);
            display:       flex;
            align-items:   center;
            justify-content: center;
            font-size:     2.5rem;
        }}

        /* ═══════════════════════════════════════════════
           DEVELOPER PORTFOLIO TIMELINE
        ═══════════════════════════════════════════════ */
        .timeline-item {{
            position:      relative;
            padding-left:  32px;
            padding-bottom: 2rem;
        }}
        .timeline-item::before {{
            content:       '';
            position:      absolute;
            left:          10px;
            top:           0;
            bottom:        0;
            width:         2px;
            background:    var(--gradient);
        }}
        .timeline-item::after {{
            content:       '';
            position:      absolute;
            left:          4px;
            top:           4px;
            width:         14px;
            height:        14px;
            border-radius: 50%;
            background:    var(--gradient);
            box-shadow:    0 0 10px var(--primary-glow);
        }}
        .timeline-item:last-child::before {{ background: transparent; }}

        /* ═══════════════════════════════════════════════
           SPINNER OVERRIDE
        ═══════════════════════════════════════════════ */
        [data-testid="stSpinner"] > div {{
            border-top-color: var(--primary) !important;
        }}
        """

    def _animations(self) -> str:
        return """
        /* ═══════════════════════════════════════════════
           KEYFRAME ANIMATIONS
        ═══════════════════════════════════════════════ */

        @keyframes fadeUp {
            from { opacity:0; transform:translateY(24px); }
            to   { opacity:1; transform:translateY(0); }
        }
        @keyframes fadeIn {
            from { opacity:0; }
            to   { opacity:1; }
        }
        @keyframes slideUp {
            from { opacity:0; transform:translateY(16px) scale(0.96); }
            to   { opacity:1; transform:translateY(0) scale(1); }
        }
        @keyframes scaleIn {
            from { opacity:0; transform:scale(0.90); }
            to   { opacity:1; transform:scale(1); }
        }
        @keyframes shimmer {
            0%   { background-position: -400px 0; }
            100% { background-position: 400px 0; }
        }
        @keyframes bubblePulse {
            0%,100% { box-shadow: var(--shadow-lg), 0 0 20px var(--primary-glow); }
            50%      { box-shadow: var(--shadow-lg), 0 0 45px var(--primary-glow); }
        }
        @keyframes gradientShift {
            0%   { background-position: 0% 50%; }
            50%  { background-position: 100% 50%; }
            100% { background-position: 0% 50%; }
        }
        @keyframes float {
            0%,100% { transform: translateY(0px);  }
            50%      { transform: translateY(-8px); }
        }
        @keyframes glowPulse {
            0%,100% { opacity:0.6; }
            50%     { opacity:1;   }
        }
        @keyframes spin360 {
            from { transform:rotate(0deg);   }
            to   { transform:rotate(360deg); }
        }
        @keyframes countUp {
            from { opacity:0; transform:translateY(12px); }
            to   { opacity:1; transform:translateY(0);    }
        }
        @keyframes stagger-fade {
            from { opacity:0; transform:translateY(16px) scale(0.97); }
            to   { opacity:1; transform:translateY(0) scale(1);       }
        }

        /* ── Apply entry animations to common containers ── */
        .glass-card  { animation: fadeUp  0.4s ease both; }
        .bento-tile  { animation: stagger-fade 0.4s ease both; }
        .stat-card   { animation: scaleIn 0.35s ease both; }
        .login-card  { animation: fadeUp  0.5s cubic-bezier(0.34,1.56,0.64,1) both; }

        /* Stagger children */
        .bento-tile:nth-child(1) { animation-delay:0.05s; }
        .bento-tile:nth-child(2) { animation-delay:0.10s; }
        .bento-tile:nth-child(3) { animation-delay:0.15s; }
        .bento-tile:nth-child(4) { animation-delay:0.20s; }
        .bento-tile:nth-child(5) { animation-delay:0.25s; }
        .bento-tile:nth-child(6) { animation-delay:0.30s; }
        .bento-tile:nth-child(7) { animation-delay:0.35s; }
        .bento-tile:nth-child(8) { animation-delay:0.40s; }
        .bento-tile:nth-child(9) { animation-delay:0.45s; }

        /* Skeleton loader shimmer */
        .skeleton {
            background: linear-gradient(90deg,
                var(--card-bg) 25%,
                var(--hover-bg) 50%,
                var(--card-bg) 75%
            );
            background-size: 400px 100%;
            animation: shimmer 1.4s infinite linear;
            border-radius: var(--radius-md);
        }
        """


# ─────────────────────────────────────────────────────────────────────────────
# LEGACY COMPAT — old code calls get_css(theme_name) & uses THEMES dict
# ─────────────────────────────────────────────────────────────────────────────

def get_css(theme_key: str) -> str:
    """Drop-in replacement for old get_css(); returns full <style> block."""
    return ThemeManager(theme_key).inject()


# ─────────────────────────────────────────────────────────────────────────────
# SUBJECT HUB — restored lightweight page API expected by app.py
# ─────────────────────────────────────────────────────────────────────────────
try:
    from content import SUBJECTS as SUBJECTS_LIBRARY
except Exception:
    SUBJECTS_LIBRARY = {}


def subjects_page(theme: dict):
    """Render a focused subject browser from the shared content library."""
    import streamlit as st

    st.markdown(f"""
    <div style="display:flex;align-items:center;justify-content:space-between;
         gap:12px;flex-wrap:wrap;margin-bottom:1rem;">
        <div>
            <div style="font-family:Syne,sans-serif;font-size:1.9rem;font-weight:900;
                 color:{theme['text']};letter-spacing:0;">📚 Subjects</div>
            <div style="font-size:0.86rem;color:{theme['subtext']};">
                High-yield notes and topic maps for pre-clinical and clinical study.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    if not SUBJECTS_LIBRARY:
        st.warning("Subject content is not available yet.")
        return

    categories = list(SUBJECTS_LIBRARY.keys())
    selected_category = st.selectbox("Category", categories, label_visibility="collapsed")
    subjects = SUBJECTS_LIBRARY.get(selected_category, {})

    query = st.text_input("Search subjects or topics", placeholder="Search cardiology, anatomy, ACS...")
    query_l = query.strip().lower()

    cards = []
    for subject_name, data in subjects.items():
        topics = data.get("topics", [])
        haystack = " ".join([subject_name, *topics]).lower()
        if query_l and query_l not in haystack:
            continue
        cards.append((subject_name, data))

    if not cards:
        st.info("No subjects matched your search.")
        return

    cols = st.columns(3)
    for idx, (subject_name, data) in enumerate(cards):
        with cols[idx % 3]:
            color = data.get("color", theme["primary"])
            icon = data.get("icon", "📚")
            topics = data.get("topics", [])
            preview = "".join(
                f"<li>{topic}</li>" for topic in topics[:3]
            )
            st.markdown(f"""
            <div style="background:{theme['card_bg']};border:1px solid {theme['card_border']};
                 border-top:3px solid {color};border-radius:8px;padding:1rem;
                 min-height:230px;box-shadow:{theme['shadow_sm']};margin-bottom:0.75rem;">
                <div style="display:flex;align-items:center;gap:8px;margin-bottom:0.45rem;">
                    <div style="width:34px;height:34px;border-radius:8px;background:{color}18;
                         color:{color};display:flex;align-items:center;justify-content:center;">{icon}</div>
                    <div style="font-weight:900;color:{theme['text']};">{subject_name}</div>
                </div>
                <div style="font-size:0.78rem;color:{theme['subtext']};line-height:1.55;">
                    {len(topics)} focused topics · high-yield notes included
                </div>
                <ul style="margin:0.65rem 0 0 1rem;padding:0;font-size:0.76rem;
                    color:{theme['text_muted']};line-height:1.45;">{preview}</ul>
            </div>
            """, unsafe_allow_html=True)
