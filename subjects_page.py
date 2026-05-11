"""
subjects_page.py - MedStudy Oman knowledge library.
Renders every subject, topic, and high-yield note from content.py.
"""

from __future__ import annotations

import re
from html import escape

import streamlit as st

try:
    from content import SUBJECTS as SUBJECTS_LIBRARY
except Exception:
    SUBJECTS_LIBRARY = {}


EXAM_TRACKS = ["SQU-COM", "OMSB", "USMLE", "PLAB", "MRCP", "OSCE"]
CLINICAL_METHOD = [
    ("01", "Prime", "Read the outline, then predict the mechanism before opening notes."),
    ("02", "Encode", "Turn every table, nerve lesion, or drug effect into one active recall card."),
    ("03", "Apply", "Answer MCQs and explain why every wrong option is wrong."),
    ("04", "Present", "Summarise the diagnosis, evidence, and management in 60 seconds."),
]


def _slug(value: str) -> str:
    return re.sub(r"[^a-z0-9]+", "-", value.lower()).strip("-") or "subject"


def _all_subjects() -> list[tuple[str, str, dict]]:
    rows = []
    for category, subjects in SUBJECTS_LIBRARY.items():
        for subject_name, data in subjects.items():
            rows.append((category, subject_name, data))
    return rows


def _matches(query: str, category: str, subject_name: str, data: dict) -> bool:
    if not query:
        return True
    haystack = " ".join([
        category,
        subject_name,
        data.get("notes", ""),
        *data.get("topics", []),
    ]).lower()
    return query.lower() in haystack


def subjects_page(theme: dict):
    _inject_subject_css(theme)

    if not SUBJECTS_LIBRARY:
        st.warning("Subject content is not available yet.")
        return

    all_rows = _all_subjects()
    total_topics = sum(len(data.get("topics", [])) for _, _, data in all_rows)
    total_notes = sum(1 for _, _, data in all_rows if data.get("notes"))

    st.markdown(f"""
    <section class="library-hero">
        <div>
            <div class="library-kicker">MedStudy Knowledge System</div>
            <h1>Every medical subject, organised for clinical recall.</h1>
            <p>
                A complete study library for Oman medical students: pre-clinical sciences,
                clinical rotations, exam tracks, high-yield notes, topic maps, and revision workflow.
            </p>
            <div class="track-row">{''.join(f'<span>{escape(track)}</span>' for track in EXAM_TRACKS)}</div>
        </div>
        <div class="library-command">
            <div class="command-top"><span>Curriculum Coverage</span><b>LIVE</b></div>
            <div class="command-grid">
                <div><strong>{len(all_rows)}</strong><span>Subjects</span></div>
                <div><strong>{total_topics}</strong><span>Topics</span></div>
                <div><strong>{total_notes}</strong><span>Note Sets</span></div>
                <div><strong>{len(SUBJECTS_LIBRARY)}</strong><span>Phases</span></div>
            </div>
        </div>
    </section>
    """, unsafe_allow_html=True)

    filter_col, search_col, mode_col = st.columns([1.3, 2.2, 1.2])
    categories = ["All"] + list(SUBJECTS_LIBRARY.keys())
    with filter_col:
        selected_category = st.selectbox("Curriculum phase", categories, key="subject_category_filter")
    with search_col:
        query = st.text_input("Search the medical library", placeholder="Search ACS, brachial plexus, DKA, antibiotics...", key="subject_search")
    with mode_col:
        density = st.radio("View", ["Atlas", "Deep notes"], horizontal=True, key="subject_density")

    rows = [row for row in all_rows if selected_category == "All" or row[0] == selected_category]
    rows = [row for row in rows if _matches(query.strip(), *row)]

    if not rows:
        st.info("No subjects matched your search. Try a broader clinical term.")
        return

    _render_method(theme)

    left, right = st.columns([1.05, 1.45], gap="large")
    with left:
        st.markdown('<div class="library-section-title">Subject Atlas</div>', unsafe_allow_html=True)
        for category, subject_name, data in rows:
            _subject_card(theme, category, subject_name, data)

    with right:
        selected = st.session_state.get("selected_subject")
        available_names = {name for _, name, _ in rows}
        if not selected or selected not in available_names:
            selected = rows[0][1]
            st.session_state.selected_subject = selected
        selected_row = next((row for row in rows if row[1] == selected), rows[0])
        _subject_detail(theme, *selected_row, deep=(density == "Deep notes"))


def _render_method(theme: dict):
    cells = []
    for number, label, body in CLINICAL_METHOD:
        cells.append(
            f'<div class="method-cell"><b>{number}</b><strong>{escape(label)}</strong>'
            f'<span>{escape(body)}</span></div>'
        )
    st.markdown(f'<div class="method-grid">{"".join(cells)}</div>', unsafe_allow_html=True)


def _subject_card(theme: dict, category: str, subject_name: str, data: dict):
    color = data.get("color", theme["primary"])
    icon = data.get("icon", "📚")
    topics = data.get("topics", [])
    active = st.session_state.get("selected_subject") == subject_name
    key = f"subject_pick_{_slug(category)}_{_slug(subject_name)}"

    st.markdown(f"""
    <div class="subject-card {'active' if active else ''}" style="--subject-color:{color};">
        <div class="subject-card-head">
            <span>{escape(icon)}</span>
            <div><b>{escape(subject_name)}</b><small>{escape(category)} · {len(topics)} topics</small></div>
        </div>
        <p>{escape(topics[0] if topics else 'High-yield clinical framework and notes.')}</p>
    </div>
    """, unsafe_allow_html=True)

    if st.button(f"Open {subject_name}", key=key, use_container_width=True, type="primary" if active else "secondary"):
        st.session_state.selected_subject = subject_name
        st.rerun()


def _subject_detail(theme: dict, category: str, subject_name: str, data: dict, deep: bool):
    color = data.get("color", theme["primary"])
    topics = data.get("topics", [])
    notes = data.get("notes", "").strip()

    st.markdown(f"""
    <article class="detail-panel" style="--subject-color:{color};">
        <div class="detail-topline">{escape(category)}</div>
        <div class="detail-header">
            <div class="detail-icon">{escape(data.get('icon', '📚'))}</div>
            <div>
                <h2>{escape(subject_name)}</h2>
                <p>{len(topics)} focused topics · high-yield notes · recall-first workflow</p>
            </div>
        </div>
    </article>
    """, unsafe_allow_html=True)

    tabs = st.tabs(["Topic Map", "High-Yield Notes", "Exam Drill", "Clinical Links"])

    with tabs[0]:
        cols = st.columns(2)
        for idx, topic in enumerate(topics):
            with cols[idx % 2]:
                st.markdown(f"""
                <div class="topic-row">
                    <span>{idx + 1:02d}</span>
                    <b>{escape(topic)}</b>
                </div>
                """, unsafe_allow_html=True)

    with tabs[1]:
        if notes:
            st.markdown('<div class="notes-shell">', unsafe_allow_html=True)
            st.markdown(notes)
            st.markdown('</div>', unsafe_allow_html=True)
        else:
            st.info("Detailed notes for this subject are being prepared.")
        if deep:
            _deep_note_builder(theme, subject_name, topics)

    with tabs[2]:
        _exam_drill(theme, subject_name, topics)

    with tabs[3]:
        _clinical_links(theme, subject_name)


def _deep_note_builder(theme: dict, subject_name: str, topics: list[str]):
    st.markdown('<div class="library-section-title">Active Recall Builder</div>', unsafe_allow_html=True)
    for topic in topics[:6]:
        st.markdown(f"""
        <div class="recall-card">
            <b>{escape(topic)}</b>
            <span>Ask: mechanism, key presentation, investigation, management, complication, and one Oman/Gulf relevance point.</span>
        </div>
        """, unsafe_allow_html=True)


def _exam_drill(theme: dict, subject_name: str, topics: list[str]):
    st.markdown('<div class="library-section-title">Exam Drill Protocol</div>', unsafe_allow_html=True)
    drills = [
        ("MCQ", f"Do 20 questions from {subject_name}; write a one-line rule for every miss."),
        ("OSCE", f"Present one {subject_name} case aloud using summary, positives, negatives, plan."),
        ("Flashcard", "Create cards only from errors, not from everything you read."),
        ("Teach-back", "Explain the mechanism to a junior student in under two minutes."),
    ]
    for label, body in drills:
        st.markdown(f'<div class="drill-row"><strong>{escape(label)}</strong><span>{escape(body)}</span></div>', unsafe_allow_html=True)


def _clinical_links(theme: dict, subject_name: str):
    links = [
        ("Patient safety", "Red flags, escalation triggers, contraindications."),
        ("Oman context", "Local epidemiology, MOH pathways, common presentations."),
        ("Ward skill", "History, examination, focused investigations, handover."),
        ("Board angle", "OMSB/USMLE-style discriminators and traps."),
    ]
    for title, body in links:
        st.markdown(f'<div class="link-tile"><b>{escape(title)}</b><span>{escape(body)}</span></div>', unsafe_allow_html=True)


def _inject_subject_css(t: dict):
    st.markdown(f"""
    <style>
    .library-hero {{
        display:grid;grid-template-columns:minmax(0,1.35fr) minmax(280px,.65fr);gap:1rem;align-items:stretch;
        border:1px solid {t['card_border']};border-radius:8px;padding:clamp(1rem,2.4vw,2rem);margin-bottom:1rem;
        background:linear-gradient(135deg,{t['primary']}16,transparent 42%),linear-gradient(160deg,{t['surface']},{t['surface_raised']});
        box-shadow:{t['shadow_md']};
    }}
    .library-kicker {{font-size:.68rem;font-weight:900;text-transform:uppercase;color:{t['primary']} !important;margin-bottom:.55rem;}}
    .library-hero h1 {{font-size:clamp(2rem,4vw,3.5rem);line-height:1.03;margin:.1rem 0 .75rem;color:{t['text']} !important;}}
    .library-hero p {{max-width:760px;font-size:1rem;line-height:1.65;color:{t['text_muted']} !important;margin:0 0 1rem;}}
    .track-row {{display:flex;flex-wrap:wrap;gap:8px;}}
    .track-row span {{border:1px solid {t['card_border']};background:{t['glass_bg']};border-radius:8px;padding:6px 10px;font-size:.72rem;font-weight:800;color:{t['text_muted']} !important;}}
    .library-command {{border:1px solid {t['card_border']};border-radius:8px;background:{t['card_bg']};padding:1rem;box-shadow:{t['shadow_sm']};}}
    .command-top {{display:flex;justify-content:space-between;align-items:center;border-bottom:1px solid {t['card_border']};padding-bottom:.75rem;margin-bottom:.75rem;font-size:.72rem;font-weight:900;text-transform:uppercase;color:{t['subtext']} !important;}}
    .command-top b {{color:{t['success']} !important;}}
    .command-grid {{display:grid;grid-template-columns:repeat(2,1fr);gap:.65rem;}}
    .command-grid div {{background:{t['glass_bg']};border:1px solid {t['card_border']};border-radius:8px;padding:.75rem;}}
    .command-grid strong {{display:block;font-family:Syne,sans-serif;font-size:1.55rem;color:{t['primary']} !important;}}
    .command-grid span {{font-size:.68rem;font-weight:800;color:{t['subtext']} !important;}}
    .method-grid {{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:.65rem;margin:.8rem 0 1rem;}}
    .method-cell {{background:{t['card_bg']};border:1px solid {t['card_border']};border-radius:8px;padding:.8rem;min-height:116px;}}
    .method-cell b {{font-family:DM Mono,monospace;color:{t['primary']} !important;font-size:.72rem;}}
    .method-cell strong {{display:block;margin:.35rem 0;color:{t['text']} !important;}}
    .method-cell span {{font-size:.74rem;line-height:1.45;color:{t['text_muted']} !important;}}
    .library-section-title {{font-family:Syne,sans-serif;font-weight:900;color:{t['text']} !important;margin:.75rem 0 .65rem;}}
    .subject-card {{border:1px solid {t['card_border']};border-left:4px solid var(--subject-color);border-radius:8px;padding:.8rem;background:{t['card_bg']};box-shadow:{t['shadow_sm']};margin-bottom:.35rem;}}
    .subject-card.active {{background:linear-gradient(135deg,var(--subject-color)16,{t['card_bg']});border-color:var(--subject-color);}}
    .subject-card-head {{display:flex;gap:.65rem;align-items:center;}}
    .subject-card-head > span {{width:38px;height:38px;border-radius:8px;background:var(--subject-color)18;color:var(--subject-color);display:grid;place-items:center;font-size:1.25rem;}}
    .subject-card b {{display:block;color:{t['text']} !important;}}
    .subject-card small,.subject-card p {{color:{t['subtext']} !important;}}
    .subject-card p {{font-size:.76rem;line-height:1.45;margin:.55rem 0 0;}}
    .detail-panel {{border:1px solid {t['card_border']};border-top:4px solid var(--subject-color);border-radius:8px;background:{t['card_bg']};padding:1rem;margin-bottom:.85rem;box-shadow:{t['shadow_sm']};}}
    .detail-topline {{font-size:.68rem;font-weight:900;text-transform:uppercase;color:var(--subject-color) !important;margin-bottom:.45rem;}}
    .detail-header {{display:flex;align-items:center;gap:.85rem;}}
    .detail-icon {{width:56px;height:56px;border-radius:8px;background:var(--subject-color)18;color:var(--subject-color);display:grid;place-items:center;font-size:1.75rem;}}
    .detail-header h2 {{font-size:1.55rem;margin:0;color:{t['text']} !important;}}
    .detail-header p {{margin:.2rem 0 0;color:{t['subtext']} !important;font-size:.82rem;}}
    .topic-row,.recall-card,.drill-row,.link-tile {{border:1px solid {t['card_border']};background:{t['card_bg']};border-radius:8px;padding:.78rem;margin-bottom:.55rem;}}
    .topic-row {{display:flex;gap:.65rem;align-items:flex-start;min-height:76px;}}
    .topic-row span {{font-family:DM Mono,monospace;color:var(--subject-color) !important;font-weight:900;}}
    .topic-row b,.recall-card b,.link-tile b {{color:{t['text']} !important;}}
    .recall-card span,.drill-row span,.link-tile span {{display:block;margin-top:.35rem;color:{t['text_muted']} !important;font-size:.78rem;line-height:1.45;}}
    .drill-row strong {{color:{t['primary']} !important;}}
    .notes-shell {{border:1px solid {t['card_border']};border-radius:8px;background:{t['glass_bg']};padding:1rem;}}
    @media (max-width:900px) {{.library-hero,.method-grid {{grid-template-columns:1fr;}}}}
    </style>
    """, unsafe_allow_html=True)
