"""
styles.py — MedStudy Oman  19 Medical Themes — Sidebar Always Visible
"""

THEMES = {
    "🩺 Clinical Snow": {"name":"Clinical Snow","family":"light","primary":"#c8102e","primary_glow":"rgba(200,16,46,0.22)","secondary":"#003087","accent":"#005eb8","bg":"#f4f6f9","surface":"#ffffff","surface_raised":"#edf0f5","card_bg":"rgba(255,255,255,0.88)","card_border":"rgba(200,210,228,0.85)","sidebar_bg":"#d0ddf0","glass_bg":"rgba(255,255,255,0.70)","glass_border":"rgba(255,255,255,0.95)","glass_blur":"20px","text":"#0d1117","text_muted":"#4a5568","subtext":"#718096","text_inverse":"#ffffff","gradient":"linear-gradient(135deg,#c8102e,#003087)","hero_gradient":"linear-gradient(160deg,#f4f6f9,#eaf0fb 60%,#e2eaf8)","card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.9),rgba(237,240,245,0.75))","glow":"0 0 24px rgba(200,16,46,0.18)","shadow_sm":"0 2px 8px rgba(13,17,23,0.07)","shadow_md":"0 8px 32px rgba(13,17,23,0.11)","shadow_lg":"0 20px 60px rgba(13,17,23,0.16)","hover_bg":"rgba(200,16,46,0.06)","focus_ring":"0 0 0 3px rgba(200,16,46,0.28)","success":"#15803d","warning":"#b45309","error":"#c8102e","info":"#0369a1","chart_1":"#c8102e","chart_2":"#003087","chart_3":"#15803d","chart_4":"#b45309"},
    "🌑 Deep Surgeon": {"name":"Deep Surgeon","family":"dark","primary":"#00e5ff","primary_glow":"rgba(0,229,255,0.28)","secondary":"#00b8d4","accent":"#006064","bg":"#080d1a","surface":"#0f1829","surface_raised":"#162035","card_bg":"rgba(15,24,41,0.85)","card_border":"rgba(0,229,255,0.13)","sidebar_bg":"#04090f","glass_bg":"rgba(0,229,255,0.04)","glass_border":"rgba(0,229,255,0.18)","glass_blur":"24px","text":"#ddf4ff","text_muted":"#7db8cc","subtext":"#4a7a90","text_inverse":"#080d1a","gradient":"linear-gradient(135deg,#00e5ff,#0050ef)","hero_gradient":"linear-gradient(160deg,#080d1a,#0c1530 55%,#080d20)","card_gradient":"linear-gradient(145deg,rgba(0,229,255,0.07),rgba(0,80,239,0.04))","glow":"0 0 36px rgba(0,229,255,0.28)","shadow_sm":"0 2px 8px rgba(0,0,0,0.45)","shadow_md":"0 8px 32px rgba(0,0,0,0.55)","shadow_lg":"0 20px 60px rgba(0,0,0,0.65)","hover_bg":"rgba(0,229,255,0.07)","focus_ring":"0 0 0 3px rgba(0,229,255,0.32)","success":"#00e676","warning":"#ffd740","error":"#ff5252","info":"#40c4ff","chart_1":"#00e5ff","chart_2":"#7c4dff","chart_3":"#00e676","chart_4":"#ffd740"},
    "🌿 Oasis Health": {"name":"Oasis Health","family":"warm","primary":"#00695c","primary_glow":"rgba(0,105,92,0.24)","secondary":"#e6a817","accent":"#bf360c","bg":"#f9f5ee","surface":"#ffffff","surface_raised":"#f3ede1","card_bg":"rgba(255,252,242,0.90)","card_border":"rgba(180,145,60,0.28)","sidebar_bg":"#dccf9e","glass_bg":"rgba(255,252,242,0.72)","glass_border":"rgba(230,168,23,0.36)","glass_blur":"18px","text":"#1a2418","text_muted":"#3d5239","subtext":"#6b7d65","text_inverse":"#ffffff","gradient":"linear-gradient(135deg,#00695c,#e6a817)","hero_gradient":"linear-gradient(160deg,#f9f5ee,#f3ede1 55%,#ede5d3)","card_gradient":"linear-gradient(145deg,rgba(255,252,242,0.96),rgba(243,237,225,0.82))","glow":"0 0 24px rgba(0,105,92,0.20)","shadow_sm":"0 2px 8px rgba(26,36,24,0.09)","shadow_md":"0 8px 32px rgba(26,36,24,0.13)","shadow_lg":"0 20px 60px rgba(26,36,24,0.18)","hover_bg":"rgba(0,105,92,0.07)","focus_ring":"0 0 0 3px rgba(0,105,92,0.28)","success":"#00695c","warning":"#e6a817","error":"#bf360c","info":"#1565c0","chart_1":"#00695c","chart_2":"#e6a817","chart_3":"#bf360c","chart_4":"#4caf50"},
    "⚡ Cyber-Med": {"name":"Cyber-Med","family":"dark","primary":"#b84aff","primary_glow":"rgba(184,74,255,0.32)","secondary":"#ff2d78","accent":"#5a00cc","bg":"#030006","surface":"#0a000f","surface_raised":"#120018","card_bg":"rgba(10,0,15,0.80)","card_border":"rgba(184,74,255,0.18)","sidebar_bg":"#020004","glass_bg":"rgba(184,74,255,0.055)","glass_border":"rgba(184,74,255,0.22)","glass_blur":"32px","text":"#f3e8ff","text_muted":"#a87dcc","subtext":"#6d4a90","text_inverse":"#030006","gradient":"linear-gradient(135deg,#b84aff,#ff2d78)","hero_gradient":"linear-gradient(160deg,#030006,#0c0018 55%,#060010)","card_gradient":"linear-gradient(145deg,rgba(184,74,255,0.09),rgba(255,45,120,0.04))","glow":"0 0 40px rgba(184,74,255,0.32)","shadow_sm":"0 2px 8px rgba(0,0,0,0.65)","shadow_md":"0 8px 32px rgba(0,0,0,0.72)","shadow_lg":"0 20px 60px rgba(0,0,0,0.82)","hover_bg":"rgba(184,74,255,0.09)","focus_ring":"0 0 0 3px rgba(184,74,255,0.38)","success":"#39ff7c","warning":"#ffe03a","error":"#ff3a5e","info":"#38d9ff","chart_1":"#b84aff","chart_2":"#ff2d78","chart_3":"#39ff7c","chart_4":"#ffe03a"},
    "🏥 Hospital White": {"name":"Hospital White","family":"light","primary":"#005eb8","primary_glow":"rgba(0,94,184,0.20)","secondary":"#00a86b","accent":"#0041a8","bg":"#ffffff","surface":"#ffffff","surface_raised":"#f5f7fa","card_bg":"rgba(255,255,255,0.95)","card_border":"rgba(200,210,230,0.80)","sidebar_bg":"#c0d0e8","glass_bg":"rgba(255,255,255,0.80)","glass_border":"rgba(220,230,245,0.90)","glass_blur":"16px","text":"#0d1b2a","text_muted":"#3a4a5c","subtext":"#6b7a8d","text_inverse":"#ffffff","gradient":"linear-gradient(135deg,#005eb8,#00a86b)","hero_gradient":"linear-gradient(160deg,#ffffff,#f0f5ff 50%,#e8f2ff)","card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.98),rgba(240,245,255,0.85))","glow":"0 0 24px rgba(0,94,184,0.16)","shadow_sm":"0 1px 6px rgba(13,27,42,0.08)","shadow_md":"0 4px 24px rgba(13,27,42,0.10)","shadow_lg":"0 12px 48px rgba(13,27,42,0.14)","hover_bg":"rgba(0,94,184,0.05)","focus_ring":"0 0 0 3px rgba(0,94,184,0.25)","success":"#00a86b","warning":"#f59e0b","error":"#dc2626","info":"#0066cc","chart_1":"#005eb8","chart_2":"#00a86b","chart_3":"#f59e0b","chart_4":"#dc2626"},
    "🚨 Code Red": {"name":"Code Red","family":"dark","primary":"#ff3333","primary_glow":"rgba(255,51,51,0.32)","secondary":"#ff6b35","accent":"#8b0000","bg":"#0d0000","surface":"#1a0000","surface_raised":"#250000","card_bg":"rgba(26,0,0,0.88)","card_border":"rgba(255,51,51,0.18)","sidebar_bg":"#0a0000","glass_bg":"rgba(255,51,51,0.06)","glass_border":"rgba(255,51,51,0.22)","glass_blur":"20px","text":"#ffe8e8","text_muted":"#cc9999","subtext":"#886666","text_inverse":"#0d0000","gradient":"linear-gradient(135deg,#ff3333,#ff6b35)","hero_gradient":"linear-gradient(160deg,#0d0000,#1a0500 50%,#0d0000)","card_gradient":"linear-gradient(145deg,rgba(255,51,51,0.10),rgba(139,0,0,0.06))","glow":"0 0 40px rgba(255,51,51,0.30)","shadow_sm":"0 2px 8px rgba(0,0,0,0.55)","shadow_md":"0 8px 32px rgba(0,0,0,0.65)","shadow_lg":"0 20px 60px rgba(0,0,0,0.75)","hover_bg":"rgba(255,51,51,0.09)","focus_ring":"0 0 0 3px rgba(255,51,51,0.35)","success":"#00ff88","warning":"#ffd700","error":"#ff3333","info":"#ff6b35","chart_1":"#ff3333","chart_2":"#ff6b35","chart_3":"#ffd700","chart_4":"#00ff88"},
    "💚 OR Suite": {"name":"OR Suite","family":"light","primary":"#1a6b3c","primary_glow":"rgba(26,107,60,0.22)","secondary":"#2e8b57","accent":"#0d4a2a","bg":"#f0f7f2","surface":"#ffffff","surface_raised":"#e8f5ec","card_bg":"rgba(255,255,255,0.90)","card_border":"rgba(46,139,87,0.25)","sidebar_bg":"#b8d8c0","glass_bg":"rgba(240,247,242,0.75)","glass_border":"rgba(46,139,87,0.35)","glass_blur":"18px","text":"#0d2e1a","text_muted":"#2d5a3d","subtext":"#5a8c6a","text_inverse":"#ffffff","gradient":"linear-gradient(135deg,#1a6b3c,#2e8b57)","hero_gradient":"linear-gradient(160deg,#f0f7f2,#e0f0e6 50%,#d4ead9)","card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.95),rgba(232,245,236,0.85))","glow":"0 0 24px rgba(26,107,60,0.20)","shadow_sm":"0 2px 8px rgba(13,46,26,0.08)","shadow_md":"0 8px 28px rgba(13,46,26,0.12)","shadow_lg":"0 16px 52px rgba(13,46,26,0.16)","hover_bg":"rgba(26,107,60,0.06)","focus_ring":"0 0 0 3px rgba(26,107,60,0.28)","success":"#1a6b3c","warning":"#d97706","error":"#c0392b","info":"#0077b6","chart_1":"#1a6b3c","chart_2":"#2e8b57","chart_3":"#d97706","chart_4":"#0077b6"},
    "🌊 ICU Blue": {"name":"ICU Blue","family":"light","primary":"#1d4ed8","primary_glow":"rgba(29,78,216,0.22)","secondary":"#0ea5e9","accent":"#0c3474","bg":"#f0f4ff","surface":"#ffffff","surface_raised":"#e8efff","card_bg":"rgba(255,255,255,0.90)","card_border":"rgba(29,78,216,0.20)","sidebar_bg":"#b8c8f8","glass_bg":"rgba(255,255,255,0.72)","glass_border":"rgba(29,78,216,0.28)","glass_blur":"18px","text":"#0c1445","text_muted":"#2c4a8c","subtext":"#5470b0","text_inverse":"#ffffff","gradient":"linear-gradient(135deg,#1d4ed8,#0ea5e9)","hero_gradient":"linear-gradient(160deg,#f0f4ff,#dde8ff 50%,#d0e2ff)","card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.95),rgba(221,232,255,0.85))","glow":"0 0 24px rgba(29,78,216,0.20)","shadow_sm":"0 2px 8px rgba(12,20,69,0.08)","shadow_md":"0 8px 28px rgba(12,20,69,0.12)","shadow_lg":"0 16px 52px rgba(12,20,69,0.16)","hover_bg":"rgba(29,78,216,0.06)","focus_ring":"0 0 0 3px rgba(29,78,216,0.28)","success":"#059669","warning":"#d97706","error":"#dc2626","info":"#0ea5e9","chart_1":"#1d4ed8","chart_2":"#0ea5e9","chart_3":"#059669","chart_4":"#f59e0b"},
    "🌸 Paediatric Ward": {"name":"Paediatric Ward","family":"light","primary":"#e91e8c","primary_glow":"rgba(233,30,140,0.22)","secondary":"#ff9a3c","accent":"#9c1060","bg":"#fff5f8","surface":"#ffffff","surface_raised":"#ffedf4","card_bg":"rgba(255,255,255,0.90)","card_border":"rgba(233,30,140,0.20)","sidebar_bg":"#edb0cc","glass_bg":"rgba(255,255,255,0.72)","glass_border":"rgba(233,30,140,0.28)","glass_blur":"16px","text":"#2a0a18","text_muted":"#7a2a50","subtext":"#aa6080","text_inverse":"#ffffff","gradient":"linear-gradient(135deg,#e91e8c,#ff9a3c)","hero_gradient":"linear-gradient(160deg,#fff5f8,#ffe0ed 50%,#ffd6e7)","card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.96),rgba(255,224,237,0.85))","glow":"0 0 24px rgba(233,30,140,0.22)","shadow_sm":"0 2px 8px rgba(42,10,24,0.08)","shadow_md":"0 8px 28px rgba(42,10,24,0.12)","shadow_lg":"0 16px 52px rgba(42,10,24,0.16)","hover_bg":"rgba(233,30,140,0.06)","focus_ring":"0 0 0 3px rgba(233,30,140,0.28)","success":"#10b981","warning":"#f59e0b","error":"#ef4444","info":"#6366f1","chart_1":"#e91e8c","chart_2":"#ff9a3c","chart_3":"#10b981","chart_4":"#6366f1"},
    "📟 ECG Monitor": {"name":"ECG Monitor","family":"dark","primary":"#00ff41","primary_glow":"rgba(0,255,65,0.30)","secondary":"#00cc33","accent":"#005c14","bg":"#000a00","surface":"#001400","surface_raised":"#001e00","card_bg":"rgba(0,20,0,0.88)","card_border":"rgba(0,255,65,0.15)","sidebar_bg":"#000800","glass_bg":"rgba(0,255,65,0.04)","glass_border":"rgba(0,255,65,0.18)","glass_blur":"20px","text":"#ccffcc","text_muted":"#66cc66","subtext":"#33883a","text_inverse":"#000a00","gradient":"linear-gradient(135deg,#00ff41,#00cc33)","hero_gradient":"linear-gradient(160deg,#000a00,#001800 50%,#000a00)","card_gradient":"linear-gradient(145deg,rgba(0,255,65,0.06),rgba(0,204,51,0.03))","glow":"0 0 40px rgba(0,255,65,0.28)","shadow_sm":"0 2px 8px rgba(0,0,0,0.55)","shadow_md":"0 8px 32px rgba(0,0,0,0.65)","shadow_lg":"0 20px 60px rgba(0,0,0,0.75)","hover_bg":"rgba(0,255,65,0.07)","focus_ring":"0 0 0 3px rgba(0,255,65,0.35)","success":"#00ff41","warning":"#ccff00","error":"#ff4141","info":"#00ccff","chart_1":"#00ff41","chart_2":"#ccff00","chart_3":"#00ccff","chart_4":"#ff9900"},
    "🔬 Lab Dark": {"name":"Lab Dark","family":"dark","primary":"#7c3aff","primary_glow":"rgba(124,58,255,0.30)","secondary":"#00d4ff","accent":"#4a00cc","bg":"#050510","surface":"#0a0a1e","surface_raised":"#0f0f28","card_bg":"rgba(10,10,30,0.88)","card_border":"rgba(124,58,255,0.18)","sidebar_bg":"#030310","glass_bg":"rgba(124,58,255,0.05)","glass_border":"rgba(124,58,255,0.20)","glass_blur":"24px","text":"#e8e0ff","text_muted":"#9988cc","subtext":"#665588","text_inverse":"#050510","gradient":"linear-gradient(135deg,#7c3aff,#00d4ff)","hero_gradient":"linear-gradient(160deg,#050510,#0a0820 50%,#050510)","card_gradient":"linear-gradient(145deg,rgba(124,58,255,0.08),rgba(0,212,255,0.04))","glow":"0 0 36px rgba(124,58,255,0.28)","shadow_sm":"0 2px 8px rgba(0,0,0,0.55)","shadow_md":"0 8px 32px rgba(0,0,0,0.65)","shadow_lg":"0 20px 60px rgba(0,0,0,0.75)","hover_bg":"rgba(124,58,255,0.08)","focus_ring":"0 0 0 3px rgba(124,58,255,0.35)","success":"#00ff88","warning":"#ffcc00","error":"#ff4466","info":"#00d4ff","chart_1":"#7c3aff","chart_2":"#00d4ff","chart_3":"#00ff88","chart_4":"#ffcc00"},
    "🎓 Ivory Hall": {"name":"Ivory Hall","family":"light","primary":"#8b5e0a","primary_glow":"rgba(139,94,10,0.22)","secondary":"#2c4a7c","accent":"#5c3a00","bg":"#fafaf0","surface":"#ffffff","surface_raised":"#f5f5e8","card_bg":"rgba(255,255,248,0.90)","card_border":"rgba(139,94,10,0.22)","sidebar_bg":"#ccc090","glass_bg":"rgba(255,255,248,0.75)","glass_border":"rgba(139,94,10,0.32)","glass_blur":"16px","text":"#1a1408","text_muted":"#4a3a18","subtext":"#7a6840","text_inverse":"#ffffff","gradient":"linear-gradient(135deg,#8b5e0a,#2c4a7c)","hero_gradient":"linear-gradient(160deg,#fafaf0,#f5f0d8 50%,#ede8cc)","card_gradient":"linear-gradient(145deg,rgba(255,255,248,0.96),rgba(245,240,216,0.85))","glow":"0 0 24px rgba(139,94,10,0.20)","shadow_sm":"0 2px 8px rgba(26,20,8,0.10)","shadow_md":"0 8px 28px rgba(26,20,8,0.14)","shadow_lg":"0 16px 52px rgba(26,20,8,0.18)","hover_bg":"rgba(139,94,10,0.06)","focus_ring":"0 0 0 3px rgba(139,94,10,0.28)","success":"#2d6a2d","warning":"#c87941","error":"#c0392b","info":"#2c4a7c","chart_1":"#8b5e0a","chart_2":"#2c4a7c","chart_3":"#2d6a2d","chart_4":"#c87941"},
    "🏛️ Royal College": {"name":"Royal College","family":"dark","primary":"#ffd700","primary_glow":"rgba(255,215,0,0.28)","secondary":"#c0a000","accent":"#806800","bg":"#050510","surface":"#080820","surface_raised":"#0c0c2a","card_bg":"rgba(8,8,32,0.88)","card_border":"rgba(255,215,0,0.16)","sidebar_bg":"#030318","glass_bg":"rgba(255,215,0,0.04)","glass_border":"rgba(255,215,0,0.20)","glass_blur":"22px","text":"#fff8e0","text_muted":"#cca820","subtext":"#886c00","text_inverse":"#050510","gradient":"linear-gradient(135deg,#ffd700,#c0a000)","hero_gradient":"linear-gradient(160deg,#050510,#0a0820 50%,#05050a)","card_gradient":"linear-gradient(145deg,rgba(255,215,0,0.07),rgba(192,160,0,0.03))","glow":"0 0 40px rgba(255,215,0,0.26)","shadow_sm":"0 2px 8px rgba(0,0,0,0.55)","shadow_md":"0 8px 32px rgba(0,0,0,0.65)","shadow_lg":"0 20px 60px rgba(0,0,0,0.75)","hover_bg":"rgba(255,215,0,0.07)","focus_ring":"0 0 0 3px rgba(255,215,0,0.32)","success":"#00e676","warning":"#ffd700","error":"#ff5252","info":"#40c4ff","chart_1":"#ffd700","chart_2":"#40c4ff","chart_3":"#00e676","chart_4":"#ff5252"},
    "🌅 Desert Gold": {"name":"Desert Gold","family":"warm","primary":"#c9861a","primary_glow":"rgba(201,134,26,0.25)","secondary":"#8b4513","accent":"#6b3000","bg":"#fdf6e3","surface":"#ffffff","surface_raised":"#f8edd0","card_bg":"rgba(255,252,240,0.90)","card_border":"rgba(201,134,26,0.28)","sidebar_bg":"#d8b860","glass_bg":"rgba(255,252,240,0.72)","glass_border":"rgba(201,134,26,0.36)","glass_blur":"18px","text":"#2a1800","text_muted":"#6a4010","subtext":"#9a7040","text_inverse":"#ffffff","gradient":"linear-gradient(135deg,#c9861a,#8b4513)","hero_gradient":"linear-gradient(160deg,#fdf6e3,#f8edd0 50%,#f2e2b4)","card_gradient":"linear-gradient(145deg,rgba(255,252,240,0.96),rgba(248,237,208,0.85))","glow":"0 0 24px rgba(201,134,26,0.24)","shadow_sm":"0 2px 8px rgba(42,24,0,0.10)","shadow_md":"0 8px 28px rgba(42,24,0,0.14)","shadow_lg":"0 16px 52px rgba(42,24,0,0.18)","hover_bg":"rgba(201,134,26,0.07)","focus_ring":"0 0 0 3px rgba(201,134,26,0.30)","success":"#2d6a2d","warning":"#c9861a","error":"#c0392b","info":"#2563eb","chart_1":"#c9861a","chart_2":"#8b4513","chart_3":"#2d6a2d","chart_4":"#2563eb"},
    "🌙 Night Shift": {"name":"Night Shift","family":"dark","primary":"#4facfe","primary_glow":"rgba(79,172,254,0.28)","secondary":"#00f2fe","accent":"#0044aa","bg":"#000814","surface":"#001020","surface_raised":"#001828","card_bg":"rgba(0,16,32,0.88)","card_border":"rgba(79,172,254,0.16)","sidebar_bg":"#000510","glass_bg":"rgba(79,172,254,0.05)","glass_border":"rgba(79,172,254,0.20)","glass_blur":"22px","text":"#ddeeff","text_muted":"#7799cc","subtext":"#446688","text_inverse":"#000814","gradient":"linear-gradient(135deg,#4facfe,#00f2fe)","hero_gradient":"linear-gradient(160deg,#000814,#001428 50%,#000814)","card_gradient":"linear-gradient(145deg,rgba(79,172,254,0.08),rgba(0,242,254,0.04))","glow":"0 0 36px rgba(79,172,254,0.26)","shadow_sm":"0 2px 8px rgba(0,0,0,0.55)","shadow_md":"0 8px 32px rgba(0,0,0,0.65)","shadow_lg":"0 20px 60px rgba(0,0,0,0.75)","hover_bg":"rgba(79,172,254,0.08)","focus_ring":"0 0 0 3px rgba(79,172,254,0.32)","success":"#00e676","warning":"#ffd740","error":"#ff5252","info":"#00f2fe","chart_1":"#4facfe","chart_2":"#00f2fe","chart_3":"#00e676","chart_4":"#ffd740"},
    "🌿 Botanic Heal": {"name":"Botanic Heal","family":"light","primary":"#2d6a2d","primary_glow":"rgba(45,106,45,0.22)","secondary":"#8bc34a","accent":"#1a4020","bg":"#f1f8f0","surface":"#ffffff","surface_raised":"#e4f4e2","card_bg":"rgba(255,255,255,0.90)","card_border":"rgba(45,106,45,0.22)","sidebar_bg":"#b0ccb4","glass_bg":"rgba(241,248,240,0.75)","glass_border":"rgba(139,195,74,0.35)","glass_blur":"16px","text":"#0d2010","text_muted":"#2d522d","subtext":"#5a845a","text_inverse":"#ffffff","gradient":"linear-gradient(135deg,#2d6a2d,#8bc34a)","hero_gradient":"linear-gradient(160deg,#f1f8f0,#e0f0dc 50%,#d0e8cc)","card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.96),rgba(228,244,226,0.85))","glow":"0 0 24px rgba(45,106,45,0.20)","shadow_sm":"0 2px 8px rgba(13,32,16,0.09)","shadow_md":"0 8px 28px rgba(13,32,16,0.13)","shadow_lg":"0 16px 52px rgba(13,32,16,0.17)","hover_bg":"rgba(45,106,45,0.06)","focus_ring":"0 0 0 3px rgba(45,106,45,0.28)","success":"#2d6a2d","warning":"#f59e0b","error":"#c0392b","info":"#0277bd","chart_1":"#2d6a2d","chart_2":"#8bc34a","chart_3":"#f59e0b","chart_4":"#0277bd"},
    "🫀 Cardiac Arrest": {"name":"Cardiac Arrest","family":"dark","primary":"#ff2d55","primary_glow":"rgba(255,45,85,0.35)","secondary":"#ff9f0a","accent":"#8b0030","bg":"#08000a","surface":"#100015","surface_raised":"#180020","card_bg":"rgba(16,0,21,0.88)","card_border":"rgba(255,45,85,0.20)","sidebar_bg":"#050008","glass_bg":"rgba(255,45,85,0.06)","glass_border":"rgba(255,45,85,0.24)","glass_blur":"22px","text":"#ffe8ec","text_muted":"#cc7788","subtext":"#884455","text_inverse":"#08000a","gradient":"linear-gradient(135deg,#ff2d55,#ff9f0a)","hero_gradient":"linear-gradient(160deg,#08000a,#14000a 50%,#08000a)","card_gradient":"linear-gradient(145deg,rgba(255,45,85,0.09),rgba(255,159,10,0.04))","glow":"0 0 44px rgba(255,45,85,0.32)","shadow_sm":"0 2px 8px rgba(0,0,0,0.60)","shadow_md":"0 8px 32px rgba(0,0,0,0.70)","shadow_lg":"0 20px 60px rgba(0,0,0,0.80)","hover_bg":"rgba(255,45,85,0.09)","focus_ring":"0 0 0 3px rgba(255,45,85,0.38)","success":"#30d158","warning":"#ff9f0a","error":"#ff2d55","info":"#64d2ff","chart_1":"#ff2d55","chart_2":"#ff9f0a","chart_3":"#30d158","chart_4":"#64d2ff"},
    "🩻 Radiology": {"name":"Radiology","family":"dark","primary":"#ddeeff","primary_glow":"rgba(221,238,255,0.20)","secondary":"#90a8c0","accent":"#506070","bg":"#000000","surface":"#050505","surface_raised":"#0a0a0a","card_bg":"rgba(5,5,5,0.88)","card_border":"rgba(221,238,255,0.14)","sidebar_bg":"#000000","glass_bg":"rgba(221,238,255,0.04)","glass_border":"rgba(221,238,255,0.16)","glass_blur":"20px","text":"#ddeeff","text_muted":"#8899aa","subtext":"#445566","text_inverse":"#000000","gradient":"linear-gradient(135deg,#ddeeff,#90a8c0)","hero_gradient":"linear-gradient(160deg,#000000,#050a10 50%,#000000)","card_gradient":"linear-gradient(145deg,rgba(221,238,255,0.06),rgba(144,168,192,0.03))","glow":"0 0 30px rgba(221,238,255,0.18)","shadow_sm":"0 2px 8px rgba(0,0,0,0.70)","shadow_md":"0 8px 32px rgba(0,0,0,0.80)","shadow_lg":"0 20px 60px rgba(0,0,0,0.90)","hover_bg":"rgba(221,238,255,0.06)","focus_ring":"0 0 0 3px rgba(221,238,255,0.25)","success":"#30d158","warning":"#ffd60a","error":"#ff453a","info":"#64d2ff","chart_1":"#ddeeff","chart_2":"#64d2ff","chart_3":"#30d158","chart_4":"#ffd60a"},
    "🎨 Soft Rounds": {"name":"Soft Rounds","family":"light","primary":"#f06a35","primary_glow":"rgba(240,106,53,0.22)","secondary":"#7c4dff","accent":"#b03800","bg":"#fef9f5","surface":"#ffffff","surface_raised":"#fdeee6","card_bg":"rgba(255,255,255,0.90)","card_border":"rgba(240,106,53,0.22)","sidebar_bg":"#e0a888","glass_bg":"rgba(255,255,255,0.75)","glass_border":"rgba(240,106,53,0.30)","glass_blur":"16px","text":"#2a1008","text_muted":"#6a3a20","subtext":"#9a6a50","text_inverse":"#ffffff","gradient":"linear-gradient(135deg,#f06a35,#7c4dff)","hero_gradient":"linear-gradient(160deg,#fef9f5,#fdeee6 50%,#fae0d4)","card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.96),rgba(253,238,230,0.85))","glow":"0 0 24px rgba(240,106,53,0.22)","shadow_sm":"0 2px 8px rgba(42,16,8,0.09)","shadow_md":"0 8px 28px rgba(42,16,8,0.13)","shadow_lg":"0 16px 52px rgba(42,16,8,0.17)","hover_bg":"rgba(240,106,53,0.06)","focus_ring":"0 0 0 3px rgba(240,106,53,0.28)","success":"#10b981","warning":"#f59e0b","error":"#ef4444","info":"#7c4dff","chart_1":"#f06a35","chart_2":"#7c4dff","chart_3":"#10b981","chart_4":"#f59e0b"},
}


class ThemeManager:
    def __init__(self, theme_key: str):
        self.key = theme_key
        self.t   = THEMES.get(theme_key, THEMES["🩺 Clinical Snow"])

    def inject(self) -> str:
        t  = self.t
        sb = t["sidebar_bg"]
        p  = t["primary"]
        txt = t["text"]
        sub = t["subtext"]
        cs  = "dark" if t["family"] == "dark" else "light"

        return f"""<style>
@import url('https://fonts.googleapis.com/css2?family=Syne:wght@400;600;700;800;900&family=DM+Sans:ital,opsz,wght@0,9..40,300;0,9..40,400;0,9..40,500;0,9..40,600;0,9..40,700;1,9..40,400&family=DM+Mono:wght@400;500&display=swap');

:root {{
    color-scheme: {cs};
    --primary:        {t["primary"]};
    --primary-glow:   {t["primary_glow"]};
    --secondary:      {t["secondary"]};
    --bg:             {t["bg"]};
    --surface:        {t["surface"]};
    --surface-raised: {t["surface_raised"]};
    --card-bg:        {t["card_bg"]};
    --card-border:    {t["card_border"]};
    --sidebar-bg:     {t["sidebar_bg"]};
    --glass-bg:       {t["glass_bg"]};
    --glass-border:   {t["glass_border"]};
    --text:           {t["text"]};
    --text-muted:     {t["text_muted"]};
    --subtext:        {t["subtext"]};
    --text-inverse:   {t["text_inverse"]};
    --gradient:       {t["gradient"]};
    --hero-gradient:  {t["hero_gradient"]};
    --glow:           {t["glow"]};
    --shadow-sm:      {t["shadow_sm"]};
    --shadow-md:      {t["shadow_md"]};
    --shadow-lg:      {t["shadow_lg"]};
    --hover-bg:       {t["hover_bg"]};
    --focus-ring:     {t["focus_ring"]};
    --success:        {t["success"]};
    --warning:        {t["warning"]};
    --error:          {t["error"]};
    --info:           {t["info"]};
}}

/* ── Fonts & Base ──────────────────────────────────────────── */
*,*::before,*::after {{ font-family:'DM Sans',system-ui,sans-serif !important; -webkit-font-smoothing:antialiased; box-sizing:border-box; }}
h1,h2,h3,h4,h5,h6 {{ font-family:'Syne',sans-serif !important; font-weight:800 !important; letter-spacing:-0.02em; color:var(--text) !important; }}
html,body {{ background:var(--bg) !important; color:var(--text) !important; }}
.stApp {{ background:var(--hero-gradient) !important; }}
.main,.main .block-container,[data-testid="stAppViewContainer"],[data-testid="stAppViewContainer"] > .main,[data-testid="stMain"],[data-testid="stVerticalBlock"],[data-testid="stColumn"],.element-container {{ background:transparent !important; color:var(--text) !important; }}
p,li,span,label,td,th,.stMarkdown,.stMarkdown *,[data-testid="stMarkdownContainer"],[data-testid="stMarkdownContainer"] * {{ color:var(--text) !important; }}
small,.stCaption {{ color:var(--subtext) !important; }}

/* ── SIDEBAR — background + border only, no forced width ────── */
[data-testid="stSidebar"] > div:first-child {{
    background-color: {sb} !important;
    background:       {sb} !important;
    border-right:     3px solid {p} !important;
    box-shadow:       6px 0 24px rgba(0,0,0,0.20) !important;
}}
[data-testid="stSidebar"] p,
[data-testid="stSidebar"] span,
[data-testid="stSidebar"] label,
[data-testid="stSidebar"] div {{ color:{txt} !important; }}

/* ── Sidebar toggle arrow — ALWAYS visible ──────────────────── */
[data-testid="collapsedControl"],
[data-testid="collapsedControl"] button,
[data-testid="stSidebarCollapsedControl"],
[data-testid="stSidebarCollapsedControl"] button {{
    display:    flex !important;
    visibility: visible !important;
    opacity:    1 !important;
    z-index:    999999 !important;
}}

/* ── Header — transparent but kept in DOM for toggle arrow ─── */
[data-testid="stHeader"] {{
    background:    transparent !important;
    border-bottom: none !important;
}}

/* ── Hide only deploy/status chrome, NOT the toolbar itself ── */
[data-testid="stDecoration"],
[data-testid="stStatusWidget"],
[data-testid="stDeployButton"],
#MainMenu,
footer {{ display:none !important; }}

/* ── Block container ─────────────────────────────────────────── */
.block-container {{ padding-top:1.5rem !important; padding-bottom:3rem !important; }}

/* ── Inputs ──────────────────────────────────────────────────── */
.stTextInput > div > div > input,.stTextArea > div > div > textarea,.stNumberInput > div > div > input {{ background:var(--glass-bg) !important; color:var(--text) !important; border:1.5px solid var(--card-border) !important; border-radius:12px !important; font-size:16px !important; }}
.stSelectbox > div > div,.stMultiSelect > div > div {{ background:var(--glass-bg) !important; color:var(--text) !important; border:1.5px solid var(--card-border) !important; border-radius:12px !important; }}
[data-baseweb="popover"] > div,[data-baseweb="menu"] {{ background:var(--surface) !important; border:1px solid var(--card-border) !important; border-radius:12px !important; }}
[role="option"] {{ color:var(--text) !important; background:transparent !important; }}
[role="option"]:hover {{ background:var(--hover-bg) !important; }}

/* ── Buttons ─────────────────────────────────────────────────── */
.stButton > button {{ background:var(--glass-bg) !important; border:1.5px solid var(--card-border) !important; border-radius:14px !important; color:var(--text) !important; font-weight:600 !important; min-height:44px !important; transition:all 0.2s ease !important; }}
.stButton > button:hover {{ background:var(--primary) !important; border-color:var(--primary) !important; color:var(--text-inverse) !important; transform:translateY(-2px) !important; }}
.stButton > button[kind="primary"] {{ background:var(--gradient) !important; border:none !important; color:var(--text-inverse) !important; }}

/* ── Tabs ────────────────────────────────────────────────────── */
.stTabs [data-baseweb="tab-list"] {{ background:var(--glass-bg) !important; border:1px solid var(--card-border) !important; border-radius:999px !important; padding:5px !important; }}
.stTabs [data-baseweb="tab"] {{ color:var(--text-muted) !important; background:transparent !important; border:none !important; border-radius:999px !important; }}
.stTabs [aria-selected="true"] {{ background:var(--gradient) !important; color:var(--text-inverse) !important; }}

/* ── Forms & Expanders ───────────────────────────────────────── */
[data-testid="stForm"] {{ background:var(--glass-bg) !important; border:1px solid var(--card-border) !important; border-radius:16px !important; }}
[data-testid="stForm"] * {{ color:var(--text) !important; }}
[data-testid="stExpander"] {{ background:var(--glass-bg) !important; border:1px solid var(--card-border) !important; border-radius:14px !important; }}
.streamlit-expanderHeader {{ background:transparent !important; color:var(--text) !important; }}

/* ── Scrollbar ───────────────────────────────────────────────── */
::-webkit-scrollbar {{ width:5px; height:5px; }}
::-webkit-scrollbar-track {{ background:transparent; }}
::-webkit-scrollbar-thumb {{ background:var(--primary); border-radius:999px; opacity:.6; }}

/* ── Animations ──────────────────────────────────────────────── */
@keyframes fadeUp {{ from {{ opacity:0; transform:translateY(20px); }} to {{ opacity:1; transform:translateY(0); }} }}
@keyframes fadeIn {{ from {{ opacity:0; }} to {{ opacity:1; }} }}
@keyframes float {{ 0%,100% {{ transform:translateY(0); }} 50% {{ transform:translateY(-8px); }} }}
@keyframes glowPulse {{ 0%,100% {{ opacity:.6; }} 50% {{ opacity:1; }} }}
@keyframes scaleIn {{ from {{ opacity:0; transform:scale(.92); }} to {{ opacity:1; transform:scale(1); }} }}
@keyframes stagger-fade {{ from {{ opacity:0; transform:translateY(14px); }} to {{ opacity:1; transform:translateY(0); }} }}
</style>"""


def get_css(theme_key: str) -> str:
    return ThemeManager(theme_key).inject()
