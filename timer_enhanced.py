"""
timer_page.py — MedStudy Oman 🩺
Phase 4: OSCE-Grade Multi-Style Timer
Style A — Radial Ring    · circular depletion ring
Style B — LCD Pro        · retro-futuristic clinical display
Style C — Minimal Bar    · fixed top-bar, colour-shifts green→yellow→red
Phase Intervals: Reading phase + Station phase (configurable)
OSCE Presets: 12 station types with recommended timing
"""

import streamlit as st
import time
import math


# ─────────────────────────────────────────────────────────────────────────────
# OSCE STATION PRESETS
# ─────────────────────────────────────────────────────────────────────────────
OSCE_PRESETS = {
    "🩺 History Taking":         {"read": 2, "station": 8,  "total": 10, "color": "#e63946"},
    "🖐️ Physical Examination":   {"read": 2, "station": 8,  "total": 10, "color": "#ef4444"},
    "💊 Clinical Management":    {"read": 2, "station": 8,  "total": 10, "color": "#0891b2"},
    "📋 Data Interpretation":    {"read": 2, "station": 8,  "total": 10, "color": "#8b5cf6"},
    "🩻 Radiology Reading":      {"read": 2, "station": 6,  "total": 8,  "color": "#64748b"},
    "📝 Written Station":        {"read": 3, "station": 12, "total": 15, "color": "#f59e0b"},
    "⚕️  Procedural Skills":     {"read": 2, "station": 8,  "total": 10, "color": "#10b981"},
    "💬 Communication Skills":   {"read": 2, "station": 10, "total": 12, "color": "#ec4899"},
    "🧪 Laboratory Diagnosis":   {"read": 2, "station": 6,  "total": 8,  "color": "#84cc16"},
    "👶 Paediatric History":     {"read": 2, "station": 10, "total": 12, "color": "#f97316"},
    "🤰 Obstetric Assessment":   {"read": 2, "station": 8,  "total": 10, "color": "#ec4899"},
    "🧠 Psychiatric Assessment": {"read": 2, "station": 10, "total": 12, "color": "#a855f7"},
}

TIMER_STYLES = [
    ("radial",  "⭕",  "Radial Ring",  "Circular depletion ring"),
    ("lcd",     "💻",  "LCD Pro",      "Clinical digital display"),
    ("minimal", "▬",   "Minimal Bar",  "Top-bar colour shift"),
]


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE HELPERS
# ─────────────────────────────────────────────────────────────────────────────
def _init_timer_state():
    defaults = {
        "timer_style":        "radial",
        "osce_preset":        "🩺 History Taking",
        "osce_phase":         "reading",   # "reading" | "station" | "done"
        "osce_running":       False,
        "osce_phase_start":   None,
        "osce_custom_read":   2,
        "osce_custom_station": 8,
        "osce_use_custom":    False,
        "osce_completed":     0,
        "osce_total_elapsed": 0.0,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


def _get_phase_config():
    """Return (read_secs, station_secs, accent_color) for current preset/custom."""
    if st.session_state.osce_use_custom:
        r = st.session_state.osce_custom_read    * 60
        s = st.session_state.osce_custom_station * 60
        c = "#06b6d4"
    else:
        p = OSCE_PRESETS[st.session_state.osce_preset]
        r = p["read"]    * 60
        s = p["station"] * 60
        c = p["color"]
    return r, s, c


def _phase_remaining():
    """Return (remaining_secs, phase_label, phase_color, total_phase_secs)."""
    r_secs, s_secs, accent = _get_phase_config()
    phase = st.session_state.osce_phase

    if phase == "done":
        return 0, "Done", accent, s_secs

    phase_duration = r_secs if phase == "reading" else s_secs
    phase_label    = "📖 Reading" if phase == "reading" else "🩺 Station"

    if st.session_state.osce_running and st.session_state.osce_phase_start:
        elapsed   = time.time() - st.session_state.osce_phase_start
        remaining = max(0.0, phase_duration - elapsed)
    else:
        remaining = float(phase_duration)

    # Auto-advance phases
    if remaining == 0 and st.session_state.osce_running:
        if phase == "reading":
            st.session_state.osce_phase       = "station"
            st.session_state.osce_phase_start = time.time()
            remaining     = float(s_secs)
            phase_duration = s_secs
            phase_label    = "🩺 Station"
        elif phase == "station":
            st.session_state.osce_phase   = "done"
            st.session_state.osce_running = False
            st.session_state.osce_completed += 1
            remaining = 0

    # Dynamic colour
    pct = remaining / phase_duration if phase_duration else 0
    if pct > 0.5:
        phase_color = "#16a34a"  # green
    elif pct > 0.2:
        phase_color = "#d97706"  # amber
    else:
        phase_color = "#dc2626"  # red

    return remaining, phase_label, phase_color, phase_duration


# ─────────────────────────────────────────────────────────────────────────────
# MAIN ENTRY POINT
# ─────────────────────────────────────────────────────────────────────────────
def timer_page(theme: dict):
    _init_timer_state()
    _inject_timer_css(theme)

    # ── Page header ──────────────────────────────────────────────────────────
    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:14px;margin-bottom:1.5rem;">
        <div style="width:48px;height:48px;border-radius:14px;
             background:{theme['gradient']};display:flex;align-items:center;
             justify-content:center;font-size:1.6rem;
             box-shadow:0 4px 16px {theme['primary_glow']};">⏱️</div>
        <div>
            <div style="font-family:'Syne',sans-serif;font-size:1.8rem;font-weight:900;
                 color:{theme['text']};letter-spacing:-0.03em;">OSCE Timer</div>
            <div style="font-size:0.82rem;color:{theme['subtext']};">
                 3 display styles · Phase intervals · 12 station presets</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Style selector ────────────────────────────────────────────────────────
    st.markdown(f"""
    <div style="font-size:0.72rem;font-weight:800;color:{theme['subtext']};
         letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.7rem;">
         Display Style
    </div>
    """, unsafe_allow_html=True)

    sc1, sc2, sc3, _ = st.columns([1, 1, 1, 2])
    for col, (s_id, s_ico, s_name, s_sub) in zip(
        [sc1, sc2, sc3], TIMER_STYLES
    ):
        with col:
            active = st.session_state.timer_style == s_id
            st.markdown(f"""
            <div class="style-tile {'style-tile-active' if active else ''}"
                 style="{'border-color:' + theme['primary'] + ';background:' + theme['primary'] + '12;' if active else ''}">
                <div class="st-ico">{s_ico}</div>
                <div class="st-name">{s_name}</div>
                <div class="st-sub">{s_sub}</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(s_name, key=f"style_{s_id}", use_container_width=True,
                         label_visibility="collapsed",
                         type="primary" if active else "secondary"):
                st.session_state.timer_style = s_id
                st.rerun()

    st.markdown("<div style='height:1.2rem'></div>", unsafe_allow_html=True)

    # ── Main layout: Timer | Controls ────────────────────────────────────────
    col_timer, col_ctrl = st.columns([3, 2])

    with col_timer:
        _render_active_timer(theme)

    with col_ctrl:
        _render_controls(theme)

    # ── Station log ───────────────────────────────────────────────────────────
    st.markdown("<div style='height:1.5rem'></div>", unsafe_allow_html=True)
    _render_station_log(theme)

    # Auto-refresh while running
    remaining, _, _, _ = _phase_remaining()
    if st.session_state.osce_running and remaining > 0:
        time.sleep(0.5)
        st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# TIMER RENDERERS
# ─────────────────────────────────────────────────────────────────────────────
def _render_active_timer(theme: dict):
    remaining, phase_label, phase_color, total_secs = _phase_remaining()
    pct  = remaining / total_secs if total_secs else 0
    mins = int(remaining) // 60
    secs = int(remaining) % 60

    style = st.session_state.timer_style

    if style == "radial":
        _render_radial(theme, mins, secs, pct, remaining, phase_label, phase_color, total_secs)
    elif style == "lcd":
        _render_lcd(theme, mins, secs, pct, remaining, phase_label, phase_color, total_secs)
    else:
        _render_minimal(theme, mins, secs, pct, remaining, phase_label, phase_color, total_secs)


def _render_radial(theme, mins, secs, pct, remaining, phase_label, phase_color, total):
    """Style A — Concentric rings: outer = total, inner = phase."""
    r_outer, r_inner = 110, 82
    circ_o = 2 * math.pi * r_outer
    circ_i = 2 * math.pi * r_inner

    # Outer ring = fraction of total station time
    r_read, s_read, _ = _get_phase_config()
    total_full = r_read + s_read
    if total_full > 0:
        elapsed_total = total_full - (
            (r_read + s_read) if st.session_state.osce_phase == "reading"
            else s_read
        ) + (total - remaining)
        pct_outer = max(0, min(1, 1 - elapsed_total / total_full))
    else:
        pct_outer = pct

    dash_o_f = circ_o * pct_outer
    dash_o_e = circ_o - dash_o_f
    dash_i_f = circ_i * pct
    dash_i_e = circ_i - dash_i_f

    # Pulsing glow when < 30 secs
    pulse = "animation:glowPulse 0.8s ease-in-out infinite;" if remaining < 30 else ""

    phase_done = st.session_state.osce_phase == "done"

    st.markdown(f"""
    <div class="radial-wrapper">
        
        <div style="position:absolute;width:280px;height:280px;border-radius:50%;
             background:radial-gradient(circle, {phase_color}22, transparent 70%);
             {pulse}pointer-events:none;"></div>

        <svg width="280" height="280" viewBox="0 0 280 280" style="position:relative;z-index:1;">
            
            <circle cx="140" cy="140" r="{r_outer}"
                fill="none" stroke="{theme['card_border']}" stroke-width="8" opacity="0.5"/>
            
            <circle cx="140" cy="140" r="{r_outer}"
                fill="none" stroke="{theme['primary']}60" stroke-width="8"
                stroke-linecap="round"
                stroke-dasharray="{dash_o_f:.2f} {dash_o_e:.2f}"
                style="transform:rotate(-90deg);transform-origin:50% 50%;
                       transition:stroke-dasharray 0.5s linear;"/>
            
            <circle cx="140" cy="140" r="{r_inner}"
                fill="none" stroke="{theme['card_border']}" stroke-width="12" opacity="0.4"/>
            
            <circle cx="140" cy="140" r="{r_inner}"
                fill="none" stroke="{phase_color}" stroke-width="12"
                stroke-linecap="round"
                stroke-dasharray="{dash_i_f:.2f} {dash_i_e:.2f}"
                style="transform:rotate(-90deg);transform-origin:50% 50%;
                       transition:stroke-dasharray 0.5s linear;
                       filter:drop-shadow(0 0 10px {phase_color}80);"/>
            
            {"".join(
                f'<line x1="140" y1="20" x2="140" y2="30" stroke="{theme["card_border"]}"'
                f' stroke-width="2" opacity="0.5"'
                f' style="transform:rotate({i*30}deg);transform-origin:140px 140px;"/>'
                for i in range(12)
            )}
        </svg>

        
        <div class="radial-centre">
            {'<div style="font-size:2rem;animation:float 1.5s ease infinite;">✅</div>' if phase_done else f'''
            <div class="radial-time" style="color:{phase_color};">{mins:02d}:{secs:02d}</div>
            <div class="radial-phase" style="color:{phase_color};">{phase_label}</div>
            '''}
        </div>
    </div>
    """, unsafe_allow_html=True)

    if phase_done:
        st.markdown(f"""
        <div style="text-align:center;padding:1rem;
             background:{theme['success']}15;border:1px solid {theme['success']}40;
             border-radius:14px;margin-top:0.5rem;">
            <div style="font-size:1.2rem;font-weight:800;color:{theme['success']};">
                 ✅ Station Complete!</div>
            <div style="font-size:0.82rem;color:{theme['subtext']};margin-top:0.2rem;">
                 Total stations completed: {st.session_state.osce_completed}</div>
        </div>
        """, unsafe_allow_html=True)


def _render_lcd(theme, mins, secs, pct, remaining, phase_label, phase_color, total):
    """Style B — Clinical LCD display, scanline texture, digit segments."""
    phase_done = st.session_state.osce_phase == "done"
    is_reading = st.session_state.osce_phase == "reading"

    # Urgency class
    if remaining < 30 and not phase_done:
        urgency_anim = "animation:glowPulse 0.6s ease-in-out infinite;"
    elif remaining < 60 and not phase_done:
        urgency_anim = "animation:glowPulse 1.2s ease-in-out infinite;"
    else:
        urgency_anim = ""

    r_read, s_read, _ = _get_phase_config()
    phase_total = r_read if is_reading else s_read
    elapsed_phase = phase_total - (remaining * (phase_total / total) if total else 0)

    bar_pct = pct * 100

    st.markdown(f"""
    <div class="lcd-wrapper" style="{urgency_anim}">
        
        <div class="lcd-scanlines"></div>

        
        <div class="lcd-badge">
            <span class="lcd-dot" style="background:{phase_color};
                {'animation:glowPulse 0.8s ease-in-out infinite;' if st.session_state.osce_running else ''}">
            </span>
            {'LIVE · ' if st.session_state.osce_running else ''}
            {st.session_state.osce_preset if not st.session_state.osce_use_custom else 'Custom Station'}
        </div>

        
        <div class="lcd-phase-label" style="color:{phase_color}80;">
            {'COMPLETE' if phase_done else phase_label.upper()}
        </div>

        
        <div class="lcd-time" style="color:{phase_color};{urgency_anim}">
            {'-- : --' if phase_done else f'{mins:02d} : {secs:02d}'}
        </div>

        
        <div class="lcd-bar-track">
            <div class="lcd-bar-fill"
                 style="width:{bar_pct:.1f}%;background:{phase_color};
                        box-shadow:0 0 10px {phase_color}80;"></div>
        </div>

        
        <div class="lcd-phases">
            <div class="lcd-ph-item {'lcd-ph-active' if st.session_state.osce_phase == 'reading' else 'lcd-ph-done' if st.session_state.osce_phase in ('station','done') else ''}">
                <span>📖</span> READING
                <span class="lcd-ph-time">{r_read//60:02d}:00</span>
            </div>
            <div class="lcd-ph-sep">▶</div>
            <div class="lcd-ph-item {'lcd-ph-active' if st.session_state.osce_phase == 'station' else 'lcd-ph-done' if st.session_state.osce_phase == 'done' else ''}">
                <span>🩺</span> STATION
                <span class="lcd-ph-time">{s_read//60:02d}:00</span>
            </div>
        </div>

        
        <div class="lcd-footer">
            STATIONS COMPLETED : {st.session_state.osce_completed:02d}
        </div>
    </div>
    """, unsafe_allow_html=True)


def _render_minimal(theme, mins, secs, pct, remaining, phase_label, phase_color, total):
    """Style C — Fixed top bar + large clean centre display."""
    phase_done = st.session_state.osce_phase == "done"
    bar_pct    = pct * 100

    r_read, s_read, _ = _get_phase_config()
    is_reading         = st.session_state.osce_phase == "reading"

    # Top bar (fixed position)
    st.markdown(f"""
    <div style="position:fixed;top:0;left:0;right:0;height:5px;z-index:9999;
         background:{theme['card_border']};">
        <div style="height:100%;width:{bar_pct:.2f}%;background:{phase_color};
             transition:width 0.5s linear,background 0.8s ease;
             box-shadow:0 0 12px {phase_color}80;"></div>
    </div>
    """, unsafe_allow_html=True)

    # Phase pill strip
    st.markdown(f"""
    <div style="display:flex;align-items:center;justify-content:center;
         gap:8px;margin-bottom:1.5rem;">
        <div style="padding:5px 14px;border-radius:999px;
             background:{'#16a34a20' if is_reading else '#16a34a'};
             color:{'#16a34a' if is_reading else 'white'};
             border:1px solid {'#16a34a' if is_reading else '#16a34a'};
             font-size:0.75rem;font-weight:700;letter-spacing:0.06em;
             transition:all 0.4s ease;">
             📖 READING &nbsp; {r_read//60}:00
        </div>
        <div style="color:{theme['subtext']};font-size:0.8rem;">›</div>
        <div style="padding:5px 14px;border-radius:999px;
             background:{'#0891b220' if not is_reading and not phase_done else '#0891b2' if not phase_done else '#16a34a20'};
             color:{'#0891b2' if not is_reading and not phase_done else 'white' if not phase_done else theme['subtext']};
             border:1px solid {'#0891b2' if not is_reading and not phase_done else '#0891b2' if not phase_done else theme['card_border']};
             font-size:0.75rem;font-weight:700;letter-spacing:0.06em;
             transition:all 0.4s ease;">
             🩺 STATION &nbsp; {s_read//60}:00
        </div>
        {"<div style='padding:5px 14px;border-radius:999px;background:#16a34a;color:white;font-size:0.75rem;font-weight:700;'>✅ DONE</div>" if phase_done else ""}
    </div>
    """, unsafe_allow_html=True)

    # Big time
    if phase_done:
        st.markdown(f"""
        <div style="text-align:center;padding:4rem 2rem;">
            <div style="font-size:5rem;margin-bottom:1rem;animation:float 2s ease infinite;">🏁</div>
            <div style="font-family:'Syne',sans-serif;font-size:1.8rem;font-weight:900;
                 color:{theme['success']};">Station Complete</div>
            <div style="font-size:1rem;color:{theme['subtext']};margin-top:0.5rem;">
                 {st.session_state.osce_completed} stations done this session</div>
        </div>
        """, unsafe_allow_html=True)
    else:
        # Urgency ring
        urgency = ""
        if remaining < 30:
            urgency = f"animation:glowPulse 0.6s ease-in-out infinite;color:{phase_color};"
        elif remaining < 60:
            urgency = f"animation:glowPulse 1.2s ease-in-out infinite;"

        st.markdown(f"""
        <div style="text-align:center;padding:3rem 2rem 2rem;">
            <div style="font-size:0.72rem;font-weight:800;color:{phase_color};
                 letter-spacing:0.16em;text-transform:uppercase;margin-bottom:0.5rem;">
                 {phase_label}
            </div>
            <div style="font-family:'DM Mono',monospace;font-size:6.5rem;font-weight:500;
                 color:{phase_color};line-height:1;letter-spacing:0.04em;{urgency}">
                 {mins:02d}:{secs:02d}
            </div>
            <div style="font-size:0.85rem;color:{theme['subtext']};margin-top:0.8rem;">
                 {st.session_state.osce_preset if not st.session_state.osce_use_custom else 'Custom Station'}
            </div>
            
            <div style="margin-top:1.5rem;display:inline-flex;align-items:center;gap:8px;
                 padding:6px 16px;background:{theme['glass_bg']};
                 border:1px solid {theme['card_border']};border-radius:999px;">
                <div style="width:8px;height:8px;border-radius:50%;background:{phase_color};
                     {'animation:glowPulse 0.8s ease-in-out infinite;' if st.session_state.osce_running else ''}">
                </div>
                <span style="font-size:0.76rem;color:{theme['text_muted']};font-weight:600;">
                     {'RUNNING' if st.session_state.osce_running else 'PAUSED'}
                </span>
            </div>
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# CONTROLS PANEL
# ─────────────────────────────────────────────────────────────────────────────
def _render_controls(theme: dict):
    r_read, s_read, accent = _get_phase_config()
    phase = st.session_state.osce_phase
    phase_done = phase == "done"

    st.markdown(f"""
    <div style="background:{theme['glass_bg']};border:1px solid {theme['glass_border']};
         border-radius:22px;padding:1.5rem;backdrop-filter:blur(16px);">

        <div style="font-size:0.7rem;font-weight:800;color:{theme['subtext']};
             letter-spacing:0.12em;text-transform:uppercase;margin-bottom:1rem;">
             Station Setup
        </div>
    """, unsafe_allow_html=True)

    # Preset or Custom toggle
    use_custom = st.checkbox("Custom timing", key="osce_use_custom_cb",
                             value=st.session_state.osce_use_custom)
    st.session_state.osce_use_custom = use_custom

    if not use_custom:
        preset = st.selectbox(
            "Station preset",
            list(OSCE_PRESETS.keys()),
            index=list(OSCE_PRESETS.keys()).index(st.session_state.osce_preset),
            key="osce_preset_sel",
            label_visibility="collapsed",
        )
        if preset != st.session_state.osce_preset:
            st.session_state.osce_preset   = preset
            st.session_state.osce_phase    = "reading"
            st.session_state.osce_running  = False
            st.session_state.osce_phase_start = None
            st.rerun()

        p = OSCE_PRESETS[st.session_state.osce_preset]
        st.markdown(f"""
        <div style="display:flex;gap:8px;margin-top:0.6rem;flex-wrap:wrap;">
            <span style="background:{p['color']}18;color:{p['color']};border-radius:8px;
                  padding:4px 10px;font-size:0.75rem;font-weight:700;">
                  📖 Read: {p['read']} min</span>
            <span style="background:{p['color']}18;color:{p['color']};border-radius:8px;
                  padding:4px 10px;font-size:0.75rem;font-weight:700;">
                  🩺 Station: {p['station']} min</span>
            <span style="background:{p['color']}18;color:{p['color']};border-radius:8px;
                  padding:4px 10px;font-size:0.75rem;font-weight:700;">
                  ⏱ Total: {p['total']} min</span>
        </div>
        """, unsafe_allow_html=True)
    else:
        cc1, cc2 = st.columns(2)
        with cc1:
            r_custom = st.number_input("📖 Read (min)", min_value=0, max_value=10,
                                       value=st.session_state.osce_custom_read,
                                       key="r_custom_inp")
            st.session_state.osce_custom_read = r_custom
        with cc2:
            s_custom = st.number_input("🩺 Station (min)", min_value=1, max_value=30,
                                       value=st.session_state.osce_custom_station,
                                       key="s_custom_inp")
            st.session_state.osce_custom_station = s_custom

    st.markdown("</div>", unsafe_allow_html=True)
    st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)

    # ── Control buttons ───────────────────────────────────────────────────────
    if phase_done or (not st.session_state.osce_running and st.session_state.osce_phase == "reading" and st.session_state.osce_phase_start is None):
        # Start / Restart
        btn_label = "▶️  Start Station" if not phase_done else "🔁  Next Station"
        if st.button(btn_label, type="primary", use_container_width=True, key="osce_start"):
            st.session_state.osce_phase       = "reading"
            st.session_state.osce_running     = True
            st.session_state.osce_phase_start = time.time()
            st.rerun()
    else:
        bc1, bc2 = st.columns(2)
        with bc1:
            if st.session_state.osce_running:
                if st.button("⏸  Pause", use_container_width=True, key="osce_pause"):
                    st.session_state.osce_running = False
                    # Save remaining duration into pomo_duration style
                    remaining, _, _, total_ph = _phase_remaining()
                    st.session_state.osce_phase_start = None
                    # Store the paused remaining
                    st.session_state[f"osce_paused_{phase}"] = remaining
                    st.rerun()
            else:
                if st.button("▶️  Resume", use_container_width=True,
                             type="primary", key="osce_resume"):
                    st.session_state.osce_running     = True
                    st.session_state.osce_phase_start = time.time()
                    st.rerun()
        with bc2:
            if st.button("⏭  Skip Phase", use_container_width=True, key="osce_skip"):
                if phase == "reading":
                    st.session_state.osce_phase       = "station"
                    st.session_state.osce_phase_start = time.time()
                    st.session_state.osce_running     = True
                else:
                    st.session_state.osce_phase   = "done"
                    st.session_state.osce_running = False
                    st.session_state.osce_completed += 1
                st.rerun()

    if st.button("🔄  Reset", use_container_width=True, key="osce_reset"):
        st.session_state.osce_phase       = "reading"
        st.session_state.osce_running     = False
        st.session_state.osce_phase_start = None
        st.rerun()

    # ── Completed counter ─────────────────────────────────────────────────────
    st.markdown(f"""
    <div style="background:{theme['card_bg']};border:1px solid {theme['card_border']};
         border-radius:16px;padding:1rem;text-align:center;margin-top:0.8rem;">
        <div style="font-size:2.2rem;font-weight:900;font-family:'Syne',sans-serif;
             color:{theme['primary']};">{st.session_state.osce_completed}</div>
        <div style="font-size:0.76rem;color:{theme['subtext']};font-weight:600;">
             Stations completed</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Phase guide ───────────────────────────────────────────────────────────
    st.markdown(f"""
    <div style="background:{theme['glass_bg']};border:1px solid {theme['card_border']};
         border-radius:14px;padding:0.9rem;margin-top:0.8rem;
         font-size:0.78rem;color:{theme['subtext']};backdrop-filter:blur(8px);">
        <b style="color:{theme['text']}">Phase Guide</b><br><br>
        📖 <b>Reading phase</b> — Read the station instructions carefully.
        Do not enter until the bell.<br><br>
        🩺 <b>Station phase</b> — Perform the clinical task. Manage your time.<br><br>
        🔔 <b>Auto-advance</b> — Reading automatically transitions to Station when time elapses.
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# STATION LOG
# ─────────────────────────────────────────────────────────────────────────────
def _render_station_log(theme: dict):
    st.markdown(f"""
    <div style="font-family:'Syne',sans-serif;font-size:1rem;font-weight:800;
         color:{theme['text']};margin-bottom:0.8rem;display:flex;align-items:center;gap:10px;">
         📋 All 12 OSCE Station Presets
         <div style="flex:1;height:1px;background:{theme['card_border']};"></div>
    </div>
    """, unsafe_allow_html=True)

    cols = st.columns(4)
    for i, (name, cfg) in enumerate(OSCE_PRESETS.items()):
        with cols[i % 4]:
            is_active = (not st.session_state.osce_use_custom and
                         st.session_state.osce_preset == name)
            st.markdown(f"""
            <div style="background:{cfg['color']}{'20' if is_active else '0a'};
                 border:1.5px solid {cfg['color']}{'80' if is_active else '30'};
                 border-radius:12px;padding:0.8rem;margin-bottom:0.6rem;
                 transition:all 0.2s ease;cursor:pointer;">
                <div style="font-size:1.1rem;">{name.split(' ')[0]}</div>
                <div style="font-size:0.8rem;font-weight:700;color:{theme['text']};
                     margin:0.2rem 0;">{' '.join(name.split(' ')[1:])}</div>
                <div style="font-size:0.7rem;color:{theme['subtext']};">
                     📖 {cfg['read']}min + 🩺 {cfg['station']}min</div>
            </div>
            """, unsafe_allow_html=True)
            if st.button(f"Load", key=f"load_{name}", use_container_width=True,
                         label_visibility="collapsed",
                         type="primary" if is_active else "secondary"):
                st.session_state.osce_preset      = name
                st.session_state.osce_use_custom  = False
                st.session_state.osce_phase       = "reading"
                st.session_state.osce_running     = False
                st.session_state.osce_phase_start = None
                st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────────────────────
def _inject_timer_css(t: dict):
    st.markdown(f"""
    <style>
    /* ── Style selector tiles ─────────────────────── */
    .style-tile {{
        background:    {t['card_bg']};
        border:        1.5px solid {t['card_border']};
        border-radius: 16px;
        padding:       1rem 0.8rem;
        text-align:    center;
        cursor:        pointer;
        transition:    all 0.22s ease;
        backdrop-filter: blur(10px);
        margin-bottom: 2px;
    }}
    .style-tile:hover {{
        border-color:  {t['primary']};
        transform:     translateY(-2px);
        box-shadow:    0 6px 16px {t['primary_glow']};
    }}
    .style-tile-active {{
        border-color:  {t['primary']} !important;
        background:    {t['primary']}12 !important;
        box-shadow:    0 4px 18px {t['primary_glow']};
    }}
    .st-ico  {{ font-size:1.6rem; margin-bottom:0.3rem; }}
    .st-name {{ font-family:'Syne',sans-serif; font-size:0.88rem; font-weight:800;
                color:{t['text']}; }}
    .st-sub  {{ font-size:0.70rem; color:{t['subtext']}; margin-top:1px; }}

    /* ── Radial wrapper ───────────────────────────── */
    .radial-wrapper {{
        position:     relative;
        display:      flex;
        align-items:  center;
        justify-content: center;
        width:        280px;
        height:       280px;
        margin:       0 auto 1rem;
    }}
    .radial-centre {{
        position:     absolute;
        text-align:   center;
        pointer-events: none;
    }}
    .radial-time {{
        font-family:   'DM Mono', monospace;
        font-size:     3.2rem;
        font-weight:   500;
        line-height:   1;
        letter-spacing: 0.04em;
    }}
    .radial-phase {{
        font-size:   0.78rem;
        font-weight: 700;
        margin-top:  4px;
        letter-spacing: 0.08em;
    }}

    /* ── LCD wrapper ──────────────────────────────── */
    .lcd-wrapper {{
        position:      relative;
        background:    #04060a;
        border:        1px solid #1a2234;
        border-radius: 20px;
        padding:       1.5rem 1.8rem 1.2rem;
        overflow:      hidden;
        max-width:     400px;
        margin:        0 auto;
    }}
    /* Scanline effect */
    .lcd-scanlines {{
        position:  absolute; inset: 0;
        background: repeating-linear-gradient(
            0deg,
            transparent,
            transparent 2px,
            rgba(0,0,0,0.06) 2px,
            rgba(0,0,0,0.06) 4px
        );
        pointer-events: none;
        z-index: 1;
    }}
    .lcd-badge {{
        font-size:     0.67rem;
        font-weight:   700;
        letter-spacing: 0.14em;
        text-transform: uppercase;
        color:         #334155;
        margin-bottom: 0.6rem;
        display:       flex;
        align-items:   center;
        gap:           6px;
        position:      relative;
        z-index:       2;
    }}
    .lcd-dot {{
        width: 6px; height: 6px; border-radius: 50%; display:inline-block;
    }}
    .lcd-phase-label {{
        font-size:     0.65rem;
        font-weight:   700;
        letter-spacing: 0.18em;
        text-transform: uppercase;
        margin-bottom: 0.2rem;
        position:      relative;
        z-index:       2;
    }}
    .lcd-time {{
        font-family:   'DM Mono', monospace;
        font-size:     4.8rem;
        font-weight:   500;
        letter-spacing: 0.1em;
        line-height:   1;
        position:      relative;
        z-index:       2;
        margin-bottom: 0.8rem;
    }}
    .lcd-bar-track {{
        width:  100%; height: 4px;
        background: #0f172a;
        border-radius: 999px;
        overflow: hidden;
        margin-bottom: 1rem;
        position: relative; z-index: 2;
    }}
    .lcd-bar-fill {{
        height: 100%;
        border-radius: 999px;
        transition: width 0.5s linear, background 0.8s ease;
    }}
    .lcd-phases {{
        display:     flex;
        align-items: center;
        gap:         8px;
        margin-bottom: 0.8rem;
        position:    relative; z-index: 2;
    }}
    .lcd-ph-item {{
        display:     flex;
        align-items: center;
        gap:         5px;
        font-size:   0.68rem;
        font-weight: 700;
        letter-spacing: 0.08em;
        color:       #334155;
        padding:     4px 10px;
        border-radius: 6px;
        border:      1px solid #1a2234;
        transition:  all 0.3s ease;
    }}
    .lcd-ph-active {{
        color:         #e2e8f0;
        border-color:  #334155;
        background:    #0f172a;
    }}
    .lcd-ph-done {{
        color:         #16a34a;
        border-color:  #16a34a40;
        background:    #16a34a10;
    }}
    .lcd-ph-sep {{
        font-size:0.7rem;color:#1e293b;
    }}
    .lcd-ph-time {{
        margin-left: 4px;
        font-size:   0.62rem;
        opacity:     0.6;
    }}
    .lcd-footer {{
        font-size:     0.6rem;
        letter-spacing: 0.14em;
        color:         #1e293b;
        text-transform: uppercase;
        position:      relative; z-index: 2;
        border-top:    1px solid #0f172a;
        padding-top:   0.6rem;
    }}
    </style>
    """, unsafe_allow_html=True)