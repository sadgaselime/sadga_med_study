"""
clinical_tools_pages.py - high-yield clinical study modules for MedStudy Oman.
"""

from __future__ import annotations

import math
import sqlite3
from datetime import date, timedelta

import pandas as pd
import streamlit as st

from database import DB_NAME


def _inject_tool_css(theme: dict):
    st.markdown(
        f"""
        <style>
        .tool-grid {{
            display:grid;
            grid-template-columns: repeat(auto-fit, minmax(230px, 1fr));
            gap: 14px;
            margin: .6rem 0 1rem;
        }}
        .tool-card {{
            border:1px solid {theme['card_border']};
            border-radius:18px;
            background:{theme['card_bg']};
            box-shadow:{theme['shadow_sm']};
            padding:1rem;
            min-height:132px;
        }}
        .tool-kicker {{
            color:{theme['primary']} !important;
            font-size:.68rem;
            text-transform:uppercase;
            letter-spacing:.1em;
            font-weight:950;
            margin-bottom:.4rem;
        }}
        .tool-title {{
            color:{theme['text']} !important;
            font-size:1.05rem;
            font-weight:950;
            line-height:1.15;
        }}
        .tool-copy {{
            color:{theme['text_muted']} !important;
            font-size:.82rem;
            line-height:1.55;
            margin-top:.5rem;
        }}
        .case-step {{
            border:1px solid {theme['card_border']};
            border-left:5px solid {theme['primary']};
            border-radius:18px;
            background:{theme['glass_bg']};
            padding:1rem 1.1rem;
            box-shadow:{theme['shadow_sm']};
            margin-bottom:.85rem;
        }}
        .case-pill-row {{
            display:flex;
            gap:8px;
            flex-wrap:wrap;
            margin-top:.65rem;
        }}
        .case-pill {{
            border:1px solid {theme['card_border']};
            border-radius:999px;
            background:{theme['hover_bg']};
            color:{theme['text']} !important;
            padding:6px 10px;
            font-size:.76rem;
            font-weight:850;
        }}
        .atlas-grid {{
            display:grid;
            grid-template-columns: repeat(auto-fit, minmax(260px, 1fr));
            gap:14px;
        }}
        .atlas-card {{
            border:1px solid {theme['card_border']};
            border-radius:18px;
            overflow:hidden;
            background:{theme['card_bg']};
            box-shadow:{theme['shadow_sm']};
        }}
        .atlas-media {{
            min-height:190px;
            position:relative;
            background:
                linear-gradient(135deg, rgba(15,23,42,.92), rgba(30,64,175,.54)),
                repeating-linear-gradient(90deg, rgba(255,255,255,.09) 0 1px, transparent 1px 18px);
            display:grid;
            place-items:center;
            color:white !important;
            font-weight:950;
            letter-spacing:.08em;
            text-transform:uppercase;
        }}
        .atlas-annotation {{
            position:absolute;
            inset:18px;
            border:2px dashed rgba(250,204,21,.92);
            border-radius:18px;
            box-shadow:0 0 0 999px rgba(15,23,42,.16);
        }}
        .atlas-body {{
            padding:1rem;
        }}
        .score-band {{
            border:1px solid {theme['card_border']};
            border-radius:18px;
            background:linear-gradient(135deg, {theme['primary']}18, {theme['secondary']}12);
            padding:1rem;
            margin:.85rem 0;
        }}
        </style>
        """,
        unsafe_allow_html=True,
    )


PATIENT_CASES = [
    {
        "title": "Pleuritic chest pain after long flight",
        "chief": "A 34-year-old woman presents with pleuritic chest pain, mild hemoptysis, tachycardia, and recent 9-hour travel.",
        "history": ["No fever", "Uses combined oral contraceptive pill", "Right calf discomfort for 2 days"],
        "orders": {
            "ECG": "Sinus tachycardia; no ST elevation.",
            "D-dimer": "Elevated.",
            "CT Pulmonary Angiography": "Filling defect in a segmental pulmonary artery.",
            "Troponin": "Normal.",
            "Chest X-ray": "No consolidation or pneumothorax.",
        },
        "interpretation": "Segmental pulmonary embolism without biomarker evidence of right heart strain.",
        "diagnosis": "Pulmonary embolism",
    },
    {
        "title": "Vomiting and Kussmaul breathing",
        "chief": "A 21-year-old with type 1 diabetes has vomiting, abdominal pain, polyuria, and deep labored breathing.",
        "history": ["Missed insulin for 24 hours", "Dry mucous membranes", "Capillary glucose very high"],
        "orders": {
            "Venous blood gas": "pH 7.12, HCO3 9 mmol/L.",
            "Serum ketones": "Positive.",
            "Urea/electrolytes": "Potassium 4.8 mmol/L, mild AKI.",
            "ECG": "Sinus tachycardia.",
            "Urine culture": "Pending; infection screen sent.",
        },
        "interpretation": "High anion gap metabolic acidosis with ketonaemia in insulin deficiency.",
        "diagnosis": "Diabetic ketoacidosis",
    },
]


def render_interactive_cases(theme: dict):
    _inject_tool_css(theme)
    st.markdown("### Diagnostic Simulator")
    st.caption("Branching clinical reasoning practice. Content is modular so a future case database can replace these starter cases.")
    case = st.selectbox("Case", PATIENT_CASES, format_func=lambda item: item["title"], key="case_select")
    if st.session_state.get("case_title") != case["title"]:
        st.session_state.case_title = case["title"]
        st.session_state.case_step = 1
        st.session_state.case_orders = []
        st.session_state.case_dx = ""

    st.markdown(
        f"""
        <div class="case-step">
            <div class="tool-kicker">Chief complaint</div>
            <div class="tool-title">{case['chief']}</div>
            <div class="case-pill-row">{''.join(f'<span class="case-pill">{item}</span>' for item in case['history'])}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    st.progress((st.session_state.get("case_step", 1) - 1) / 3)
    if st.session_state.case_step == 1:
        st.markdown("#### Step 1: Order investigations")
        st.session_state.case_orders = st.multiselect("Choose labs or imaging", list(case["orders"]), default=st.session_state.get("case_orders", []))
        if st.button("Review ordered results", type="primary", use_container_width=True, key="case_step_1"):
            st.session_state.case_step = 2
            st.rerun()
    elif st.session_state.case_step == 2:
        st.markdown("#### Step 2: Interpret results")
        selected = st.session_state.get("case_orders", [])
        if not selected:
            st.warning("No investigations ordered. Go back and choose at least one.")
        for order in selected:
            st.info(f"**{order}:** {case['orders'][order]}")
        interpretation = st.radio(
            "Most accurate interpretation",
            [
                case["interpretation"],
                "Findings are most consistent with uncomplicated viral illness.",
                "Immediate thrombolysis is mandatory in all patients.",
                "The workup rules out dangerous cardiopulmonary disease.",
            ],
            key="case_interpretation",
        )
        c1, c2 = st.columns(2)
        with c1:
            if st.button("Back to orders", use_container_width=True, key="case_back_1"):
                st.session_state.case_step = 1
                st.rerun()
        with c2:
            if st.button("Commit interpretation", type="primary", use_container_width=True, key="case_step_2"):
                st.session_state.case_step = 3
                st.session_state.case_interpretation_correct = interpretation == case["interpretation"]
                st.rerun()
    else:
        st.markdown("#### Step 3: Select diagnosis")
        dx_options = [case["diagnosis"], "Acute coronary syndrome", "Pneumonia", "Panic attack"]
        st.session_state.case_dx = st.radio("Most likely diagnosis", dx_options, key="case_dx_select")
        if st.button("Submit diagnostic decision", type="primary", use_container_width=True, key="case_submit"):
            if st.session_state.case_dx == case["diagnosis"] and st.session_state.get("case_interpretation_correct"):
                st.success(f"Correct. Diagnosis: {case['diagnosis']}.")
            elif st.session_state.case_dx == case["diagnosis"]:
                st.warning("Diagnosis is correct, but review the interpretation step.")
            else:
                st.error(f"Best diagnosis: {case['diagnosis']}.")
            st.info("Framework: risk factors -> targeted testing -> result interpretation -> management-safe diagnosis.")
        if st.button("Reset case", use_container_width=True, key="case_reset"):
            st.session_state.case_step = 1
            st.session_state.case_orders = []
            st.rerun()


def render_clinical_calculators(theme: dict):
    _inject_tool_css(theme)
    calculators = ["Glasgow Coma Scale", "Wells Criteria for PE", "TIMI Risk Score", "eGFR CKD-EPI 2021"]
    query = st.text_input("Search calculators", placeholder="GCS, Wells, TIMI, eGFR...", key="calc_search")
    filtered = [item for item in calculators if query.lower() in item.lower()] if query else calculators
    st.markdown('<div class="tool-grid">', unsafe_allow_html=True)
    for item in filtered:
        st.markdown(f'<div class="tool-card"><div class="tool-kicker">Calculator</div><div class="tool-title">{item}</div><div class="tool-copy">Interactive risk score with transparent clinical inputs.</div></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)
    selected = st.selectbox("Open calculator", filtered or calculators, key="calc_selected")
    if selected == "Glasgow Coma Scale":
        _render_gcs(theme)
    elif selected == "Wells Criteria for PE":
        _render_wells_pe(theme)
    elif selected == "TIMI Risk Score":
        _render_timi(theme)
    else:
        _render_egfr(theme)


def _render_score(title: str, score: float, interpretation: str):
    st.markdown(
        f"""
        <div class="score-band">
            <div class="tool-kicker">{title}</div>
            <div class="tool-title">Score: {score}</div>
            <div class="tool-copy">{interpretation}</div>
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_gcs(theme: dict):
    eye = st.selectbox("Eye opening", [("Spontaneous", 4), ("To voice", 3), ("To pain", 2), ("None", 1)], format_func=lambda x: f"{x[0]} ({x[1]})")
    verbal = st.selectbox("Verbal response", [("Oriented", 5), ("Confused", 4), ("Words", 3), ("Sounds", 2), ("None", 1)], format_func=lambda x: f"{x[0]} ({x[1]})")
    motor = st.selectbox("Motor response", [("Obeys commands", 6), ("Localizes pain", 5), ("Withdraws", 4), ("Abnormal flexion", 3), ("Extension", 2), ("None", 1)], format_func=lambda x: f"{x[0]} ({x[1]})")
    score = eye[1] + verbal[1] + motor[1]
    severity = "Severe brain injury; airway risk if <= 8." if score <= 8 else "Moderate impairment." if score <= 12 else "Mild or normal range."
    _render_score("Glasgow Coma Scale", score, severity)


def _render_wells_pe(theme: dict):
    items = [
        ("Clinical signs of DVT", 3.0),
        ("PE more likely than alternative diagnosis", 3.0),
        ("Heart rate > 100", 1.5),
        ("Immobilization or surgery in previous 4 weeks", 1.5),
        ("Previous DVT/PE", 1.5),
        ("Hemoptysis", 1.0),
        ("Malignancy", 1.0),
    ]
    score = sum(weight for label, weight in items if st.checkbox(f"{label} (+{weight})", key=f"wells_{label}"))
    _render_score("Wells Criteria for PE", score, "PE likely: consider imaging pathway." if score > 4 else "PE unlikely: D-dimer pathway may be appropriate if low risk.")


def _render_timi(theme: dict):
    factors = [
        "Age >= 65",
        "At least 3 CAD risk factors",
        "Known CAD stenosis >= 50%",
        "Aspirin use in last 7 days",
        "Severe angina in last 24 hours",
        "ST deviation >= 0.5 mm",
        "Positive cardiac marker",
    ]
    score = sum(1 for factor in factors if st.checkbox(factor, key=f"timi_{factor}"))
    _render_score("TIMI Risk Score", score, "Higher risk; consider early invasive strategy and aggressive ACS management." if score >= 3 else "Lower TIMI risk, but continue full ACS evaluation.")


def _render_egfr(theme: dict):
    age = st.slider("Age", 18, 100, 45)
    sex = st.radio("Sex", ["Female", "Male"], horizontal=True)
    creatinine = st.number_input("Serum creatinine (mg/dL)", min_value=0.3, max_value=15.0, value=1.0, step=0.1)
    female = sex == "Female"
    k = 0.7 if female else 0.9
    alpha = -0.241 if female else -0.302
    egfr = 142 * (min(creatinine / k, 1) ** alpha) * (max(creatinine / k, 1) ** -1.2) * (0.9938 ** age) * (1.012 if female else 1)
    stage = "G1/G2 range if no other kidney damage marker" if egfr >= 60 else "CKD G3 or worse range; correlate clinically and repeat."
    _render_score("eGFR CKD-EPI 2021", round(egfr, 1), stage)


ATLAS_ITEMS = [
    {"title": "Right lower lobe pneumonia", "type": "X-ray", "system": "Respiratory", "finding": "Lobar opacity with air bronchograms"},
    {"title": "Extradural hemorrhage", "type": "CT", "system": "Neuro", "finding": "Biconvex hyperdense collection"},
    {"title": "Reed-Sternberg cells", "type": "Histology", "system": "Pathology", "finding": "Large bilobed cells in inflammatory background"},
    {"title": "Osteoarthritis knee", "type": "X-ray", "system": "MSK", "finding": "Joint-space narrowing and osteophytes"},
]


def render_imaging_pathology_atlas(theme: dict):
    _inject_tool_css(theme)
    media_type = st.selectbox("Media type", ["All", "X-ray", "CT", "MRI", "Histology"], key="atlas_type")
    system = st.selectbox("System", ["All"] + sorted({item["system"] for item in ATLAS_ITEMS}), key="atlas_system")
    annotated = st.toggle("Show annotation overlay", value=True, key="atlas_annotation")
    items = [
        item for item in ATLAS_ITEMS
        if (media_type == "All" or item["type"] == media_type) and (system == "All" or item["system"] == system)
    ]
    st.markdown('<div class="atlas-grid">', unsafe_allow_html=True)
    for item in items:
        overlay = '<div class="atlas-annotation"></div>' if annotated else ""
        st.markdown(
            f"""
            <div class="atlas-card">
                <div class="atlas-media">{item['type']}{overlay}</div>
                <div class="atlas-body">
                    <div class="tool-kicker">{item['system']}</div>
                    <div class="tool-title">{item['title']}</div>
                    <div class="tool-copy">{item['finding']}</div>
                </div>
            </div>
            """,
            unsafe_allow_html=True,
        )
    st.markdown('</div>', unsafe_allow_html=True)


DRUG_ROWS = [
    {"Drug/Class": "Carbamazepine", "MOA": "Voltage-gated sodium channel blockade", "Critical Side Effects": "SJS/TEN, agranulocytosis, hyponatraemia", "Black Box / Exam Warning": "HLA-B*1502 risk in susceptible ancestry", "Interactions": "CYP inducer; reduces OCP/warfarin effectiveness"},
    {"Drug/Class": "Clozapine", "MOA": "Atypical antipsychotic; D2/5-HT2A effects", "Critical Side Effects": "Agranulocytosis, myocarditis, seizures", "Black Box / Exam Warning": "Mandatory ANC monitoring", "Interactions": "Additive CNS depression; smoking alters levels"},
    {"Drug/Class": "Warfarin", "MOA": "Inhibits vitamin K epoxide reductase", "Critical Side Effects": "Bleeding, skin necrosis, teratogenicity", "Black Box / Exam Warning": "Many food/drug interactions", "Interactions": "Amiodarone, TMP-SMX, metronidazole increase INR"},
    {"Drug/Class": "ACE inhibitors", "MOA": "Reduce angiotensin II and aldosterone", "Critical Side Effects": "Cough, hyperkalaemia, angioedema", "Black Box / Exam Warning": "Contraindicated in pregnancy", "Interactions": "K-sparing diuretics increase hyperkalaemia risk"},
    {"Drug/Class": "Linezolid", "MOA": "Blocks 50S initiation complex", "Critical Side Effects": "Thrombocytopenia, serotonin syndrome", "Black Box / Exam Warning": "Monitor blood counts with prolonged use", "Interactions": "SSRIs/SNRIs increase serotonin syndrome risk"},
]


def render_pharmacology_matrix(theme: dict):
    _inject_tool_css(theme)
    df = pd.DataFrame(DRUG_ROWS)
    query = st.text_input("Search drug, mechanism, toxicity, or interaction", placeholder="SJS, agranulocytosis, warfarin, CYP...", key="pharm_search")
    if query:
        mask = df.apply(lambda row: row.astype(str).str.contains(query, case=False, regex=False).any(), axis=1)
        df = df[mask]
    st.dataframe(df, use_container_width=True, hide_index=True)
    if not df.empty:
        row = st.selectbox("Open high-yield drug card", df.to_dict("records"), format_func=lambda item: item["Drug/Class"], key="pharm_card")
        st.markdown(
            f"""
            <div class="tool-card">
                <div class="tool-kicker">High-yield pharmacology</div>
                <div class="tool-title">{row['Drug/Class']}</div>
                <div class="tool-copy"><b>MOA:</b> {row['MOA']}</div>
                <div class="tool-copy"><b>Critical effects:</b> {row['Critical Side Effects']}</div>
                <div class="tool-copy"><b>Warnings:</b> {row['Black Box / Exam Warning']}</div>
                <div class="tool-copy"><b>Interactions:</b> {row['Interactions']}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )


def render_spaced_repetition_analytics(theme: dict):
    _inject_tool_css(theme)
    user = st.session_state.get("user") if st.session_state.get("logged_in") else None
    stats = _load_sr_stats(user["id"] if user else None)
    st.markdown("#### Spaced Repetition Analytics")
    c1, c2, c3 = st.columns(3)
    c1.metric("Due tomorrow", stats["due_tomorrow"])
    c2.metric("Mastered", stats["mastered"])
    c3.metric("Review streak", f"{stats['streak']} days")
    st.line_chart(stats["curve"], x="Day", y="Retention", use_container_width=True)


def _load_sr_stats(user_id: int | None):
    curve = pd.DataFrame({
        "Day": list(range(0, 15)),
        "Retention": [round(100 * math.exp(-day / 9), 1) for day in range(0, 15)],
    })
    if not user_id:
        return {"due_tomorrow": 8, "mastered": 14, "streak": 4, "curve": curve}
    conn = sqlite3.connect(DB_NAME)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    tomorrow = (date.today() + timedelta(days=1)).isoformat()
    c.execute("SELECT COUNT(*) AS n FROM flashcard_progress WHERE user_id = ? AND next_review <= ?", (user_id, tomorrow))
    due_tomorrow = int(c.fetchone()["n"] or 0)
    c.execute("SELECT COUNT(*) AS n FROM flashcard_progress WHERE user_id = ? AND times_reviewed >= 3", (user_id,))
    mastered = int(c.fetchone()["n"] or 0)
    c.execute("SELECT DISTINCT substr(next_review, 1, 10) AS d FROM flashcard_progress WHERE user_id = ? ORDER BY d DESC", (user_id,))
    review_days = [row["d"] for row in c.fetchall() if row["d"]]
    conn.close()
    streak = _review_streak(review_days)
    return {"due_tomorrow": due_tomorrow, "mastered": mastered, "streak": streak, "curve": curve}


def _review_streak(days: list[str]) -> int:
    day_set = set(days)
    today = date.today()
    streak = 0
    for offset in range(30):
        if (today - timedelta(days=offset)).isoformat() in day_set:
            streak += 1
        else:
            break
    return streak
