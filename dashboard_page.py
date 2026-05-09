"""
dashboard_page.py — MedStudy Oman 🩺
Phase 6: Analytics & Dashboard Engine
KPI cards · Knowledge Heatmap · Study Streak · MCQ Trends
Subject Radar · Score Progression · Goals · Activity Feed
"""

import streamlit as st
import plotly.graph_objects as go
import plotly.express as px
import random
import datetime
from collections import defaultdict


# ─────────────────────────────────────────────────────────────────────────────
# DEMO DATA GENERATOR  (used when real DB stats are sparse)
# ─────────────────────────────────────────────────────────────────────────────
def _generate_demo_stats(user: dict) -> dict:
    """Produce realistic-looking demo analytics data."""
    random.seed(42)
    today     = datetime.date.today()
    days_back = 365

    # Daily study minutes — last 365 days
    daily_minutes = {}
    for i in range(days_back):
        d = today - datetime.timedelta(days=i)
        if random.random() > 0.25:  # ~75% days studied
            mins = random.randint(20, 180)
        else:
            mins = 0
        daily_minutes[d.isoformat()] = mins

    # MCQ sessions — accuracy per session last 60 days
    mcq_sessions = []
    base_accuracy = 55.0
    for i in range(60):
        d     = today - datetime.timedelta(days=59 - i)
        acc   = min(95, base_accuracy + i * 0.5 + random.uniform(-8, 8))
        count = random.randint(10, 40)
        mcq_sessions.append({"date": d.isoformat(), "accuracy": round(acc, 1),
                              "count": count})

    # Subject performance (0–100 per subject)
    subjects = [
        "Cardiology", "Neurology", "Pulmonology", "Nephrology",
        "Gastro", "Endocrine", "Haematology", "Pharmacology",
        "Pathology", "Anatomy", "Physiology", "Microbiology",
    ]
    subject_scores = {s: random.randint(40, 95) for s in subjects}
    subject_scores["Cardiology"]   = 82
    subject_scores["Pharmacology"] = 74
    subject_scores["Pathology"]    = 88
    subject_scores["Anatomy"]      = 69

    # Mock exam scores
    mock_scores = []
    score = 58.0
    for i in range(12):
        d     = today - datetime.timedelta(days=330 - i * 28)
        score = min(92, score + random.uniform(0.5, 3.5))
        mock_scores.append({"date": d.isoformat(), "score": round(score, 1),
                             "exam": f"Mock {i+1}"})

    # Weekly goals
    goals = [
        {"label": "Study Hours",    "icon": "⏱️", "current": 14, "target": 20,
         "unit": "hrs", "color": "#e63946"},
        {"label": "MCQs Practiced", "icon": "📝", "current": 87, "target": 100,
         "unit": "Qs",  "color": "#10b981"},
        {"label": "Flashcards",     "icon": "🃏", "current": 45, "target": 50,
         "unit": "",    "color": "#8b5cf6"},
        {"label": "Subjects",       "icon": "📚", "current": 3,  "target": 5,
         "unit": "",    "color": "#f59e0b"},
    ]

    # Recent activity
    activities = [
        {"time": "2 min ago",  "icon": "📝", "text": "Completed 25-question Cardiology MCQ",
         "badge": "+25 pts",  "badge_color": "#10b981"},
        {"time": "1 hr ago",   "icon": "⏱️", "text": "Finished 25-min Pomodoro — Pharmacology",
         "badge": "🍅 ×1",   "badge_color": "#ef4444"},
        {"time": "3 hrs ago",  "icon": "🃏", "text": "Reviewed 30 Neurology flashcards",
         "badge": "SRS +1d",  "badge_color": "#8b5cf6"},
        {"time": "Yesterday",  "icon": "🩺", "text": "Completed OSCE — History Taking station",
         "badge": "✅ Done",  "badge_color": "#0891b2"},
        {"time": "Yesterday",  "icon": "💡", "text": "Added 3 mnemonics to Personal Vault",
         "badge": "🏦 Saved", "badge_color": "#f59e0b"},
        {"time": "2 days ago", "icon": "📖", "text": "Studied Pathology — Neoplasia chapter",
         "badge": "90 min",   "badge_color": "#7c3aed"},
        {"time": "3 days ago", "icon": "🤖", "text": "AI Tutor session — DKA pathophysiology",
         "badge": "Session",  "badge_color": "#ec4899"},
    ]

    # Streak calculation
    streak = 0
    for i in range(days_back):
        d = (today - datetime.timedelta(days=i)).isoformat()
        if daily_minutes.get(d, 0) > 0:
            streak += 1
        else:
            break

    return {
        "streak":          streak,
        "total_hours":     round(sum(daily_minutes.values()) / 60, 1),
        "mcqs_done":       sum(s["count"] for s in mcq_sessions),
        "current_score":   mock_scores[-1]["score"] if mock_scores else 72.0,
        "rank":            24,
        "daily_minutes":   daily_minutes,
        "mcq_sessions":    mcq_sessions,
        "subject_scores":  subject_scores,
        "mock_scores":     mock_scores,
        "goals":           goals,
        "activities":      activities,
        "target_score":    90.0,
        "target_exam":     "OMSB Part 1",
    }


def _merge_stats(db_stats: dict, user: dict) -> dict:
    """Merge real DB stats with demo fallbacks."""
    demo  = _generate_demo_stats(user)
    if not db_stats:
        return demo
    merged = {**demo, **{k: v for k, v in db_stats.items() if v is not None}}
    return merged


# ─────────────────────────────────────────────────────────────────────────────
# PLOTLY THEME HELPER
# ─────────────────────────────────────────────────────────────────────────────
def _plotly_layout(theme: dict, title: str = "", height: int = 300) -> dict:
    """Return base Plotly layout dict matching the current theme."""
    is_dark = theme["family"] == "dark"
    return dict(
        title       = dict(text=title, font=dict(
            family="Syne, sans-serif", size=14,
            color=theme["text"]
        )) if title else None,
        height       = height,
        paper_bgcolor= "rgba(0,0,0,0)",
        plot_bgcolor = "rgba(0,0,0,0)",
        font         = dict(family="DM Sans, sans-serif",
                            color=theme["text_muted"], size=11),
        margin       = dict(l=10, r=10, t=30 if title else 10, b=10),
        showlegend   = False,
        xaxis        = dict(
            gridcolor   = theme["card_border"],
            linecolor   = theme["card_border"],
            tickcolor   = theme["card_border"],
            tickfont    = dict(color=theme["subtext"], size=10),
            showgrid    = True,
            zeroline    = False,
        ),
        yaxis        = dict(
            gridcolor   = theme["card_border"],
            linecolor   = theme["card_border"],
            tickcolor   = theme["card_border"],
            tickfont    = dict(color=theme["subtext"], size=10),
            showgrid    = True,
            zeroline    = False,
        ),
    )


def _plotly_config() -> dict:
    return dict(
        displayModeBar  = False,
        responsive      = True,
        staticPlot      = False,
    )


# ─────────────────────────────────────────────────────────────────────────────
# MAIN ENTRY
# ─────────────────────────────────────────────────────────────────────────────
def dashboard_page(theme: dict, db_stats: dict = None):
    user  = st.session_state.get("user", {"name": "Student", "id": 0})
    stats = _merge_stats(db_stats or {}, user)

    _inject_dashboard_css(theme)

    # ── Page header ───────────────────────────────────────────────────────────
    st.markdown(f"""
    <div style="display:flex;align-items:center;justify-content:space-between;
         margin-bottom:1.5rem;flex-wrap:wrap;gap:12px;">
        <div>
            <div style="font-family:'Syne',sans-serif;font-size:1.8rem;font-weight:900;
                 color:{theme['text']};letter-spacing:-0.03em;">
                 📊 Analytics Dashboard
            </div>
            <div style="font-size:0.82rem;color:{theme['subtext']};margin-top:0.2rem;">
                 Your personal study intelligence · Target:
                 <span style="color:{theme['primary']};font-weight:700;">
                 {stats['target_exam']} — {stats['target_score']}%</span>
            </div>
        </div>
        <div style="font-size:0.76rem;color:{theme['subtext']};
             background:{theme['glass_bg']};border:1px solid {theme['card_border']};
             border-radius:10px;padding:6px 14px;backdrop-filter:blur(8px);">
             Last updated: {datetime.date.today().strftime('%d %b %Y')}
        </div>
    </div>
    """, unsafe_allow_html=True)

    _render_kpi_row(theme, stats)
    _render_heatmap(theme, stats)

    col_l, col_r = st.columns([3, 2])
    with col_l:
        _render_study_trend(theme, stats)
    with col_r:
        _render_weekly_goals(theme, stats)

    col_a, col_b = st.columns(2)
    with col_a:
        _render_mcq_accuracy(theme, stats)
    with col_b:
        _render_subject_radar(theme, stats)

    col_c, col_d = st.columns([3, 2])
    with col_c:
        _render_score_progression(theme, stats)
    with col_d:
        _render_activity_feed(theme, stats)


# ─────────────────────────────────────────────────────────────────────────────
# KPI ROW
# ─────────────────────────────────────────────────────────────────────────────
def _render_kpi_row(theme: dict, stats: dict):
    kpis = [
        ("🔥", str(stats["streak"]),             "Day Streak",         theme["primary"],  "Keep going!"),
        ("📊", f"{stats['current_score']:.1f}%", "Current Score",      "#10b981",         f"Target {stats['target_score']}%"),
        ("📝", str(stats["mcqs_done"]),           "MCQs Practiced",     "#8b5cf6",         "Total all-time"),
        ("⏱️", f"{stats['total_hours']:.0f}h",   "Study Hours",        "#f59e0b",         "All-time total"),
        ("🏆", f"#{stats['rank']}",               "National Rank",      "#0891b2",         "Among all students"),
    ]

    cols = st.columns(5)
    for col, (icon, value, label, color, sub) in zip(cols, kpis):
        with col:
            st.markdown(f"""
            <div class="kpi-card" style="border-top:3px solid {color};">
                <div class="kpi-icon" style="background:{color}18;color:{color};">{icon}</div>
                <div class="kpi-value" style="color:{color};">{value}</div>
                <div class="kpi-label">{label}</div>
                <div class="kpi-sub">{sub}</div>
            </div>
            """, unsafe_allow_html=True)

    st.markdown("<div style='height:1.2rem'></div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# KNOWLEDGE HEATMAP
# ─────────────────────────────────────────────────────────────────────────────
def _render_heatmap(theme: dict, stats: dict):
    st.markdown(f"""
    <div class="dash-section-title">
        🗓️ Knowledge Heatmap
        <span class="dash-section-sub">Daily study activity — last 12 months</span>
    </div>
    """, unsafe_allow_html=True)

    daily = stats["daily_minutes"]
    today = datetime.date.today()

    # Build 52-week grid (Sun→Sat)
    # Start from 52 weeks ago, on the nearest Sunday
    start = today - datetime.timedelta(weeks=52)
    # Snap to Sunday
    start = start - datetime.timedelta(days=start.weekday() + 1)

    weeks, days_grid = [], []
    d = start
    while d <= today:
        week = []
        for _ in range(7):
            mins  = daily.get(d.isoformat(), 0)
            week.append({"date": d.isoformat(), "mins": mins, "day": d})
            d += datetime.timedelta(days=1)
        weeks.append(week)

    # Map minutes → intensity 0-4
    def _intensity(mins):
        if mins == 0:   return 0
        if mins < 30:   return 1
        if mins < 60:   return 2
        if mins < 120:  return 3
        return 4

    # Colour scales per theme family
    if theme["family"] == "dark":
        scale = [
            theme["surface_raised"],
            theme["primary"] + "30",
            theme["primary"] + "55",
            theme["primary"] + "88",
            theme["primary"],
        ]
    else:
        p = theme["primary"]
        scale = ["#e8ecf0", p + "40", p + "70", p + "aa", p]

    # Build HTML grid
    month_labels = {}
    for wi, week in enumerate(weeks):
        for cell in week:
            m = cell["day"].strftime("%b")
            if m not in month_labels:
                month_labels[m] = wi

    # Month header
    month_html  = '<div class="hmap-month-row">'
    prev_wi     = 0
    for month, wi in sorted(month_labels.items(), key=lambda x: x[1]):
        span = wi - prev_wi
        month_html += (f'<div style="width:{span*16}px;min-width:{span*16}px;'
                       f'font-size:0.65rem;color:{theme["subtext"]};'
                       f'font-weight:600;">{month}</div>')
        prev_wi = wi
    month_html += "</div>"

    # Day labels (Mon, Wed, Fri only)
    day_labels = '<div class="hmap-day-labels">'
    for label in ["", "Mon", "", "Wed", "", "Fri", ""]:
        day_labels += (f'<div style="height:14px;line-height:14px;font-size:0.6rem;'
                       f'color:{theme["subtext"]};text-align:right;'
                       f'padding-right:4px;">{label}</div>')
    day_labels += "</div>"

    # Cells
    cells_html = '<div class="hmap-grid">'
    for week in weeks:
        cells_html += '<div class="hmap-col">'
        for cell in week:
            lvl   = _intensity(cell["mins"])
            color = scale[lvl]
            tip   = f"{cell['date']}: {cell['mins']} min" if cell["mins"] else cell["date"]
            cells_html += (
                f'<div class="hmap-cell" style="background:{color};" '
                f'title="{tip}"></div>'
            )
        cells_html += "</div>"
    cells_html += "</div>"

    # Legend
    legend_html = (
        f'<div class="hmap-legend">'
        f'<span style="font-size:0.65rem;color:{theme["subtext"]};">Less</span>'
    )
    for s in scale:
        legend_html += (
            f'<div style="width:12px;height:12px;border-radius:3px;'
            f'background:{s};"></div>'
        )
    legend_html += (
        f'<span style="font-size:0.65rem;color:{theme["subtext"]};">More</span>'
        f"</div>"
    )

    st.markdown(f"""
    <div class="dash-card" style="margin-bottom:1.2rem;">
        <div style="overflow-x:auto;padding-bottom:4px;">
            <div style="display:flex;gap:0;min-width:fit-content;">
                {day_labels}
                <div>
                    {month_html}
                    {cells_html}
                </div>
            </div>
        </div>
        {legend_html}
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# STUDY TREND (bar chart — last 30 days)
# ─────────────────────────────────────────────────────────────────────────────
def _render_study_trend(theme: dict, stats: dict):
    st.markdown(f"""
    <div class="dash-section-title">
        ⏱️ Daily Study Minutes
        <span class="dash-section-sub">Last 30 days</span>
    </div>
    """, unsafe_allow_html=True)

    today = datetime.date.today()
    dates, minutes = [], []
    for i in range(29, -1, -1):
        d = today - datetime.timedelta(days=i)
        dates.append(d.strftime("%d %b"))
        minutes.append(stats["daily_minutes"].get(d.isoformat(), 0))

    colors = []
    for m in minutes:
        if m == 0:      colors.append(theme["card_border"])
        elif m < 60:    colors.append(theme["primary"] + "80")
        else:           colors.append(theme["primary"])

    fig = go.Figure(go.Bar(
        x           = dates,
        y           = minutes,
        marker_color= colors,
        marker_line_width = 0,
        hovertemplate = "<b>%{x}</b><br>%{y} minutes<extra></extra>",
    ))

    # Target line at 60 mins
    fig.add_hline(
        y              = 60,
        line_dash      = "dot",
        line_color     = theme["primary"] + "60",
        annotation_text= "60 min goal",
        annotation_font_color = theme["subtext"],
        annotation_font_size  = 10,
    )

    layout = _plotly_layout(theme, height=240)
    layout["bargap"]     = 0.3
    layout["xaxis"]["showticklabels"] = True
    layout["xaxis"]["tickangle"] = -45
    layout["xaxis"]["nticks"]    = 10
    fig.update_layout(**layout)

    st.plotly_chart(fig, use_container_width=True, config=_plotly_config())


# ─────────────────────────────────────────────────────────────────────────────
# WEEKLY GOALS
# ─────────────────────────────────────────────────────────────────────────────
def _render_weekly_goals(theme: dict, stats: dict):
    st.markdown(f"""
    <div class="dash-section-title">
        🎯 Weekly Goals
        <span class="dash-section-sub">This week's targets</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<div class="dash-card">', unsafe_allow_html=True)
    for g in stats["goals"]:
        pct = min(100, g["current"] / g["target"] * 100)
        done = pct >= 100
        bar_color = theme["success"] if done else g["color"]
        st.markdown(f"""
        <div style="margin-bottom:1.1rem;">
            <div style="display:flex;justify-content:space-between;
                 align-items:center;margin-bottom:5px;">
                <div style="display:flex;align-items:center;gap:7px;">
                    <span style="font-size:1rem;">{g['icon']}</span>
                    <span style="font-size:0.83rem;font-weight:600;color:{theme['text']};">
                        {g['label']}</span>
                    {'<span style="font-size:0.7rem;background:#16a34a20;color:#16a34a;border-radius:999px;padding:1px 8px;font-weight:700;">✓ Done!</span>' if done else ''}
                </div>
                <span style="font-size:0.8rem;font-weight:700;color:{g['color']};">
                    {g['current']}{g['unit']}
                    <span style="color:{theme['subtext']};font-weight:400;">
                        / {g['target']}{g['unit']}
                    </span>
                </span>
            </div>
            <div style="width:100%;height:7px;background:{theme['card_border']};
                 border-radius:999px;overflow:hidden;">
                <div style="height:100%;width:{pct:.1f}%;
                     background:{bar_color};border-radius:999px;
                     transition:width 0.8s cubic-bezier(0.4,0,0.2,1);
                     {'box-shadow:0 0 8px ' + bar_color + '80;' if done else ''}">
                </div>
            </div>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# MCQ ACCURACY TREND
# ─────────────────────────────────────────────────────────────────────────────
def _render_mcq_accuracy(theme: dict, stats: dict):
    st.markdown(f"""
    <div class="dash-section-title">
        📝 MCQ Accuracy Trend
        <span class="dash-section-sub">Last 60 days</span>
    </div>
    """, unsafe_allow_html=True)

    sessions = stats["mcq_sessions"]
    dates    = [s["date"][5:]   for s in sessions]   # MM-DD
    accuracy = [s["accuracy"]   for s in sessions]
    counts   = [s["count"]      for s in sessions]

    # Smooth line + bar combo
    fig = go.Figure()

    # Volume bars (secondary)
    fig.add_trace(go.Bar(
        x              = dates,
        y              = counts,
        name           = "Questions",
        marker_color   = theme["primary"] + "25",
        marker_line_width = 0,
        yaxis          = "y2",
        hovertemplate  = "<b>%{x}</b><br>%{y} questions<extra></extra>",
    ))

    # Accuracy line (primary)
    fig.add_trace(go.Scatter(
        x              = dates,
        y              = accuracy,
        name           = "Accuracy %",
        mode           = "lines+markers",
        line           = dict(color=theme["primary"], width=2.5,
                              shape="spline", smoothing=1.2),
        marker         = dict(size=4, color=theme["primary"],
                              line=dict(width=1.5, color=theme["surface"])),
        fill           = "tozeroy",
        fillcolor      = theme["primary"] + "12",
        hovertemplate  = "<b>%{x}</b><br>Accuracy: %{y:.1f}%<extra></extra>",
    ))

    # 70% target line
    fig.add_hline(
        y=70, line_dash="dot", line_color=theme["success"] + "60",
        annotation_text="70% target",
        annotation_font_color=theme["subtext"],
        annotation_font_size=10,
    )

    layout           = _plotly_layout(theme, height=270)
    layout["yaxis"]  = {**layout["yaxis"], "range": [0, 100],
                        "ticksuffix": "%", "title": None}
    layout["yaxis2"] = dict(
        overlaying = "y", side = "right", showgrid = False,
        tickfont   = dict(color=theme["subtext"], size=9),
        title      = None,
    )
    layout["showlegend"] = False
    layout["xaxis"]["nticks"] = 8
    layout["xaxis"]["tickangle"] = -30
    layout["bargap"] = 0.15
    fig.update_layout(**layout)

    st.plotly_chart(fig, use_container_width=True, config=_plotly_config())


# ─────────────────────────────────────────────────────────────────────────────
# SUBJECT RADAR
# ─────────────────────────────────────────────────────────────────────────────
def _render_subject_radar(theme: dict, stats: dict):
    st.markdown(f"""
    <div class="dash-section-title">
        🔭 Subject Performance Radar
        <span class="dash-section-sub">Score per subject</span>
    </div>
    """, unsafe_allow_html=True)

    subjects = list(stats["subject_scores"].keys())
    scores   = list(stats["subject_scores"].values())
    # Close the polygon
    subjects_c = subjects + [subjects[0]]
    scores_c   = scores   + [scores[0]]

    fig = go.Figure()

    # Filled area
    fig.add_trace(go.Scatterpolar(
        r           = scores_c,
        theta       = subjects_c,
        fill        = "toself",
        fillcolor   = theme["primary"] + "22",
        line        = dict(color=theme["primary"], width=2),
        mode        = "lines+markers",
        marker      = dict(size=5, color=theme["primary"]),
        hovertemplate = "<b>%{theta}</b><br>Score: %{r}%<extra></extra>",
    ))

    # Target outline
    target_scores = [80] * len(subjects) + [80]
    fig.add_trace(go.Scatterpolar(
        r         = target_scores,
        theta     = subjects_c,
        mode      = "lines",
        line      = dict(color=theme["success"] + "60", width=1.5, dash="dot"),
        hoverinfo = "skip",
    ))

    layout = _plotly_layout(theme, height=300)
    layout["polar"] = dict(
        bgcolor     = "rgba(0,0,0,0)",
        radialaxis  = dict(
            visible   = True, range=[0, 100],
            tickfont  = dict(size=8, color=theme["subtext"]),
            gridcolor = theme["card_border"],
            linecolor = theme["card_border"],
            ticksuffix= "%",
        ),
        angularaxis = dict(
            tickfont  = dict(size=9, color=theme["text_muted"]),
            gridcolor = theme["card_border"],
            linecolor = theme["card_border"],
        ),
    )
    layout.pop("xaxis", None)
    layout.pop("yaxis", None)
    fig.update_layout(**layout)

    st.plotly_chart(fig, use_container_width=True, config=_plotly_config())


# ─────────────────────────────────────────────────────────────────────────────
# SCORE PROGRESSION
# ─────────────────────────────────────────────────────────────────────────────
def _render_score_progression(theme: dict, stats: dict):
    st.markdown(f"""
    <div class="dash-section-title">
        🏆 Mock Exam Score Progression
        <span class="dash-section-sub">All mock exams · Target: {stats['target_score']}%</span>
    </div>
    """, unsafe_allow_html=True)

    mocks  = stats["mock_scores"]
    labels = [m["exam"]  for m in mocks]
    scores = [m["score"] for m in mocks]

    fig = go.Figure()

    # Area fill
    fig.add_trace(go.Scatter(
        x            = labels,
        y            = scores,
        mode         = "lines+markers+text",
        line         = dict(color=theme["primary"], width=3, shape="spline"),
        marker       = dict(
            size  = 8, color=theme["primary"],
            line  = dict(width=2, color=theme["surface"]),
        ),
        text         = [f"{s:.0f}%" for s in scores],
        textposition = "top center",
        textfont     = dict(size=9, color=theme["text_muted"]),
        fill         = "tozeroy",
        fillcolor    = theme["primary"] + "10",
        hovertemplate= "<b>%{x}</b><br>Score: %{y:.1f}%<extra></extra>",
    ))

    # Target line
    fig.add_hline(
        y=stats["target_score"],
        line_dash="dash",
        line_color=theme["success"],
        annotation_text=f"Target {stats['target_score']:.0f}%",
        annotation_font_color=theme["success"],
        annotation_font_size=11,
    )

    # Passing line
    fig.add_hline(
        y=60,
        line_dash="dot",
        line_color=theme["warning"] + "80",
        annotation_text="Pass 60%",
        annotation_font_color=theme["subtext"],
        annotation_font_size=10,
    )

    layout = _plotly_layout(theme, height=270)
    layout["yaxis"]["range"]      = [50, 100]
    layout["yaxis"]["ticksuffix"] = "%"
    layout["xaxis"]["tickangle"]  = -20
    fig.update_layout(**layout)

    st.plotly_chart(fig, use_container_width=True, config=_plotly_config())


# ─────────────────────────────────────────────────────────────────────────────
# ACTIVITY FEED
# ─────────────────────────────────────────────────────────────────────────────
def _render_activity_feed(theme: dict, stats: dict):
    st.markdown(f"""
    <div class="dash-section-title">
        ⚡ Recent Activity
        <span class="dash-section-sub">Your last 7 sessions</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown(f'<div class="dash-card" style="padding:0.8rem 1rem;">', unsafe_allow_html=True)
    for i, act in enumerate(stats["activities"]):
        border = f"border-bottom:1px solid {theme['card_border']};" if i < len(stats["activities"]) - 1 else ""
        st.markdown(f"""
        <div style="display:flex;align-items:flex-start;gap:10px;
             padding:0.6rem 0;{border}">
            <div style="width:32px;height:32px;border-radius:10px;
                 background:{theme['glass_bg']};border:1px solid {theme['card_border']};
                 display:flex;align-items:center;justify-content:center;
                 font-size:0.9rem;flex-shrink:0;">{act['icon']}</div>
            <div style="flex:1;min-width:0;">
                <div style="font-size:0.8rem;color:{theme['text']};line-height:1.4;
                     font-weight:500;white-space:nowrap;overflow:hidden;
                     text-overflow:ellipsis;">{act['text']}</div>
                <div style="font-size:0.7rem;color:{theme['subtext']};
                     margin-top:2px;">{act['time']}</div>
            </div>
            <span style="font-size:0.68rem;font-weight:700;
                 background:{act['badge_color']}18;color:{act['badge_color']};
                 border-radius:6px;padding:2px 7px;white-space:nowrap;
                 flex-shrink:0;">{act['badge']}</span>
        </div>
        """, unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)

    # Weak subjects alert
    weak = [(s, v) for s, v in stats["subject_scores"].items() if v < 65]

    # Build weak subject rows outside the f-string
    if weak:
        weak_rows = "".join(
            f'<div style="display:flex;justify-content:space-between;margin-bottom:3px;">'
            f'<span style="font-size:0.78rem;color:{theme["text"]};">{s}</span>'
            f'<span style="font-size:0.78rem;font-weight:700;color:{theme["warning"]};">{v}%</span>'
            f'</div>'
            for s, v in sorted(weak, key=lambda x: x[1])[:4]
        )
        st.markdown(f"""
        <div style="background:{theme['warning']}12;border:1px solid {theme['warning']}40;
             border-radius:14px;padding:0.9rem 1rem;margin-top:0.8rem;">
            <div style="font-size:0.72rem;font-weight:800;color:{theme['warning']};
                 letter-spacing:0.08em;text-transform:uppercase;margin-bottom:0.5rem;">
                 ⚠️ Needs Attention
            </div>
            {weak_rows}
        </div>
        """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────────────────────
def _inject_dashboard_css(t: dict):
    st.markdown(f"""
    <style>
    /* ── KPI cards ─────────────────────────────────── */
    .kpi-card {{
        background:     {t['card_bg']};
        border:         1px solid {t['card_border']};
        border-radius:  18px;
        padding:        1.1rem 0.9rem;
        text-align:     center;
        transition:     all 0.25s ease;
        backdrop-filter: blur(12px);
        animation:      scaleIn 0.4s ease both;
        margin-bottom:  0.5rem;
    }}
    .kpi-card:hover {{
        transform:  translateY(-4px);
        box-shadow: var(--shadow-md), var(--glow);
    }}
    .kpi-icon {{
        width:  40px; height: 40px; border-radius: 12px;
        display: flex; align-items: center; justify-content: center;
        font-size: 1.1rem; margin: 0 auto 0.5rem;
    }}
    .kpi-value {{
        font-family: 'Syne', sans-serif;
        font-size:   1.7rem; font-weight: 900; line-height: 1;
    }}
    .kpi-label {{
        font-size:   0.73rem; font-weight: 700;
        color:       {t['text']}; margin-top: 2px;
    }}
    .kpi-sub {{
        font-size:   0.65rem; color: {t['subtext']};
        margin-top:  2px;
    }}

    /* ── Section header ─────────────────────────────── */
    .dash-section-title {{
        font-family:   'Syne', sans-serif;
        font-size:     0.95rem;
        font-weight:   800;
        color:         {t['text']};
        margin-bottom: 0.6rem;
        display:       flex;
        align-items:   baseline;
        gap:           8px;
    }}
    .dash-section-sub {{
        font-family:   'DM Sans', sans-serif;
        font-size:     0.72rem;
        font-weight:   400;
        color:         {t['subtext']};
    }}

    /* ── Generic card wrapper ────────────────────────── */
    .dash-card {{
        background:    {t['card_bg']};
        border:        1px solid {t['card_border']};
        border-radius: 18px;
        padding:       1.2rem 1.3rem;
        backdrop-filter: blur(12px);
        margin-bottom: 0.3rem;
    }}

    /* ── Heatmap ──────────────────────────────────────── */
    .hmap-grid {{
        display:  flex;
        gap:      3px;
    }}
    .hmap-col {{
        display:        flex;
        flex-direction: column;
        gap:            3px;
    }}
    .hmap-cell {{
        width:         14px;
        height:        14px;
        border-radius: 3px;
        cursor:        default;
        transition:    transform 0.15s ease;
        flex-shrink:   0;
    }}
    .hmap-cell:hover {{
        transform: scale(1.4);
        z-index:   10;
    }}
    .hmap-month-row {{
        display:       flex;
        margin-bottom: 4px;
        height:        16px;
    }}
    .hmap-day-labels {{
        display:        flex;
        flex-direction: column;
        gap:            3px;
        padding-top:    20px;
        margin-right:   4px;
        flex-shrink:    0;
    }}
    .hmap-legend {{
        display:     flex;
        align-items: center;
        gap:         4px;
        margin-top:  8px;
    }}

    /* ── Plotly chart container ───────────────────────── */
    .js-plotly-plot .plotly {{
        border-radius: 12px !important;
    }}
    </style>
    """, unsafe_allow_html=True)