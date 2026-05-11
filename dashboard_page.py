import streamlit as st

try:
    import plotly.graph_objects as go
except ModuleNotFoundError:
    go = None

import random
import datetime


def _generate_demo_stats(user: dict) -> dict:
    random.seed(42)
    today = datetime.date.today()
    days_back = 365

    daily_minutes = {}
    for i in range(days_back):
        d = today - datetime.timedelta(days=i)
        daily_minutes[d.isoformat()] = random.randint(20, 180) if random.random() > 0.25 else 0

    mcq_sessions = []
    base_accuracy = 55.0
    for i in range(60):
        d = today - datetime.timedelta(days=59 - i)
        acc = min(95, base_accuracy + i * 0.5 + random.uniform(-8, 8))
        count = random.randint(10, 40)
        mcq_sessions.append({
            "date": d.isoformat(),
            "accuracy": round(acc, 1),
            "count": count,
        })

    subjects = [
        "Cardiology", "Neurology", "Pulmonology", "Nephrology",
        "Gastro", "Endocrine", "Haematology", "Pharmacology",
        "Pathology", "Anatomy", "Physiology", "Microbiology",
    ]
    subject_scores = {subject: random.randint(40, 95) for subject in subjects}
    subject_scores["Cardiology"] = 82
    subject_scores["Pharmacology"] = 74
    subject_scores["Pathology"] = 88
    subject_scores["Anatomy"] = 69

    mock_scores = []
    score = 58.0
    for i in range(12):
        d = today - datetime.timedelta(days=330 - i * 28)
        score = min(92, score + random.uniform(0.5, 3.5))
        mock_scores.append({
            "date": d.isoformat(),
            "score": round(score, 1),
            "exam": f"Mock {i + 1}",
        })

    goals = [
        {"label": "Study Hours", "icon": "⏱️", "current": 14, "target": 20, "unit": "hrs", "color": "#e63946"},
        {"label": "MCQs Practiced", "icon": "📝", "current": 87, "target": 100, "unit": "Qs", "color": "#10b981"},
        {"label": "Flashcards", "icon": "🃏", "current": 45, "target": 50, "unit": "", "color": "#8b5cf6"},
        {"label": "Subjects", "icon": "📚", "current": 3, "target": 5, "unit": "", "color": "#f59e0b"},
    ]

    activities = [
        {"time": "2 min ago", "icon": "📝", "text": "Completed 25-question Cardiology MCQ", "badge": "+25 pts", "badge_color": "#10b981"},
        {"time": "1 hr ago", "icon": "⏱️", "text": "Finished 25-min Pomodoro", "badge": "Focus", "badge_color": "#ef4444"},
        {"time": "3 hrs ago", "icon": "🃏", "text": "Reviewed Neurology flashcards", "badge": "SRS", "badge_color": "#8b5cf6"},
        {"time": "Yesterday", "icon": "🩺", "text": "Completed OSCE History Taking", "badge": "Done", "badge_color": "#0891b2"},
        {"time": "2 days ago", "icon": "🤖", "text": "AI Tutor session on DKA", "badge": "AI", "badge_color": "#ec4899"},
    ]

    streak = 0
    for i in range(days_back):
        d = (today - datetime.timedelta(days=i)).isoformat()
        if daily_minutes.get(d, 0) > 0:
            streak += 1
        else:
            break

    return {
        "streak": streak,
        "total_hours": round(sum(daily_minutes.values()) / 60, 1),
        "mcqs_done": sum(s["count"] for s in mcq_sessions),
        "current_score": mock_scores[-1]["score"],
        "rank": 24,
        "daily_minutes": daily_minutes,
        "mcq_sessions": mcq_sessions,
        "subject_scores": subject_scores,
        "mock_scores": mock_scores,
        "goals": goals,
        "activities": activities,
        "target_score": 90.0,
        "target_exam": "OMSB Part 1",
    }


def _merge_stats(db_stats: dict, user: dict) -> dict:
    demo = _generate_demo_stats(user)
    if not db_stats:
        return demo
    return {**demo, **{k: v for k, v in db_stats.items() if v is not None}}


def dashboard_page(theme: dict, db_stats: dict = None):
    user = st.session_state.get("user", {"name": "Student", "id": 0})
    stats = _merge_stats(db_stats or {}, user)

    _inject_dashboard_css(theme)

    st.markdown(f"""
    <div style="display:flex;align-items:center;justify-content:space-between;
                margin-bottom:1.5rem;flex-wrap:wrap;gap:12px;">
        <div>
            <div style="font-family:Syne,sans-serif;font-size:1.8rem;font-weight:900;color:{theme['text']};">
                📊 Analytics Dashboard
            </div>
            <div style="font-size:0.82rem;color:{theme['subtext']};margin-top:0.2rem;">
                Target:
                <span style="color:{theme['primary']};font-weight:700;">
                    {stats['target_exam']} · {stats['target_score']}%
                </span>
            </div>
        </div>
        <div style="font-size:0.76rem;color:{theme['subtext']};
                    background:{theme['glass_bg']};border:1px solid {theme['card_border']};
                    border-radius:8px;padding:6px 14px;">
            Last updated: {datetime.date.today().strftime('%d %b %Y')}
        </div>
    </div>
    """, unsafe_allow_html=True)

    _render_kpis(theme, stats)
    _render_heatmap(theme, stats)

    if go is None:
        _render_chartless_dashboard(theme, stats)
        return

    col_l, col_r = st.columns([3, 2])
    with col_l:
        _render_study_trend(theme, stats)
    with col_r:
        _render_weekly_goals(theme, stats)

    col_a, col_b = st.columns(2)
    with col_a:
        _render_mcq_accuracy(theme, stats)
    with col_b:
        _render_subject_scores(theme, stats)

    col_c, col_d = st.columns([3, 2])
    with col_c:
        _render_score_progression(theme, stats)
    with col_d:
        _render_activity_feed(theme, stats)


def _inject_dashboard_css(t: dict):
    st.markdown(f"""
    <style>
    .dash-card {{
        background: {t["card_bg"]};
        border: 1px solid {t["card_border"]};
        border-radius: 8px;
        padding: 1rem;
        box-shadow: {t["shadow_sm"]};
        margin-bottom: 1rem;
    }}
    .dash-section-title {{
        font-family: Syne, sans-serif;
        font-size: 1rem;
        font-weight: 900;
        color: {t["text"]};
        margin: 1rem 0 0.55rem;
        display: flex;
        align-items: center;
        gap: 8px;
    }}
    .dash-section-sub {{
        font-family: DM Sans, sans-serif;
        font-size: 0.68rem;
        font-weight: 700;
        color: {t["subtext"]};
    }}
    .dash-kpi {{
        background: {t["card_bg"]};
        border: 1px solid {t["card_border"]};
        border-radius: 8px;
        padding: 1rem;
        min-height: 116px;
        box-shadow: {t["shadow_sm"]};
    }}
    .dash-kpi-icon {{
        width: 34px;
        height: 34px;
        border-radius: 8px;
        display: grid;
        place-items: center;
        margin-bottom: 0.55rem;
    }}
    .dash-kpi-value {{
        font-family: Syne, sans-serif;
        font-size: 1.55rem;
        font-weight: 900;
        line-height: 1;
    }}
    .dash-kpi-label {{
        margin-top: 0.35rem;
        font-size: 0.72rem;
        color: {t["subtext"]};
        font-weight: 700;
    }}
    .heat-cell {{
        width: 12px;
        height: 12px;
        border-radius: 3px;
        margin: 1px;
    }}
    </style>
    """, unsafe_allow_html=True)


def _render_kpis(theme: dict, stats: dict):
    items = [
        ("🔥", stats["streak"], "Day Streak", theme["primary"]),
        ("⏱️", stats["total_hours"], "Study Hours", "#10b981"),
        ("📝", stats["mcqs_done"], "MCQs Done", "#8b5cf6"),
        ("🏆", f"#{stats['rank']}", "Rank", "#f59e0b"),
        ("🎯", f"{stats['current_score']}%", "Current Score", "#ef4444"),
    ]

    cols = st.columns(5)
    for col, (icon, value, label, color) in zip(cols, items):
        with col:
            st.markdown(f"""
            <div class="dash-kpi">
                <div class="dash-kpi-icon" style="background:{color}18;color:{color};">{icon}</div>
                <div class="dash-kpi-value" style="color:{color};">{value}</div>
                <div class="dash-kpi-label">{label}</div>
            </div>
            """, unsafe_allow_html=True)


def _render_heatmap(theme: dict, stats: dict):
    st.markdown("""
    <div class="dash-section-title">
        📅 Knowledge Heatmap
        <span class="dash-section-sub">Last 12 months</span>
    </div>
    """, unsafe_allow_html=True)

    today = datetime.date.today()
    levels = [
        theme["surface_raised"],
        f"{theme['primary']}28",
        f"{theme['primary']}55",
        f"{theme['primary']}88",
        theme["primary"],
    ]

    cells = []
    for i in range(364, -1, -1):
        d = today - datetime.timedelta(days=i)
        minutes = stats["daily_minutes"].get(d.isoformat(), 0)
        if minutes == 0:
            color = levels[0]
        elif minutes < 45:
            color = levels[1]
        elif minutes < 90:
            color = levels[2]
        elif minutes < 140:
            color = levels[3]
        else:
            color = levels[4]
        cells.append(f'<div class="heat-cell" title="{d.isoformat()} · {minutes} min" style="background:{color};"></div>')

    st.markdown(
        f"""
        <div class="dash-card" style="overflow-x:auto;">
            <div style="display:flex;flex-wrap:wrap;max-width:760px;">
                {''.join(cells)}
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _plotly_layout(theme: dict, height: int = 280):
    return dict(
        height=height,
        paper_bgcolor="rgba(0,0,0,0)",
        plot_bgcolor="rgba(0,0,0,0)",
        font=dict(family="DM Sans, sans-serif", color=theme["text_muted"], size=11),
        margin=dict(l=10, r=10, t=20, b=20),
        showlegend=False,
        xaxis=dict(gridcolor=theme["card_border"], zeroline=False),
        yaxis=dict(gridcolor=theme["card_border"], zeroline=False),
    )


def _alpha(color: str, alpha: float) -> str:
    if isinstance(color, str) and color.startswith("#") and len(color) == 7:
        r = int(color[1:3], 16)
        g = int(color[3:5], 16)
        b = int(color[5:7], 16)
        return f"rgba({r},{g},{b},{alpha})"
    return color


def _render_study_trend(theme: dict, stats: dict):
    st.markdown("""
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

    colors = [theme["primary"] if m >= 60 else _alpha(theme["primary"], 0.45) if m else theme["card_border"] for m in minutes]

    fig = go.Figure(go.Bar(x=dates, y=minutes, marker_color=colors, marker_line_width=0))
    fig.add_hline(y=60, line_dash="dot", line_color=_alpha(theme["primary"], 0.38))
    fig.update_layout(**_plotly_layout(theme, 250))
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})


def _render_weekly_goals(theme: dict, stats: dict):
    st.markdown("""
    <div class="dash-section-title">
        🎯 Weekly Goals
        <span class="dash-section-sub">This week</span>
    </div>
    """, unsafe_allow_html=True)

    rows = ""
    for goal in stats["goals"]:
        pct = min(100, goal["current"] / goal["target"] * 100)
        rows += f"""
        <div style="margin-bottom:1rem;">
            <div style="display:flex;justify-content:space-between;font-size:0.82rem;font-weight:700;">
                <span>{goal['icon']} {goal['label']}</span>
                <span style="color:{goal['color']};">{goal['current']}{goal['unit']} / {goal['target']}{goal['unit']}</span>
            </div>
            <div style="height:7px;background:{theme['card_border']};border-radius:999px;overflow:hidden;margin-top:6px;">
                <div style="height:100%;width:{pct:.1f}%;background:{goal['color']};"></div>
            </div>
        </div>
        """

    st.markdown(f'<div class="dash-card">{rows}</div>', unsafe_allow_html=True)


def _render_mcq_accuracy(theme: dict, stats: dict):
    st.markdown("""
    <div class="dash-section-title">
        📝 MCQ Accuracy Trend
        <span class="dash-section-sub">Last 60 days</span>
    </div>
    """, unsafe_allow_html=True)

    sessions = stats["mcq_sessions"]
    dates = [s["date"][5:] for s in sessions]
    accuracy = [s["accuracy"] for s in sessions]
    counts = [s["count"] for s in sessions]

    fig = go.Figure()
    fig.add_trace(go.Bar(x=dates, y=counts, marker_color=_alpha(theme["primary"], 0.15), yaxis="y2"))
    fig.add_trace(go.Scatter(
        x=dates,
        y=accuracy,
        mode="lines+markers",
        line=dict(color=theme["primary"], width=2.5, shape="spline"),
        marker=dict(size=4, color=theme["primary"]),
        fill="tozeroy",
        fillcolor=_alpha(theme["primary"], 0.07),
    ))
    fig.add_hline(y=70, line_dash="dot", line_color=_alpha(theme["success"], 0.38))

    layout = _plotly_layout(theme, 280)
    layout["yaxis"] = {**layout["yaxis"], "range": [0, 100], "ticksuffix": "%"}
    layout["yaxis2"] = dict(overlaying="y", side="right", showgrid=False)
    fig.update_layout(**layout)

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})


def _render_subject_scores(theme: dict, stats: dict):
    st.markdown("""
    <div class="dash-section-title">
        🔭 Subject Performance
        <span class="dash-section-sub">Scores</span>
    </div>
    """, unsafe_allow_html=True)

    subjects = list(stats["subject_scores"].keys())
    scores = list(stats["subject_scores"].values())

    fig = go.Figure(go.Bar(
        x=scores,
        y=subjects,
        orientation="h",
        marker_color=theme["primary"],
    ))
    fig.update_layout(**_plotly_layout(theme, 280))
    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})


def _render_score_progression(theme: dict, stats: dict):
    st.markdown(f"""
    <div class="dash-section-title">
        🏆 Mock Exam Score Progression
        <span class="dash-section-sub">Target {stats['target_score']}%</span>
    </div>
    """, unsafe_allow_html=True)

    mocks = stats["mock_scores"]
    labels = [m["exam"] for m in mocks]
    scores = [m["score"] for m in mocks]

    fig = go.Figure(go.Scatter(
        x=labels,
        y=scores,
        mode="lines+markers+text",
        line=dict(color=theme["primary"], width=3, shape="spline"),
        marker=dict(size=8, color=theme["primary"]),
        text=[f"{s:.0f}%" for s in scores],
        textposition="top center",
        fill="tozeroy",
        fillcolor=_alpha(theme["primary"], 0.06),
    ))
    fig.add_hline(y=stats["target_score"], line_dash="dash", line_color=theme["success"])
    fig.add_hline(y=60, line_dash="dot", line_color=_alpha(theme["warning"], 0.5))

    layout = _plotly_layout(theme, 280)
    layout["yaxis"]["range"] = [50, 100]
    layout["yaxis"]["ticksuffix"] = "%"
    fig.update_layout(**layout)

    st.plotly_chart(fig, use_container_width=True, config={"displayModeBar": False})


def _render_activity_feed(theme: dict, stats: dict):
    st.markdown("""
    <div class="dash-section-title">
        ⚡ Recent Activity
        <span class="dash-section-sub">Latest sessions</span>
    </div>
    """, unsafe_allow_html=True)

    rows = ""
    for activity in stats["activities"]:
        rows += f"""
        <div style="display:flex;align-items:flex-start;gap:10px;padding:0.65rem 0;
                    border-bottom:1px solid {theme['card_border']};">
            <div style="width:32px;height:32px;border-radius:8px;background:{theme['glass_bg']};
                        border:1px solid {theme['card_border']};display:grid;place-items:center;">
                {activity['icon']}
            </div>
            <div style="flex:1;">
                <div style="font-size:0.82rem;font-weight:700;color:{theme['text']};">
                    {activity['text']}
                </div>
                <div style="font-size:0.7rem;color:{theme['subtext']};">
                    {activity['time']}
                </div>
            </div>
            <span style="font-size:0.68rem;font-weight:700;background:{activity['badge_color']}18;
                         color:{activity['badge_color']};border-radius:6px;padding:2px 7px;">
                {activity['badge']}
            </span>
        </div>
        """

    st.markdown(f'<div class="dash-card">{rows}</div>', unsafe_allow_html=True)


def _render_chartless_dashboard(theme: dict, stats: dict):
    st.info("Interactive Plotly charts are unavailable, so a lightweight dashboard view is shown.")

    col_l, col_r = st.columns([3, 2])
    with col_l:
        _render_chartless_bars(theme, stats)
    with col_r:
        _render_weekly_goals(theme, stats)

    col_a, col_b = st.columns(2)
    with col_a:
        _render_chartless_mcq(theme, stats)
    with col_b:
        _render_chartless_subjects(theme, stats)

    _render_activity_feed(theme, stats)


def _render_chartless_bars(theme: dict, stats: dict):
    st.markdown("""
    <div class="dash-section-title">
        ⏱️ Daily Study Minutes
        <span class="dash-section-sub">Last 14 days</span>
    </div>
    """, unsafe_allow_html=True)

    today = datetime.date.today()
    bars = []

    for i in range(13, -1, -1):
        d = today - datetime.timedelta(days=i)
        minutes = stats["daily_minutes"].get(d.isoformat(), 0)
        height = max(8, min(96, int(minutes / 180 * 96)))
        color = theme["primary"] if minutes else theme["card_border"]

        bars.append(f"""
        <div style="display:flex;flex-direction:column;align-items:center;gap:6px;min-width:28px;">
            <div style="height:104px;display:flex;align-items:flex-end;">
                <div title="{minutes} min" style="width:18px;height:{height}px;
                            border-radius:6px 6px 3px 3px;background:{color};"></div>
            </div>
            <span style="font-size:0.62rem;color:{theme['subtext']};">{d.strftime('%d')}</span>
        </div>
        """)

    st.markdown(
        f'<div class="dash-card" style="overflow-x:auto;"><div style="display:flex;gap:10px;align-items:flex-end;">{"".join(bars)}</div></div>',
        unsafe_allow_html=True,
    )


def _render_chartless_mcq(theme: dict, stats: dict):
    st.markdown("""
    <div class="dash-section-title">
        📝 MCQ Accuracy
        <span class="dash-section-sub">Latest sessions</span>
    </div>
    """, unsafe_allow_html=True)

    rows = ""
    for session in stats["mcq_sessions"][-6:]:
        rows += f"""
        <div style="margin-bottom:0.8rem;">
            <div style="display:flex;justify-content:space-between;font-size:0.78rem;font-weight:700;">
                <span>{session['date'][5:]}</span>
                <span style="color:{theme['primary']};">{session['accuracy']}%</span>
            </div>
            <div style="height:7px;background:{theme['card_border']};border-radius:999px;overflow:hidden;margin-top:5px;">
                <div style="height:100%;width:{session['accuracy']}%;background:{theme['primary']};"></div>
            </div>
        </div>
        """

    st.markdown(f'<div class="dash-card">{rows}</div>', unsafe_allow_html=True)


def _render_chartless_subjects(theme: dict, stats: dict):
    st.markdown("""
    <div class="dash-section-title">
        🔭 Top Subjects
        <span class="dash-section-sub">Performance score</span>
    </div>
    """, unsafe_allow_html=True)

    rows = ""
    top_subjects = sorted(stats["subject_scores"].items(), key=lambda item: item[1], reverse=True)[:6]

    for subject, score in top_subjects:
        rows += f"""
        <div style="display:flex;align-items:center;justify-content:space-between;
                    border-bottom:1px solid {theme['card_border']};padding:0.55rem 0;">
            <span style="font-size:0.82rem;font-weight:700;color:{theme['text']};">{subject}</span>
            <strong style="color:{theme['primary']};">{score}%</strong>
        </div>
        """

    st.markdown(f'<div class="dash-card">{rows}</div>', unsafe_allow_html=True)
