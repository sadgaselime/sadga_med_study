"""
flashcards_page.py — MedStudy Oman 🩺
Phase 8: Smart Flashcards — Full Redesign
3D Card Flip · Spaced Repetition (SM-2) · Subject Filter · Session Stats
"""

import streamlit as st
import random
import datetime

# ─────────────────────────────────────────────────────────────────────────────
# BUILT-IN FLASHCARD DECKS
# ─────────────────────────────────────────────────────────────────────────────
BUILTIN_CARDS = [
    # ── Cardiology ──────────────────────────────────────────────────────────
    {"id": 1,  "subject": "Cardiology", "front": "What is the CHA₂DS₂-VASc score used for?",
     "back": "Stroke risk stratification in Atrial Fibrillation.\n\nC = CHF (1), H = HTN (1), A₂ = Age ≥75 (2), D = DM (1), S₂ = Stroke/TIA (2), V = Vascular disease (1), A = Age 65–74 (1), Sc = Sex female (1).\n\nAnticoagulate if score ≥2 (men) or ≥3 (women).",
     "tags": ["AF", "Stroke"]},
    {"id": 2,  "subject": "Cardiology", "front": "Name the branches of the left coronary artery.",
     "back": "Left main → bifurcates into:\n• Left Anterior Descending (LAD): supplies anterior wall + septum\n• Left Circumflex (LCx): supplies lateral wall\n\nSome have Left Marginal branch from LCx.\n\n🎯 LAD occlusion = anterior STEMI (V1–V4)",
     "tags": ["Anatomy", "STEMI"]},
    {"id": 3,  "subject": "Cardiology", "front": "What is the NYHA classification for heart failure?",
     "back": "Class I: No limitation, ordinary activity\nClass II: Slight limitation, comfortable at rest\nClass III: Marked limitation, comfortable only at rest\nClass IV: Symptoms at rest, unable to carry on any activity\n\n🎯 Pearl: Class III/IV = consider advanced therapies (CRT, ICD)",
     "tags": ["Heart Failure", "Classification"]},
    {"id": 4,  "subject": "Cardiology", "front": "What are the 4 components of tetralogy of Fallot?",
     "back": "PROVE mnemonic:\n• Pulmonary stenosis (right ventricular outflow obstruction)\n• Right ventricular hypertrophy\n• Overriding aorta\n• Ventricular septal defect (VSD)\n\n🎯 'Boot-shaped' heart on CXR. Cyanotic CHD. Tet spells — knee-chest position.",
     "tags": ["Congenital", "Cyanotic"]},

    # ── Pharmacology ────────────────────────────────────────────────────────
    {"id": 5,  "subject": "Pharmacology", "front": "What is the mechanism of action of metformin?",
     "back": "Biguanide — activates AMPK → reduces hepatic gluconeogenesis (main effect). Also increases peripheral insulin sensitivity and reduces GI glucose absorption.\n\nAdvantages: No hypoglycaemia, weight neutral/loss, cardioprotective.\nContraindications: eGFR <30, contrast dye (hold 48h), severe illness.\n\n🎯 First-line for T2DM (NICE/ADA guidelines)",
     "tags": ["Diabetes", "First-line"]},
    {"id": 6,  "subject": "Pharmacology", "front": "What drugs should be avoided in G6PD deficiency?",
     "back": "Oxidant drugs trigger haemolysis:\n• Antimalarials: Primaquine, Chloroquine\n• Sulfonamides: Sulfamethoxazole (co-trimoxazole)\n• Nitrofurantoin\n• Dapsone\n• Aspirin (high dose)\n• Naphthalene (mothballs)\n\nSAFE: Penicillins, Cephalosporins, Paracetamol, Macrolides\n\n🇴🇲 G6PD deficiency common in Oman",
     "tags": ["G6PD", "Haemolysis"]},
    {"id": 7,  "subject": "Pharmacology", "front": "Name the 4 classes of anti-diabetic drugs and their mechanisms.",
     "back": "1. Biguanides (Metformin) — ↓gluconeogenesis\n2. Sulfonylureas (Glibenclamide) — stimulate insulin secretion\n3. GLP-1 agonists (Liraglutide) — ↑insulin, ↓glucagon, weight loss\n4. SGLT-2 inhibitors (Empagliflozin) — glucosuria, cardio/renal protective\n5. DPP-4 inhibitors (Sitagliptin) — ↑incretin\n6. Thiazolidinediones (Pioglitazone) — ↑insulin sensitivity\n\n🎯 SGLT-2 + GLP-1 have proven CV/renal benefits beyond glucose control",
     "tags": ["Diabetes", "Mechanism"]},
    {"id": 8,  "subject": "Pharmacology", "front": "What is the antidote for organophosphate poisoning?",
     "back": "Atropine + Pralidoxime (2-PAM)\n\nOrganophosphates inhibit AChE → ACh accumulation → SLUDGE:\nSalivation, Lacrimation, Urination, Defaecation, GI distress, Emesis\n\nAtropine: blocks muscarinic receptors (large doses — titrate to dry secretions)\nPralidoxime: reactivates AChE (give within 24-48h, before 'ageing' of enzyme)\n\n🎯 Give atropine first and in large doses — 2-4mg IV, repeat q5-10min",
     "tags": ["Toxicology", "Antidote"]},

    # ── Pathology ───────────────────────────────────────────────────────────
    {"id": 9,  "subject": "Pathology", "front": "What are the 5 types of necrosis and their causes?",
     "back": "1. Coagulative — ischaemia (MI, kidney infarct). Cell outlines preserved.\n2. Liquefactive — brain infarct, abscess. Neutrophil digestion.\n3. Caseous — TB, fungi. 'Cheesy' + granuloma.\n4. Fat — pancreatitis. Saponification by lipases.\n5. Fibrinoid — malignant hypertension, vasculitis. Immune complexes.\n6. Gangrenous — ischaemia + infection.\n\n🎯 Exception: Brain → liquefactive (even with ischaemia, due to high lipid content)",
     "tags": ["Necrosis", "Types"]},
    {"id": 10, "subject": "Pathology", "front": "What is Virchow's triad? Give clinical examples.",
     "back": "Virchow's triad — risk factors for thrombosis:\n\n1. Stasis: immobility, AF, heart failure\n2. Endothelial injury: trauma, surgery, hypertension, smoking\n3. Hypercoagulability: Factor V Leiden, OCP, malignancy, antiphospholipid syndrome, pregnancy\n\n🎯 DVT/PE risk: all 3 components. Immobilised post-op patient = classic scenario.",
     "tags": ["DVT", "Thrombosis"]},

    # ── Anatomy ─────────────────────────────────────────────────────────────
    {"id": 11, "subject": "Anatomy", "front": "What are the contents of the femoral triangle?",
     "back": "Mnemonic: NAVY (lateral to medial):\n• Nerve (femoral nerve)\n• Artery (femoral artery)\n• Vein (femoral vein)\n• Y-fronts (empty space + lymphatics)\n\nBoundaries: Inguinal ligament (superior), Sartorius (lateral), Adductor longus (medial)\nFloor: Iliopsoas + Pectineus\n\n🎯 Femoral hernia passes medial to femoral vein through femoral canal",
     "tags": ["Lower limb", "Vessels"]},
    {"id": 12, "subject": "Anatomy", "front": "Which nerve is damaged in wrist drop? Which bone causes this?",
     "back": "Radial nerve — winds around the spiral groove of the humerus (mid-shaft).\n\nWrist drop = inability to extend wrist/fingers.\n\nCauses:\n• Mid-shaft humeral fracture (spiral fracture)\n• Saturday night palsy (axillary compression)\n• Lead poisoning (bilateral wrist drop)\n\n🎯 Compare:\n• Surgical neck → Axillary nerve (deltoid paralysis)\n• Medial epicondyle → Ulnar nerve (claw hand)\n• Carpal tunnel → Median nerve (thenar wasting)",
     "tags": ["Nerve injuries", "Upper limb"]},
    {"id": 13, "subject": "Anatomy", "front": "Name the rotator cuff muscles and their actions.",
     "back": "SITS mnemonic:\n• Supraspinatus — initiation of abduction (0-15°), also full abduction with deltoid\n• Infraspinatus — external rotation\n• Teres minor — external rotation\n• Subscapularis — internal rotation\n\nAll insert on greater tubercle (except subscapularis → lesser tubercle)\n\n🎯 Supraspinatus most commonly torn. Test: Empty can test. Infraspinatus: external rotation against resistance.",
     "tags": ["Shoulder", "Muscles"]},

    # ── Physiology ──────────────────────────────────────────────────────────
    {"id": 14, "subject": "Physiology", "front": "What is the normal acid-base status? Define the 4 primary disorders.",
     "back": "Normal: pH 7.35–7.45, PaCO₂ 35–45, HCO₃ 22–26\n\n1. Metabolic acidosis: ↓pH, ↓HCO₃ (DKA, renal failure, lactic acidosis)\n2. Metabolic alkalosis: ↑pH, ↑HCO₃ (vomiting, diuretics)\n3. Respiratory acidosis: ↓pH, ↑PaCO₂ (COPD, hypoventilation)\n4. Respiratory alkalosis: ↑pH, ↓PaCO₂ (hyperventilation, PE, anxiety)\n\n🎯 Approach: Check pH → Primary disorder → Compensation adequate?",
     "tags": ["ABG", "Acid-base"]},
    {"id": 15, "subject": "Physiology", "front": "What are the 4 lung volumes and 4 lung capacities?",
     "back": "VOLUMES (cannot overlap):\n• TV = 500mL (tidal)\n• IRV = 3000mL (inspiratory reserve)\n• ERV = 1200mL (expiratory reserve)\n• RV = 1200mL (residual — cannot be measured by spirometry)\n\nCAPACITIES (sum of volumes):\n• TLC = TV+IRV+ERV+RV = 6L\n• VC = TV+IRV+ERV = 4.8L\n• IC = TV+IRV = 3.5L\n• FRC = ERV+RV = 2.4L\n\n🎯 RV, FRC, TLC require helium dilution or body plethysmography",
     "tags": ["Lung volumes", "Spirometry"]},

    # ── Microbiology ────────────────────────────────────────────────────────
    {"id": 16, "subject": "Microbiology", "front": "What are the TORCH infections? What features do they share?",
     "back": "TORCH = congenital infections:\n• Toxoplasma (cat litter, undercooked meat)\n• Other: Syphilis, VZV, Parvovirus B19, HIV, Zika\n• Rubella (German measles — vaccine preventable)\n• CMV (most common congenital infection)\n• Herpes simplex virus (HSV-2)\n\nShared features: IUGR, hepatosplenomegaly, thrombocytopenia, rash\n\n🎯 CMV = most common. Rubella = most severe (cataracts + deafness + PDA = classic triad).",
     "tags": ["TORCH", "Congenital"]},
    {"id": 17, "subject": "Microbiology", "front": "What is the mechanism of action of beta-lactam antibiotics?",
     "back": "Beta-lactams (penicillins, cephalosporins, carbapenems, monobactams):\n\nMechanism: Bind penicillin-binding proteins (PBPs) → inhibit transpeptidase → prevent cross-linking of peptidoglycan → cell wall weakening → bactericidal\n\nResistance mechanisms:\n1. Beta-lactamase production (cleaves beta-lactam ring)\n2. Modified PBPs (MRSA)\n3. Efflux pumps\n4. Reduced permeability\n\n🎯 Beta-lactamase inhibitors: Clavulanate, Sulbactam, Tazobactam",
     "tags": ["Antibiotics", "Mechanism"]},

    # ── Clinical Skills ──────────────────────────────────────────────────────
    {"id": 18, "subject": "Clinical Skills", "front": "What are the components of the Glasgow Coma Scale (GCS)?",
     "back": "GCS = Eye + Verbal + Motor (max 15, min 3)\n\nEYE opening (1-4):\n4=Spontaneous, 3=To voice, 2=To pain, 1=None\n\nVERBAL (1-5):\n5=Oriented, 4=Confused, 3=Words, 2=Sounds, 1=None\n\nMOTOR (1-6):\n6=Obeys, 5=Localises, 4=Withdraws, 3=Abnormal flexion, 2=Extension, 1=None\n\n🎯 GCS ≤8 = severe TBI → intubate. GCS <8 = 'GCS ate' = airway at risk.",
     "tags": ["GCS", "Neurology", "OSCE"]},
    {"id": 19, "subject": "Clinical Skills", "front": "What is the ABCDE approach to the acutely unwell patient?",
     "back": "A — Airway: Patent? Talking? Stridor? Noisy breathing? → Open/secure\nB — Breathing: RR, SpO2, chest expansion, percussion, auscultation → O2, treat\nC — Circulation: HR, BP, CRT, JVP, urine output → IV access, fluids/vasopressors\nD — Disability: GCS, pupils, BGL, temperature\nE — Exposure: Rashes, wounds, abdomen, temperature → Full examination\n\n🎯 Treat life-threatening findings at each step BEFORE moving to next.\nREASSESS after every intervention.",
     "tags": ["ABCDE", "Emergency", "OSCE"]},
    {"id": 20, "subject": "Clinical Skills", "front": "What features differentiate right from left heart failure on examination?",
     "back": "LEFT heart failure (pulmonary congestion):\n• Dyspnoea, orthopnoea, PND\n• Bibasal crackles\n• S3 gallop (ventricular), S4\n• Laterally displaced apex\n• Low SpO2\n\nRIGHT heart failure (systemic congestion):\n• Peripheral pitting oedema (ankles/sacrum)\n• Elevated JVP\n• Hepatomegaly, hepatojugular reflux\n• Ascites (severe)\n• RV heave\n\n🎯 Most common cause of RHF = LHF. Cor pulmonale = RHF from lung disease.",
     "tags": ["Heart Failure", "Examination", "OSCE"]},
]

SUBJECTS = ["All"] + sorted(set(c["subject"] for c in BUILTIN_CARDS))


def _load_cards(subject: str = "All") -> list:
    cards = []
    try:
        from flashcards_page import FLASHCARD_BANK
        cards = FLASHCARD_BANK
    except Exception:
        pass
    if not cards:
        cards = BUILTIN_CARDS
    if subject != "All":
        cards = [c for c in cards if c.get("subject") == subject]
    return cards


# ─────────────────────────────────────────────────────────────────────────────
# SPACED REPETITION  (simplified SM-2)
# ─────────────────────────────────────────────────────────────────────────────
def _update_sr(card_id: int, rating: int):
    """rating: 0=Again, 1=Hard, 2=Good, 3=Easy"""
    sr_key = f"sr_{card_id}"
    sr = st.session_state.get(sr_key, {"interval": 1, "ease": 2.5, "reps": 0})

    if rating == 0:   # Again
        sr["interval"] = 1
        sr["reps"]     = 0
    elif rating == 1: # Hard
        sr["interval"] = max(1, int(sr["interval"] * 1.2))
        sr["ease"]     = max(1.3, sr["ease"] - 0.15)
        sr["reps"]    += 1
    elif rating == 2: # Good
        sr["interval"] = max(1, int(sr["interval"] * sr["ease"]))
        sr["reps"]    += 1
    else:             # Easy
        sr["interval"] = max(1, int(sr["interval"] * sr["ease"] * 1.3))
        sr["ease"]     = min(3.0, sr["ease"] + 0.15)
        sr["reps"]    += 1

    sr["next_review"] = (
        datetime.date.today() + datetime.timedelta(days=sr["interval"])
    ).isoformat()
    st.session_state[sr_key] = sr


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init_fc_state():
    defaults = {
        "fc_subject":   "All",
        "fc_cards":     [],
        "fc_idx":       0,
        "fc_flipped":   False,
        "fc_session":   {"again": 0, "hard": 0, "good": 0, "easy": 0},
        "fc_started":   False,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


# ─────────────────────────────────────────────────────────────────────────────
# MAIN ENTRY
# ─────────────────────────────────────────────────────────────────────────────
def flashcards_page(theme: dict = None):
    if theme is None:
        from styles import THEMES
        theme = THEMES.get(
            st.session_state.get("theme", "🩺 Clinical Snow"),
            list(THEMES.values())[0]
        )

    _init_fc_state()
    _inject_fc_css(theme)

    if not st.session_state.fc_started:
        _render_fc_setup(theme)
    else:
        _render_fc_main(theme)


# ─────────────────────────────────────────────────────────────────────────────
# SETUP
# ─────────────────────────────────────────────────────────────────────────────
def _render_fc_setup(theme: dict):
    t = theme

    st.markdown(
        f'<div style="font-family:Syne,sans-serif;font-size:1.8rem;font-weight:900;'
        f'color:{t["text"]};letter-spacing:-0.03em;margin-bottom:0.3rem;">🃏 Smart Flashcards</div>'
        f'<div style="font-size:0.85rem;color:{t["subtext"]};margin-bottom:1.5rem;">'
        f'Spaced repetition · SM-2 algorithm · {len(BUILTIN_CARDS)}+ cards across medical subjects</div>',
        unsafe_allow_html=True,
    )

    col_l, col_r = st.columns([2, 1])
    with col_l:
        subj = st.selectbox("📚 Subject", SUBJECTS, key="fc_subj_sel")
        cards = _load_cards(subj)

        st.markdown(
            f'<div style="background:{t["primary"]}12;border:1px solid {t["primary"]}30;'
            f'border-radius:12px;padding:0.7rem 1rem;font-size:0.82rem;color:{t["text"]};'
            f'margin-bottom:1rem;">'
            f'✅ <strong>{len(cards)}</strong> flashcards available for this selection.</div>',
            unsafe_allow_html=True,
        )

        shuffle = st.checkbox("🔀 Shuffle cards", value=True, key="fc_shuffle")

        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)
        if len(cards) > 0:
            if st.button("▶️  Start Flashcards", type="primary", use_container_width=True):
                deck = list(cards)
                if shuffle:
                    random.shuffle(deck)
                st.session_state.fc_cards   = deck
                st.session_state.fc_subject = subj
                st.session_state.fc_idx     = 0
                st.session_state.fc_flipped = False
                st.session_state.fc_session = {"again": 0, "hard": 0, "good": 0, "easy": 0}
                st.session_state.fc_started = True
                st.rerun()

    with col_r:
        # SR stats
        all_cards = _load_cards()
        mastered  = sum(1 for c in all_cards
                        if st.session_state.get(f"sr_{c['id']}", {}).get("reps", 0) >= 3)
        due_today = sum(1 for c in all_cards
                        if st.session_state.get(f"sr_{c['id']}", {}).get(
                            "next_review", "2000-01-01") <= datetime.date.today().isoformat())

        st.markdown(
            f'<div style="background:{t["glass_bg"]};border:1px solid {t["card_border"]};'
            f'border-radius:18px;padding:1.4rem;backdrop-filter:blur(12px);">'
            f'<div style="font-size:0.68rem;font-weight:800;color:{t["primary"]};'
            f'letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.8rem;">Your Progress</div>',
            unsafe_allow_html=True,
        )
        for icon, val, lbl in [
            ("📚", str(len(all_cards)), "Total Cards"),
            ("✅", str(mastered), "Mastered"),
            ("📅", str(due_today), "Due Today"),
        ]:
            st.markdown(
                f'<div style="display:flex;justify-content:space-between;align-items:center;'
                f'padding:0.5rem 0;border-bottom:1px solid {t["card_border"]};">'
                f'<span style="font-size:0.8rem;color:{t["text_muted"]};">{icon} {lbl}</span>'
                f'<span style="font-size:0.9rem;font-weight:800;color:{t["primary"]};">{val}</span>'
                f'</div>',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# MAIN FLASHCARD SESSION
# ─────────────────────────────────────────────────────────────────────────────
def _render_fc_main(theme: dict):
    t     = theme
    cards = st.session_state.fc_cards
    idx   = st.session_state.fc_idx
    total = len(cards)
    sess  = st.session_state.fc_session

    # Done state
    if idx >= total:
        _render_fc_done(theme, sess, total)
        return

    card    = cards[idx]
    flipped = st.session_state.fc_flipped
    pct     = (idx / total) * 100

    # ── Header ────────────────────────────────────────────────────────────────
    hc1, hc2 = st.columns([4, 1])
    with hc1:
        st.markdown(
            f'<div style="font-family:Syne,sans-serif;font-size:1rem;font-weight:800;'
            f'color:{t["text"]};margin-bottom:0.3rem;">🃏 {st.session_state.fc_subject} Flashcards</div>',
            unsafe_allow_html=True,
        )
    with hc2:
        if st.button("✕ End", use_container_width=True):
            st.session_state.fc_started = False
            st.rerun()

    # Progress bar
    done_count = sess["again"] + sess["hard"] + sess["good"] + sess["easy"]
    st.markdown(
        f'<div style="display:flex;justify-content:space-between;font-size:0.75rem;'
        f'color:{t["subtext"]};margin-bottom:4px;">'
        f'<span>Card {idx+1} of {total}</span>'
        f'<span>✅ {sess["good"]+sess["easy"]} Good &nbsp;·&nbsp; ❌ {sess["again"]} Again</span>'
        f'</div>'
        f'<div style="height:5px;background:{t["card_border"]};border-radius:999px;'
        f'margin-bottom:1.2rem;overflow:hidden;">'
        f'<div style="height:100%;width:{pct:.1f}%;background:{t["gradient"]};'
        f'border-radius:999px;transition:width 0.3s ease;"></div></div>',
        unsafe_allow_html=True,
    )

    # ── Card (flip effect via state toggle) ───────────────────────────────────
    tags_html = " ".join(
        f'<span style="background:{t["glass_bg"]};border:1px solid {t["card_border"]};'
        f'border-radius:999px;padding:2px 9px;font-size:0.67rem;color:{t["subtext"]};">{tag}</span>'
        for tag in card.get("tags", [])[:3]
    )
    subj_color = {
        "Cardiology": "#e63946", "Pharmacology": "#8b5cf6", "Pathology": "#dc2626",
        "Anatomy": "#f59e0b", "Physiology": "#0891b2", "Microbiology": "#16a34a",
        "Clinical Skills": "#06b6d4", "Biochemistry": "#a855f7",
    }.get(card.get("subject", ""), t["primary"])

    if not flipped:
        # FRONT
        st.markdown(
            f'<div style="background:{t["card_bg"]};border:2px solid {subj_color}50;'
            f'border-top:5px solid {subj_color};border-radius:24px;'
            f'min-height:280px;padding:2.5rem 2.5rem;text-align:center;'
            f'display:flex;flex-direction:column;align-items:center;justify-content:center;'
            f'backdrop-filter:blur(14px);position:relative;overflow:hidden;'
            f'box-shadow:0 8px 32px {subj_color}15;">'
            f'<div style="position:absolute;top:12px;left:16px;">'
            f'<span style="background:{subj_color}18;color:{subj_color};border-radius:999px;'
            f'padding:3px 10px;font-size:0.7rem;font-weight:700;">{card.get("subject","")}</span>'
            f'</div>'
            f'<div style="position:absolute;top:12px;right:16px;font-size:0.68rem;'
            f'color:{t["subtext"]};">FRONT</div>'
            f'<div style="font-family:Syne,sans-serif;font-size:1.25rem;font-weight:800;'
            f'color:{t["text"]};line-height:1.5;max-width:600px;margin:0.5rem 0 1rem;">'
            f'{card["front"]}</div>'
            f'<div style="display:flex;gap:6px;flex-wrap:wrap;justify-content:center;">'
            f'{tags_html}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )
        st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)
        _, mid, _ = st.columns([1, 2, 1])
        with mid:
            if st.button("👁️  Reveal Answer", type="primary", use_container_width=True):
                st.session_state.fc_flipped = True
                st.rerun()
    else:
        # BACK
        back_text = card["back"].replace('\n', '<br>')
        st.markdown(
            f'<div style="background:linear-gradient(145deg,{subj_color}10,{t["card_bg"]});'
            f'border:2px solid {subj_color};border-radius:24px;'
            f'min-height:280px;padding:2rem 2.5rem;'
            f'backdrop-filter:blur(14px);position:relative;'
            f'box-shadow:0 8px 32px {subj_color}25;">'
            f'<div style="position:absolute;top:12px;right:16px;font-size:0.68rem;'
            f'color:{subj_color};font-weight:700;">ANSWER ✅</div>'
            f'<div style="font-size:0.88rem;color:{t["text"]};line-height:1.8;'
            f'margin-top:0.5rem;">{back_text}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

        # ── Rating buttons ────────────────────────────────────────────────────
        st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)
        st.markdown(
            f'<div style="text-align:center;font-size:0.72rem;color:{t["subtext"]};'
            f'margin-bottom:6px;font-weight:600;letter-spacing:0.06em;text-transform:uppercase;">'
            f'How well did you know this?</div>',
            unsafe_allow_html=True,
        )

        rc1, rc2, rc3, rc4 = st.columns(4)
        ratings = [
            (rc1, 0, "❌ Again",  "#dc2626", "Forgot completely"),
            (rc2, 1, "😓 Hard",  "#d97706", "Struggled"),
            (rc3, 2, "✅ Good",  "#16a34a", "Got it"),
            (rc4, 3, "🚀 Easy",  "#0891b2", "Perfect recall"),
        ]

        for col, rating, label, color, sublabel in ratings:
            with col:
                st.markdown(
                    f'<div style="text-align:center;margin-bottom:3px;">'
                    f'<div style="font-size:0.65rem;color:{color};font-weight:600;">{sublabel}</div>'
                    f'</div>',
                    unsafe_allow_html=True,
                )
                if st.button(label, key=f"rate_{card['id']}_{rating}",
                             use_container_width=True):
                    _update_sr(card["id"], rating)
                    rating_key = ["again", "hard", "good", "easy"][rating]
                    st.session_state.fc_session[rating_key] += 1
                    st.session_state.fc_idx     = idx + 1
                    st.session_state.fc_flipped = False
                    st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# SESSION DONE SCREEN
# ─────────────────────────────────────────────────────────────────────────────
def _render_fc_done(theme: dict, sess: dict, total: int):
    t     = theme
    good  = sess["good"] + sess["easy"]
    score = (good / total * 100) if total else 0
    score_color = "#16a34a" if score >= 70 else "#d97706" if score >= 50 else "#dc2626"

    st.markdown(
        f'<div style="text-align:center;background:{t["glass_bg"]};'
        f'border:1.5px solid {score_color}50;border-radius:24px;'
        f'padding:3rem 2rem;backdrop-filter:blur(16px);margin-bottom:1.5rem;">'
        f'<div style="font-size:3.5rem;margin-bottom:1rem;">🎉</div>'
        f'<div style="font-family:Syne,sans-serif;font-size:1.6rem;font-weight:900;'
        f'color:{t["text"]};margin-bottom:0.5rem;">Session Complete!</div>'
        f'<div style="font-size:3.5rem;font-weight:900;color:{score_color};'
        f'font-family:Syne,sans-serif;">{score:.0f}%</div>'
        f'<div style="font-size:0.9rem;color:{t["subtext"]};margin:0.4rem 0 1.5rem;">'
        f'{good} / {total} cards rated Good or Easy</div>'
        f'<div style="display:flex;gap:12px;justify-content:center;flex-wrap:wrap;">'
        f'<span style="background:#dc262618;color:#dc2626;border-radius:999px;'
        f'padding:5px 14px;font-size:0.8rem;font-weight:700;">❌ Again: {sess["again"]}</span>'
        f'<span style="background:#d9770618;color:#d97706;border-radius:999px;'
        f'padding:5px 14px;font-size:0.8rem;font-weight:700;">😓 Hard: {sess["hard"]}</span>'
        f'<span style="background:#16a34a18;color:#16a34a;border-radius:999px;'
        f'padding:5px 14px;font-size:0.8rem;font-weight:700;">✅ Good: {sess["good"]}</span>'
        f'<span style="background:#0891b218;color:#0891b2;border-radius:999px;'
        f'padding:5px 14px;font-size:0.8rem;font-weight:700;">🚀 Easy: {sess["easy"]}</span>'
        f'</div></div>',
        unsafe_allow_html=True,
    )

    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("🔄 Repeat Again", type="primary", use_container_width=True):
            random.shuffle(st.session_state.fc_cards)
            st.session_state.fc_idx     = 0
            st.session_state.fc_flipped = False
            st.session_state.fc_session = {"again":0,"hard":0,"good":0,"easy":0}
            st.rerun()
    with b2:
        if st.button("📚 Study Again Cards Only", use_container_width=True):
            # Re-study only the 'again' cards
            all_cards = st.session_state.fc_cards
            again_ids = [
                c["id"] for c in all_cards
                if st.session_state.get(f"sr_{c['id']}", {}).get("reps", 0) == 0
            ]
            deck = [c for c in all_cards if c["id"] in again_ids]
            if deck:
                st.session_state.fc_cards   = deck
                st.session_state.fc_idx     = 0
                st.session_state.fc_flipped = False
                st.session_state.fc_session = {"again":0,"hard":0,"good":0,"easy":0}
                st.rerun()
            else:
                st.success("🎉 No 'Again' cards remaining!")
    with b3:
        if st.button("🏠 Back to Setup", use_container_width=True):
            st.session_state.fc_started = False
            st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────────────────────
def _inject_fc_css(t: dict):
    st.markdown(f"""
    <style>
    /* Rating button styling */
    .stButton > button {{
        font-size:     0.82rem  !important;
        border-radius: 12px     !important;
        font-weight:   700      !important;
        transition:    all 0.18s ease !important;
    }}
    .stButton > button:hover {{
        transform: translateY(-2px) !important;
    }}
    </style>
    """, unsafe_allow_html=True)