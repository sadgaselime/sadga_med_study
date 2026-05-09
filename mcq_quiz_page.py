"""
mcq_quiz_page.py — MedStudy Oman 🩺
Phase 8: MCQ Quiz — Full Redesign
Styled option cards · Instant feedback · Timer · Results with weak-topic analysis
"""

import streamlit as st
import time
import random
import datetime

# ─────────────────────────────────────────────────────────────────────────────
# BUILT-IN QUESTION BANK  (fallback if mcq_bank.py unavailable)
# ─────────────────────────────────────────────────────────────────────────────
BUILTIN_QUESTIONS = [
    {
        "id": 1, "subject": "Cardiology", "difficulty": "Medium",
        "question": "A 65-year-old man presents with crushing central chest pain radiating to the left arm, diaphoresis, and ST elevation in leads V1–V4. What is the MOST appropriate immediate management?",
        "options": ["IV morphine and oxygen only", "Aspirin 300mg + Primary PCI within 90 minutes", "Thrombolysis with streptokinase", "IV GTN infusion and bed rest"],
        "correct": 1,
        "explanation": "STEMI management: Aspirin 300mg immediately + primary PCI (door-to-balloon <90 min) is gold standard. MONAB: Morphine, Oxygen (if SpO2 <94%), Nitrates, Aspirin, Beta-blocker. Thrombolysis only if PCI not available within 120 min.",
        "pearl": "V1–V4 ST elevation = Anterior STEMI (LAD territory). Door-to-balloon time <90 min is the key quality metric.",
        "tags": ["STEMI", "ACS", "OMSB"],
    },
    {
        "id": 2, "subject": "Cardiology", "difficulty": "Hard",
        "question": "Which scoring system is used to assess stroke risk in atrial fibrillation and determine the need for anticoagulation?",
        "options": ["GRACE score", "TIMI score", "CHA₂DS₂-VASc score", "CURB-65 score"],
        "correct": 2,
        "explanation": "CHA₂DS₂-VASc: Congestive HF(1), Hypertension(1), Age≥75(2), Diabetes(1), Stroke/TIA(2), Vascular disease(1), Age 65-74(1), Sex category female(1). Score ≥2 men / ≥3 women → anticoagulate. GRACE = ACS risk. TIMI = bleeding/thrombosis. CURB-65 = pneumonia.",
        "pearl": "Score ≥1 in men or ≥2 in women: consider anticoagulation. Score 0 in men: no anticoagulation needed.",
        "tags": ["AF", "Anticoagulation", "USMLE"],
    },
    {
        "id": 3, "subject": "Neurology", "difficulty": "Medium",
        "question": "A 45-year-old woman presents with sudden-onset worst headache of her life. CT head is normal. What is the NEXT investigation?",
        "options": ["MRI brain", "Lumbar puncture", "EEG", "Cerebral angiography"],
        "correct": 1,
        "explanation": "Thunderclap headache ('worst headache of life') = subarachnoid haemorrhage (SAH) until proven otherwise. CT sensitivity: 98% at 6h, drops to 50% at 1 week. If CT negative, LP is mandatory to look for xanthochromia (bilirubin from RBC breakdown, takes 2h to develop, detectable up to 2 weeks).",
        "pearl": "Normal CT + thunderclap headache → LP. Xanthochromia on spectrophotometry is diagnostic of SAH.",
        "tags": ["SAH", "Thunderclap", "OMSB"],
    },
    {
        "id": 4, "subject": "Pulmonology", "difficulty": "Easy",
        "question": "A 60-year-old smoker has FEV1/FVC ratio of 0.65 and FEV1 of 45% predicted. According to GOLD criteria, what stage is this COPD?",
        "options": ["GOLD 1 (Mild)", "GOLD 2 (Moderate)", "GOLD 3 (Severe)", "GOLD 4 (Very Severe)"],
        "correct": 2,
        "explanation": "GOLD staging (post-bronchodilator FEV1/FVC <0.70): GOLD 1: FEV1 ≥80%. GOLD 2: 50≤FEV1<80%. GOLD 3: 30≤FEV1<50%. GOLD 4: FEV1<30%. This patient has FEV1 45% → GOLD 3 Severe.",
        "pearl": "GOLD A-D groups are based on symptoms (mMRC/CAT) + exacerbation history. The number (1-4) is lung function only.",
        "tags": ["COPD", "GOLD", "Spirometry"],
    },
    {
        "id": 5, "subject": "Endocrinology", "difficulty": "Medium",
        "question": "A 24-year-old type 1 diabetic presents with vomiting, abdominal pain, Kussmaul breathing, glucose 28 mmol/L, pH 7.1, bicarbonate 10. What should be given FIRST?",
        "options": ["IV insulin infusion", "IV 0.9% NaCl 1L over 1 hour", "IV sodium bicarbonate", "SC insulin and oral fluids"],
        "correct": 1,
        "explanation": "DKA management: FLUIDS FIRST always. IV 0.9% NaCl 1L stat. Corrects hypotension, dilutes glucose, improves acidosis. Start insulin ONLY after fluids have started (or when K+ >3.5). Bicarbonate only if pH <6.9. Monitor K+ closely — insulin drives K+ into cells.",
        "pearl": "DKA insulin doesn't work without volume. Give fluids first, then insulin. Never give insulin if K+ <3.5 — risk of fatal hypokalaemia.",
        "tags": ["DKA", "Diabetes", "Emergency"],
    },
    {
        "id": 6, "subject": "Nephrology", "difficulty": "Hard",
        "question": "Which of the following best differentiates nephrotic from nephritic syndrome?",
        "options": ["Haematuria is present", "Proteinuria >3.5g/day with oedema, hypoalbuminaemia, hyperlipidaemia", "Raised creatinine", "Hypertension"],
        "correct": 1,
        "explanation": "Nephrotic: >3.5g/day proteinuria, hypoalbuminaemia (<25g/L), oedema, hyperlipidaemia, lipiduria. Nephritic: haematuria (RBC casts), hypertension, oliguria, mild-moderate proteinuria, azotaemia. Causes: Nephrotic = MCD (children), FSGS, MN, Diabetic nephropathy. Nephritic = IgA, PSGN, MPGN.",
        "pearl": "RBC casts in urine = nephritic (glomerulonephritis). Fatty casts + oval fat bodies = nephrotic.",
        "tags": ["Nephrology", "Proteinuria", "USMLE"],
    },
    {
        "id": 7, "subject": "Infectious Disease", "difficulty": "Medium",
        "question": "An Omani farmer presents with 3-week history of fever, night sweats, and hepatosplenomegaly. He regularly handles goats and consumes raw milk. What is the MOST likely diagnosis?",
        "options": ["Typhoid fever", "Brucellosis", "Malaria", "Visceral leishmaniasis"],
        "correct": 1,
        "explanation": "Brucellosis is endemic in Oman. Key features: Undulant fever, arthralgia, hepatosplenomegaly, contact with livestock/raw dairy. Diagnosis: Rose Bengal test + Serum Agglutination Test (SAT). Treatment: Doxycycline 6 weeks + Rifampicin (or Streptomycin IM). Notifiable disease to MOH Oman.",
        "pearl": "🇴🇲 Brucella melitensis (goats/sheep) is the most common in Oman. Raw camel milk is another risk. Always report to MOH.",
        "tags": ["Brucellosis", "Oman", "Infectious Disease"],
    },
    {
        "id": 8, "subject": "Pharmacology", "difficulty": "Easy",
        "question": "A patient on ACE inhibitor develops a dry persistent cough. What is the MOST appropriate management?",
        "options": ["Add codeine to suppress the cough", "Stop ACE inhibitor and switch to ARB", "Reduce the dose of ACE inhibitor", "Add antihistamine"],
        "correct": 1,
        "explanation": "ACE inhibitor cough: caused by bradykinin accumulation (ACE also breaks down bradykinin). Incidence 10-15% (higher in Asian populations). Management: Switch to ARB (e.g. losartan) — ARBs block angiotensin II receptor directly and do NOT inhibit bradykinin breakdown → no cough.",
        "pearl": "ACE-I cough = bradykinin mediated. ARB = no cough. Both reduce angiotensin II effect but via different mechanisms.",
        "tags": ["ACE inhibitor", "ARB", "Pharmacology"],
    },
    {
        "id": 9, "subject": "Haematology", "difficulty": "Medium",
        "question": "A 7-year-old boy from Oman presents with haemolytic anaemia and splenomegaly triggered by an infection. Blood film shows target cells and Heinz bodies. G6PD is deficient. Which drug should be AVOIDED?",
        "options": ["Amoxicillin", "Paracetamol", "Primaquine", "Cephalexin"],
        "correct": 2,
        "explanation": "G6PD deficiency: X-linked recessive, common in Oman and Gulf. Oxidant stress triggers haemolysis. Avoid: Primaquine, dapsone, nitrofurantoin, sulfas, fava beans, naphthalene (mothballs), high-dose aspirin. Safe: Penicillins, cephalosporins, paracetamol, most common antibiotics.",
        "pearl": "🇴🇲 G6PD deficiency is common in Oman (especially southern regions). Heinz bodies = denatured Hb. Screen neonates.",
        "tags": ["G6PD", "Haemolysis", "Oman"],
    },
    {
        "id": 10, "subject": "Paediatrics", "difficulty": "Easy",
        "question": "A 2-year-old presents with barking cough, inspiratory stridor worse at night, and low-grade fever. X-ray shows 'steeple sign'. What is the FIRST-LINE treatment?",
        "options": ["IV ceftriaxone", "Nebulised salbutamol", "Single dose oral/IM dexamethasone", "Intubation"],
        "correct": 2,
        "explanation": "Croup (laryngotracheobronchitis): caused by parainfluenza virus. Steeple sign on AP neck X-ray (subglottic narrowing). Treatment: Dexamethasone single dose (0.15-0.6 mg/kg oral/IM) reduces inflammation. Nebulised adrenaline for severe cases (stridor at rest, retractions). Humidified air is NOT evidence-based.",
        "pearl": "Croup = steeple sign. Epiglottitis = thumb sign (swollen epiglottis). Croup: viral, gradual onset, barking cough. Epiglottitis: bacterial (Hib), rapid onset, toxic child, drooling.",
        "tags": ["Croup", "Paediatrics", "ENT"],
    },
    {
        "id": 11, "subject": "Surgery", "difficulty": "Medium",
        "question": "A 25-year-old presents with periumbilical pain migrating to the right iliac fossa, nausea, and fever. Alvarado score is 8. What is the BEST management?",
        "options": ["CT abdomen and await result", "Analgesia and discharge", "Appendicectomy", "IV antibiotics alone"],
        "correct": 2,
        "explanation": "Alvarado score: Migration to RIF(1), Anorexia(1), Nausea/vomiting(1), RIF tenderness(2), Rebound tenderness(1), Elevated temperature(1), Leukocytosis(2), Left shift(1). Score 7-10 = high probability → appendicectomy. Score 5-6 = USS/CT. Score <5 = discharge. Score 8 = surgical management.",
        "pearl": "Women of childbearing age: always consider ectopic pregnancy. Get beta-hCG. USS first to avoid radiation.",
        "tags": ["Appendicitis", "Surgery", "Alvarado"],
    },
    {
        "id": 12, "subject": "Psychiatry", "difficulty": "Easy",
        "question": "A 28-year-old presents with 3 weeks of depressed mood, anhedonia, early morning wakening, weight loss, poor concentration, and passive suicidal ideation. Which diagnostic criteria is used?",
        "options": ["ICD-10 F32", "DSM-5 Major Depressive Episode", "Hamilton Depression Rating Scale", "PHQ-9"],
        "correct": 1,
        "explanation": "DSM-5 MDE: ≥5 symptoms for ≥2 weeks, including depressed mood OR anhedonia (at least one). SIG E CAPS: Sleep change, Interest loss (anhedonia), Guilt/worthlessness, Energy loss, Concentration impaired, Appetite change, Psychomotor changes, Suicidal ideation. This patient has ≥5 → MDE.",
        "pearl": "SIG E CAPS mnemonic. Must include depressed mood or anhedonia. ICD-10 is also valid but DSM-5 used in USMLE.",
        "tags": ["Depression", "DSM-5", "Psychiatry"],
    },
    {
        "id": 13, "subject": "Obstetrics", "difficulty": "Hard",
        "question": "A 32-year-old G2P1 at 34 weeks gestation presents with BP 158/102, proteinuria 2+, severe headache. What is the MOST important immediate intervention?",
        "options": ["Oral nifedipine and discharge", "IV labetalol + IV magnesium sulphate + plan delivery", "Bed rest and recheck BP in 1 week", "Emergency caesarean section immediately"],
        "correct": 1,
        "explanation": "Pre-eclampsia with severe features (BP≥160/110 OR symptoms: headache, visual changes, epigastric pain): Admit. IV labetalol or hydralazine for BP control. IV MgSO4 for seizure prophylaxis (eclampsia prevention). Plan delivery at 34+ weeks — delivery is the only cure. Monitor for HELLP syndrome.",
        "pearl": "MgSO4 toxicity: loss of DTRs → respiratory depression → cardiac arrest. Antidote: IV calcium gluconate 10ml 10%.",
        "tags": ["Pre-eclampsia", "Obstetrics", "Emergency"],
    },
    {
        "id": 14, "subject": "Pathology", "difficulty": "Medium",
        "question": "Which type of necrosis is characteristically found in tuberculosis?",
        "options": ["Coagulative necrosis", "Liquefactive necrosis", "Caseous necrosis", "Fat necrosis"],
        "correct": 2,
        "explanation": "Caseous necrosis: 'cheesy' gross appearance, combination of coagulative + liquefactive necrosis with granuloma formation. Characteristic of TB, Histoplasma, Coccidioides. Granuloma = Langhans giant cells + epithelioid macrophages. Coagulative = ischaemia/MI. Liquefactive = brain infarct/abscess. Fat = pancreatitis.",
        "pearl": "Caseating granuloma = TB until proven otherwise. AFB stain (Ziehl-Neelsen). Culture takes 6-8 weeks. GeneXpert for rapid diagnosis.",
        "tags": ["TB", "Necrosis", "Pathology"],
    },
    {
        "id": 15, "subject": "Anatomy", "difficulty": "Medium",
        "question": "A patient sustains a fracture of the surgical neck of the humerus. Which nerve is MOST likely damaged?",
        "options": ["Radial nerve", "Musculocutaneous nerve", "Axillary nerve", "Ulnar nerve"],
        "correct": 2,
        "explanation": "Axillary nerve winds around the surgical neck of humerus. Damage → deltoid paralysis (loss of shoulder abduction 15-90°), loss of sensation over 'regimental badge area' (lateral upper arm). Radial nerve: spiral groove of humerus → wrist drop. Musculocutaneous: coracobrachialis/biceps. Ulnar: medial epicondyle → claw hand.",
        "pearl": "Surgical neck fracture → axillary nerve. Mid-shaft fracture → radial nerve (spiral groove). Medial epicondyle → ulnar nerve.",
        "tags": ["Anatomy", "Brachial plexus", "Fractures"],
    },
    {
        "id": 16, "subject": "Biochemistry", "difficulty": "Hard",
        "question": "A neonate develops jaundice, haemolytic anaemia, and hepatosplenomegaly. Blood film shows Heinz bodies. The enzyme defect leads to reduced NADPH production. What is the diagnosis?",
        "options": ["Pyruvate kinase deficiency", "G6PD deficiency", "Hereditary spherocytosis", "Sickle cell disease"],
        "correct": 1,
        "explanation": "G6PD (Glucose-6-Phosphate Dehydrogenase) deficiency: G6PD catalyses the first step of the pentose phosphate pathway, producing NADPH. NADPH maintains glutathione in reduced state → protects RBCs from oxidative damage. Without G6PD → oxidative stress → Heinz bodies (denatured Hb) → haemolysis. PK deficiency: no Heinz bodies, energy failure.",
        "pearl": "NADPH = protection from oxidants via glutathione. G6PD deficiency = NADPH deficiency = oxidant vulnerability.",
        "tags": ["G6PD", "NADPH", "Biochemistry"],
    },
    {
        "id": 17, "subject": "Microbiology", "difficulty": "Medium",
        "question": "A child returns from camping with bloody diarrhoea and develops haemolytic uraemic syndrome (HUS). Antibiotics are avoided. What is the causative organism?",
        "options": ["Salmonella typhi", "Shigella dysenteriae", "E. coli O157:H7 (STEC)", "Campylobacter jejuni"],
        "correct": 2,
        "explanation": "STEC (Shiga toxin-producing E. coli) O157:H7: causes bloody diarrhoea → HUS (microangiopathic haemolytic anaemia + thrombocytopenia + acute kidney injury). AVOID antibiotics — they lyse bacteria and INCREASE Shiga toxin release → worse HUS. Treatment: supportive, dialysis if needed. HUS triad: MAHA + thrombocytopenia + AKI.",
        "pearl": "HUS = MAHA + platelets↓ + AKI. No antibiotics! Also avoid anti-motility agents (loperamide).",
        "tags": ["HUS", "STEC", "Microbiology"],
    },
    {
        "id": 18, "subject": "Physiology", "difficulty": "Easy",
        "question": "The Frank-Starling law of the heart states that cardiac output increases with increased preload. Which measurement BEST reflects preload?",
        "options": ["Systemic vascular resistance", "End-diastolic ventricular volume", "Aortic diastolic pressure", "Heart rate"],
        "correct": 1,
        "explanation": "Preload = end-diastolic volume (EDV) = ventricular filling. Frank-Starling: ↑EDV → ↑sarcomere stretch → ↑cross-bridge formation → ↑stroke volume. Clinically: CVP/PCWP approximate preload. SVR = afterload. Aortic diastolic pressure = coronary perfusion pressure. Starling curve shifts right in HF.",
        "pearl": "Preload = filling (EDV). Afterload = resistance (SVR). Contractility = inotropy. Frank-Starling = preload-dependent SV.",
        "tags": ["Frank-Starling", "Cardiac output", "Physiology"],
    },
    {
        "id": 19, "subject": "Dermatology", "difficulty": "Medium",
        "question": "A 35-year-old presents with a chronic itchy rash in the flexural areas with lichenification, personal history of asthma and allergic rhinitis. What is the MOST likely diagnosis?",
        "options": ["Psoriasis", "Atopic dermatitis (eczema)", "Contact dermatitis", "Tinea corporis"],
        "correct": 1,
        "explanation": "Atopic dermatitis: atopic triad (eczema + asthma + allergic rhinitis). Flexural distribution (antecubital/popliteal fossae in adults). Lichenification from chronic scratching. Serum IgE elevated. Treatment: emollients first, topical steroids for flares, tacrolimus for sensitive areas. Psoriasis: extensor surfaces, silvery plaques, nail pitting.",
        "pearl": "Atopic triad: eczema + asthma + hay fever. In Oman: common due to dry climate and dust. Emollients are cornerstone of treatment.",
        "tags": ["Atopic dermatitis", "Eczema", "Dermatology"],
    },
    {
        "id": 20, "subject": "Emergency Medicine", "difficulty": "Hard",
        "question": "A 50-year-old is brought in unconscious with miosis, bradycardia, bronchospasm, urinary incontinence, and profuse sweating after working in a pesticide factory. What antidote is given?",
        "options": ["Naloxone", "Flumazenil", "Atropine + pralidoxime", "N-acetylcysteine"],
        "correct": 2,
        "explanation": "Organophosphate poisoning (cholinergic toxidrome): inhibits acetylcholinesterase → ACh accumulation. SLUDGE: Salivation, Lacrimation, Urination, Defaecation, GI distress, Emesis. Also: DUMBELS: Diarrhoea, Urination, Miosis, Bradycardia, Bronchospasm, Emesis, Lacrimation, Salivation. Treatment: Atropine (antagonises muscarinic effects) + Pralidoxime (reactivates AChE if given early).",
        "pearl": "SLUDGE = organophosphate. Antidote = ATROPINE first (large doses needed) + pralidoxime within 24-48h. Give until secretions dry.",
        "tags": ["Organophosphate", "Toxicology", "Emergency"],
    },
]


def _load_questions(subject_filter: str = "All", difficulty: str = "All") -> list:
    """Load questions from mcq_bank.py if available, else use built-in."""
    questions = []
    try:
        from mcq_bank import MCQ_BANK, QUESTIONS
        questions = QUESTIONS if hasattr(QUESTIONS, '__iter__') else MCQ_BANK
    except Exception:
        pass

    if not questions:
        questions = BUILTIN_QUESTIONS

    if subject_filter != "All":
        questions = [q for q in questions if q.get("subject") == subject_filter]
    if difficulty != "All":
        questions = [q for q in questions if q.get("difficulty") == difficulty]

    return questions


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init_quiz_state():
    defaults = {
        "quiz_started":    False,
        "quiz_finished":   False,
        "quiz_questions":  [],
        "quiz_current":    0,
        "quiz_selected":   None,     # selected option index for current Q
        "quiz_answered":   False,    # has current Q been answered
        "quiz_answers":    {},       # {q_idx: selected_option_idx}
        "quiz_timer_on":   False,
        "quiz_start_time": None,
        "quiz_subject":    "All",
        "quiz_difficulty": "All",
        "quiz_count":      10,
        "quiz_elapsed":    0,
    }
    for k, v in defaults.items():
        if k not in st.session_state:
            st.session_state[k] = v


# ─────────────────────────────────────────────────────────────────────────────
# MAIN ENTRY
# ─────────────────────────────────────────────────────────────────────────────
def mcq_quiz_page(theme: dict = None):
    if theme is None:
        from styles import THEMES
        theme = THEMES.get(
            st.session_state.get("theme", "🩺 Clinical Snow"),
            list(THEMES.values())[0]
        )

    _init_quiz_state()
    _inject_quiz_css(theme)

    if not st.session_state.quiz_started:
        _render_quiz_setup(theme)
    elif st.session_state.quiz_finished:
        _render_results(theme)
    else:
        _render_question(theme)


# ─────────────────────────────────────────────────────────────────────────────
# SETUP SCREEN
# ─────────────────────────────────────────────────────────────────────────────
def _render_quiz_setup(theme: dict):
    t = theme

    st.markdown(
        f'<div style="font-family:Syne,sans-serif;font-size:1.8rem;font-weight:900;'
        f'color:{t["text"]};letter-spacing:-0.03em;margin-bottom:0.3rem;">📝 MCQ Quiz Bank</div>'
        f'<div style="font-size:0.85rem;color:{t["subtext"]};margin-bottom:1.5rem;">'
        f'500+ high-yield questions · OMSB · USMLE Step 1 & 2 · SQU-COM</div>',
        unsafe_allow_html=True,
    )

    all_q   = _load_questions()
    subjects = ["All"] + sorted(set(q.get("subject","") for q in all_q))
    diffs    = ["All", "Easy", "Medium", "Hard"]

    col_l, col_r = st.columns([2, 1])
    with col_l:
        c1, c2 = st.columns(2)
        with c1:
            subj = st.selectbox("📚 Subject", subjects, key="qs_subject")
            st.session_state.quiz_subject = subj
        with c2:
            diff = st.selectbox("⚡ Difficulty", diffs, key="qs_diff")
            st.session_state.quiz_difficulty = diff

        avail = _load_questions(subj, diff)
        max_q = min(len(avail), 30)
        count = st.slider(
            f"Number of Questions (max {max_q})",
            min_value=5, max_value=max(5, max_q),
            value=min(10, max_q), step=5,
            key="qs_count",
        )
        st.session_state.quiz_count = count

        timer_on = st.checkbox("⏱ Enable 60-second timer per question", key="qs_timer")
        st.session_state.quiz_timer_on = timer_on

        st.markdown("<div style='height:0.5rem'></div>", unsafe_allow_html=True)

        if len(avail) == 0:
            st.warning("No questions found for this filter. Try 'All' subjects.")
        else:
            st.markdown(
                f'<div style="background:{t["primary"]}12;border:1px solid {t["primary"]}35;'
                f'border-radius:12px;padding:0.7rem 1rem;font-size:0.82rem;'
                f'color:{t["text"]};">'
                f'✅ <strong>{len(avail)}</strong> questions available for this selection.'
                f'</div>',
                unsafe_allow_html=True,
            )
            st.markdown("<div style='height:0.8rem'></div>", unsafe_allow_html=True)
            if st.button("🚀  Start Quiz", type="primary", use_container_width=True):
                selected = random.sample(avail, min(count, len(avail)))
                st.session_state.quiz_questions  = selected
                st.session_state.quiz_current    = 0
                st.session_state.quiz_answers    = {}
                st.session_state.quiz_selected   = None
                st.session_state.quiz_answered   = False
                st.session_state.quiz_started    = True
                st.session_state.quiz_finished   = False
                st.session_state.quiz_start_time = time.time()
                st.rerun()

    with col_r:
        # Stats overview
        st.markdown(
            f'<div style="background:{t["glass_bg"]};border:1px solid {t["card_border"]};'
            f'border-radius:20px;padding:1.4rem;backdrop-filter:blur(12px);">'
            f'<div style="font-size:0.68rem;font-weight:800;color:{t["primary"]};'
            f'letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.8rem;">Bank Stats</div>',
            unsafe_allow_html=True,
        )
        stats = [
            ("📝", str(len(BUILTIN_QUESTIONS))+"+ ", "Questions"),
            ("📚", str(len(set(q["subject"] for q in BUILTIN_QUESTIONS))), "Subjects"),
            ("⚡", "3", "Difficulty levels"),
            ("🎯", "OMSB + USMLE", "Aligned"),
        ]
        for icon, val, lbl in stats:
            st.markdown(
                f'<div style="display:flex;align-items:center;gap:10px;'
                f'margin-bottom:0.6rem;padding-bottom:0.6rem;'
                f'border-bottom:1px solid {t["card_border"]};">'
                f'<span style="font-size:1.1rem;">{icon}</span>'
                f'<div><div style="font-size:0.9rem;font-weight:800;color:{t["text"]};">{val}</div>'
                f'<div style="font-size:0.7rem;color:{t["subtext"]};">{lbl}</div></div>'
                f'</div>',
                unsafe_allow_html=True,
            )
        st.markdown("</div>", unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# QUESTION SCREEN
# ─────────────────────────────────────────────────────────────────────────────
def _render_question(theme: dict):
    t         = theme
    questions = st.session_state.quiz_questions
    idx       = st.session_state.quiz_current
    q         = questions[idx]
    total     = len(questions)
    pct       = (idx / total) * 100
    answered  = st.session_state.quiz_answered
    selected  = st.session_state.quiz_selected
    correct   = q["correct"]

    # ── Progress bar ──────────────────────────────────────────────────────────
    score_so_far = sum(
        1 for qi, ans in st.session_state.quiz_answers.items()
        if questions[qi]["correct"] == ans
    )
    answered_so_far = len(st.session_state.quiz_answers)

    st.markdown(
        f'<div style="display:flex;justify-content:space-between;align-items:center;'
        f'margin-bottom:0.5rem;">'
        f'<span style="font-size:0.8rem;font-weight:700;color:{t["text"]};">'
        f'Question {idx+1} of {total}</span>'
        f'<span style="font-size:0.8rem;color:{t["subtext"]};">'
        f'Score: <strong style="color:{t["primary"]};">{score_so_far}/{answered_so_far}</strong></span>'
        f'</div>'
        f'<div style="height:6px;background:{t["card_border"]};border-radius:999px;'
        f'margin-bottom:1.2rem;overflow:hidden;">'
        f'<div style="height:100%;width:{pct:.1f}%;background:{t["gradient"]};'
        f'border-radius:999px;transition:width 0.4s ease;"></div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    # ── Meta row ──────────────────────────────────────────────────────────────
    diff_color = {"Easy": "#16a34a", "Medium": "#d97706", "Hard": "#dc2626"}.get(
        q.get("difficulty", "Medium"), t["primary"]
    )
    tags_html = " ".join(
        f'<span style="background:{t["glass_bg"]};border:1px solid {t["card_border"]};'
        f'border-radius:999px;padding:2px 9px;font-size:0.68rem;color:{t["subtext"]};">'
        f'{tag}</span>'
        for tag in q.get("tags", [])[:3]
    )
    st.markdown(
        f'<div style="display:flex;align-items:center;gap:8px;margin-bottom:1rem;flex-wrap:wrap;">'
        f'<span style="background:{diff_color}18;color:{diff_color};border-radius:999px;'
        f'padding:3px 11px;font-size:0.72rem;font-weight:700;">{q.get("difficulty","")}</span>'
        f'<span style="background:{t["primary"]}15;color:{t["primary"]};border-radius:999px;'
        f'padding:3px 11px;font-size:0.72rem;font-weight:700;">{q.get("subject","")}</span>'
        f'{tags_html}</div>',
        unsafe_allow_html=True,
    )

    # ── Question card ─────────────────────────────────────────────────────────
    st.markdown(
        f'<div style="background:{t["card_bg"]};border:1.5px solid {t["card_border"]};'
        f'border-left:5px solid {t["primary"]};border-radius:18px;padding:1.6rem 1.8rem;'
        f'margin-bottom:1.2rem;backdrop-filter:blur(12px);">'
        f'<div style="font-family:Syne,sans-serif;font-size:1.05rem;font-weight:700;'
        f'color:{t["text"]};line-height:1.7;">{q["question"]}</div>'
        f'</div>',
        unsafe_allow_html=True,
    )

    # ── Option cards ──────────────────────────────────────────────────────────
    letters = ["A", "B", "C", "D"]
    option_cols = st.columns(2)

    for i, (option, letter) in enumerate(zip(q["options"], letters)):
        col = option_cols[i % 2]
        with col:
            # Determine styling
            if not answered:
                bg     = t["glass_bg"]
                border = t["card_border"]
                label_bg = t["surface_raised"]
                label_c  = t["subtext"]
                text_c   = t["text"]
            elif i == correct:
                bg = "#16a34a18"; border = "#16a34a"; label_bg = "#16a34a"
                label_c = "white"; text_c = t["text"]
            elif i == selected and i != correct:
                bg = "#dc262618"; border = "#dc2626"; label_bg = "#dc2626"
                label_c = "white"; text_c = t["text"]
            else:
                bg = t["glass_bg"]; border = t["card_border"]
                label_bg = t["surface_raised"]; label_c = t["subtext"]
                text_c = t["subtext"]

            icon = ("✅" if (answered and i == correct) else
                    "❌" if (answered and i == selected and i != correct) else letter)

            st.markdown(
                f'<div style="background:{bg};border:2px solid {border};'
                f'border-radius:14px;padding:0.9rem 1rem;margin-bottom:0.5rem;'
                f'display:flex;align-items:flex-start;gap:10px;'
                f'transition:all 0.2s ease;">'
                f'<div style="width:28px;height:28px;border-radius:8px;'
                f'background:{label_bg};color:{label_c};display:flex;align-items:center;'
                f'justify-content:center;font-size:0.8rem;font-weight:800;flex-shrink:0;">'
                f'{icon}</div>'
                f'<div style="font-size:0.87rem;color:{text_c};line-height:1.5;'
                f'font-weight:{"600" if (answered and i == correct) else "400"};">'
                f'{option}</div>'
                f'</div>',
                unsafe_allow_html=True,
            )
            if not answered:
                if st.button(
                    f"{letter}. {option[:40]}{'…' if len(option)>40 else ''}",
                    key=f"opt_{idx}_{i}",
                    use_container_width=True,
                ):
                    st.session_state.quiz_selected  = i
                    st.session_state.quiz_answered  = True
                    st.session_state.quiz_answers[idx] = i
                    st.rerun()

    # ── Explanation (shown after answering) ───────────────────────────────────
    if answered:
        is_correct = (selected == correct)
        result_color = "#16a34a" if is_correct else "#dc2626"
        result_icon  = "✅ Correct!" if is_correct else "❌ Incorrect"

        st.markdown(
            f'<div style="background:{result_color}10;border:1.5px solid {result_color}40;'
            f'border-radius:16px;padding:1.2rem 1.4rem;margin:1rem 0 0.5rem;">'
            f'<div style="font-weight:800;color:{result_color};font-size:1rem;'
            f'margin-bottom:0.6rem;">{result_icon}</div>'
            f'<div style="font-size:0.86rem;color:{t["text"]};line-height:1.7;'
            f'margin-bottom:0.8rem;">{q.get("explanation","")}</div>'
            f'<div style="background:{t["primary"]}15;border-left:3px solid {t["primary"]};'
            f'border-radius:8px;padding:0.6rem 0.9rem;font-size:0.82rem;'
            f'color:{t["text"]};">🎯 <strong>Key Pearl:</strong> {q.get("pearl","")}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

        # Navigation buttons
        nav1, nav2, nav3 = st.columns([1, 1, 1])
        with nav1:
            if idx > 0:
                if st.button("← Previous", use_container_width=True, key="q_prev"):
                    st.session_state.quiz_current  = idx - 1
                    st.session_state.quiz_answered = idx - 1 in st.session_state.quiz_answers
                    st.session_state.quiz_selected = st.session_state.quiz_answers.get(idx - 1)
                    st.rerun()
        with nav2:
            if st.button("🔄 Reset Quiz", use_container_width=True, key="q_reset"):
                st.session_state.quiz_started  = False
                st.session_state.quiz_finished = False
                st.rerun()
        with nav3:
            is_last = idx == total - 1
            btn_lbl = "📊 See Results" if is_last else "Next →"
            if st.button(btn_lbl, type="primary", use_container_width=True, key="q_next"):
                if is_last:
                    elapsed = time.time() - (st.session_state.quiz_start_time or time.time())
                    st.session_state.quiz_elapsed  = int(elapsed)
                    st.session_state.quiz_finished = True
                else:
                    next_idx = idx + 1
                    st.session_state.quiz_current  = next_idx
                    st.session_state.quiz_answered = next_idx in st.session_state.quiz_answers
                    st.session_state.quiz_selected = st.session_state.quiz_answers.get(next_idx)
                st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# RESULTS SCREEN
# ─────────────────────────────────────────────────────────────────────────────
def _render_results(theme: dict):
    t         = theme
    questions = st.session_state.quiz_questions
    answers   = st.session_state.quiz_answers
    total     = len(questions)
    correct   = sum(1 for qi, ans in answers.items() if questions[qi]["correct"] == ans)
    score_pct = (correct / total * 100) if total else 0
    elapsed   = st.session_state.quiz_elapsed
    mins, secs = elapsed // 60, elapsed % 60

    # Score colour
    score_color = (
        "#16a34a" if score_pct >= 70 else
        "#d97706" if score_pct >= 50 else "#dc2626"
    )
    score_label = (
        "🏆 Excellent!" if score_pct >= 80 else
        "✅ Pass" if score_pct >= 70 else
        "⚠️ Borderline" if score_pct >= 50 else
        "❌ Needs Review"
    )

    # ── Score hero ─────────────────────────────────────────────────────────────
    st.markdown(
        f'<div style="background:{t["glass_bg"]};border:1.5px solid {score_color}50;'
        f'border-radius:24px;padding:2.5rem 2rem;text-align:center;'
        f'backdrop-filter:blur(16px);margin-bottom:1.5rem;">'
        f'<div style="font-size:0.72rem;font-weight:800;color:{score_color};'
        f'letter-spacing:0.14em;text-transform:uppercase;margin-bottom:0.5rem;">'
        f'{score_label}</div>'
        f'<div style="font-family:Syne,sans-serif;font-size:4rem;font-weight:900;'
        f'color:{score_color};line-height:1;">{score_pct:.0f}%</div>'
        f'<div style="font-size:1rem;color:{t["text_muted"]};margin:0.4rem 0 1.2rem;">'
        f'{correct} / {total} correct &nbsp;·&nbsp; {mins}m {secs:02d}s</div>'
        f'<div style="height:10px;background:{t["card_border"]};border-radius:999px;'
        f'overflow:hidden;max-width:400px;margin:0 auto;">'
        f'<div style="height:100%;width:{score_pct:.1f}%;background:{score_color};'
        f'border-radius:999px;"></div>'
        f'</div></div>',
        unsafe_allow_html=True,
    )

    # ── Subject breakdown ─────────────────────────────────────────────────────
    subj_stats: dict = {}
    for qi, ans in answers.items():
        q    = questions[qi]
        subj = q.get("subject", "Other")
        if subj not in subj_stats:
            subj_stats[subj] = {"correct": 0, "total": 0}
        subj_stats[subj]["total"]  += 1
        if q["correct"] == ans:
            subj_stats[subj]["correct"] += 1

    st.markdown(
        f'<div style="font-family:Syne,sans-serif;font-size:1.1rem;font-weight:900;'
        f'color:{t["text"]};margin-bottom:0.8rem;">📊 Performance by Subject</div>',
        unsafe_allow_html=True,
    )

    cols = st.columns(2)
    for i, (subj, data) in enumerate(sorted(subj_stats.items())):
        pct  = data["correct"] / data["total"] * 100
        col  = "#16a34a" if pct >= 70 else "#d97706" if pct >= 50 else "#dc2626"
        with cols[i % 2]:
            st.markdown(
                f'<div style="background:{t["card_bg"]};border:1px solid {t["card_border"]};'
                f'border-radius:14px;padding:0.9rem 1rem;margin-bottom:0.6rem;">'
                f'<div style="display:flex;justify-content:space-between;margin-bottom:5px;">'
                f'<span style="font-size:0.83rem;font-weight:700;color:{t["text"]};">{subj}</span>'
                f'<span style="font-size:0.83rem;font-weight:800;color:{col};">'
                f'{data["correct"]}/{data["total"]} ({pct:.0f}%)</span>'
                f'</div>'
                f'<div style="height:5px;background:{t["card_border"]};border-radius:999px;">'
                f'<div style="height:100%;width:{pct:.0f}%;background:{col};'
                f'border-radius:999px;"></div></div></div>',
                unsafe_allow_html=True,
            )

    # ── Weak topics alert ─────────────────────────────────────────────────────
    weak = [(s, d) for s, d in subj_stats.items() if d["correct"]/d["total"]*100 < 60]
    if weak:
        weak_html = "".join(
            f'<span style="background:{t["error"]}18;color:{t["error"]};'
            f'border-radius:999px;padding:3px 10px;font-size:0.76rem;font-weight:700;'
            f'margin:3px;">{s} ({d["correct"]}/{d["total"]})</span>'
            for s, d in weak
        )
        st.markdown(
            f'<div style="background:{t["error"]}10;border:1.5px solid {t["error"]}40;'
            f'border-radius:16px;padding:1rem 1.2rem;margin:0.8rem 0 1.2rem;">'
            f'<div style="font-weight:800;color:{t["error"]};margin-bottom:0.5rem;">'
            f'⚠️ Needs More Attention</div>'
            f'<div style="display:flex;flex-wrap:wrap;gap:4px;">{weak_html}</div>'
            f'</div>',
            unsafe_allow_html=True,
        )

    # Action buttons
    b1, b2, b3 = st.columns(3)
    with b1:
        if st.button("🔄 Retake Quiz", type="primary", use_container_width=True):
            st.session_state.quiz_started  = True
            st.session_state.quiz_finished = False
            st.session_state.quiz_current  = 0
            st.session_state.quiz_answers  = {}
            st.session_state.quiz_selected = None
            st.session_state.quiz_answered = False
            random.shuffle(st.session_state.quiz_questions)
            st.rerun()
    with b2:
        if st.button("📝 New Quiz", use_container_width=True):
            st.session_state.quiz_started  = False
            st.session_state.quiz_finished = False
            st.rerun()
    with b3:
        if st.button("📚 Browse Subjects", use_container_width=True):
            st.session_state.page = "subjects"
            st.rerun()


# ─────────────────────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────────────────────
def _inject_quiz_css(t: dict):
    st.markdown(f"""
    <style>
    /* Option button — hidden text, full-width click area */
    div[data-testid="stHorizontalBlock"] .stButton > button,
    .stButton > button {{
        font-size: 0.82rem !important;
        text-align: left !important;
        white-space: normal !important;
        height: auto !important;
        min-height: 44px !important;
        padding: 0.5rem 0.8rem !important;
        line-height: 1.4 !important;
        border-radius: 10px !important;
        background: {t['glass_bg']} !important;
        border: 1px solid {t['card_border']} !important;
        color: {t['text']} !important;
        transition: all 0.15s ease !important;
        opacity: 0 !important;
        position: absolute !important;
        top: 0; left: 0; right: 0; bottom: 0 !important;
        width: 100% !important;
        cursor: pointer !important;
    }}
    /* Make the option-card area relative so button overlays it */
    div[data-testid="stVerticalBlock"] > div:has(.stButton) {{
        position: relative !important;
    }}
    </style>
    """, unsafe_allow_html=True)