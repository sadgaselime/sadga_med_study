"""
styles.py — MedStudy Oman ✦ Next-Generation Design System
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
15 Premium Medical Aesthetic Themes  ·  Glassmorphism  ·  Bento Grid
World-class typography · Fluid animations · Micro-interactions
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
"""

# ═══════════════════════════════════════════════════════════════════════════════
# 15 PREMIUM MEDICAL AESTHETIC THEMES
# ═══════════════════════════════════════════════════════════════════════════════

THEMES = {

    # ─── 1. MIDNIGHT ROUNDS ── The Signature "AI Medical Platform" Dark ────────
    "🌌 Midnight Rounds": {
        "name": "Midnight Rounds", "family": "dark",
        "primary": "#22d3ee", "primary_glow": "rgba(34,211,238,0.30)",
        "secondary": "#0891b2", "accent": "#164e63",
        "bg": "#020617", "surface": "#0a1628", "surface_raised": "#0f1f38",
        "card_bg": "rgba(10,22,40,0.80)", "card_border": "rgba(34,211,238,0.14)",
        "sidebar_bg": "#060f1e",
        "glass_bg": "rgba(34,211,238,0.045)", "glass_border": "rgba(34,211,238,0.18)",
        "glass_blur": "28px",
        "text": "#e2f4ff", "text_muted": "#7ab8d4", "subtext": "#3d6a88",
        "text_inverse": "#020617",
        "gradient": "linear-gradient(135deg,#22d3ee,#3b82f6)",
        "hero_gradient": "linear-gradient(160deg,#020617 0%,#061228 55%,#020a1a 100%)",
        "card_gradient": "linear-gradient(145deg,rgba(34,211,238,0.06),rgba(59,130,246,0.03))",
        "glow": "0 0 40px rgba(34,211,238,0.28)", "glow_lg": "0 0 80px rgba(34,211,238,0.15)",
        "shadow_sm": "0 2px 8px rgba(0,0,0,0.50)", "shadow_md": "0 8px 32px rgba(0,0,0,0.60)",
        "shadow_lg": "0 24px 64px rgba(0,0,0,0.70)", "hover_bg": "rgba(34,211,238,0.08)",
        "focus_ring": "0 0 0 3px rgba(34,211,238,0.32)",
        "success": "#10d982", "warning": "#fbbf24", "error": "#f43f5e", "info": "#22d3ee",
        "chart_1": "#22d3ee", "chart_2": "#818cf8", "chart_3": "#10d982", "chart_4": "#fbbf24",
        "sidebar_accent": "#22d3ee", "nav_active_bg": "rgba(34,211,238,0.12)",
        "badge_bg": "rgba(34,211,238,0.15)", "streak_color": "#fbbf24",
    },

    # ─── 2. CLINICAL PRECISION ── Apple Health Meets Medical Science ───────────
    "🩺 Clinical Precision": {
        "name": "Clinical Precision", "family": "light",
        "primary": "#0066cc", "primary_glow": "rgba(0,102,204,0.20)",
        "secondary": "#34c759", "accent": "#004a9f",
        "bg": "#f5f7fa", "surface": "#ffffff", "surface_raised": "#eef1f6",
        "card_bg": "rgba(255,255,255,0.92)", "card_border": "rgba(0,102,204,0.14)",
        "sidebar_bg": "#1c3557",
        "glass_bg": "rgba(255,255,255,0.75)", "glass_border": "rgba(0,102,204,0.22)",
        "glass_blur": "20px",
        "text": "#0d1f3c", "text_muted": "#3a5280", "subtext": "#6b82a8",
        "text_inverse": "#ffffff",
        "gradient": "linear-gradient(135deg,#0066cc,#34c759)",
        "hero_gradient": "linear-gradient(160deg,#f5f7fa 0%,#eaf0fb 55%,#e0eaf8 100%)",
        "card_gradient": "linear-gradient(145deg,rgba(255,255,255,0.97),rgba(238,241,246,0.88))",
        "glow": "0 0 28px rgba(0,102,204,0.18)", "glow_lg": "0 0 60px rgba(0,102,204,0.10)",
        "shadow_sm": "0 1px 6px rgba(13,31,60,0.07)", "shadow_md": "0 6px 24px rgba(13,31,60,0.10)",
        "shadow_lg": "0 16px 52px rgba(13,31,60,0.14)", "hover_bg": "rgba(0,102,204,0.06)",
        "focus_ring": "0 0 0 3px rgba(0,102,204,0.25)",
        "success": "#34c759", "warning": "#ff9500", "error": "#ff3b30", "info": "#0066cc",
        "chart_1": "#0066cc", "chart_2": "#34c759", "chart_3": "#ff9500", "chart_4": "#af52de",
        "sidebar_accent": "#22d3ee", "nav_active_bg": "rgba(255,255,255,0.15)",
        "badge_bg": "rgba(34,199,89,0.18)", "streak_color": "#ff9500",
    },

    # ─── 3. DNA MATRIX ── Bioluminescent Green Lab Aesthetic ──────────────────
    "🧬 DNA Matrix": {
        "name": "DNA Matrix", "family": "dark",
        "primary": "#00ffa3", "primary_glow": "rgba(0,255,163,0.28)",
        "secondary": "#00cc82", "accent": "#004433",
        "bg": "#000d07", "surface": "#011208", "surface_raised": "#01180a",
        "card_bg": "rgba(1,18,8,0.85)", "card_border": "rgba(0,255,163,0.14)",
        "sidebar_bg": "#00080300",
        "glass_bg": "rgba(0,255,163,0.04)", "glass_border": "rgba(0,255,163,0.18)",
        "glass_blur": "26px",
        "text": "#ccffe8", "text_muted": "#5aad88", "subtext": "#2a6650",
        "text_inverse": "#000d07",
        "gradient": "linear-gradient(135deg,#00ffa3,#00bfff)",
        "hero_gradient": "linear-gradient(160deg,#000d07 0%,#010e06 55%,#000d07 100%)",
        "card_gradient": "linear-gradient(145deg,rgba(0,255,163,0.06),rgba(0,191,255,0.03))",
        "glow": "0 0 44px rgba(0,255,163,0.26)", "glow_lg": "0 0 90px rgba(0,255,163,0.12)",
        "shadow_sm": "0 2px 8px rgba(0,0,0,0.60)", "shadow_md": "0 8px 32px rgba(0,0,0,0.70)",
        "shadow_lg": "0 24px 64px rgba(0,0,0,0.80)", "hover_bg": "rgba(0,255,163,0.07)",
        "focus_ring": "0 0 0 3px rgba(0,255,163,0.32)",
        "success": "#00ffa3", "warning": "#ffe066", "error": "#ff4466", "info": "#00bfff",
        "chart_1": "#00ffa3", "chart_2": "#00bfff", "chart_3": "#ffe066", "chart_4": "#ff77aa",
        "sidebar_accent": "#00ffa3", "nav_active_bg": "rgba(0,255,163,0.10)",
        "badge_bg": "rgba(0,255,163,0.14)", "streak_color": "#ffe066",
        "sidebar_bg": "#000b05",
    },

    # ─── 4. CARDIAC PULSE ── Dark Premium with Living Red-Amber Heartbeat ──────
    "🫀 Cardiac Pulse": {
        "name": "Cardiac Pulse", "family": "dark",
        "primary": "#ff4757", "primary_glow": "rgba(255,71,87,0.32)",
        "secondary": "#ff8c42", "accent": "#8b0000",
        "bg": "#07000a", "surface": "#10000f", "surface_raised": "#160014",
        "card_bg": "rgba(16,0,15,0.85)", "card_border": "rgba(255,71,87,0.16)",
        "sidebar_bg": "#050008",
        "glass_bg": "rgba(255,71,87,0.05)", "glass_border": "rgba(255,71,87,0.20)",
        "glass_blur": "24px",
        "text": "#ffe4e8", "text_muted": "#cc8899", "subtext": "#774455",
        "text_inverse": "#07000a",
        "gradient": "linear-gradient(135deg,#ff4757,#ff8c42)",
        "hero_gradient": "linear-gradient(160deg,#07000a 0%,#120008 55%,#07000a 100%)",
        "card_gradient": "linear-gradient(145deg,rgba(255,71,87,0.08),rgba(255,140,66,0.04))",
        "glow": "0 0 44px rgba(255,71,87,0.30)", "glow_lg": "0 0 90px rgba(255,71,87,0.12)",
        "shadow_sm": "0 2px 8px rgba(0,0,0,0.65)", "shadow_md": "0 8px 32px rgba(0,0,0,0.75)",
        "shadow_lg": "0 24px 64px rgba(0,0,0,0.85)", "hover_bg": "rgba(255,71,87,0.09)",
        "focus_ring": "0 0 0 3px rgba(255,71,87,0.35)",
        "success": "#30d158", "warning": "#ff8c42", "error": "#ff4757", "info": "#64d2ff",
        "chart_1": "#ff4757", "chart_2": "#ff8c42", "chart_3": "#30d158", "chart_4": "#64d2ff",
        "sidebar_accent": "#ff4757", "nav_active_bg": "rgba(255,71,87,0.10)",
        "badge_bg": "rgba(255,71,87,0.15)", "streak_color": "#ff8c42",
    },

    # ─── 5. RADIOLOGY SUITE ── Pure X-Ray Monochrome Diagnostic Precision ──────
    "🔭 Radiology Suite": {
        "name": "Radiology Suite", "family": "dark",
        "primary": "#c8dfff", "primary_glow": "rgba(200,223,255,0.18)",
        "secondary": "#7fa8d8", "accent": "#3a6090",
        "bg": "#000000", "surface": "#060606", "surface_raised": "#0b0b0b",
        "card_bg": "rgba(6,6,6,0.90)", "card_border": "rgba(200,223,255,0.12)",
        "sidebar_bg": "#000000",
        "glass_bg": "rgba(200,223,255,0.035)", "glass_border": "rgba(200,223,255,0.14)",
        "glass_blur": "22px",
        "text": "#d8ebff", "text_muted": "#6688aa", "subtext": "#334455",
        "text_inverse": "#000000",
        "gradient": "linear-gradient(135deg,#c8dfff,#7fa8d8)",
        "hero_gradient": "linear-gradient(160deg,#000000 0%,#040810 55%,#000000 100%)",
        "card_gradient": "linear-gradient(145deg,rgba(200,223,255,0.05),rgba(127,168,216,0.03))",
        "glow": "0 0 32px rgba(200,223,255,0.16)", "glow_lg": "0 0 70px rgba(200,223,255,0.08)",
        "shadow_sm": "0 2px 8px rgba(0,0,0,0.80)", "shadow_md": "0 8px 32px rgba(0,0,0,0.88)",
        "shadow_lg": "0 24px 64px rgba(0,0,0,0.95)", "hover_bg": "rgba(200,223,255,0.06)",
        "focus_ring": "0 0 0 3px rgba(200,223,255,0.22)",
        "success": "#30d158", "warning": "#ffd60a", "error": "#ff453a", "info": "#64d2ff",
        "chart_1": "#c8dfff", "chart_2": "#64d2ff", "chart_3": "#30d158", "chart_4": "#ffd60a",
        "sidebar_accent": "#c8dfff", "nav_active_bg": "rgba(200,223,255,0.08)",
        "badge_bg": "rgba(200,223,255,0.10)", "streak_color": "#ffd60a",
    },

    # ─── 6. DEEPWATER ICU ── Ocean-Depth Dark Aqua Intelligence ───────────────
    "🌊 Deepwater ICU": {
        "name": "Deepwater ICU", "family": "dark",
        "primary": "#06b6d4", "primary_glow": "rgba(6,182,212,0.30)",
        "secondary": "#0284c7", "accent": "#0c4a6e",
        "bg": "#00080f", "surface": "#010e1c", "surface_raised": "#021626",
        "card_bg": "rgba(1,14,28,0.85)", "card_border": "rgba(6,182,212,0.15)",
        "sidebar_bg": "#000710",
        "glass_bg": "rgba(6,182,212,0.05)", "glass_border": "rgba(6,182,212,0.20)",
        "glass_blur": "26px",
        "text": "#caf4ff", "text_muted": "#4a9ab5", "subtext": "#1f5a72",
        "text_inverse": "#00080f",
        "gradient": "linear-gradient(135deg,#06b6d4,#0284c7)",
        "hero_gradient": "linear-gradient(160deg,#00080f 0%,#010e20 55%,#00080f 100%)",
        "card_gradient": "linear-gradient(145deg,rgba(6,182,212,0.07),rgba(2,132,199,0.04))",
        "glow": "0 0 44px rgba(6,182,212,0.28)", "glow_lg": "0 0 90px rgba(6,182,212,0.12)",
        "shadow_sm": "0 2px 8px rgba(0,0,0,0.60)", "shadow_md": "0 8px 32px rgba(0,0,0,0.70)",
        "shadow_lg": "0 24px 64px rgba(0,0,0,0.80)", "hover_bg": "rgba(6,182,212,0.08)",
        "focus_ring": "0 0 0 3px rgba(6,182,212,0.32)",
        "success": "#10d982", "warning": "#fbbf24", "error": "#f43f5e", "info": "#06b6d4",
        "chart_1": "#06b6d4", "chart_2": "#818cf8", "chart_3": "#10d982", "chart_4": "#fbbf24",
        "sidebar_accent": "#06b6d4", "nav_active_bg": "rgba(6,182,212,0.10)",
        "badge_bg": "rgba(6,182,212,0.14)", "streak_color": "#fbbf24",
    },

    # ─── 7. DESERT HEALER ── Warm Oman-Inspired Amber Sand Premium Light ───────
    "☀️ Desert Healer": {
        "name": "Desert Healer", "family": "warm",
        "primary": "#d97706", "primary_glow": "rgba(217,119,6,0.24)",
        "secondary": "#b45309", "accent": "#78350f",
        "bg": "#fdf8f0", "surface": "#fffcf5", "surface_raised": "#fef3d8",
        "card_bg": "rgba(255,252,240,0.92)", "card_border": "rgba(217,119,6,0.22)",
        "sidebar_bg": "#1c1408",
        "glass_bg": "rgba(255,252,240,0.72)", "glass_border": "rgba(217,119,6,0.30)",
        "glass_blur": "18px",
        "text": "#1c0f00", "text_muted": "#6b3e00", "subtext": "#9a6e3a",
        "text_inverse": "#ffffff",
        "gradient": "linear-gradient(135deg,#d97706,#b45309)",
        "hero_gradient": "linear-gradient(160deg,#fdf8f0 0%,#fef3d8 55%,#fce9b8 100%)",
        "card_gradient": "linear-gradient(145deg,rgba(255,252,240,0.97),rgba(254,243,216,0.88))",
        "glow": "0 0 28px rgba(217,119,6,0.22)", "glow_lg": "0 0 60px rgba(217,119,6,0.10)",
        "shadow_sm": "0 2px 8px rgba(28,15,0,0.10)", "shadow_md": "0 8px 28px rgba(28,15,0,0.14)",
        "shadow_lg": "0 20px 52px rgba(28,15,0,0.18)", "hover_bg": "rgba(217,119,6,0.07)",
        "focus_ring": "0 0 0 3px rgba(217,119,6,0.28)",
        "success": "#16a34a", "warning": "#d97706", "error": "#dc2626", "info": "#0284c7",
        "chart_1": "#d97706", "chart_2": "#b45309", "chart_3": "#16a34a", "chart_4": "#7c3aed",
        "sidebar_accent": "#d97706", "nav_active_bg": "rgba(255,255,255,0.15)",
        "badge_bg": "rgba(217,119,6,0.15)", "streak_color": "#d97706",
    },

    # ─── 8. SAKURA WARD ── Soft Japanese Aesthetic for Calm Focus ─────────────
    "🌸 Sakura Ward": {
        "name": "Sakura Ward", "family": "light",
        "primary": "#e879a0", "primary_glow": "rgba(232,121,160,0.22)",
        "secondary": "#f0abcb", "accent": "#9d174d",
        "bg": "#fdf4f8", "surface": "#ffffff", "surface_raised": "#fce8f2",
        "card_bg": "rgba(255,255,255,0.90)", "card_border": "rgba(232,121,160,0.20)",
        "sidebar_bg": "#2a0f1e",
        "glass_bg": "rgba(255,255,255,0.72)", "glass_border": "rgba(232,121,160,0.28)",
        "glass_blur": "18px",
        "text": "#1a040f", "text_muted": "#78304e", "subtext": "#b07090",
        "text_inverse": "#ffffff",
        "gradient": "linear-gradient(135deg,#e879a0,#f9a8d4)",
        "hero_gradient": "linear-gradient(160deg,#fdf4f8 0%,#fce8f2 55%,#fad6e8 100%)",
        "card_gradient": "linear-gradient(145deg,rgba(255,255,255,0.97),rgba(252,232,242,0.88))",
        "glow": "0 0 28px rgba(232,121,160,0.22)", "glow_lg": "0 0 60px rgba(232,121,160,0.10)",
        "shadow_sm": "0 2px 8px rgba(26,4,15,0.08)", "shadow_md": "0 8px 28px rgba(26,4,15,0.12)",
        "shadow_lg": "0 20px 52px rgba(26,4,15,0.16)", "hover_bg": "rgba(232,121,160,0.07)",
        "focus_ring": "0 0 0 3px rgba(232,121,160,0.28)",
        "success": "#10b981", "warning": "#f59e0b", "error": "#ef4444", "info": "#6366f1",
        "chart_1": "#e879a0", "chart_2": "#818cf8", "chart_3": "#10b981", "chart_4": "#f59e0b",
        "sidebar_accent": "#e879a0", "nav_active_bg": "rgba(255,255,255,0.15)",
        "badge_bg": "rgba(232,121,160,0.14)", "streak_color": "#f59e0b",
    },

    # ─── 9. NEURAL INTERFACE ── Cyberpunk Electric Purple-Blue ────────────────
    "⚡ Neural Interface": {
        "name": "Neural Interface", "family": "dark",
        "primary": "#a855f7", "primary_glow": "rgba(168,85,247,0.32)",
        "secondary": "#3b82f6", "accent": "#581c87",
        "bg": "#04000c", "surface": "#080014", "surface_raised": "#0c001e",
        "card_bg": "rgba(8,0,20,0.85)", "card_border": "rgba(168,85,247,0.16)",
        "sidebar_bg": "#030009",
        "glass_bg": "rgba(168,85,247,0.05)", "glass_border": "rgba(168,85,247,0.20)",
        "glass_blur": "30px",
        "text": "#f0e8ff", "text_muted": "#9d7acc", "subtext": "#5c3d88",
        "text_inverse": "#04000c",
        "gradient": "linear-gradient(135deg,#a855f7,#3b82f6)",
        "hero_gradient": "linear-gradient(160deg,#04000c 0%,#090018 55%,#04000c 100%)",
        "card_gradient": "linear-gradient(145deg,rgba(168,85,247,0.08),rgba(59,130,246,0.04))",
        "glow": "0 0 44px rgba(168,85,247,0.30)", "glow_lg": "0 0 90px rgba(168,85,247,0.13)",
        "shadow_sm": "0 2px 8px rgba(0,0,0,0.70)", "shadow_md": "0 8px 32px rgba(0,0,0,0.78)",
        "shadow_lg": "0 24px 64px rgba(0,0,0,0.86)", "hover_bg": "rgba(168,85,247,0.09)",
        "focus_ring": "0 0 0 3px rgba(168,85,247,0.35)",
        "success": "#10d982", "warning": "#fbbf24", "error": "#f43f5e", "info": "#38bdf8",
        "chart_1": "#a855f7", "chart_2": "#3b82f6", "chart_3": "#10d982", "chart_4": "#fbbf24",
        "sidebar_accent": "#a855f7", "nav_active_bg": "rgba(168,85,247,0.10)",
        "badge_bg": "rgba(168,85,247,0.15)", "streak_color": "#fbbf24",
    },

    # ─── 10. RAINFOREST MEDICINE ── Rich Botanical Deep Green Serenity ─────────
    "🌿 Rainforest Medicine": {
        "name": "Rainforest Medicine", "family": "dark",
        "primary": "#4ade80", "primary_glow": "rgba(74,222,128,0.28)",
        "secondary": "#22c55e", "accent": "#14532d",
        "bg": "#010a04", "surface": "#020e06", "surface_raised": "#031409",
        "card_bg": "rgba(2,14,6,0.85)", "card_border": "rgba(74,222,128,0.14)",
        "sidebar_bg": "#010703",
        "glass_bg": "rgba(74,222,128,0.045)", "glass_border": "rgba(74,222,128,0.18)",
        "glass_blur": "24px",
        "text": "#dcfce7", "text_muted": "#52876a", "subtext": "#244a30",
        "text_inverse": "#010a04",
        "gradient": "linear-gradient(135deg,#4ade80,#22c55e)",
        "hero_gradient": "linear-gradient(160deg,#010a04 0%,#020e06 55%,#010a04 100%)",
        "card_gradient": "linear-gradient(145deg,rgba(74,222,128,0.07),rgba(34,197,94,0.03))",
        "glow": "0 0 40px rgba(74,222,128,0.26)", "glow_lg": "0 0 85px rgba(74,222,128,0.11)",
        "shadow_sm": "0 2px 8px rgba(0,0,0,0.60)", "shadow_md": "0 8px 32px rgba(0,0,0,0.70)",
        "shadow_lg": "0 24px 64px rgba(0,0,0,0.80)", "hover_bg": "rgba(74,222,128,0.08)",
        "focus_ring": "0 0 0 3px rgba(74,222,128,0.32)",
        "success": "#4ade80", "warning": "#fbbf24", "error": "#f43f5e", "info": "#38bdf8",
        "chart_1": "#4ade80", "chart_2": "#38bdf8", "chart_3": "#fbbf24", "chart_4": "#c084fc",
        "sidebar_accent": "#4ade80", "nav_active_bg": "rgba(74,222,128,0.10)",
        "badge_bg": "rgba(74,222,128,0.14)", "streak_color": "#fbbf24",
    },

    # ─── 11. GRAND ROUNDS ── Prestige Navy & Gold Academic Excellence ──────────
    "🏛️ Grand Rounds": {
        "name": "Grand Rounds", "family": "dark",
        "primary": "#f59e0b", "primary_glow": "rgba(245,158,11,0.28)",
        "secondary": "#d97706", "accent": "#78350f",
        "bg": "#030614", "surface": "#070c22", "surface_raised": "#0b1130",
        "card_bg": "rgba(7,12,34,0.85)", "card_border": "rgba(245,158,11,0.14)",
        "sidebar_bg": "#020510",
        "glass_bg": "rgba(245,158,11,0.04)", "glass_border": "rgba(245,158,11,0.18)",
        "glass_blur": "24px",
        "text": "#fff8e8", "text_muted": "#b8922a", "subtext": "#6b5012",
        "text_inverse": "#030614",
        "gradient": "linear-gradient(135deg,#f59e0b,#d97706)",
        "hero_gradient": "linear-gradient(160deg,#030614 0%,#070a20 55%,#030614 100%)",
        "card_gradient": "linear-gradient(145deg,rgba(245,158,11,0.07),rgba(217,119,6,0.03))",
        "glow": "0 0 44px rgba(245,158,11,0.26)", "glow_lg": "0 0 90px rgba(245,158,11,0.12)",
        "shadow_sm": "0 2px 8px rgba(0,0,0,0.60)", "shadow_md": "0 8px 32px rgba(0,0,0,0.70)",
        "shadow_lg": "0 24px 64px rgba(0,0,0,0.80)", "hover_bg": "rgba(245,158,11,0.08)",
        "focus_ring": "0 0 0 3px rgba(245,158,11,0.30)",
        "success": "#10d982", "warning": "#f59e0b", "error": "#f43f5e", "info": "#38bdf8",
        "chart_1": "#f59e0b", "chart_2": "#38bdf8", "chart_3": "#10d982", "chart_4": "#c084fc",
        "sidebar_accent": "#f59e0b", "nav_active_bg": "rgba(245,158,11,0.10)",
        "badge_bg": "rgba(245,158,11,0.15)", "streak_color": "#f59e0b",
    },

    # ─── 12. QUANTUM LAB ── Holographic Iridescent Multi-Spectrum Dark ─────────
    "🔬 Quantum Lab": {
        "name": "Quantum Lab", "family": "dark",
        "primary": "#e879f9", "primary_glow": "rgba(232,121,249,0.30)",
        "secondary": "#06b6d4", "accent": "#701a75",
        "bg": "#030008", "surface": "#070010", "surface_raised": "#0b0018",
        "card_bg": "rgba(7,0,16,0.85)", "card_border": "rgba(232,121,249,0.14)",
        "sidebar_bg": "#020006",
        "glass_bg": "rgba(232,121,249,0.045)", "glass_border": "rgba(232,121,249,0.18)",
        "glass_blur": "32px",
        "text": "#fce8ff", "text_muted": "#9d5ab5", "subtext": "#4a2060",
        "text_inverse": "#030008",
        "gradient": "linear-gradient(135deg,#e879f9,#06b6d4)",
        "hero_gradient": "linear-gradient(160deg,#030008 0%,#080012 55%,#030008 100%)",
        "card_gradient": "linear-gradient(145deg,rgba(232,121,249,0.08),rgba(6,182,212,0.04))",
        "glow": "0 0 44px rgba(232,121,249,0.28)", "glow_lg": "0 0 90px rgba(232,121,249,0.12)",
        "shadow_sm": "0 2px 8px rgba(0,0,0,0.70)", "shadow_md": "0 8px 32px rgba(0,0,0,0.80)",
        "shadow_lg": "0 24px 64px rgba(0,0,0,0.88)", "hover_bg": "rgba(232,121,249,0.08)",
        "focus_ring": "0 0 0 3px rgba(232,121,249,0.32)",
        "success": "#10d982", "warning": "#fbbf24", "error": "#f43f5e", "info": "#06b6d4",
        "chart_1": "#e879f9", "chart_2": "#06b6d4", "chart_3": "#10d982", "chart_4": "#fbbf24",
        "sidebar_accent": "#e879f9", "nav_active_bg": "rgba(232,121,249,0.10)",
        "badge_bg": "rgba(232,121,249,0.14)", "streak_color": "#fbbf24",
    },

    # ─── 13. AURORA BOREALIS ── Nordic Dark with Living Green-Purple Aurora ─────
    "🌅 Aurora Borealis": {
        "name": "Aurora Borealis", "family": "dark",
        "primary": "#34d399", "primary_glow": "rgba(52,211,153,0.28)",
        "secondary": "#818cf8", "accent": "#064e3b",
        "bg": "#010c0a", "surface": "#021510", "surface_raised": "#031c16",
        "card_bg": "rgba(2,21,16,0.85)", "card_border": "rgba(52,211,153,0.14)",
        "sidebar_bg": "#000d08",
        "glass_bg": "rgba(52,211,153,0.05)", "glass_border": "rgba(52,211,153,0.18)",
        "glass_blur": "28px",
        "text": "#d1fae5", "text_muted": "#3d9e78", "subtext": "#174534",
        "text_inverse": "#010c0a",
        "gradient": "linear-gradient(135deg,#34d399,#818cf8)",
        "hero_gradient": "linear-gradient(160deg,#010c0a 0%,#021410 55%,#010c0a 100%)",
        "card_gradient": "linear-gradient(145deg,rgba(52,211,153,0.07),rgba(129,140,248,0.03))",
        "glow": "0 0 44px rgba(52,211,153,0.26)", "glow_lg": "0 0 90px rgba(52,211,153,0.11)",
        "shadow_sm": "0 2px 8px rgba(0,0,0,0.60)", "shadow_md": "0 8px 32px rgba(0,0,0,0.70)",
        "shadow_lg": "0 24px 64px rgba(0,0,0,0.80)", "hover_bg": "rgba(52,211,153,0.08)",
        "focus_ring": "0 0 0 3px rgba(52,211,153,0.30)",
        "success": "#34d399", "warning": "#fbbf24", "error": "#f43f5e", "info": "#818cf8",
        "chart_1": "#34d399", "chart_2": "#818cf8", "chart_3": "#fbbf24", "chart_4": "#f43f5e",
        "sidebar_accent": "#34d399", "nav_active_bg": "rgba(52,211,153,0.10)",
        "badge_bg": "rgba(52,211,153,0.14)", "streak_color": "#fbbf24",
    },

    # ─── 14. IVORY ATLAS ── Warm Cream Academic Minimalism ───────────────────
    "📜 Ivory Atlas": {
        "name": "Ivory Atlas", "family": "light",
        "primary": "#7c5c28", "primary_glow": "rgba(124,92,40,0.20)",
        "secondary": "#1e3a6e", "accent": "#4a3200",
        "bg": "#fbf9f3", "surface": "#ffffff", "surface_raised": "#f5f2e8",
        "card_bg": "rgba(255,255,250,0.93)", "card_border": "rgba(124,92,40,0.18)",
        "sidebar_bg": "#1a1206",
        "glass_bg": "rgba(255,255,250,0.76)", "glass_border": "rgba(124,92,40,0.26)",
        "glass_blur": "16px",
        "text": "#16100a", "text_muted": "#4a3818", "subtext": "#7a6440",
        "text_inverse": "#ffffff",
        "gradient": "linear-gradient(135deg,#7c5c28,#1e3a6e)",
        "hero_gradient": "linear-gradient(160deg,#fbf9f3 0%,#f5f2e8 55%,#ede8d2 100%)",
        "card_gradient": "linear-gradient(145deg,rgba(255,255,250,0.97),rgba(245,242,232,0.88))",
        "glow": "0 0 28px rgba(124,92,40,0.18)", "glow_lg": "0 0 60px rgba(124,92,40,0.09)",
        "shadow_sm": "0 2px 8px rgba(22,16,10,0.09)", "shadow_md": "0 8px 28px rgba(22,16,10,0.13)",
        "shadow_lg": "0 20px 52px rgba(22,16,10,0.17)", "hover_bg": "rgba(124,92,40,0.07)",
        "focus_ring": "0 0 0 3px rgba(124,92,40,0.26)",
        "success": "#16a34a", "warning": "#b45309", "error": "#c0392b", "info": "#1e3a6e",
        "chart_1": "#7c5c28", "chart_2": "#1e3a6e", "chart_3": "#16a34a", "chart_4": "#b45309",
        "sidebar_accent": "#f59e0b", "nav_active_bg": "rgba(255,255,255,0.15)",
        "badge_bg": "rgba(124,92,40,0.12)", "streak_color": "#b45309",
    },

    # ─── 15. MODERN ER ── High-Contrast Urgent Blue-White Emergency Design ─────
    "🏥 Modern ER": {
        "name": "Modern ER", "family": "light",
        "primary": "#2563eb", "primary_glow": "rgba(37,99,235,0.22)",
        "secondary": "#16a34a", "accent": "#1d4ed8",
        "bg": "#f8faff", "surface": "#ffffff", "surface_raised": "#eef3ff",
        "card_bg": "rgba(255,255,255,0.94)", "card_border": "rgba(37,99,235,0.16)",
        "sidebar_bg": "#0f172a",
        "glass_bg": "rgba(255,255,255,0.78)", "glass_border": "rgba(37,99,235,0.24)",
        "glass_blur": "18px",
        "text": "#0a1628", "text_muted": "#2a4080", "subtext": "#6680b0",
        "text_inverse": "#ffffff",
        "gradient": "linear-gradient(135deg,#2563eb,#16a34a)",
        "hero_gradient": "linear-gradient(160deg,#f8faff 0%,#eef3ff 55%,#e4edff 100%)",
        "card_gradient": "linear-gradient(145deg,rgba(255,255,255,0.97),rgba(238,243,255,0.88))",
        "glow": "0 0 28px rgba(37,99,235,0.18)", "glow_lg": "0 0 60px rgba(37,99,235,0.09)",
        "shadow_sm": "0 1px 6px rgba(10,22,40,0.08)", "shadow_md": "0 6px 24px rgba(10,22,40,0.12)",
        "shadow_lg": "0 16px 52px rgba(10,22,40,0.16)", "hover_bg": "rgba(37,99,235,0.06)",
        "focus_ring": "0 0 0 3px rgba(37,99,235,0.26)",
        "success": "#16a34a", "warning": "#d97706", "error": "#dc2626", "info": "#2563eb",
        "chart_1": "#2563eb", "chart_2": "#16a34a", "chart_3": "#d97706", "chart_4": "#dc2626",
        "sidebar_accent": "#38bdf8", "nav_active_bg": "rgba(255,255,255,0.15)",
        "badge_bg": "rgba(37,99,235,0.12)", "streak_color": "#d97706",
    },
}


# ═══════════════════════════════════════════════════════════════════════════════
# THEME MANAGER — Injects CSS into Streamlit
# ═══════════════════════════════════════════════════════════════════════════════

class ThemeManager:
    def __init__(self, theme_key: str):
        self.key = theme_key
        self.t   = THEMES.get(theme_key, THEMES["🌌 Midnight Rounds"])

    def inject(self) -> str:
        t   = self.t
        p   = t["primary"]
        sb  = t["sidebar_bg"]
        txt = t["text"]
        cs  = "dark" if t.get("family") == "dark" else "light"
        sa  = t.get("sidebar_accent", p)
        nab = t.get("nav_active_bg", "rgba(255,255,255,0.12)")
        is_dark = t.get("family") == "dark"
        sidebar_txt = "#e8f4ff" if is_dark else "#f0f4ff"
        sidebar_sub = "rgba(232,244,255,0.55)" if is_dark else "rgba(240,244,255,0.65)"

        return f"""<style>
/* ═══════════════════════════════════════════════════════════════════
   MedStudy Oman — Next-Gen Design System
   Fonts: Bricolage Grotesque (headings) + Plus Jakarta Sans (body) + DM Mono
   ═══════════════════════════════════════════════════════════════════ */
@import url('https://fonts.googleapis.com/css2?family=Bricolage+Grotesque:opsz,wght@12..96,300;12..96,400;12..96,500;12..96,600;12..96,700;12..96,800;12..96,900&family=Plus+Jakarta+Sans:ital,wght@0,300;0,400;0,500;0,600;0,700;0,800;1,400&family=DM+Mono:wght@400;500&display=swap');

/* ── CSS Custom Properties ─────────────────────────────────────── */
:root {{
    color-scheme: {cs};
    --primary:        {t["primary"]};
    --primary-glow:   {t["primary_glow"]};
    --secondary:      {t["secondary"]};
    --accent:         {t["accent"]};
    --bg:             {t["bg"]};
    --surface:        {t["surface"]};
    --surface-raised: {t["surface_raised"]};
    --card-bg:        {t["card_bg"]};
    --card-border:    {t["card_border"]};
    --sidebar-bg:     {sb};
    --glass-bg:       {t["glass_bg"]};
    --glass-border:   {t["glass_border"]};
    --blur:           {t["glass_blur"]};
    --text:           {t["text"]};
    --text-muted:     {t["text_muted"]};
    --subtext:        {t["subtext"]};
    --text-inverse:   {t["text_inverse"]};
    --gradient:       {t["gradient"]};
    --hero-gradient:  {t["hero_gradient"]};
    --card-gradient:  {t["card_gradient"]};
    --glow:           {t["glow"]};
    --glow-lg:        {t.get("glow_lg", t["glow"])};
    --shadow-sm:      {t["shadow_sm"]};
    --shadow-md:      {t["shadow_md"]};
    --shadow-lg:      {t["shadow_lg"]};
    --hover-bg:       {t["hover_bg"]};
    --focus-ring:     {t["focus_ring"]};
    --success:        {t["success"]};
    --warning:        {t["warning"]};
    --error:          {t["error"]};
    --info:           {t["info"]};
    --sidebar-accent: {sa};
    --nav-active-bg:  {nab};
    --badge-bg:       {t.get("badge_bg", t["glass_bg"])};
    --streak-color:   {t.get("streak_color", t["warning"])};
    /* Spacing scale */
    --space-1: 0.25rem; --space-2: 0.5rem; --space-3: 0.75rem;
    --space-4: 1rem;    --space-5: 1.25rem; --space-6: 1.5rem;
    --space-8: 2rem;    --space-10: 2.5rem; --space-12: 3rem;
    /* Radius scale */
    --r-sm: 8px; --r-md: 14px; --r-lg: 20px; --r-xl: 28px; --r-full: 9999px;
    /* Transition */
    --ease: cubic-bezier(0.22,1,0.36,1);
    --duration: 0.22s;
}}

/* ── Base Reset & Typography ────────────────────────────────────── */
*,*::before,*::after {{
    font-family: 'Plus Jakarta Sans', system-ui, sans-serif !important;
    -webkit-font-smoothing: antialiased;
    -moz-osx-font-smoothing: grayscale;
    box-sizing: border-box;
}}
h1,h2,h3,h4,h5,h6 {{
    font-family: 'Bricolage Grotesque', sans-serif !important;
    font-weight: 800 !important;
    letter-spacing: -0.03em;
    line-height: 1.1;
    color: var(--text) !important;
}}
code,pre,kbd {{ font-family: 'DM Mono', monospace !important; }}
html,body {{ background: var(--bg) !important; color: var(--text) !important; }}
.stApp {{ background: var(--hero-gradient) !important; }}

/* ── Transparent Containers ─────────────────────────────────────── */
.main,
.main .block-container,
[data-testid="stAppViewContainer"],
[data-testid="stAppViewContainer"] > .main,
[data-testid="stMain"],
[data-testid="stVerticalBlock"],
[data-testid="column"],
.element-container {{
    background: transparent !important;
    color: var(--text) !important;
}}

/* ── Text Propagation ───────────────────────────────────────────── */
p, li, span, label, td, th,
.stMarkdown, .stMarkdown *,
[data-testid="stMarkdownContainer"],
[data-testid="stMarkdownContainer"] * {{
    color: var(--text) !important;
}}
small, .stCaption {{ color: var(--subtext) !important; }}

/* ── SIDEBAR — Premium Design ────────────────────────────────────── */
html body section[data-testid="stSidebar"],
html body [data-testid="stSidebar"],
html body [data-testid="stSidebar"] > div,
html body [data-testid="stSidebar"] > div > div,
html body [data-testid="stSidebar"] > div > div > div {{
    background-color: {sb} !important;
    background:       {sb} !important;
    min-width: 260px !important;
    max-width: 290px !important;
    border-right: 1px solid var(--glass-border) !important;
    box-shadow: 4px 0 40px rgba(0,0,0,0.35) !important;
}}
html body [data-testid="stSidebar"] p,
html body [data-testid="stSidebar"] span,
html body [data-testid="stSidebar"] label,
html body [data-testid="stSidebar"] div {{
    color: {sidebar_txt} !important;
}}

/* ── SIDEBAR FIX: Override Streamlit's translateX slide-out ─────── */
/* Streamlit hides the sidebar with transform:translateX(-100%).     */
/* We force it back to translateX(0) regardless of aria-expanded.   */
[data-testid="stSidebar"] {{
    transform: translateX(0) !important;
    margin-left: 0 !important;
    visibility: visible !important;
}}
[data-testid="stSidebar"][aria-expanded="false"] {{
    transform: translateX(0) !important;
    margin-left: 0 !important;
    min-width: 260px !important;
    width: 260px !important;
    visibility: visible !important;
}}
[data-testid="stSidebar"] > div:first-child {{
    min-width: 260px !important;
    transform: translateX(0) !important;
}}
/* Hide the collapse toggle so users cannot hide the sidebar */
[data-testid="collapsedControl"] {{
    display: none !important;
}}

/* ── Header ─────────────────────────────────────────────────────── */
[data-testid="stHeader"] {{
    background: transparent !important;
    border-bottom: none !important;
}}

/* ── Hide Chrome Clutter ─────────────────────────────────────────── */
[data-testid="stToolbar"],
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
[data-testid="stDeployButton"],
#MainMenu, footer {{
    display: none !important;
}}

/* ── Block Container ─────────────────────────────────────────────── */
.block-container {{
    padding-top: 1.8rem !important;
    padding-bottom: 4rem !important;
    max-width: 1400px !important;
}}

/* ── Premium Input Fields ────────────────────────────────────────── */
.stTextInput > div > div > input,
.stTextArea > div > div > textarea,
.stNumberInput > div > div > input {{
    background: var(--glass-bg) !important;
    color: var(--text) !important;
    border: 1.5px solid var(--card-border) !important;
    border-radius: var(--r-md) !important;
    font-size: 0.95rem !important;
    padding: 0.65rem 1rem !important;
    transition: border-color var(--duration) var(--ease), box-shadow var(--duration) var(--ease) !important;
    backdrop-filter: blur(var(--blur)) !important;
}}
.stTextInput > div > div > input:focus,
.stTextArea > div > div > textarea:focus,
.stNumberInput > div > div > input:focus {{
    border-color: var(--primary) !important;
    box-shadow: var(--focus-ring) !important;
    outline: none !important;
}}

/* ── Premium Select ─────────────────────────────────────────────── */
.stSelectbox > div > div,
.stMultiSelect > div > div {{
    background: var(--glass-bg) !important;
    color: var(--text) !important;
    border: 1.5px solid var(--card-border) !important;
    border-radius: var(--r-md) !important;
    backdrop-filter: blur(var(--blur)) !important;
}}
[data-baseweb="popover"] > div,
[data-baseweb="menu"] {{
    background: var(--surface) !important;
    border: 1px solid var(--card-border) !important;
    border-radius: var(--r-lg) !important;
    box-shadow: var(--shadow-lg) !important;
    backdrop-filter: blur(var(--blur)) !important;
}}
[role="option"] {{ color: var(--text) !important; background: transparent !important; }}
[role="option"]:hover {{ background: var(--hover-bg) !important; border-radius: var(--r-sm) !important; }}

/* ── Premium Buttons ─────────────────────────────────────────────── */
.stButton > button {{
    background: var(--glass-bg) !important;
    border: 1.5px solid var(--card-border) !important;
    border-radius: var(--r-md) !important;
    color: var(--text) !important;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
    letter-spacing: 0.01em;
    min-height: 44px !important;
    padding: 0.55rem 1.4rem !important;
    transition: all var(--duration) var(--ease) !important;
    backdrop-filter: blur(12px) !important;
    position: relative;
    overflow: hidden;
}}
.stButton > button::before {{
    content: '';
    position: absolute;
    inset: 0;
    background: var(--gradient);
    opacity: 0;
    transition: opacity var(--duration) var(--ease);
    border-radius: inherit;
}}
.stButton > button:hover {{
    border-color: var(--primary) !important;
    color: var(--text-inverse) !important;
    transform: translateY(-2px) !important;
    box-shadow: var(--glow), var(--shadow-md) !important;
}}
.stButton > button:hover::before {{ opacity: 1; }}
.stButton > button:hover span {{ position: relative; z-index: 1; }}
.stButton > button:active {{ transform: translateY(0) !important; }}
.stButton > button[kind="primary"] {{
    background: var(--gradient) !important;
    border: none !important;
    color: var(--text-inverse) !important;
    box-shadow: var(--glow) !important;
}}
.stButton > button[kind="primary"]:hover {{
    box-shadow: var(--glow-lg), var(--shadow-md) !important;
    transform: translateY(-3px) !important;
}}

/* ── Premium Tabs ────────────────────────────────────────────────── */
.stTabs [data-baseweb="tab-list"] {{
    background: var(--glass-bg) !important;
    border: 1px solid var(--card-border) !important;
    border-radius: var(--r-full) !important;
    padding: 5px !important;
    gap: 2px !important;
    backdrop-filter: blur(var(--blur)) !important;
}}
.stTabs [data-baseweb="tab"] {{
    color: var(--text-muted) !important;
    background: transparent !important;
    border: none !important;
    border-radius: var(--r-full) !important;
    font-weight: 600 !important;
    font-size: 0.88rem !important;
    padding: 0.45rem 1.1rem !important;
    transition: all var(--duration) var(--ease) !important;
}}
.stTabs [aria-selected="true"] {{
    background: var(--gradient) !important;
    color: var(--text-inverse) !important;
    box-shadow: var(--glow) !important;
}}

/* ── Forms & Expanders ───────────────────────────────────────────── */
[data-testid="stForm"] {{
    background: var(--glass-bg) !important;
    border: 1px solid var(--card-border) !important;
    border-radius: var(--r-xl) !important;
    padding: 1.5rem !important;
    backdrop-filter: blur(var(--blur)) !important;
}}
[data-testid="stForm"] * {{ color: var(--text) !important; }}
[data-testid="stExpander"] {{
    background: var(--glass-bg) !important;
    border: 1px solid var(--card-border) !important;
    border-radius: var(--r-lg) !important;
    backdrop-filter: blur(var(--blur)) !important;
    transition: box-shadow var(--duration) var(--ease) !important;
}}
[data-testid="stExpander"]:hover {{
    box-shadow: var(--shadow-md) !important;
}}
.streamlit-expanderHeader {{
    background: transparent !important;
    color: var(--text) !important;
    font-weight: 600 !important;
}}

/* ── Metrics ─────────────────────────────────────────────────────── */
[data-testid="metric-container"] {{
    background: var(--card-bg) !important;
    border: 1px solid var(--card-border) !important;
    border-radius: var(--r-lg) !important;
    padding: 1.2rem !important;
    backdrop-filter: blur(var(--blur)) !important;
    transition: transform var(--duration) var(--ease), box-shadow var(--duration) var(--ease) !important;
}}
[data-testid="metric-container"]:hover {{
    transform: translateY(-3px) !important;
    box-shadow: var(--shadow-md) !important;
}}
[data-testid="stMetricValue"] {{
    font-family: 'Bricolage Grotesque', sans-serif !important;
    font-size: 2rem !important;
    font-weight: 800 !important;
    color: var(--primary) !important;
}}
[data-testid="stMetricLabel"] {{
    font-size: 0.78rem !important;
    font-weight: 600 !important;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--subtext) !important;
}}
[data-testid="stMetricDelta"] {{
    font-size: 0.82rem !important;
    font-weight: 600 !important;
}}

/* ── Sliders ─────────────────────────────────────────────────────── */
[data-testid="stSlider"] [class*="thumb"] {{
    background: var(--primary) !important;
    box-shadow: var(--glow) !important;
    border: 2px solid var(--text-inverse) !important;
    width: 20px !important;
    height: 20px !important;
}}
[data-testid="stSlider"] [class*="track"] {{ background: var(--card-border) !important; }}
[data-testid="stSlider"] [class*="track"][class*="filled"] {{ background: var(--gradient) !important; }}

/* ── Checkboxes & Radio ──────────────────────────────────────────── */
[data-testid="stCheckbox"] input[type="checkbox"]:checked + div,
[data-testid="stRadio"] input[type="radio"]:checked + div {{
    background: var(--primary) !important;
    border-color: var(--primary) !important;
}}

/* ── Progress Bar ───────────────────────────────────────────────── */
.stProgress > div > div > div > div {{
    background: var(--gradient) !important;
    border-radius: var(--r-full) !important;
    box-shadow: var(--glow) !important;
}}

/* ── Info / Success / Warning / Error Alerts ────────────────────── */
[data-testid="stAlert"] {{
    border-radius: var(--r-lg) !important;
    border: 1px solid var(--card-border) !important;
    backdrop-filter: blur(12px) !important;
}}

/* ── Scrollbar ───────────────────────────────────────────────────── */
::-webkit-scrollbar {{ width: 4px; height: 4px; }}
::-webkit-scrollbar-track {{ background: transparent; }}
::-webkit-scrollbar-thumb {{
    background: var(--primary);
    border-radius: var(--r-full);
    opacity: 0.5;
}}
::-webkit-scrollbar-thumb:hover {{ opacity: 1; }}

/* ── Selection ───────────────────────────────────────────────────── */
::selection {{
    background: var(--primary-glow);
    color: var(--text);
}}

/* ═══════════════════════════════════════════════════════════════════
   PREMIUM COMPONENT LIBRARY
   ═══════════════════════════════════════════════════════════════════ */

/* ── Glass Card ─────────────────────────────────────────────────── */
.med-card {{
    background: var(--card-bg);
    border: 1px solid var(--card-border);
    border-radius: var(--r-xl);
    padding: var(--space-6);
    backdrop-filter: blur(var(--blur));
    -webkit-backdrop-filter: blur(var(--blur));
    transition: transform var(--duration) var(--ease),
                box-shadow var(--duration) var(--ease),
                border-color var(--duration) var(--ease);
    position: relative;
    overflow: hidden;
}}
.med-card::before {{
    content: '';
    position: absolute;
    inset: 0;
    background: var(--card-gradient);
    border-radius: inherit;
    pointer-events: none;
}}
.med-card:hover {{
    transform: translateY(-4px);
    box-shadow: var(--shadow-lg);
    border-color: var(--primary);
}}
.med-card-glow:hover {{
    box-shadow: var(--glow), var(--shadow-lg);
}}

/* ── Hero Badge ─────────────────────────────────────────────────── */
.med-badge {{
    display: inline-flex;
    align-items: center;
    gap: 6px;
    background: var(--badge-bg);
    border: 1px solid var(--card-border);
    border-radius: var(--r-full);
    padding: 0.28rem 0.85rem;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.08em;
    text-transform: uppercase;
    color: var(--primary) !important;
    backdrop-filter: blur(12px);
}}

/* ── Streak Widget ──────────────────────────────────────────────── */
.med-streak {{
    display: inline-flex;
    align-items: center;
    gap: 5px;
    background: var(--badge-bg);
    border-radius: var(--r-full);
    padding: 0.3rem 0.9rem;
    font-size: 0.85rem;
    font-weight: 800;
    color: var(--streak-color) !important;
}}

/* ── Primary Button ─────────────────────────────────────────────── */
.med-btn-primary {{
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    background: var(--gradient);
    border: none;
    border-radius: var(--r-md);
    padding: 0.7rem 1.6rem;
    font-family: 'Plus Jakarta Sans', sans-serif !important;
    font-size: 0.92rem;
    font-weight: 700;
    color: var(--text-inverse) !important;
    cursor: pointer;
    transition: all var(--duration) var(--ease);
    box-shadow: var(--glow);
    text-decoration: none;
}}
.med-btn-primary:hover {{
    transform: translateY(-3px);
    box-shadow: var(--glow-lg), var(--shadow-md);
}}

/* ── Section Label ──────────────────────────────────────────────── */
.med-label {{
    font-size: 0.68rem;
    font-weight: 800;
    letter-spacing: 0.14em;
    text-transform: uppercase;
    color: var(--primary) !important;
    margin-bottom: 0.4rem;
    display: block;
}}

/* ── Divider ────────────────────────────────────────────────────── */
.med-divider {{
    border: none;
    height: 1px;
    background: var(--card-border);
    margin: var(--space-6) 0;
}}

/* ── Floating AI Bubble ─────────────────────────────────────────── */
.ai-bubble {{
    position: fixed;
    bottom: 28px;
    right: 28px;
    z-index: 9999;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: var(--gradient);
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.6rem;
    cursor: pointer;
    box-shadow: var(--glow), var(--shadow-lg);
    transition: all var(--duration) var(--ease);
    animation: floatBubble 3s ease-in-out infinite;
}}
.ai-bubble:hover {{
    transform: scale(1.15);
    box-shadow: var(--glow-lg), var(--shadow-lg);
}}

/* ── Bento Grid ─────────────────────────────────────────────────── */
.bento-grid {{
    display: grid;
    grid-template-columns: repeat(auto-fit, minmax(280px, 1fr));
    gap: var(--space-5);
    margin: var(--space-6) 0;
}}

/* ── Stat Number ────────────────────────────────────────────────── */
.med-stat-value {{
    font-family: 'Bricolage Grotesque', sans-serif !important;
    font-size: 2.2rem;
    font-weight: 900;
    letter-spacing: -0.04em;
    line-height: 1;
    color: var(--primary) !important;
}}

/* ── Nav Item ────────────────────────────────────────────────────── */
.nav-item {{
    display: flex;
    align-items: center;
    gap: 10px;
    padding: 0.6rem 1rem;
    border-radius: var(--r-md);
    cursor: pointer;
    font-weight: 600;
    font-size: 0.9rem;
    color: {sidebar_sub} !important;
    transition: all var(--duration) var(--ease);
    margin-bottom: 2px;
}}
.nav-item:hover {{
    background: var(--nav-active-bg);
    color: {sidebar_txt} !important;
    transform: translateX(3px);
}}
.nav-item.active {{
    background: var(--nav-active-bg);
    color: {sidebar_txt} !important;
    border-left: 3px solid var(--sidebar-accent);
    padding-left: calc(1rem - 3px);
}}

/* ═══════════════════════════════════════════════════════════════════
   ANIMATIONS
   ═══════════════════════════════════════════════════════════════════ */

@keyframes fadeUp {{
    from {{ opacity:0; transform:translateY(24px); }}
    to   {{ opacity:1; transform:translateY(0); }}
}}
@keyframes fadeIn {{
    from {{ opacity:0; }}
    to   {{ opacity:1; }}
}}
@keyframes scaleIn {{
    from {{ opacity:0; transform:scale(0.93); }}
    to   {{ opacity:1; transform:scale(1); }}
}}
@keyframes floatBubble {{
    0%,100% {{ transform:translateY(0); }}
    50%     {{ transform:translateY(-8px); }}
}}
@keyframes glowPulse {{
    0%,100% {{ opacity:0.6; box-shadow:var(--glow); }}
    50%     {{ opacity:1;   box-shadow:var(--glow-lg); }}
}}
@keyframes shimmer {{
    0%   {{ background-position: -200% center; }}
    100% {{ background-position: 200% center; }}
}}
@keyframes heartbeat {{
    0%,100% {{ transform:scale(1); }}
    14%     {{ transform:scale(1.06); }}
    28%     {{ transform:scale(1); }}
    42%     {{ transform:scale(1.04); }}
    70%     {{ transform:scale(1); }}
}}
@keyframes slideInLeft {{
    from {{ opacity:0; transform:translateX(-20px); }}
    to   {{ opacity:1; transform:translateX(0); }}
}}
@keyframes slideInRight {{
    from {{ opacity:0; transform:translateX(20px); }}
    to   {{ opacity:1; transform:translateX(0); }}
}}
@keyframes staggerFade {{
    from {{ opacity:0; transform:translateY(16px); }}
    to   {{ opacity:1; transform:translateY(0); }}
}}

/* ── Animation Utilities ─────────────────────────────────────────── */
.anim-fade-up   {{ animation: fadeUp 0.5s var(--ease) both; }}
.anim-fade-in   {{ animation: fadeIn 0.4s var(--ease) both; }}
.anim-scale-in  {{ animation: scaleIn 0.4s var(--ease) both; }}
.anim-slide-l   {{ animation: slideInLeft 0.5s var(--ease) both; }}
.anim-slide-r   {{ animation: slideInRight 0.5s var(--ease) both; }}
.anim-heartbeat {{ animation: heartbeat 1.5s ease-in-out infinite; }}
.anim-glow-pulse {{ animation: glowPulse 2.5s ease-in-out infinite; }}

.delay-1 {{ animation-delay: 0.08s; }}
.delay-2 {{ animation-delay: 0.16s; }}
.delay-3 {{ animation-delay: 0.24s; }}
.delay-4 {{ animation-delay: 0.32s; }}
.delay-5 {{ animation-delay: 0.40s; }}

/* ── Shimmer Skeleton ────────────────────────────────────────────── */
.shimmer {{
    background: linear-gradient(90deg, var(--surface) 25%, var(--surface-raised) 50%, var(--surface) 75%);
    background-size: 200% 100%;
    animation: shimmer 1.8s infinite;
    border-radius: var(--r-md);
}}

/* ── Page Entry Animation ────────────────────────────────────────── */
.main .block-container > div:first-child {{
    animation: fadeUp 0.5s var(--ease) both;
}}

/* ── Hover Glow Cards (applied via class in Python) ──────────────── */
.glow-card:hover {{
    box-shadow: var(--glow), var(--shadow-lg) !important;
    border-color: var(--primary) !important;
}}

/* ── Mobile Responsive ───────────────────────────────────────────── */
@media (max-width: 768px) {{
    .block-container {{
        padding: 1rem 0.8rem 5rem !important;
    }}
    .bento-grid {{
        grid-template-columns: 1fr !important;
    }}
    .med-stat-value {{
        font-size: 1.8rem;
    }}
    h1 {{ font-size: 1.6rem !important; }}
    h2 {{ font-size: 1.3rem !important; }}
}}

</style>"""


def get_css(theme_key: str) -> str:
    return ThemeManager(theme_key).inject()


# ═══════════════════════════════════════════════════════════════════════════════
# THEME PREVIEW CARDS — For the sidebar theme selector
# ═══════════════════════════════════════════════════════════════════════════════

def render_theme_preview(theme_key: str) -> str:
    """Returns an HTML snippet showing a tiny swatch for the theme picker."""
    t = THEMES.get(theme_key, {})
    p = t.get("primary", "#888")
    bg = t.get("bg", "#fff")
    sb = t.get("sidebar_bg", "#111")
    return (
        f'<div style="display:inline-flex;align-items:center;gap:6px;">'
        f'<span style="width:10px;height:10px;border-radius:50%;background:{p};'
        f'box-shadow:0 0 6px {t.get("primary_glow","rgba(0,0,0,0)")};display:inline-block;"></span>'
        f'<span style="width:10px;height:10px;border-radius:2px;background:{bg};'
        f'border:1px solid rgba(128,128,128,0.3);display:inline-block;"></span>'
        f'</div>'
    )
