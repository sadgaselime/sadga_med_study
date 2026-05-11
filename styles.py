"""
styles.py — MedStudy Oman  19 Medical Themes — Sidebar Always Visible
"""

THEMES = {
    "💎 MedStudy Midnight": {"name":"MedStudy Midnight","family":"dark","primary":"#38d5ff","primary_glow":"rgba(56,213,255,0.30)","secondary":"#2ee59d","accent":"#7dd3fc","bg":"#06111f","surface":"#0a1b2f","surface_raised":"#10243b","card_bg":"rgba(255,255,255,0.92)","card_border":"rgba(185,232,255,0.20)","sidebar_bg":"#07182b","glass_bg":"rgba(255,255,255,0.10)","glass_border":"rgba(185,232,255,0.22)","glass_blur":"26px","text":"#eaf7ff","text_muted":"#b9d3e6","subtext":"#8ea9bd","text_inverse":"#03111d","gradient":"linear-gradient(135deg,#38d5ff,#2ee59d)","hero_gradient":"linear-gradient(145deg,#04101f 0%,#07182b 48%,#0a1422 100%)","card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.13),rgba(255,255,255,0.06))","glow":"0 0 42px rgba(56,213,255,0.24)","shadow_sm":"0 2px 10px rgba(0,0,0,0.35)","shadow_md":"0 10px 34px rgba(0,0,0,0.45)","shadow_lg":"0 24px 80px rgba(0,0,0,0.58)","hover_bg":"rgba(56,213,255,0.10)","focus_ring":"0 0 0 3px rgba(56,213,255,0.32)","success":"#2ee59d","warning":"#fbbf24","error":"#fb7185","info":"#38d5ff","chart_1":"#38d5ff","chart_2":"#2ee59d","chart_3":"#a78bfa","chart_4":"#fbbf24"},
    "🌸 Light Lavender": {"name":"Light Lavender","family":"light","primary":"#8b5cf6","primary_glow":"rgba(139,92,246,0.22)","secondary":"#06b6d4","accent":"#ec4899","bg":"#f7f2ff","surface":"#ffffff","surface_raised":"#efe7ff","card_bg":"rgba(255,255,255,0.92)","card_border":"rgba(139,92,246,0.18)","sidebar_bg":"#eadcff","glass_bg":"rgba(255,255,255,0.74)","glass_border":"rgba(139,92,246,0.24)","glass_blur":"20px","text":"#24163d","text_muted":"#5b4a77","subtext":"#7d6f96","text_inverse":"#ffffff","gradient":"linear-gradient(135deg,#8b5cf6,#06b6d4)","hero_gradient":"linear-gradient(145deg,#fbf8ff 0%,#f1e8ff 50%,#eafcff 100%)","card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.96),rgba(243,235,255,0.86))","glow":"0 0 28px rgba(139,92,246,0.18)","shadow_sm":"0 2px 8px rgba(36,22,61,0.06)","shadow_md":"0 10px 32px rgba(36,22,61,0.10)","shadow_lg":"0 24px 70px rgba(36,22,61,0.14)","hover_bg":"rgba(139,92,246,0.08)","focus_ring":"0 0 0 3px rgba(139,92,246,0.22)","success":"#10b981","warning":"#f59e0b","error":"#ef4444","info":"#06b6d4","chart_1":"#8b5cf6","chart_2":"#06b6d4","chart_3":"#10b981","chart_4":"#ec4899"},
    "🌿 Light Mint": {"name":"Light Mint","family":"light","primary":"#10b981","primary_glow":"rgba(16,185,129,0.22)","secondary":"#0ea5e9","accent":"#14b8a6","bg":"#f1fff8","surface":"#ffffff","surface_raised":"#ddfbea","card_bg":"rgba(255,255,255,0.92)","card_border":"rgba(16,185,129,0.20)","sidebar_bg":"#d7f8e8","glass_bg":"rgba(255,255,255,0.76)","glass_border":"rgba(16,185,129,0.26)","glass_blur":"20px","text":"#083323","text_muted":"#315c4b","subtext":"#638477","text_inverse":"#ffffff","gradient":"linear-gradient(135deg,#10b981,#0ea5e9)","hero_gradient":"linear-gradient(145deg,#f7fffb 0%,#e4fff1 52%,#e8f8ff 100%)","card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.96),rgba(226,252,239,0.86))","glow":"0 0 28px rgba(16,185,129,0.18)","shadow_sm":"0 2px 8px rgba(8,51,35,0.06)","shadow_md":"0 10px 32px rgba(8,51,35,0.10)","shadow_lg":"0 24px 70px rgba(8,51,35,0.14)","hover_bg":"rgba(16,185,129,0.08)","focus_ring":"0 0 0 3px rgba(16,185,129,0.22)","success":"#059669","warning":"#d97706","error":"#dc2626","info":"#0284c7","chart_1":"#10b981","chart_2":"#0ea5e9","chart_3":"#84cc16","chart_4":"#14b8a6"},
    "🌷 Soft Pink": {"name":"Soft Pink","family":"light","primary":"#ec4899","primary_glow":"rgba(236,72,153,0.20)","secondary":"#8b5cf6","accent":"#f97316","bg":"#fff5fb","surface":"#ffffff","surface_raised":"#ffe7f4","card_bg":"rgba(255,255,255,0.93)","card_border":"rgba(236,72,153,0.18)","sidebar_bg":"#ffe0f0","glass_bg":"rgba(255,255,255,0.76)","glass_border":"rgba(236,72,153,0.24)","glass_blur":"20px","text":"#3b1028","text_muted":"#6f3856","subtext":"#985e7a","text_inverse":"#ffffff","gradient":"linear-gradient(135deg,#ec4899,#8b5cf6)","hero_gradient":"linear-gradient(145deg,#fff9fd 0%,#ffe9f5 52%,#f3e8ff 100%)","card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.96),rgba(255,231,244,0.86))","glow":"0 0 28px rgba(236,72,153,0.16)","shadow_sm":"0 2px 8px rgba(59,16,40,0.06)","shadow_md":"0 10px 32px rgba(59,16,40,0.10)","shadow_lg":"0 24px 70px rgba(59,16,40,0.14)","hover_bg":"rgba(236,72,153,0.08)","focus_ring":"0 0 0 3px rgba(236,72,153,0.22)","success":"#10b981","warning":"#f97316","error":"#e11d48","info":"#8b5cf6","chart_1":"#ec4899","chart_2":"#8b5cf6","chart_3":"#f97316","chart_4":"#10b981"},
    "🌼 Warm Yellow": {"name":"Warm Yellow","family":"light","primary":"#eab308","primary_glow":"rgba(234,179,8,0.22)","secondary":"#22c55e","accent":"#f97316","bg":"#fffbea","surface":"#ffffff","surface_raised":"#fff3bd","card_bg":"rgba(255,255,255,0.92)","card_border":"rgba(234,179,8,0.24)","sidebar_bg":"#fff0a8","glass_bg":"rgba(255,255,255,0.76)","glass_border":"rgba(234,179,8,0.30)","glass_blur":"18px","text":"#3a2a05","text_muted":"#6c5a1a","subtext":"#917c34","text_inverse":"#1f1600","gradient":"linear-gradient(135deg,#facc15,#22c55e)","hero_gradient":"linear-gradient(145deg,#fffdf2 0%,#fff3bf 55%,#e9ffe9 100%)","card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.96),rgba(255,245,196,0.86))","glow":"0 0 28px rgba(234,179,8,0.18)","shadow_sm":"0 2px 8px rgba(58,42,5,0.06)","shadow_md":"0 10px 32px rgba(58,42,5,0.10)","shadow_lg":"0 24px 70px rgba(58,42,5,0.14)","hover_bg":"rgba(234,179,8,0.10)","focus_ring":"0 0 0 3px rgba(234,179,8,0.24)","success":"#16a34a","warning":"#ca8a04","error":"#dc2626","info":"#0ea5e9","chart_1":"#eab308","chart_2":"#22c55e","chart_3":"#f97316","chart_4":"#0ea5e9"},
    "🍃 Sage Green": {"name":"Sage Green","family":"light","primary":"#4f9f73","primary_glow":"rgba(79,159,115,0.22)","secondary":"#60a5fa","accent":"#84cc16","bg":"#f5fbf3","surface":"#ffffff","surface_raised":"#e7f4e2","card_bg":"rgba(255,255,255,0.92)","card_border":"rgba(79,159,115,0.22)","sidebar_bg":"#dcefd7","glass_bg":"rgba(255,255,255,0.76)","glass_border":"rgba(79,159,115,0.28)","glass_blur":"18px","text":"#172b1e","text_muted":"#405f4b","subtext":"#6c846f","text_inverse":"#ffffff","gradient":"linear-gradient(135deg,#4f9f73,#60a5fa)","hero_gradient":"linear-gradient(145deg,#fbfff9 0%,#e7f4e2 55%,#e8f3ff 100%)","card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.96),rgba(232,244,226,0.86))","glow":"0 0 28px rgba(79,159,115,0.18)","shadow_sm":"0 2px 8px rgba(23,43,30,0.06)","shadow_md":"0 10px 32px rgba(23,43,30,0.10)","shadow_lg":"0 24px 70px rgba(23,43,30,0.14)","hover_bg":"rgba(79,159,115,0.09)","focus_ring":"0 0 0 3px rgba(79,159,115,0.24)","success":"#15803d","warning":"#d97706","error":"#dc2626","info":"#2563eb","chart_1":"#4f9f73","chart_2":"#60a5fa","chart_3":"#84cc16","chart_4":"#f59e0b"},
    "🫧 Sky Glass": {"name":"Sky Glass","family":"light","primary":"#0ea5e9","primary_glow":"rgba(14,165,233,0.22)","secondary":"#a78bfa","accent":"#14b8a6","bg":"#f2fbff","surface":"#ffffff","surface_raised":"#dff5ff","card_bg":"rgba(255,255,255,0.92)","card_border":"rgba(14,165,233,0.20)","sidebar_bg":"#d7f0fb","glass_bg":"rgba(255,255,255,0.76)","glass_border":"rgba(14,165,233,0.26)","glass_blur":"20px","text":"#082b3d","text_muted":"#31586b","subtext":"#638294","text_inverse":"#ffffff","gradient":"linear-gradient(135deg,#0ea5e9,#a78bfa)","hero_gradient":"linear-gradient(145deg,#f8fdff 0%,#dcf4ff 52%,#f0eaff 100%)","card_gradient":"linear-gradient(145deg,rgba(255,255,255,0.96),rgba(224,245,255,0.86))","glow":"0 0 28px rgba(14,165,233,0.18)","shadow_sm":"0 2px 8px rgba(8,43,61,0.06)","shadow_md":"0 10px 32px rgba(8,43,61,0.10)","shadow_lg":"0 24px 70px rgba(8,43,61,0.14)","hover_bg":"rgba(14,165,233,0.08)","focus_ring":"0 0 0 3px rgba(14,165,233,0.22)","success":"#10b981","warning":"#f59e0b","error":"#ef4444","info":"#0ea5e9","chart_1":"#0ea5e9","chart_2":"#a78bfa","chart_3":"#14b8a6","chart_4":"#f59e0b"},
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
        sb = t["sidebar_bg"]   # hardcoded bg for guaranteed visibility
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
h1,h2,h3,h4,h5,h6 {{ font-family:'Syne',sans-serif !important; font-weight:800 !important; letter-spacing:0 !important; color:var(--text) !important; }}
html,body {{ background:var(--bg) !important; color:var(--text) !important; }}
.stApp {{
    background:
        linear-gradient(180deg, rgba(255,255,255,0.10), rgba(255,255,255,0)),
        var(--hero-gradient) !important;
}}

.main,.main .block-container,[data-testid="stAppViewContainer"],[data-testid="stAppViewContainer"] > .main,[data-testid="stMain"],[data-testid="stVerticalBlock"],[data-testid="column"],.element-container {{ background:transparent !important; color:var(--text) !important; }}
p,li,span,label,td,th,.stMarkdown,.stMarkdown *,[data-testid="stMarkdownContainer"],[data-testid="stMarkdownContainer"] * {{ color:var(--text) !important; }}
small,.stCaption {{ color:var(--subtext) !important; }}

/* ── SIDEBAR — HARDCODED BACKGROUND (guaranteed visible) ────── */
html body section[data-testid="stSidebar"],
html body [data-testid="stSidebar"],
html body [data-testid="stSidebar"] > div,
html body [data-testid="stSidebar"] > div > div,
html body [data-testid="stSidebar"] > div > div > div {{
    background-color: {sb} !important;
    background:       {sb} !important;
    min-width:        250px !important;
    max-width:        280px !important;
    width:            250px !important;
    transform:        none !important;
    left:             0 !important;
    opacity:          1 !important;
    visibility:       visible !important;
    border-right:     3px solid {p} !important;
    box-shadow:       6px 0 24px rgba(0,0,0,0.20) !important;
}}
html body [data-testid="stSidebar"] p,
html body [data-testid="stSidebar"] span,
html body [data-testid="stSidebar"] label,
html body [data-testid="stSidebar"] div {{ color:{txt} !important; }}

html body [data-testid="stSidebar"] {{
    overflow: auto !important;
}}
html body [data-testid="stSidebar"] *,
html body [data-testid="stSidebar"] [data-testid="stSidebarContent"],
html body [data-testid="stSidebar"] [data-testid="stSidebarContent"] * {{
    opacity: 1 !important;
    visibility: visible !important;
}}
html body [data-testid="stSidebar"] [data-testid="stSidebarContent"] {{
    display: block !important;
    width: 100% !important;
    min-width: 250px !important;
    transform: none !important;
    left: 0 !important;
}}
html body [data-testid="stSidebar"] [data-testid="stVerticalBlock"] {{
    gap: 0.35rem !important;
}}
html body [data-testid="stSidebar"] .stButton > button {{
    justify-content: flex-start !important;
    min-height: 38px !important;
    padding: 0.45rem 0.65rem !important;
    border-radius: 8px !important;
    font-size: 0.82rem !important;
    font-weight: 700 !important;
    box-shadow: none !important;
}}
html body [data-testid="stSidebar"] .stButton > button[kind="primary"] {{
    background: var(--gradient) !important;
    color: var(--text-inverse) !important;
}}
html body [data-testid="stSidebar"] .stButton > button:hover {{
    transform: none !important;
}}

/* ── Sidebar toggle — ALWAYS show ──────────────────────────── */
[data-testid="collapsedControl"] {{ display:flex !important; visibility:visible !important; opacity:1 !important; }}

/* ── Header transparent (keep in DOM for sidebar toggle) ────── */
[data-testid="stHeader"] {{ background:transparent !important; border-bottom:none !important; }}

/* ── Hide only chrome we don't need ─────────────────────────── */
[data-testid="stToolbar"],[data-testid="stDecoration"],[data-testid="stStatusWidget"],
[data-testid="stDeployButton"],#MainMenu,footer {{ display:none !important; }}

/* ── Block container ─────────────────────────────────────────── */
.block-container {{ padding-top:1.25rem !important; padding-bottom:3rem !important; max-width:1380px !important; }}

/* ── World-class product shell polish ─────────────────────────── */
.block-container {{
    padding-left: clamp(0.8rem, 2vw, 2.1rem) !important;
    padding-right: clamp(0.8rem, 2vw, 2.1rem) !important;
}}
[data-testid="stHorizontalBlock"] {{
    row-gap: 0.65rem !important;
}}
.stMetric, [data-testid="metric-container"] {{
    background: var(--card-bg) !important;
    border: 1px solid var(--card-border) !important;
    border-radius: 8px !important;
    padding: 0.85rem !important;
    box-shadow: var(--shadow-sm) !important;
}}
hr {{
    border-color: var(--card-border) !important;
}}
.stAlert {{
    border-radius: 8px !important;
    border: 1px solid var(--card-border) !important;
}}
[data-testid="stDataFrame"], [data-testid="stTable"] {{
    border: 1px solid var(--card-border) !important;
    border-radius: 8px !important;
    overflow: hidden !important;
}}
.stDownloadButton > button, .stLinkButton > a {{
    border-radius: 8px !important;
    font-weight: 800 !important;
}}
@media (max-width: 1100px) {{
    .block-container {{ padding-top: 0.8rem !important; }}
    div[data-testid="column"] {{ min-width: 0 !important; }}
}}
@media (max-width: 760px) {{
    .stButton > button {{ min-height: 46px !important; font-size: 0.82rem !important; }}
    div[data-testid="stHorizontalBlock"] {{ gap: 0.45rem !important; }}
}}


/* ── Inputs ──────────────────────────────────────────────────── */
.stTextInput > div > div > input,.stTextArea > div > div > textarea,.stNumberInput > div > div > input {{ background:var(--glass-bg) !important; color:var(--text) !important; border:1px solid var(--card-border) !important; border-radius:8px !important; font-size:16px !important; box-shadow:var(--shadow-sm) !important; }}
.stSelectbox > div > div,.stMultiSelect > div > div {{ background:var(--glass-bg) !important; color:var(--text) !important; border:1px solid var(--card-border) !important; border-radius:8px !important; }}
[data-baseweb="popover"] > div,[data-baseweb="menu"] {{ background:var(--surface) !important; border:1px solid var(--card-border) !important; border-radius:8px !important; }}
[role="option"] {{ color:var(--text) !important; background:transparent !important; }}
[role="option"]:hover {{ background:var(--hover-bg) !important; }}

/* ── Buttons ─────────────────────────────────────────────────── */
.stButton > button {{ background:var(--glass-bg) !important; border:1px solid var(--card-border) !important; border-radius:8px !important; color:var(--text) !important; font-weight:700 !important; min-height:42px !important; transition:all 0.18s ease !important; box-shadow:var(--shadow-sm) !important; }}
.stButton > button:hover {{ background:var(--primary) !important; border-color:var(--primary) !important; color:var(--text-inverse) !important; transform:translateY(-1px) !important; box-shadow:var(--shadow-md) !important; }}
.stButton > button[kind="primary"] {{ background:var(--gradient) !important; border:none !important; color:var(--text-inverse) !important; }}

/* ── Tabs ────────────────────────────────────────────────────── */
.stTabs [data-baseweb="tab-list"] {{ background:var(--glass-bg) !important; border:1px solid var(--card-border) !important; border-radius:8px !important; padding:4px !important; }}
.stTabs [data-baseweb="tab"] {{ color:var(--text-muted) !important; background:transparent !important; border:none !important; border-radius:6px !important; }}
.stTabs [aria-selected="true"] {{ background:var(--gradient) !important; color:var(--text-inverse) !important; }}

/* ── Forms & Expanders ───────────────────────────────────────── */
[data-testid="stForm"] {{ background:var(--glass-bg) !important; border:1px solid var(--card-border) !important; border-radius:8px !important; }}
[data-testid="stForm"] * {{ color:var(--text) !important; }}
[data-testid="stExpander"] {{ background:var(--glass-bg) !important; border:1px solid var(--card-border) !important; border-radius:8px !important; }}
.streamlit-expanderHeader {{ background:transparent !important; color:var(--text) !important; }}

.ai-bubble {{
    position: fixed;
    right: 22px;
    bottom: 22px;
    z-index: 9000;
    width: 52px;
    height: 52px;
    border-radius: 8px;
    background: var(--gradient);
    color: var(--text-inverse) !important;
    display: flex;
    align-items: center;
    justify-content: center;
    font-size: 1.35rem;
    box-shadow: var(--shadow-lg), var(--glow);
    border: 1px solid var(--glass-border);
}}

@media (max-width:768px) {{
    .ai-bubble {{ right: 14px; bottom: 82px; width: 46px; height: 46px; }}
}}

/* The app uses in-page navigation. Hide Streamlit's native sidebar because
   some desktop builds can reserve a blank collapsed layer over the content. */
section[data-testid="stSidebar"],
[data-testid="stSidebar"],
[data-testid="stSidebar"] > div,
[data-testid="stSidebar"] > div > div,
[data-testid="stSidebar"] > div > div > div,
[data-testid="collapsedControl"] {{
    display: none !important;
    min-width: 0 !important;
    max-width: 0 !important;
    width: 0 !important;
    border: 0 !important;
    box-shadow: none !important;
    padding: 0 !important;
    margin: 0 !important;
}}

/* ── Scrollbar ───────────────────────────────────────────────── */
html {{
    scrollbar-width: thin;
    scrollbar-color: var(--primary) transparent;
}}
body,
[data-testid="stAppViewContainer"],
[data-testid="stMain"],
[data-testid="stSidebar"],
[data-testid="stSidebarContent"] {{
    scrollbar-width: thin;
    scrollbar-color: var(--primary) transparent;
}}
::-webkit-scrollbar {{
    width: 10px;
    height: 10px;
}}
::-webkit-scrollbar-track {{
    background: transparent;
}}
::-webkit-scrollbar-thumb {{
    background: linear-gradient(180deg, var(--primary), var(--secondary));
    border: 2px solid transparent;
    border-radius: 999px;
    background-clip: padding-box;
}}
::-webkit-scrollbar-thumb:hover {{
    background: var(--primary);
    border: 2px solid transparent;
    background-clip: padding-box;
}}

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
