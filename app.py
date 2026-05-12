"""
PULSE.md - unified premium medical study SPA.

A single-file Streamlit application with:
- glassmorphic SaaS design system
- SPA state-machine routing through st.session_state.current_view
- local Subject -> Chapter -> Topic resource database
- AI study tools using Gemini/OpenAI-compatible secrets
- medical calculators, ABG interpretation, and MCQ assessment
"""

from __future__ import annotations

import json
import math
import re
from datetime import datetime
from typing import Any

import requests
import streamlit as st

import pulse_backend as backend


st.set_page_config(
    page_title="PULSE.md | Premium Medical Study",
    page_icon="🩺",
    layout="wide",
    initial_sidebar_state="collapsed",
)


VIEWS = {
    "home": "🏠 Home Dashboard",
    "vault": "📚 Vault Library",
    "ai_lab": "🔬 Dynamic AI Lab",
    "assessment": "📝 Assessment Arena",
    "admin": "⚙️ Admin Studio",
}

AI_TOOLS = ["Syllabus Synthesizer", "Mnemonic Craftsman", "Clinical Professor Chat"]


PULSE_DB: dict[str, dict[str, dict[str, dict[str, Any]]]] = {
    "Internal Medicine": {
        "Cardiology": {
            "Acute Coronary Syndrome": {
                "overview": (
                    "Acute coronary syndrome is myocardial ischemia caused by abrupt coronary blood flow reduction. "
                    "The key split is STEMI, NSTEMI, and unstable angina because reperfusion timing changes outcomes."
                ),
                "notes": """
### Recognition
- Central pressure-like chest pain, diaphoresis, nausea, dyspnea, syncope, or silent symptoms in diabetes/older adults.
- ECG within 10 minutes and serial troponins are core early investigations.
- Always consider lethal mimics: aortic dissection, pulmonary embolism, tension pneumothorax, esophageal rupture.

### Initial Management
- ABCDE, continuous monitoring, IV access, aspirin if not contraindicated, nitrates only if safe, analgesia, and reperfusion planning.
- STEMI is a time-critical reperfusion emergency.
- NSTEMI needs risk stratification for early invasive angiography.
""",
                "pearls": [
                    "Inferior STEMI can involve the right ventricle. Avoid nitrates if hypotensive or RV infarct is suspected.",
                    "A normal first troponin does not exclude very early ACS.",
                    "ST elevation in contiguous leads is an emergency until proven otherwise.",
                ],
                "flashcards": [
                    {"front": "Which ECG leads suggest inferior MI?", "back": "II, III, and aVF."},
                    {"front": "What is the first test in suspected ACS?", "back": "A 12-lead ECG within 10 minutes."},
                    {"front": "Name two dangerous ACS mimics.", "back": "Aortic dissection and pulmonary embolism."},
                ],
                "mcqs": [
                    {
                        "question": "A 58-year-old man has crushing chest pain and ST elevation in II, III, and aVF. What territory is involved?",
                        "options": ["Anterior", "Inferior", "Lateral", "Septal"],
                        "correct": "Inferior",
                        "explanation": "II, III, and aVF view the inferior wall, commonly supplied by the RCA.",
                    },
                    {
                        "question": "A hypotensive patient with inferior STEMI has clear lungs and raised JVP. Which medication requires caution?",
                        "options": ["Aspirin", "Nitrates", "Oxygen if hypoxic", "Unfractionated heparin"],
                        "correct": "Nitrates",
                        "explanation": "This suggests RV infarction; nitrates can drop preload and worsen shock.",
                    },
                ],
            },
            "Heart Failure": {
                "overview": "Heart failure is a clinical syndrome caused by impaired cardiac filling, ejection, or both.",
                "notes": """
### Core Model
- Think preload, afterload, contractility, rhythm, and valves.
- HFrEF commonly benefits from ARNI/ACEi/ARB, beta blocker, MRA, and SGLT2 inhibitor therapy.
- Acute pulmonary edema requires oxygen/ventilatory support, nitrates if hypertensive, diuretics if congested, and trigger treatment.
""",
                "pearls": [
                    "BNP supports diagnosis but is not a substitute for clinical assessment.",
                    "S3, raised JVP, basal crackles, and edema point toward congestion.",
                    "Always search for triggers: ischemia, arrhythmia, infection, anemia, renal failure, non-adherence.",
                ],
                "flashcards": [
                    {"front": "Name the four HFrEF mortality-benefit drug pillars.", "back": "ARNI/ACEi/ARB, beta blocker, MRA, SGLT2 inhibitor."},
                    {"front": "What does an S3 suggest?", "back": "Volume overload and increased ventricular filling pressure."},
                ],
                "mcqs": [
                    {
                        "question": "A patient with HFrEF remains symptomatic on ACE inhibitor and beta blocker. Which drug class improves survival and reduces hospitalization?",
                        "options": ["NSAID", "SGLT2 inhibitor", "Short-acting nifedipine", "Oral salbutamol"],
                        "correct": "SGLT2 inhibitor",
                        "explanation": "SGLT2 inhibitors are now core HFrEF therapy, even without diabetes.",
                    }
                ],
            },
        },
        "Endocrinology": {
            "Diabetic Ketoacidosis": {
                "overview": "DKA is insulin deficiency causing hyperglycemia, ketogenesis, and high anion gap metabolic acidosis.",
                "notes": """
### Why It Happens
- Insulin deficiency plus catecholamines, cortisol, glucagon, and growth hormone drives lipolysis and ketone production.
- Osmotic diuresis causes dehydration, sodium loss, potassium depletion, and AKI risk.

### Management Priorities
1. Fluids and hemodynamic stabilization.
2. Potassium assessment before insulin.
3. Fixed-rate IV insulin when potassium is safe.
4. Treat the trigger.
""",
                "pearls": [
                    "Total body potassium is depleted even when serum potassium is high.",
                    "Do not start insulin in severe hypokalemia.",
                    "Cerebral edema risk rises with rapid osmolar shifts, especially in younger patients.",
                ],
                "flashcards": [
                    {"front": "What three findings define DKA?", "back": "Hyperglycemia, ketones, and metabolic acidosis."},
                    {"front": "Why can potassium appear high in DKA?", "back": "Acidosis and insulin deficiency shift potassium out of cells."},
                    {"front": "First fluid in most adult DKA protocols?", "back": "Isotonic crystalloid, adjusted to local protocol and sodium/osmolality."},
                ],
                "mcqs": [
                    {
                        "question": "A patient with DKA has potassium 2.8 mmol/L. What is the safest next step?",
                        "options": ["Start insulin now", "Replace potassium before insulin", "Give bicarbonate routinely", "Stop fluids"],
                        "correct": "Replace potassium before insulin",
                        "explanation": "Insulin shifts potassium intracellularly and can precipitate life-threatening arrhythmia.",
                    }
                ],
            }
        },
    },
    "Preclinical": {
        "Neuroanatomy": {
            "Stroke Localization": {
                "overview": "Stroke localization maps deficits to vascular territories to guide imaging and reperfusion decisions.",
                "notes": """
### Territory Patterns
- MCA: contralateral face/arm weakness, aphasia if dominant hemisphere, neglect if non-dominant.
- ACA: contralateral leg weakness, abulia, urinary incontinence.
- Posterior circulation: diplopia, dysarthria, dysphagia, ataxia, vertigo, crossed signs.
""",
                "pearls": [
                    "FAST screens many anterior strokes but can miss posterior circulation events.",
                    "Dominant MCA disease produces aphasia; non-dominant MCA disease produces neglect.",
                    "Last-known-well time controls reperfusion eligibility pathways.",
                ],
                "flashcards": [
                    {"front": "Which artery is most linked to aphasia?", "back": "Dominant hemisphere MCA."},
                    {"front": "Which territory affects leg more than arm?", "back": "ACA territory."},
                ],
                "mcqs": [
                    {
                        "question": "Right arm weakness with expressive aphasia most likely localizes to which territory?",
                        "options": ["Left MCA", "Right MCA", "Left ACA", "Basilar artery"],
                        "correct": "Left MCA",
                        "explanation": "Dominant left MCA affects language cortex and contralateral face/arm motor function.",
                    }
                ],
            }
        },
        "Pharmacology": {
            "Beta Blockers": {
                "overview": "Beta blockers antagonize beta adrenergic receptors, lowering heart rate, contractility, and renin release.",
                "notes": """
### Clinical Uses
- Hypertension in selected patients, angina, post-MI secondary prevention, HFrEF with evidence-based agents, rate control, thyrotoxicosis symptoms.
- Avoid abrupt withdrawal in ischemic heart disease.

### Safety
- Watch for bradycardia, AV block, bronchospasm with nonselective agents, fatigue, and masking hypoglycemia symptoms.
""",
                "pearls": [
                    "Evidence-based HFrEF beta blockers include bisoprolol, carvedilol, and metoprolol succinate.",
                    "Nonselective beta blockers can worsen asthma/COPD bronchospasm.",
                    "Beta blockers reduce renin release through beta-1 blockade at juxtaglomerular cells.",
                ],
                "flashcards": [
                    {"front": "Which beta receptor increases heart rate?", "back": "Beta-1."},
                    {"front": "Name one nonselective beta blocker.", "back": "Propranolol, nadolol, or timolol."},
                ],
                "mcqs": [
                    {
                        "question": "A patient with asthma needs migraine prophylaxis. Which drug is most concerning?",
                        "options": ["Propranolol", "Amitriptyline", "Topiramate", "Candesartan"],
                        "correct": "Propranolol",
                        "explanation": "Propranolol is nonselective and may provoke bronchospasm.",
                    }
                ],
            }
        },
    },
}


ASSESSMENT_BANK: list[dict[str, Any]] = [
    q
    for subject in PULSE_DB.values()
    for chapter in subject.values()
    for topic in chapter.values()
    for q in topic["mcqs"]
]


def content_tree() -> dict[str, Any]:
    if "content_tree" not in st.session_state or st.session_state.get("refresh_content"):
        st.session_state.content_tree = backend.fetch_content_tree(PULSE_DB)
        st.session_state.refresh_content = False
    return st.session_state.content_tree


def assessment_bank() -> list[dict[str, Any]]:
    return backend.fetch_assessment_bank(content_tree()) or ASSESSMENT_BANK


def reset_content_cache() -> None:
    st.session_state.refresh_content = True


def init_state() -> None:
    tree = content_tree()
    default_subject = next(iter(tree))
    defaults = {
        "current_view": "home",
        "visual_mode": "light",
        "clinical_focus": False,
        "selected_subject": default_subject,
        "selected_chapter": None,
        "selected_topic": None,
        "ai_tool": AI_TOOLS[0],
        "ai_track_result": None,
        "mnemonic_result": None,
        "professor_messages": [],
        "assessment_answers": {},
        "assessment_submitted": {},
        "assessment_score": 0,
        "daily_goal_percent": 72,
        "auth": None,
        "backend_error": None,
        "admin_table": "subjects",
        "admin_ai_result": None,
        "refresh_content": False,
    }
    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value
    subject = st.session_state.selected_subject
    if subject not in tree:
        subject = default_subject
        st.session_state.selected_subject = subject
    chapters = list(tree[subject])
    if st.session_state.selected_chapter not in chapters:
        st.session_state.selected_chapter = chapters[0]
    topics = list(tree[subject][st.session_state.selected_chapter])
    if st.session_state.selected_topic not in topics:
        st.session_state.selected_topic = topics[0]


def mode_tokens() -> dict[str, str]:
    if st.session_state.visual_mode == "dark":
        return {
            "bg": "radial-gradient(circle at 15% 5%, rgba(124,58,237,0.36), transparent 34%), radial-gradient(circle at 85% 12%, rgba(6,182,212,0.24), transparent 30%), linear-gradient(135deg, #070817 0%, #111827 54%, #172554 100%)",
            "text": "#f8fbff",
            "muted": "rgba(226,232,240,0.72)",
            "card": "rgba(15,23,42,0.58)",
            "border": "rgba(148,163,184,0.22)",
            "primary": "#a78bfa",
            "secondary": "#22d3ee",
            "success": "#34d399",
            "warning": "#fbbf24",
            "danger": "#fb7185",
            "shadow": "0 18px 60px rgba(0,0,0,0.34)",
        }
    return {
        "bg": "radial-gradient(circle at 12% 8%, rgba(196,181,253,0.42), transparent 28%), radial-gradient(circle at 88% 14%, rgba(147,197,253,0.34), transparent 26%), linear-gradient(135deg, #f7f3ff 0%, #eef7ff 45%, #fafdff 100%)",
        "text": "#172033",
        "muted": "rgba(51,65,85,0.72)",
        "card": "rgba(255,255,255,0.65)",
        "border": "rgba(255,255,255,0.5)",
        "primary": "#7c3aed",
        "secondary": "#0ea5e9",
        "success": "#10b981",
        "warning": "#f59e0b",
        "danger": "#e11d48",
        "shadow": "0 8px 32px rgba(31,38,135,0.04)",
    }


def inject_design_system() -> None:
    t = mode_tokens()
    st.markdown(
        f"""
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&family=Space+Grotesk:wght@600;700;800&display=swap');

:root {{
  --pulse-bg: {t['bg']};
  --pulse-text: {t['text']};
  --pulse-muted: {t['muted']};
  --pulse-card: {t['card']};
  --pulse-border: {t['border']};
  --pulse-primary: {t['primary']};
  --pulse-secondary: {t['secondary']};
  --pulse-success: {t['success']};
  --pulse-warning: {t['warning']};
  --pulse-danger: {t['danger']};
  --pulse-shadow: {t['shadow']};
}}

html, body, [data-testid="stAppViewContainer"], .stApp {{
  background: var(--pulse-bg) !important;
  color: var(--pulse-text) !important;
  font-family: Inter, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif !important;
}}

[data-testid="stHeader"], [data-testid="stToolbar"], [data-testid="stSidebar"] {{
  display: none !important;
}}

.block-container {{
  padding-top: 1.1rem !important;
  max-width: 1440px !important;
}}

* {{
  letter-spacing: 0 !important;
}}

.pulse-shell {{
  position: relative;
  min-height: 100vh;
}}

.floating-orbit {{
  position: fixed;
  inset: auto 3vw 8vh auto;
  width: 240px;
  height: 240px;
  border-radius: 999px;
  background: radial-gradient(circle, rgba(124,58,237,0.16), transparent 68%);
  filter: blur(8px);
  pointer-events: none;
  animation: pulse-drift 11s ease-in-out infinite alternate;
}}

@keyframes pulse-drift {{
  from {{ transform: translate3d(0,0,0) scale(1); opacity: .65; }}
  to {{ transform: translate3d(-24px,-18px,0) scale(1.08); opacity: .9; }}
}}

.advanced-bento {{
  background: var(--pulse-card);
  backdrop-filter: blur(20px);
  -webkit-backdrop-filter: blur(20px);
  border: 1px solid var(--pulse-border);
  border-radius: 24px;
  box-shadow: var(--pulse-shadow);
  transition: all 0.4s cubic-bezier(0.16, 1, 0.3, 1);
  padding: 1.25rem;
  position: relative;
  overflow: hidden;
  transform: translateZ(0);
}}

.advanced-bento:hover {{
  transform: translateY(-4px) translateZ(0);
  border-color: rgba(124,58,237,0.48);
  box-shadow: 0 16px 48px rgba(124,58,237,0.13);
}}

.bento-kicker {{
  color: var(--pulse-primary);
  font-size: .72rem;
  text-transform: uppercase;
  font-weight: 900;
  margin-bottom: .45rem;
}}

.bento-title {{
  font-family: "Space Grotesk", Inter, sans-serif;
  color: var(--pulse-text);
  font-size: 1.05rem;
  font-weight: 800;
  line-height: 1.1;
}}

.bento-copy {{
  color: var(--pulse-muted);
  font-size: .86rem;
  line-height: 1.55;
  margin-top: .45rem;
}}

.hero-title {{
  font-family: "Space Grotesk", Inter, sans-serif;
  font-size: clamp(2.5rem, 6vw, 5.8rem);
  font-weight: 900;
  color: var(--pulse-text);
  line-height: .92;
  margin: 1rem 0 .8rem;
}}

.hero-subtitle {{
  color: var(--pulse-muted);
  font-size: 1.02rem;
  max-width: 680px;
  line-height: 1.7;
}}

.nav-dock {{
  display: flex;
  align-items: center;
  justify-content: space-between;
  gap: .9rem;
  padding: .72rem;
  border-radius: 28px;
  background: rgba(255,255,255,0.55);
  border: 1px solid rgba(255,255,255,0.62);
  backdrop-filter: blur(24px);
  -webkit-backdrop-filter: blur(24px);
  box-shadow: 0 16px 56px rgba(31,38,135,0.08);
  position: sticky;
  top: .85rem;
  z-index: 10;
  margin-bottom: 1.4rem;
}}

.mode-dark .nav-dock {{
  background: rgba(15,23,42,0.58);
  border-color: rgba(148,163,184,0.22);
}}

.brand-mark {{
  display: flex;
  align-items: center;
  gap: .7rem;
  padding: .2rem .7rem .2rem .35rem;
  white-space: nowrap;
}}

.brand-icon {{
  width: 42px;
  height: 42px;
  border-radius: 16px;
  display: grid;
  place-items: center;
  background: linear-gradient(135deg, var(--pulse-primary), var(--pulse-secondary));
  color: white;
  font-size: 1.25rem;
  box-shadow: 0 10px 28px rgba(124,58,237,0.24);
}}

.brand-word {{
  font-family: "Space Grotesk", Inter, sans-serif;
  color: var(--pulse-text);
  font-weight: 900;
  font-size: 1.05rem;
}}

.brand-line {{
  color: var(--pulse-muted);
  font-size: .72rem;
  font-weight: 700;
  margin-top: -2px;
}}

.stButton > button {{
  border-radius: 18px !important;
  border: 1px solid rgba(124,58,237,0.18) !important;
  background: rgba(255,255,255,0.48) !important;
  color: var(--pulse-text) !important;
  font-weight: 800 !important;
  min-height: 44px !important;
  box-shadow: none !important;
  transition: all .25s cubic-bezier(.16,1,.3,1) !important;
}}

.stButton > button:hover {{
  transform: translateY(-2px);
  border-color: rgba(124,58,237,0.48) !important;
  box-shadow: 0 10px 24px rgba(124,58,237,0.12) !important;
}}

.stButton > button[kind="primary"] {{
  color: white !important;
  background: linear-gradient(135deg, var(--pulse-primary), var(--pulse-secondary)) !important;
  border-color: rgba(255,255,255,0.32) !important;
}}

.stTabs [data-baseweb="tab-list"] {{
  gap: .55rem;
  background: rgba(255,255,255,.38);
  border: 1px solid var(--pulse-border);
  border-radius: 20px;
  padding: .45rem;
  backdrop-filter: blur(14px);
}}

.stTabs [data-baseweb="tab"] {{
  border-radius: 15px;
  color: var(--pulse-muted);
  font-weight: 800;
}}

.stTabs [aria-selected="true"] {{
  background: linear-gradient(135deg, rgba(124,58,237,.16), rgba(14,165,233,.14));
  color: var(--pulse-primary) !important;
}}

.stSelectbox div[data-baseweb="select"], .stTextInput input, .stTextArea textarea, .stNumberInput input {{
  background: rgba(255,255,255,.5) !important;
  border-radius: 18px !important;
  border-color: rgba(124,58,237,.16) !important;
  color: var(--pulse-text) !important;
}}

.metric-number {{
  font-family: "Space Grotesk", Inter, sans-serif;
  font-size: 2.2rem;
  color: var(--pulse-text);
  font-weight: 900;
  line-height: 1;
}}

.telemetry-line {{
  width: 100%;
  height: 112px;
}}

.ecg-path {{
  fill: none;
  stroke: url(#ecgGradient);
  stroke-width: 4;
  stroke-linecap: round;
  stroke-linejoin: round;
  stroke-dasharray: 480;
  stroke-dashoffset: 480;
  animation: draw-ecg 2.2s linear infinite;
  filter: drop-shadow(0 0 8px rgba(124,58,237,.22));
}}

@keyframes draw-ecg {{
  to {{ stroke-dashoffset: -480; }}
}}

.progress-ring-wrap {{
  display: grid;
  place-items: center;
  min-height: 230px;
}}

.ring-label {{
  position: absolute;
  text-align: center;
}}

.ring-value {{
  font-family: "Space Grotesk", Inter, sans-serif;
  font-size: 2.15rem;
  font-weight: 900;
  color: var(--pulse-text);
}}

.risk-chip {{
  display: inline-flex;
  align-items: center;
  gap: .4rem;
  padding: .45rem .7rem;
  border-radius: 999px;
  background: rgba(124,58,237,.12);
  color: var(--pulse-primary);
  font-size: .76rem;
  font-weight: 900;
  margin: .2rem .25rem .2rem 0;
}}

.telemetry-flag {{
  padding: .9rem 1rem;
  border-radius: 18px;
  background: linear-gradient(135deg, rgba(124,58,237,.12), rgba(14,165,233,.10));
  border: 1px solid rgba(124,58,237,.2);
  color: var(--pulse-text);
  font-weight: 800;
  margin-top: .7rem;
}}

.focus-reading {{
  max-width: 920px;
  margin: 0 auto;
  font-size: 1.04rem;
  line-height: 1.85;
}}

@media (max-width: 900px) {{
  .nav-dock {{ position: relative; top: 0; flex-direction: column; align-items: stretch; }}
  .hero-title {{ font-size: 2.45rem; }}
}}
</style>
<div class="floating-orbit"></div>
        """,
        unsafe_allow_html=True,
    )


def set_view(view: str) -> None:
    st.session_state.current_view = view
    st.rerun()


def render_nav() -> None:
    if st.session_state.get("clinical_focus") and st.session_state.current_view == "vault":
        return

    mode_class = "mode-dark" if st.session_state.visual_mode == "dark" else ""
    st.markdown(f'<div class="{mode_class}"><div class="nav-dock">', unsafe_allow_html=True)
    brand, nav, mode = st.columns([1.6, 4.2, 1.3], vertical_alignment="center")
    with brand:
        st.markdown(
            """
<div class="brand-mark">
  <div class="brand-icon">🩺</div>
  <div>
    <div class="brand-word">PULSE.md</div>
    <div class="brand-line">Clinical study cockpit</div>
  </div>
</div>
            """,
            unsafe_allow_html=True,
        )
    with nav:
        cols = st.columns(len(VIEWS))
        for idx, (view, label) in enumerate(VIEWS.items()):
            with cols[idx]:
                active = st.session_state.current_view == view
                if st.button(label, key=f"nav_{view}", use_container_width=True, type="primary" if active else "secondary"):
                    set_view(view)
    with mode:
        label = "🌙 Neon" if st.session_state.visual_mode == "light" else "☀️ Light"
        if st.button(label, key="mode_toggle", use_container_width=True):
            st.session_state.visual_mode = "dark" if st.session_state.visual_mode == "light" else "light"
            st.rerun()
    st.markdown("</div></div>", unsafe_allow_html=True)
    render_auth_strip()


def render_auth_strip() -> None:
    user = backend.current_user()
    status = "Supabase connected" if backend.is_configured() else "Demo mode - add Supabase secrets"
    c1, c2, c3, c4 = st.columns([2.2, 1.2, 1.2, 1.0])
    with c1:
        st.caption(f"Backend: {status}")
        if st.session_state.get("backend_error"):
            st.caption(f"Last backend notice: {st.session_state.backend_error[:140]}")
    if user:
        with c2:
            st.caption(f"Signed in: {user['email']}")
        with c3:
            if user["is_admin"]:
                st.caption("Admin access enabled")
        with c4:
            if st.button("Sign out", key="signout", use_container_width=True):
                st.session_state.auth = None
                st.rerun()
    else:
        with c2:
            email = st.text_input("Email", key="auth_email", label_visibility="collapsed", placeholder="email")
        with c3:
            password = st.text_input("Password", key="auth_password", type="password", label_visibility="collapsed", placeholder="password")
        with c4:
            login, signup = st.columns(2)
            with login:
                if st.button("Login", key="login_button", use_container_width=True):
                    ok, message, data = backend.auth_sign_in(email, password)
                    if ok:
                        st.session_state.auth = data
                        backend.ensure_profile()
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)
            with signup:
                if st.button("Join", key="signup_button", use_container_width=True):
                    ok, message, data = backend.auth_sign_up(email, password, email.split("@")[0])
                    if ok:
                        st.session_state.auth = data
                        backend.ensure_profile()
                        st.success(message)
                        st.rerun()
                    else:
                        st.error(message)


def card(kicker: str, title: str, copy: str = "", extra: str = "") -> None:
    st.markdown(
        f"""
<div class="advanced-bento">
  <div class="bento-kicker">{kicker}</div>
  <div class="bento-title">{title}</div>
  {f'<div class="bento-copy">{copy}</div>' if copy else ''}
  {extra}
</div>
        """,
        unsafe_allow_html=True,
    )


def svg_ecg() -> str:
    return """
<svg class="telemetry-line" viewBox="0 0 520 130" preserveAspectRatio="none">
  <defs>
    <linearGradient id="ecgGradient" x1="0%" x2="100%" y1="0%" y2="0%">
      <stop offset="0%" stop-color="#7c3aed"/>
      <stop offset="55%" stop-color="#0ea5e9"/>
      <stop offset="100%" stop-color="#10b981"/>
    </linearGradient>
  </defs>
  <path class="ecg-path" d="M0 70 L70 70 L90 48 L110 92 L130 70 L176 70 L190 60 L204 70 L224 70 L246 26 L270 108 L292 70 L360 70 L382 53 L402 70 L520 70"/>
</svg>
    """


def circular_progress(percent: int) -> str:
    radius = 76
    circumference = 2 * math.pi * radius
    offset = circumference * (1 - percent / 100)
    return f"""
<div class="progress-ring-wrap">
  <svg width="230" height="230" viewBox="0 0 230 230">
    <defs>
      <linearGradient id="ringGradient" x1="0%" x2="100%">
        <stop offset="0%" stop-color="#7c3aed"/>
        <stop offset="100%" stop-color="#0ea5e9"/>
      </linearGradient>
    </defs>
    <circle cx="115" cy="115" r="{radius}" stroke="rgba(124,58,237,.12)" stroke-width="18" fill="none"/>
    <circle cx="115" cy="115" r="{radius}" stroke="url(#ringGradient)" stroke-width="18" fill="none"
      stroke-linecap="round" stroke-dasharray="{circumference:.2f}" stroke-dashoffset="{offset:.2f}"
      transform="rotate(-90 115 115)" style="transition: stroke-dashoffset .8s cubic-bezier(.16,1,.3,1); filter: drop-shadow(0 0 10px rgba(124,58,237,.24));"/>
  </svg>
  <div class="ring-label">
    <div class="ring-value">{percent}%</div>
    <div class="bento-copy">daily goal</div>
  </div>
</div>
    """


def render_home() -> None:
    metrics = backend.dashboard_metrics()
    st.markdown('<div class="hero-title">Welcome Back,<br>Doctor</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-subtitle">Your premium medical command center for focused study, active recall, clinical reasoning, and exam-ready telemetry.</div>',
        unsafe_allow_html=True,
    )
    st.write("")

    hero_left, hero_right = st.columns([1.45, 1], gap="large")
    with hero_left:
        card(
            "Live Telemetry",
            "ECG study momentum",
            "Your session is warmed up. Keep the rhythm steady with one focused block and one recall set.",
            svg_ecg(),
        )
    with hero_right:
        st.markdown(
            f"""
<div class="advanced-bento" style="min-height:260px;">
  <div class="bento-kicker">Completion Engine</div>
  <div class="bento-title">Daily Progress</div>
  {circular_progress(int(metrics.get("completion") or st.session_state.daily_goal_percent))}
</div>
            """,
            unsafe_allow_html=True,
        )

    m1, m2, m3 = st.columns([1, 1, 1.2], gap="large")
    with m1:
        card("Active Streak", f'<span class="metric-number">{metrics.get("streak", 0)}</span> days', "Saved from your real Supabase study activity.")
    with m2:
        card("Spaced Repetition", f'<span class="metric-number">{metrics.get("due_cards", 0)}</span> due', "Flashcard priority is derived from completed and reviewed topics.")
    with m3:
        recent = metrics.get("recent") or []
        next_title = "Open the Vault" if not recent else "Resume recent topic"
        next_copy = "Pick a subject and start saving progress." if not recent else "Your last opened topics are saved in Supabase."
        card("Recently Studied", next_title, next_copy)
        for item in recent[:3]:
            st.caption(f"• Topic {item.get('topic_id')} · {str(item.get('status', '')).replace('_', ' ')}")

    st.write("")
    render_medical_tools()


def render_medical_tools() -> None:
    st.markdown("### Advanced Medical Lab & Telemetry")
    calc_col, abg_col = st.columns([1, 1], gap="large")
    with calc_col:
        render_calculators()
    with abg_col:
        render_abg_interpreter()


def render_calculators() -> None:
    st.markdown('<div class="advanced-bento">', unsafe_allow_html=True)
    st.markdown("#### Medical Calculator Module")
    calc = st.radio("Calculator", ["Glasgow Coma Scale", "CHA₂DS₂-VASc"], horizontal=True, key="calculator_choice")
    if calc == "Glasgow Coma Scale":
        eye = st.selectbox("Eye Opening", [("4 - Spontaneous", 4), ("3 - To voice", 3), ("2 - To pain", 2), ("1 - None", 1)], format_func=lambda x: x[0], key="gcs_eye")
        verbal = st.selectbox("Verbal Response", [("5 - Oriented", 5), ("4 - Confused", 4), ("3 - Words", 3), ("2 - Sounds", 2), ("1 - None", 1)], format_func=lambda x: x[0], key="gcs_verbal")
        motor = st.selectbox("Motor Response", [("6 - Obeys commands", 6), ("5 - Localizes pain", 5), ("4 - Withdraws", 4), ("3 - Flexion", 3), ("2 - Extension", 2), ("1 - None", 1)], format_func=lambda x: x[0], key="gcs_motor")
        score = eye[1] + verbal[1] + motor[1]
        severity = "Mild" if score >= 13 else "Moderate" if score >= 9 else "Severe"
        guidance = "Reassess frequently and document components." if score >= 13 else "Urgent senior review and neuroimaging context." if score >= 9 else "Airway protection, urgent critical care/neurosurgical pathway."
        st.markdown(f'<div class="telemetry-flag">GCS {score}/15 · {severity}<br>{guidance}</div>', unsafe_allow_html=True)
    else:
        fields = {
            "Congestive heart failure": 1,
            "Hypertension": 1,
            "Age 65-74": 1,
            "Age ≥75": 2,
            "Diabetes": 1,
            "Stroke/TIA/thromboembolism": 2,
            "Vascular disease": 1,
            "Female sex": 1,
        }
        score = 0
        for idx, (label, points) in enumerate(fields.items()):
            if st.checkbox(f"{label} (+{points})", key=f"cha_{idx}"):
                if label == "Age 65-74" and st.session_state.get("cha_3"):
                    continue
                score += points
        risk = "Low" if score == 0 else "Intermediate" if score == 1 else "High"
        guidance = "Anticoagulation usually not indicated solely by score." if score == 0 else "Consider anticoagulation after bleeding-risk/shared decision review." if score == 1 else "Oral anticoagulation is usually recommended unless contraindicated."
        st.markdown(f'<div class="telemetry-flag">CHA₂DS₂-VASc {score} · {risk} thromboembolic risk<br>{guidance}</div>', unsafe_allow_html=True)
    st.markdown("</div>", unsafe_allow_html=True)


def interpret_abg(ph: float, paco2: float, hco3: float) -> tuple[str, str]:
    if ph < 7.35:
        if paco2 > 45:
            return "Respiratory Acidosis", "Primary CO₂ retention. Consider hypoventilation, COPD exacerbation, CNS depression, or neuromuscular weakness."
        if hco3 < 22:
            return "Metabolic Acidosis", "Primary bicarbonate deficit. Check anion gap, lactate, ketones, renal failure, toxins, and diarrhea."
        return "Mixed or evolving acidosis", "pH is acidemic without a clean single-driver pattern."
    if ph > 7.45:
        if paco2 < 35:
            return "Respiratory Alkalosis", "Primary CO₂ washout. Consider pain, anxiety, sepsis, pregnancy, PE, or liver disease."
        if hco3 > 26:
            return "Metabolic Alkalosis", "Primary bicarbonate excess. Consider vomiting, diuretics, mineralocorticoid excess, or post-hypercapnia."
        return "Mixed or evolving alkalosis", "pH is alkalemic without a clean single-driver pattern."
    if paco2 > 45 and hco3 > 26:
        return "Compensated Respiratory Acidosis", "Near-normal pH with CO₂ retention and renal bicarbonate compensation."
    if paco2 < 35 and hco3 < 22:
        return "Compensated Respiratory Alkalosis", "Near-normal pH with low CO₂ and metabolic compensation."
    return "No major acid-base disorder detected", "Values sit near expected physiologic range. Interpret with patient context."


def render_abg_interpreter() -> None:
    st.markdown('<div class="advanced-bento">', unsafe_allow_html=True)
    st.markdown("#### Lab Value Interpreter Matrix")
    a, b, c = st.columns(3)
    with a:
        ph = st.number_input("pH", min_value=6.80, max_value=7.80, value=7.32, step=0.01, key="abg_ph")
    with b:
        paco2 = st.number_input("PaCO₂", min_value=10.0, max_value=100.0, value=52.0, step=1.0, key="abg_paco2")
    with c:
        hco3 = st.number_input("HCO₃⁻", min_value=4.0, max_value=60.0, value=25.0, step=1.0, key="abg_hco3")
    diagnosis, explanation = interpret_abg(ph, paco2, hco3)
    st.markdown(
        f"""
<div class="telemetry-flag">
  <span class="risk-chip">pH {ph:.2f}</span>
  <span class="risk-chip">PaCO₂ {paco2:.0f}</span>
  <span class="risk-chip">HCO₃⁻ {hco3:.0f}</span>
  <br><strong>{diagnosis}</strong><br>{explanation}
</div>
        """,
        unsafe_allow_html=True,
    )
    st.markdown("</div>", unsafe_allow_html=True)


def get_selected_topic() -> dict[str, Any]:
    return content_tree()[st.session_state.selected_subject][st.session_state.selected_chapter][st.session_state.selected_topic]


def render_vault() -> None:
    tree = content_tree()
    if st.session_state.clinical_focus:
        topic = get_selected_topic()
        st.markdown('<div class="focus-reading">', unsafe_allow_html=True)
        if st.button("Exit Clinical Focus Mode", key="exit_focus", type="primary"):
            st.session_state.clinical_focus = False
            st.rerun()
        st.markdown(f"# {st.session_state.selected_topic}")
        backend.mark_topic_opened(topic.get("id"))
        st.write(topic["overview"])
        st.markdown(topic["notes"])
        if topic.get("short_notes"):
            st.markdown("## Short Notes")
            st.markdown(topic["short_notes"])
        st.markdown("## High-Yield Pearls")
        for pearl in topic["pearls"]:
            st.markdown(f"- **{pearl}**")
        st.markdown("</div>", unsafe_allow_html=True)
        return

    st.markdown('<div class="hero-title">Vault Library</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">A strict Subject → Chapter → Topic knowledge engine with polished active-recall surfaces.</div>', unsafe_allow_html=True)
    st.write("")
    with st.container():
        st.markdown('<div class="advanced-bento">', unsafe_allow_html=True)
        c1, c2, c3, c4 = st.columns([1, 1, 1, .8], gap="medium")
        with c1:
            subject = st.selectbox("Subject", list(tree), key="vault_subject_select")
            if subject != st.session_state.selected_subject:
                st.session_state.selected_subject = subject
                first_topic = next(iter(next(iter(tree[subject].values()))))
                backend.save_last_opened_subject(tree[subject][list(tree[subject])[0]][first_topic].get("subject_id"))
                st.session_state.selected_chapter = list(tree[subject])[0]
                st.session_state.selected_topic = list(tree[subject][st.session_state.selected_chapter])[0]
                st.rerun()
        with c2:
            chapter = st.selectbox("Chapter", list(tree[st.session_state.selected_subject]), key="vault_chapter_select")
            if chapter != st.session_state.selected_chapter:
                st.session_state.selected_chapter = chapter
                st.session_state.selected_topic = list(tree[st.session_state.selected_subject][chapter])[0]
                st.rerun()
        with c3:
            topic = st.selectbox("Topic", list(tree[st.session_state.selected_subject][st.session_state.selected_chapter]), key="vault_topic_select")
            if topic != st.session_state.selected_topic:
                st.session_state.selected_topic = topic
                st.rerun()
        with c4:
            st.write("")
            st.write("")
            if st.toggle("Clinical Focus Mode", key="focus_toggle"):
                st.session_state.clinical_focus = True
                st.rerun()
        st.markdown("</div>", unsafe_allow_html=True)

    topic_data = get_selected_topic()
    backend.mark_topic_opened(topic_data.get("id"))
    st.write("")
    a, b, c = st.columns([1, 1, 3])
    with a:
        if st.button("Bookmark topic", key="bookmark_topic", use_container_width=True):
            backend.save_bookmark(topic_data.get("id"))
            st.success("Bookmark saved.")
    with b:
        if st.button("Mark completed", key="complete_topic", use_container_width=True):
            backend.mark_topic_completed(topic_data.get("id"))
            st.success("Progress saved.")
    tabs = st.tabs(["Overview", "High-Yield Notebook", "Active Recall Cards", "Resources", "MCQs & OSCE"])
    with tabs[0]:
        st.markdown('<div class="advanced-bento">', unsafe_allow_html=True)
        st.markdown(f"## {st.session_state.selected_topic}")
        st.write(topic_data["overview"])
        if topic_data.get("short_notes"):
            st.markdown("### Short Notes")
            st.markdown(topic_data["short_notes"])
        st.markdown(topic_data["notes"])
        if topic_data.get("mnemonics"):
            st.markdown("### Mnemonics")
            for item in topic_data["mnemonics"]:
                st.markdown(f"- {item}")
        st.markdown("</div>", unsafe_allow_html=True)
    with tabs[1]:
        for idx, pearl in enumerate(topic_data["pearls"]):
            card("Cram Pearl", f"{idx + 1:02d}", pearl)
    with tabs[2]:
        for idx, flashcard in enumerate(topic_data["flashcards"]):
            with st.expander(f"Card {idx + 1}: {flashcard['front']}"):
                st.markdown(f"**Answer:** {flashcard['back']}")
                rating = st.radio("Review rating", ["again", "hard", "good", "easy"], key=f"fc_rating_{flashcard.get('id', idx)}", horizontal=True)
                if st.button("Save card progress", key=f"save_fc_{flashcard.get('id', idx)}"):
                    backend.save_flashcard_progress(flashcard.get("id"), rating)
                    st.success("Flashcard progress saved.")
    with tabs[3]:
        resources = topic_data.get("resources") or []
        if not resources:
            st.info("No external resources have been uploaded for this topic yet.")
        for resource in resources:
            st.markdown(
                f"""
<div class="advanced-bento">
  <div class="bento-kicker">{resource.get("resource_type", "resource")}</div>
  <div class="bento-title">{resource.get("title", "Resource")}</div>
  <div class="bento-copy">{resource.get("description", "")}</div>
  <a href="{resource.get("url", "#")}" target="_blank">Open resource</a>
</div>
                """,
                unsafe_allow_html=True,
            )
    with tabs[4]:
        st.markdown("#### MCQs")
        for idx, q in enumerate(topic_data.get("mcqs") or []):
            with st.expander(q["question"]):
                st.write(", ".join(q.get("options") or []))
                st.success(f"Answer: {q.get('correct')}")
                st.caption(q.get("explanation", ""))
        st.markdown("#### OSCE / Viva")
        for item in topic_data.get("osce_viva") or []:
            st.markdown(f"- {item}")


def get_secret(*names: str) -> str | None:
    for name in names:
        try:
            value = st.secrets.get(name)
        except Exception:
            value = None
        if value:
            return str(value)
    return None


def ai_status() -> tuple[str, str | None]:
    gemini = get_secret("GEMINI_API_KEY", "gemini_api_key")
    if gemini:
        return "gemini", gemini
    openai = get_secret("OPENAI_API_KEY", "openai_api_key")
    if openai:
        return "openai", openai
    return "demo", None


def call_ai(prompt: str, system_prompt: str, max_tokens: int = 1800, temperature: float = 0.55) -> str:
    provider, key = ai_status()
    if provider == "demo":
        return (
            "Demo AI response: add `GEMINI_API_KEY` or `OPENAI_API_KEY` to Streamlit secrets for live generation.\n\n"
            "Clinical structure:\n- Mechanism first\n- Key features\n- Investigations\n- Management\n- High-yield pitfall"
        )
    try:
        if provider == "gemini":
            model = get_secret("GEMINI_MODEL", "gemini_model") or "gemini-1.5-flash"
            url = f"https://generativelanguage.googleapis.com/v1beta/models/{model}:generateContent?key={key}"
            payload = {
                "contents": [{"role": "user", "parts": [{"text": prompt}]}],
                "systemInstruction": {"parts": [{"text": system_prompt}]},
                "generationConfig": {"temperature": temperature, "maxOutputTokens": max_tokens},
            }
            response = requests.post(url, json=payload, timeout=45)
            response.raise_for_status()
            return response.json()["candidates"][0]["content"]["parts"][0]["text"]
        model = get_secret("OPENAI_MODEL", "openai_model") or "gpt-4o-mini"
        response = requests.post(
            "https://api.openai.com/v1/chat/completions",
            headers={"Authorization": f"Bearer {key}", "Content-Type": "application/json"},
            json={
                "model": model,
                "messages": [{"role": "system", "content": system_prompt}, {"role": "user", "content": prompt}],
                "temperature": temperature,
                "max_tokens": max_tokens,
            },
            timeout=45,
        )
        response.raise_for_status()
        return response.json()["choices"][0]["message"]["content"]
    except requests.exceptions.Timeout:
        return "The AI request timed out. Try a shorter prompt."
    except Exception:
        return "The AI service is unavailable right now. Check your API key, quota, and network."


def parse_json_response(text: str) -> dict[str, Any] | None:
    cleaned = re.sub(r"```(?:json)?|```", "", text).strip()
    match = re.search(r"\{.*\}", cleaned, flags=re.DOTALL)
    candidate = match.group(0) if match else cleaned
    try:
        parsed = json.loads(candidate)
    except json.JSONDecodeError:
        return None
    return parsed if isinstance(parsed, dict) else None


def render_ai_lab() -> None:
    st.markdown('<div class="hero-title">Dynamic AI Lab</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Generate structured study tracks, build memory anchors, and ask a clinical professor in one clean workspace.</div>', unsafe_allow_html=True)
    st.write("")
    try:
        tool = st.segmented_control("AI Tool", AI_TOOLS, key="ai_tool_segment", label_visibility="collapsed")
    except Exception:
        tool = st.radio("AI Tool", AI_TOOLS, horizontal=True, key="ai_tool_segment")
    st.session_state.ai_tool = tool or st.session_state.ai_tool
    st.write("")
    if st.session_state.ai_tool == "Syllabus Synthesizer":
        render_syllabus_synthesizer()
    elif st.session_state.ai_tool == "Mnemonic Craftsman":
        render_mnemonic_craftsman()
    else:
        render_professor_chat()


def render_syllabus_synthesizer() -> None:
    st.markdown('<div class="advanced-bento">', unsafe_allow_html=True)
    condition = st.text_input("Condition or topic", placeholder="e.g. Acute pancreatitis, sepsis, nephrotic syndrome", key="synth_condition")
    if st.button("Generate JSON Study Track", type="primary", use_container_width=True, key="synth_button"):
        if not condition.strip():
            st.warning("Enter a condition first.")
        else:
            prompt = f"""
Return strict JSON for a complete study track on: {condition}
Keys: overview, learning_objectives, daily_plan, high_yield, red_flags, mcqs, flashcards.
MCQs must include question, options, correct, explanation.
"""
            raw = call_ai(prompt, "You are a medical curriculum architect. Return strict JSON only.", 2600, 0.25)
            parsed = parse_json_response(raw)
            st.session_state.ai_track_result = parsed or {"raw_response": raw}
    result = st.session_state.ai_track_result
    if result:
        st.markdown("#### Generated Study Track")
        if "raw_response" in result:
            st.warning("The model did not return valid JSON, so the raw response is shown.")
            st.markdown(result["raw_response"])
        else:
            st.json(result)
    st.markdown("</div>", unsafe_allow_html=True)


def render_mnemonic_craftsman() -> None:
    st.markdown('<div class="advanced-bento">', unsafe_allow_html=True)
    facts = st.text_area("Raw symptoms, criteria, anatomy pathways, or drug list", height=180, key="mnemonic_facts")
    style = st.selectbox("Mnemonic Style", ["Academic", "Funny Slang", "Visual Story"], key="mnemonic_style")
    if st.button("Craft Memory Anchor", type="primary", use_container_width=True, key="mnemonic_button"):
        if not facts.strip():
            st.warning("Paste the facts first.")
        else:
            prompt = f"""
Facts:
{facts}

Style: {style}
Create an acronym-based medical mnemonic. Map every letter to the exact fact it represents. Include one clinical caution.
"""
            st.session_state.mnemonic_result = call_ai(prompt, "You are an elite medical mnemonic designer.", 1400, 0.85)
    if st.session_state.mnemonic_result:
        st.markdown(st.session_state.mnemonic_result)
    st.markdown("</div>", unsafe_allow_html=True)


def render_professor_chat() -> None:
    st.markdown('<div class="advanced-bento">', unsafe_allow_html=True)
    st.markdown("#### Clinical Professor Chat")
    for message in st.session_state.professor_messages:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    user_prompt = st.chat_input("Ask for a diagnostic breakdown, lab interpretation, drug explanation, or OSCE reasoning...")
    if user_prompt:
        st.session_state.professor_messages.append({"role": "user", "content": user_prompt})
        with st.chat_message("user"):
            st.markdown(user_prompt)
        history = "\n".join(f"{m['role']}: {m['content']}" for m in st.session_state.professor_messages[-8:])
        prompt = f"Conversation:\n{history}\n\nAnswer the latest question with step-by-step clinical reasoning."
        answer = call_ai(
            prompt,
            "You are an elite senior resident and clinical professor. Use structured reasoning, gentle encouragement, and high-yield clinical logic.",
            1800,
            0.55,
        )
        with st.chat_message("assistant"):
            st.markdown(answer)
        st.session_state.professor_messages.append({"role": "assistant", "content": answer})
    st.markdown("</div>", unsafe_allow_html=True)


def render_assessment() -> None:
    bank = assessment_bank()
    st.markdown('<div class="hero-title">Assessment Arena</div>', unsafe_allow_html=True)
    st.markdown('<div class="hero-subtitle">Clinical vignettes, instant scoring, and high-yield explanations in a focused testing cockpit.</div>', unsafe_allow_html=True)
    st.write("")
    total = len(bank)
    answered = sum(1 for i in range(total) if st.session_state.assessment_submitted.get(i))
    correct = st.session_state.assessment_score
    p1, p2, p3 = st.columns(3)
    with p1:
        card("Answered", f'<span class="metric-number">{answered}</span> / {total}')
    with p2:
        card("Score", f'<span class="metric-number">{correct}</span>')
    with p3:
        pct = int((correct / answered) * 100) if answered else 0
        card("Accuracy", f'<span class="metric-number">{pct}%</span>')

    for idx, q in enumerate(bank):
        st.markdown('<div class="advanced-bento">', unsafe_allow_html=True)
        st.markdown(f"#### Case {idx + 1}")
        st.write(q["question"])
        choice = st.radio("Select answer", q["options"], key=f"arena_choice_{idx}", label_visibility="collapsed")
        submitted = st.session_state.assessment_submitted.get(idx, False)
        if st.button("Submit Answer", key=f"arena_submit_{idx}", type="primary" if not submitted else "secondary"):
            was_submitted = st.session_state.assessment_submitted.get(idx, False)
            st.session_state.assessment_answers[idx] = choice
            st.session_state.assessment_submitted[idx] = True
            if not was_submitted and choice == q["correct"]:
                st.session_state.assessment_score += 1
            backend.save_quiz_attempt(
                q.get("quiz_id"),
                get_selected_topic().get("id") if st.session_state.get("selected_topic") else None,
                1 if choice == q["correct"] else 0,
                1,
                {str(q.get("id") or idx): choice},
            )
            st.rerun()
        if submitted:
            selected = st.session_state.assessment_answers.get(idx)
            if selected == q["correct"]:
                st.success(f"Correct: {q['correct']}")
            else:
                st.error(f"Selected: {selected} · Correct: {q['correct']}")
            st.info(q["explanation"])
        st.markdown("</div>", unsafe_allow_html=True)
        st.write("")


def render_admin_studio() -> None:
    user = backend.current_user()
    st.markdown('<div class="hero-title">Admin Studio</div>', unsafe_allow_html=True)
    st.markdown(
        '<div class="hero-subtitle">Upload, edit, and delete A-Z medical resources subject-wise. All writes go through Supabase.</div>',
        unsafe_allow_html=True,
    )
    if not backend.is_configured():
        st.warning("Supabase is not configured. Add SUPABASE_URL, SUPABASE_ANON_KEY, and optionally SUPABASE_SERVICE_ROLE_KEY.")
        st.code("Run supabase_schema.sql in your Supabase SQL editor first.", language="text")
        return
    if not user:
        st.info("Sign in with an admin email to use the Admin Studio.")
        return
    if not user["is_admin"]:
        st.error("Your email is not listed in ADMIN_EMAILS, so admin tools are locked.")
        return

    admin_tables = {
        "subjects": ["name", "slug", "description", "icon"],
        "chapters": ["subject_id", "title", "slug", "description"],
        "topics": ["chapter_id", "title", "slug", "overview", "full_notes", "short_notes", "high_yield_points", "mnemonics", "osce_viva"],
        "notes": ["topic_id", "title", "note_type", "content"],
        "resources": ["topic_id", "title", "resource_type", "url", "description"],
        "quizzes": ["topic_id", "title", "description", "difficulty"],
        "quiz_questions": ["quiz_id", "question", "options", "correct_answer", "explanation", "high_yield_tip"],
        "flashcards": ["topic_id", "front", "back", "mnemonic"],
    }
    table = st.selectbox("Content table", list(admin_tables), key="admin_table_select")
    st.session_state.admin_table = table
    store = backend.active_store(admin=True)
    rows = store.select(table, {"select": "*"}, "created_at.desc")

    create_tab, manage_tab, ai_tab = st.tabs(["Create / Upload", "Edit / Delete", "AI Draft Generators"])
    with create_tab:
        st.markdown('<div class="advanced-bento">', unsafe_allow_html=True)
        st.markdown(f"#### Add {table.replace('_', ' ').title()}")
        payload: dict[str, Any] = {}
        for field in admin_tables[table]:
            if field in {"full_notes", "short_notes", "content", "overview", "description", "question", "explanation", "high_yield_tip", "back"}:
                payload[field] = st.text_area(field.replace("_", " ").title(), key=f"admin_new_{table}_{field}")
            elif field in {"high_yield_points", "mnemonics", "osce_viva", "options"}:
                raw = st.text_area(f"{field.replace('_', ' ').title()} (JSON array)", value="[]", key=f"admin_new_{table}_{field}")
                try:
                    payload[field] = json.loads(raw or "[]")
                except json.JSONDecodeError:
                    st.warning(f"{field} must be valid JSON.")
                    payload[field] = []
            else:
                payload[field] = st.text_input(field.replace("_", " ").title(), key=f"admin_new_{table}_{field}")
        if st.button("Save to Supabase", key=f"admin_save_{table}", type="primary", use_container_width=True):
            cleaned = {k: v for k, v in payload.items() if v not in ("", None, [])}
            if cleaned:
                saved = backend.admin_insert(table, cleaned)
                if saved:
                    reset_content_cache()
                    st.success("Saved.")
                    st.rerun()
                else:
                    st.error("Save failed. Check required foreign keys and Supabase policies.")
            else:
                st.warning("Fill at least one field.")
        st.markdown("</div>", unsafe_allow_html=True)

    with manage_tab:
        st.markdown(f"#### Existing {table}")
        if not rows:
            st.info("No rows found.")
        for row in rows[:50]:
            label = row.get("title") or row.get("name") or row.get("question") or row.get("front") or row.get("id")
            with st.expander(str(label)):
                st.json(row)
                if st.button("Delete row", key=f"delete_{table}_{row['id']}"):
                    if backend.admin_delete(table, row["id"]):
                        reset_content_cache()
                        st.success("Deleted.")
                        st.rerun()
                    else:
                        st.error("Delete failed.")

    with ai_tab:
        st.markdown('<div class="advanced-bento">', unsafe_allow_html=True)
        st.markdown("#### AI Content Drafts")
        draft_topic = st.text_input("Topic to draft", placeholder="e.g. Rheumatic fever", key="admin_ai_topic")
        draft_type = st.selectbox("Draft type", ["AI notes generator", "AI MCQ generator", "AI flashcard generator", "AI mnemonics generator", "AI study plan generator"], key="admin_ai_type")
        if st.button("Generate draft", key="admin_ai_generate", type="primary", use_container_width=True):
            prompt = f"""
Create a production-ready medical education draft for: {draft_topic}
Tool: {draft_type}
Return structured markdown plus JSON-ready fields for Supabase insertion.
Include full notes, short notes, high-yield points, mnemonics, MCQs, flashcards, OSCE/viva, resource suggestions.
"""
            st.session_state.admin_ai_result = call_ai(prompt, "You are a senior medical education content editor.", 2400, 0.45)
        if st.session_state.admin_ai_result:
            st.markdown(st.session_state.admin_ai_result)
        st.markdown("</div>", unsafe_allow_html=True)


def main() -> None:
    init_state()
    inject_design_system()
    st.markdown('<div class="pulse-shell">', unsafe_allow_html=True)
    render_nav()
    if st.session_state.current_view == "home":
        render_home()
    elif st.session_state.current_view == "vault":
        render_vault()
    elif st.session_state.current_view == "ai_lab":
        render_ai_lab()
    elif st.session_state.current_view == "assessment":
        render_assessment()
    elif st.session_state.current_view == "admin":
        render_admin_studio()
    else:
        st.session_state.current_view = "home"
        st.rerun()
    st.markdown("</div>", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
