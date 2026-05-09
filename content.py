"""
content.py — All medical content: subjects, flashcards, mnemonics, MCQs.
This is your "medical textbook" inside the app.
"""

# ─────────────────────────────────────────
# ALL MEDICAL SUBJECTS (Pre-clinical + Clinical)
# ─────────────────────────────────────────
SUBJECTS = {
    "Pre-Clinical": {
        "🔬 Anatomy": {
            "icon": "🔬",
            "color": "#ef4444",
            "topics": [
                "Upper Limb — Bones, muscles, nerves, brachial plexus",
                "Lower Limb — Hip joint, femoral triangle, popliteal fossa",
                "Thorax — Heart anatomy, lungs, mediastinum",
                "Abdomen — GI tract, liver, spleen, kidneys",
                "Head & Neck — Cranial nerves, triangles of neck, orbit",
                "Neuroanatomy — Brain regions, spinal tracts, CSF pathways",
                "Pelvis & Perineum — Pelvic floor, reproductive organs",
                "Embryology — Organogenesis, congenital anomalies",
            ],
            "notes": """
## 🔬 Anatomy High-Yield Notes

### Brachial Plexus (Roots C5–T1)
**Mnemonic: "Randy Travis Drinks Cold Beer"**
- **R**oots → **T**runks → **D**ivisions → **C**ords → **B**ranches

### Key Nerve Injuries:
| Nerve | Injury | Deformity |
|-------|--------|-----------|
| Axillary (C5,6) | Surgical neck # | Loss of shoulder abduction |
| Radial (C5–T1) | Midshaft humerus # | Wrist drop |
| Median (C6–T1) | Carpal tunnel | Ape hand |
| Ulnar (C8,T1) | Medial epicondyle | Claw hand |
| Long thoracic | Mastectomy | Winged scapula |

### Femoral Triangle (NAVEL lateral→medial):
- **N**erve → **A**rtery → **V**ein → **E**mpty space → **L**ymphatics

### Cranial Nerves:
**"Oh Oh Oh To Touch And Feel Very Good Velvet... Ahh Heaven!"**
I=Olfactory, II=Optic, III=Oculomotor, IV=Trochlear, V=Trigeminal,
VI=Abducens, VII=Facial, VIII=Vestibulocochlear, IX=Glossopharyngeal, 
X=Vagus, XI=Accessory, XII=Hypoglossal
"""
        },
        "⚗️ Physiology": {
            "icon": "⚗️",
            "color": "#06b6d4",
            "topics": [
                "Cardiac Physiology — Cardiac cycle, ECG interpretation",
                "Respiratory Physiology — V/Q ratio, spirometry values",
                "Renal Physiology — GFR, tubular reabsorption",
                "Neurophysiology — Action potentials, synaptic transmission",
                "GI Physiology — Digestion, absorption, gut hormones",
                "Endocrine Physiology — Hypothalamic-pituitary axis",
                "Haematology — Haemopoiesis, coagulation cascade",
                "Reproductive Physiology — Menstrual cycle, spermatogenesis",
            ],
            "notes": """
## ⚗️ Physiology High-Yield Notes

### Normal Lab Values (Omani Hospital Units):
| Parameter | Normal Range |
|-----------|-------------|
| Haemoglobin (M) | 13.5–17.5 g/dL |
| Haemoglobin (F) | 12.0–15.5 g/dL |
| WBC | 4.5–11.0 × 10³/µL |
| Platelets | 150–400 × 10³/µL |
| Na⁺ | 135–145 mEq/L |
| K⁺ | 3.5–5.0 mEq/L |
| Creatinine | 0.6–1.2 mg/dL |
| Glucose (fasting) | 70–100 mg/dL |
| HbA1c | <5.7% normal, 5.7–6.4% prediabetes |

### Cardiac Output:
**CO = HR × SV**
- Normal CO: 5 L/min
- Starling's Law: ↑ preload → ↑ SV (up to a point)

### Henderson-Hasselbalch:
**pH = 6.1 + log([HCO₃⁻] / 0.03 × PaCO₂)**
- Normal pH: 7.35–7.45
- Normal PaCO₂: 35–45 mmHg
- Normal HCO₃⁻: 22–26 mEq/L
"""
        },
        "🧬 Biochemistry": {
            "icon": "🧬",
            "color": "#8b5cf6",
            "topics": [
                "Enzymes — Kinetics, Michaelis-Menten, inhibition",
                "Metabolism — Glycolysis, TCA cycle, oxidative phosphorylation",
                "Lipid Metabolism — Fatty acid synthesis/oxidation, ketogenesis",
                "Protein Metabolism — Amino acid catabolism, urea cycle",
                "Nucleotide Metabolism — Purines/pyrimidines, salvage pathways",
                "Vitamins — Water-soluble and fat-soluble, deficiency diseases",
                "Molecular Biology — DNA replication, transcription, translation",
                "Inborn Errors of Metabolism — Phenylketonuria, glycogen storage",
            ],
            "notes": """
## 🧬 Biochemistry High-Yield Notes

### Glycolysis (10 Steps — simplified):
Glucose → Glucose-6-P → Fructose-6-P → F-1,6-bisP →
(×2) G3P → 1,3-BPG → 3-PG → 2-PG → PEP → Pyruvate

**Net yield: 2 ATP, 2 NADH, 2 Pyruvate**

### Vitamins Quick Reference:
| Vitamin | Deficiency | Mnemonic |
|---------|-----------|----------|
| B1 (Thiamine) | Beriberi, Wernicke | B1 = **B**eri**B**eri |
| B3 (Niacin) | Pellagra (4Ds) | Dermatitis, Diarrhoea, Dementia, Death |
| B12 | Megaloblastic anaemia, subacute combined degeneration | |
| C | Scurvy | |
| D | Rickets (child), Osteomalacia (adult) | |
| K | Bleeding disorder | |

### Enzyme Inhibition:
- **Competitive**: ↑ Km, same Vmax — add more substrate to overcome
- **Non-competitive**: Same Km, ↓ Vmax — can't overcome with substrate
"""
        },
        "🦠 Microbiology": {
            "icon": "🦠",
            "color": "#10b981",
            "topics": [
                "Bacteriology — Gram staining, culture, antibiotics",
                "Virology — DNA/RNA viruses, replication, vaccines",
                "Mycology — Superficial and systemic fungi",
                "Parasitology — Protozoa, helminths, vectors",
                "Immunology — Innate/adaptive immunity, complement",
                "Antibiotics — Mechanisms, resistance, side effects",
                "Hospital Infections — MRSA, VRE, nosocomial pathogens",
                "Tropical Diseases — Malaria, dengue, schistosomiasis (Oman-relevant)",
            ],
            "notes": """
## 🦠 Microbiology High-Yield Notes

### Gram Positive vs Gram Negative:
**Gram +ve (purple)**: thick peptidoglycan wall
- Cocci: Staph, Strep, Enterococcus
- Rods: Bacillus, Clostridium, Listeria

**Gram -ve (pink/red)**: thin peptidoglycan + outer membrane (LPS)
- Cocci: Neisseria (meningitidis, gonorrhoeae)
- Rods: E.coli, Klebsiella, Pseudomonas, Salmonella

### Common Omani Pathogens:
- **Brucellosis** — from unpasteurised milk/cheese (common in Oman)
- **Leishmaniasis** — sandfly vector, skin lesions
- **Typhoid** — Salmonella typhi, Widal test

### Antibiotic Mechanisms:
| Drug | Target |
|------|--------|
| Penicillin/Cephalosporin | Cell wall (β-lactam) |
| Vancomycin | Cell wall (D-Ala-D-Ala) |
| Aminoglycosides | 30S ribosome |
| Tetracycline | 30S ribosome |
| Macrolides/Clindamycin | 50S ribosome |
| Fluoroquinolones | DNA gyrase |
| Metronidazole | DNA (anaerobes) |
"""
        },
        "💊 Pharmacology": {
            "icon": "💊",
            "color": "#f59e0b",
            "topics": [
                "Autonomic Pharmacology — Adrenergic, cholinergic drugs",
                "Cardiovascular Drugs — Antihypertensives, antiarrhythmics",
                "Respiratory Drugs — Bronchodilators, corticosteroids",
                "GI Drugs — PPIs, antiemetics, laxatives",
                "CNS Drugs — Anxiolytics, antidepressants, antipsychotics",
                "Antibiotics — Coverage, side effects, interactions",
                "Endocrine Drugs — Insulin, oral hypoglycaemics, steroids",
                "Analgesics — NSAIDs, opioids, local anaesthetics",
            ],
            "notes": """
## 💊 Pharmacology High-Yield Notes

### Antihypertensives (Classes):
1. **ACE Inhibitors** (-pril): Ramipril, Enalapril
   - Side effect: **Dry cough** (↑ bradykinin), AVOID in pregnancy
2. **ARBs** (-sartan): Losartan, Valsartan
   - Same as ACEi but NO cough
3. **CCBs**: Amlodipine (DHP), Verapamil/Diltiazem (non-DHP)
   - Amlodipine: causes ankle oedema
4. **Beta-blockers** (-olol): Metoprolol, Bisoprolol
   - AVOID in asthma, AVOID abrupt stopping
5. **Thiazides**: Hydrochlorothiazide — causes ↓K⁺, ↑uric acid

### Insulin Types (for Omani Diabetics):
| Insulin | Onset | Peak | Duration |
|---------|-------|------|----------|
| Rapid (Lispro) | 15 min | 1 hr | 3–5 hr |
| Regular | 30 min | 2–3 hr | 6–8 hr |
| NPH | 1–2 hr | 4–6 hr | 12 hr |
| Glargine | 1–2 hr | Flat | 24 hr |
"""
        },
        "🏥 Pathology": {
            "icon": "🏥",
            "color": "#ec4899",
            "topics": [
                "Cell Injury & Death — Necrosis vs apoptosis",
                "Inflammation — Acute and chronic, granulomas",
                "Haemodynamic Disorders — Oedema, thrombosis, embolism",
                "Neoplasia — Benign vs malignant, carcinogenesis",
                "Cardiovascular Pathology — MI, atherosclerosis",
                "Respiratory Pathology — COPD, pneumonia, lung cancer",
                "GI Pathology — PUD, IBD, colorectal cancer",
                "Renal Pathology — Glomerulonephritis, nephrotic syndrome",
            ],
            "notes": """
## 🏥 Pathology High-Yield Notes

### Types of Necrosis:
| Type | Cause | Appearance |
|------|-------|-----------|
| Coagulative | Ischaemia (most organs) | Preserved architecture |
| Liquefactive | Brain infarct, abscess | Liquid pus |
| Caseous | TB, fungi | Cheese-like |
| Fat | Pancreatitis | Calcium soap deposits |
| Gangrenous | Limb ischaemia + bacteria | Dry or wet |
| Fibrinoid | Immune complex vasculitis | Pink fibrin |

### Myocardial Infarction Timeline:
- **0–4 hrs**: No changes on light microscopy (EM changes only)
- **4–12 hrs**: Wavy fibres, pyknotic nuclei
- **12–24 hrs**: Coagulative necrosis, PMN infiltration begins
- **1–3 days**: PMN peak infiltration
- **3–7 days**: Macrophages arrive, granulation tissue begins
- **1–3 weeks**: Granulation tissue, fibroblasts
- **Months**: Dense collagen scar (white)

### Tumour Markers:
| Marker | Cancer |
|--------|--------|
| PSA | Prostate |
| AFP | Hepatocellular, testicular (non-seminoma) |
| β-hCG | Choriocarcinoma, gestational trophoblastic |
| CEA | Colorectal, pancreatic |
| CA-125 | Ovarian |
| CA 19-9 | Pancreatic |
"""
        },
    },
    "Clinical": {
        "🫀 Cardiology": {
            "icon": "🫀",
            "color": "#ef4444",
            "topics": [
                "Ischaemic Heart Disease — ACS, STEMI, NSTEMI management",
                "Heart Failure — HFrEF vs HFpEF, NYHA classification",
                "Arrhythmias — AF, VT, SVT, ECG interpretation",
                "Valvular Heart Disease — Aortic stenosis, mitral regurgitation",
                "Hypertension — Classification, treatment targets",
                "Cardiomyopathies — Dilated, hypertrophic, restrictive",
                "Pericardial Disease — Pericarditis, tamponade",
                "Congenital Heart Disease — ASD, VSD, PDA, ToF",
            ],
            "notes": """
## 🫀 Cardiology High-Yield Notes

### ACS Management (MONA + others):
- **M**orphine (pain)
- **O**xygen (if SpO₂ < 94%)
- **N**itrates (GTN spray/IV)
- **A**spirin 300mg stat + Clopidogrel/Ticagrelor

### STEMI: Primary PCI within 90 mins (Door-to-Balloon)

### Heart Failure Medications:
1. **ACE inhibitor** (mortality benefit)
2. **Beta-blocker** (Bisoprolol/Carvedilol — mortality benefit)
3. **Aldosterone antagonist** (Spironolactone)
4. **SGLT2 inhibitor** (Empagliflozin — new evidence)
5. Diuretics (symptom relief only)

### ECG Changes in STEMI by Territory:
| Territory | Leads | Artery |
|-----------|-------|--------|
| Anterior | V1–V4 | LAD |
| Inferior | II, III, aVF | RCA |
| Lateral | I, aVL, V5–V6 | LCx |
| Posterior | Tall R in V1–V2 | RCA/LCx |
"""
        },
        "🫁 Respiratory": {
            "icon": "🫁",
            "color": "#06b6d4",
            "topics": [
                "Asthma — Severity classification, stepwise management",
                "COPD — GOLD staging, exacerbation management",
                "Pneumonia — CAP, HAP, treatment guidelines",
                "Pleural Disease — Effusion, pneumothorax, empyema",
                "Pulmonary Embolism — Wells score, CTPA, anticoagulation",
                "Lung Cancer — Types, staging, paraneoplastic syndromes",
                "Interstitial Lung Disease — IPF, sarcoidosis",
                "Respiratory Failure — Type 1 vs Type 2, NIV indications",
            ],
            "notes": """
## 🫁 Respiratory High-Yield Notes

### Asthma vs COPD:
| Feature | Asthma | COPD |
|---------|--------|------|
| Age | Young | >40, smoker |
| Reversibility | Complete | Incomplete |
| FEV1/FVC | <0.7 (reversible) | <0.7 (fixed) |
| DLCO | Normal | ↓ (emphysema) |
| Eosinophils | Often ↑ | Neutrophils |

### Pleural Fluid (Light's Criteria) — Exudate if ANY:
1. Fluid protein / Serum protein **> 0.5**
2. Fluid LDH / Serum LDH **> 0.6**
3. Fluid LDH **> 2/3 upper limit of normal serum LDH**

### PE Risk Stratification (Wells Score):
- DVT symptoms: +3
- PE most likely diagnosis: +3
- HR > 100: +1.5
- Immobilisation >3 days/Surgery in 4 weeks: +1.5
- Previous DVT/PE: +1.5
- Haemoptysis: +1
- Malignancy: +1

Score >4 → High probability → CTPA
"""
        },
        "🧠 Neurology": {
            "icon": "🧠",
            "color": "#8b5cf6",
            "topics": [
                "Stroke — Ischaemic vs haemorrhagic, thrombolysis criteria",
                "Epilepsy — Seizure classification, AED selection",
                "Headache — Migraine, tension, cluster, SAH (thunderclap)",
                "Movement Disorders — Parkinson's, essential tremor",
                "Dementia — Alzheimer's, vascular, Lewy body",
                "Peripheral Neuropathy — GBS, CIDP, diabetic neuropathy",
                "Multiple Sclerosis — Types, McDonald criteria, DMTs",
                "Meningitis — Bacterial vs viral, lumbar puncture findings",
            ],
            "notes": """
## 🧠 Neurology High-Yield Notes

### Stroke: FAST + BE
- **F**ace drooping
- **A**rm weakness
- **S**peech difficulty
- **T**ime to call emergency
- **B**alance loss
- **E**yes (vision change)

### Ischaemic Stroke Management:
- IV Alteplase (tPA) within **4.5 hours** of onset
- Thrombectomy within **24 hours** (if large vessel occlusion)
- CT head first to **EXCLUDE** haemorrhage

### CSF Findings:
| Condition | Appearance | WBC | Protein | Glucose |
|-----------|-----------|-----|---------|---------|
| Bacterial | Turbid | ↑↑ PMN | ↑↑ | ↓↓ |
| Viral | Clear | ↑ Lymph | ↑ | Normal |
| TB | Xanthochromic | ↑ Lymph | ↑↑ | ↓ |
| SAH | Xanthochromic | RBC | Normal | Normal |

### Parkinson's Triad:
**TRAP** — Tremor (resting, pill-rolling), Rigidity (cogwheel), Akinesia, Postural instability
"""
        },
        "🍽️ Gastroenterology": {
            "icon": "🍽️",
            "color": "#10b981",
            "topics": [
                "PUD — H. pylori, NSAID-induced, management",
                "IBD — Crohn's vs UC, extraintestinal features",
                "Liver Disease — Cirrhosis, hepatitis, portal hypertension",
                "Pancreatitis — Acute vs chronic, Ranson's criteria",
                "GI Bleeding — Upper vs lower, management",
                "Colorectal Cancer — Screening, staging, familial syndromes",
                "Dysphagia — Achalasia, oesophageal cancer",
                "Coeliac Disease — Diagnosis, complications",
            ],
            "notes": """
## 🍽️ Gastroenterology High-Yield Notes

### Crohn's vs Ulcerative Colitis:
| Feature | Crohn's | UC |
|---------|---------|-----|
| Location | Any part of GI | Colon only (rectum always) |
| Pattern | Skip lesions | Continuous |
| Layers | Transmural | Mucosal/submucosal |
| Fistulae | Yes | No |
| Smoking | Worsens | Protective |
| Granulomas | Yes | No |

### Child-Pugh Score (Liver):
- Bilirubin, Albumin, PT/INR, Ascites, Encephalopathy
- A (5–6): Well-compensated
- B (7–9): Significant dysfunction
- C (10–15): Decompensated

### Hepatitis B Serology:
| Marker | Meaning |
|--------|---------|
| HBsAg+ | Active infection |
| Anti-HBs+ | Immunity (vaccine or recovery) |
| Anti-HBc IgM+ | Acute infection |
| HBeAg+ | High infectivity |
| Anti-HBe+ | Low infectivity |
"""
        },
        "🦴 Musculoskeletal": {
            "icon": "🦴",
            "color": "#f59e0b",
            "topics": [
                "Rheumatoid Arthritis — Diagnosis, DMARDs, complications",
                "Osteoarthritis — vs RA, management",
                "Gout — Pathophysiology, acute management, urate-lowering",
                "SLE — Criteria, lupus nephritis, ANA",
                "Osteoporosis — DEXA scan, FRAX score, bisphosphonates",
                "Fractures — Common fracture patterns, complications",
                "Back Pain — Red flags, disc herniation, cauda equina",
                "Vasculitis — Giant cell arteritis, Kawasaki, ANCA",
            ],
            "notes": """
## 🦴 Musculoskeletal High-Yield Notes

### RA vs OA:
| Feature | RA | OA |
|---------|----|----|
| Age | 30–50F | >50 |
| Joints | MCP, PIP, wrist | DIP, hip, knee |
| Stiffness | Morning >1hr | <30 min |
| Systemic | Yes | No |
| X-ray | Erosions, periarticular osteoporosis | Osteophytes, joint space ↓ |

### Kawasaki Disease — CRASH and BURN:
- **C**onjunctival injection
- **R**ash (polymorphous)
- **A**denopathy (cervical)
- **S**trawberry tongue/lip cracking
- **H**ands/feet oedema + desquamation
→ BURN: **Burn**ing fever >5 days

Treatment: **IVIG + Aspirin**

### SLE Criteria (SOAP BRAIN MD):
Serositis, Oral ulcers, Arthritis, Photosensitivity, Blood disorders,
Renal, ANA, Immunologic (anti-dsDNA), Neurological, Malar rash, Discoid rash
"""
        },
        "🚑 Emergency Medicine": {
            "icon": "🚑",
            "color": "#dc2626",
            "topics": [
                "ABCDE Assessment — Systematic approach to sick patient",
                "Resuscitation — ALS/ACLS algorithm, shockable rhythms",
                "Sepsis — Sepsis-3 definition, Sepsis-6 bundle",
                "Anaphylaxis — Recognition, IM adrenaline, management",
                "DKA — Diagnosis, fluid replacement, insulin protocol",
                "Toxicology — Common poisonings, antidotes",
                "Major Trauma — Primary/secondary survey, ATLS",
                "Burns — Rule of 9s, Parkland formula",
            ],
            "notes": """
## 🚑 Emergency Medicine High-Yield Notes

### ABCDE Approach:
1. **A**irway — Look, listen, feel. Jaw thrust, airway adjuncts
2. **B**reathing — RR, SpO₂, auscultate, chest expansion
3. **C**irculation — HR, BP, CRT, IV access × 2
4. **D**isability — GCS, pupils, BM (glucose)
5. **E**xposure — Full exposure, temperature

### Sepsis-6 Bundle (complete within 1 hour):
**Take 3, Give 3:**
- TAKE: Blood cultures, Lactate, Urine output monitoring
- GIVE: O₂, IV fluids (30 mL/kg), IV antibiotics

### DKA Diagnosis:
- BG > 11 mmol/L (or known DM)
- pH < 7.3 OR bicarbonate < 15
- Ketonaemia/ketonuria

### Anaphylaxis Management:
1. **Adrenaline 0.5mg IM** (anterolateral thigh) — FIRST!
2. Remove trigger
3. Lay flat, legs raised
4. O₂ 15L/min
5. IV Chlorphenamine + Hydrocortisone
6. IV fluids if hypotensive
"""
        },
    }
}


# ─────────────────────────────────────────
# FLASHCARD DATA
# ─────────────────────────────────────────
FLASHCARDS = [
    {
        "id": "fc001", "subject": "Anatomy",
        "front": "What are the contents of the femoral triangle from lateral to medial?",
        "back": "NAVEL:\n🔸 Nerve (femoral)\n🔸 Artery (femoral)\n🔸 Vein (femoral)\n🔸 Empty space\n🔸 Lymphatics"
    },
    {
        "id": "fc002", "subject": "Anatomy",
        "front": "Which nerve is damaged in 'Saturday night palsy'?",
        "back": "Radial nerve\n(compression in spiral groove of humerus)\n→ Wrist drop + loss of finger extension\n→ Intact triceps (branch given before groove)"
    },
    {
        "id": "fc003", "subject": "Anatomy",
        "front": "What passes through the carpal tunnel?",
        "back": "9 tendons + 1 nerve:\n• Flexor digitorum superficialis (×4)\n• Flexor digitorum profundus (×4)\n• Flexor pollicis longus (×1)\n• Median nerve\n\n❌ Ulnar nerve does NOT pass through!"
    },
    {
        "id": "fc004", "subject": "Physiology",
        "front": "What is the normal FEV1/FVC ratio, and what does a reduced ratio indicate?",
        "back": "Normal: >0.70 (70%)\n\nReduced (<70%) = Obstructive pattern\n• Asthma\n• COPD\n• Bronchiectasis\n\nRestrictive = Normal or ↑ ratio, but ↓ FVC"
    },
    {
        "id": "fc005", "subject": "Physiology",
        "front": "Name the 4 phases of the cardiac cycle.",
        "back": "1. Isovolumetric contraction\n   (MV closes → AV opens)\n2. Rapid ejection\n3. Isovolumetric relaxation\n   (AV closes → MV opens)\n4. Rapid filling (passive)\n\nHeart sounds: S1=MV close, S2=AV close"
    },
    {
        "id": "fc006", "subject": "Biochemistry",
        "front": "What enzyme deficiency causes Phenylketonuria (PKU)?",
        "back": "Phenylalanine hydroxylase\n(converts Phe → Tyrosine)\n\nResult: ↑ Phenylalanine → intellectual disability\nOman neonatal screening: Guthrie test\n\nTreatment: Low phenylalanine diet\n+ Sapropterin (BH4 cofactor)"
    },
    {
        "id": "fc007", "subject": "Biochemistry",
        "front": "Which vitamins are fat-soluble? What is their storage risk?",
        "back": "Fat-soluble: A, D, E, K\n\nMnemonic: 'All Dogs Eat Kids'\n\nRisk: TOXICITY from overdose\n(stored in liver/fat, not excreted in urine)\n\nVitamin A toxicity: Teratogenic, ↑ ICP\nVitamin D toxicity: Hypercalcaemia"
    },
    {
        "id": "fc008", "subject": "Pathology",
        "front": "What are the stages of atherosclerosis?",
        "back": "1. Endothelial injury (HTN, smoking, DM)\n2. Fatty streak (foam cells = macrophages + lipid)\n3. Fibrous plaque (smooth muscle migration)\n4. Complex plaque (calcification, necrosis)\n5. Rupture → Thrombosis → ACS/Stroke"
    },
    {
        "id": "fc009", "subject": "Microbiology",
        "front": "What is the mechanism of penicillin resistance?",
        "back": "β-lactamase enzyme\n(breaks the β-lactam ring)\n\nSolution: Add β-lactamase inhibitor:\n• Amoxicillin + Clavulanate (Co-amoxiclav)\n• Ampicillin + Sulbactam\n• Piperacillin + Tazobactam\n\nMRSA: PBP2a mutation → penicillin can't bind"
    },
    {
        "id": "fc010", "subject": "Pharmacology",
        "front": "What is the antidote for paracetamol overdose?",
        "back": "N-Acetylcysteine (NAC)\n\nMechanism:\n• Paracetamol → NAPQI (toxic)\n• Glutathione normally detoxifies NAPQI\n• Overdose depletes glutathione\n• NAC replenishes glutathione precursor\n\nGive within 8–10 hours for best effect\nMonitor: LFTs, paracetamol levels, INR"
    },
    {
        "id": "fc011", "subject": "Cardiology",
        "front": "What ECG changes occur in hyperkalaemia?",
        "back": "Progressive changes with rising K⁺:\n\nK⁺ 5.5–6.5: Peaked (tall tented) T waves\nK⁺ 6.5–7.0: Prolonged PR, widened QRS\nK⁺ >7.0: Sine wave pattern\nK⁺ >8.0: Ventricular fibrillation / asystole\n\nTreatment: Calcium gluconate (stabilise heart) → shift K⁺ in → remove K⁺"
    },
    {
        "id": "fc012", "subject": "Neurology",
        "front": "What is the Glasgow Coma Scale (GCS)? What score is intubation threshold?",
        "back": "GCS = Eye + Verbal + Motor\n\nEye (1–4): None/Pain/Voice/Spontaneous\nVerbal (1–5): None/Sounds/Words/Confused/Oriented\nMotor (1–6): None/Extension/Flexion/Withdrawal/Localise/Obeys\n\nMax = 15 (normal)\nMin = 3 (deep coma)\n\nIntubation threshold: GCS ≤ 8 (airway unprotected)"
    },
    {
        "id": "fc013", "subject": "Gastroenterology",
        "front": "What are the features of Budd-Chiari syndrome?",
        "back": "Hepatic vein thrombosis → impaired outflow\n\nClinical Triad:\n• Painful hepatomegaly\n• Ascites\n• Jaundice\n\nCauses (hypercoagulable states):\nPolycythaemia vera, Pregnancy, OCP,\nAntiphospholipid syndrome, JAK2 mutation\n\nInvestigation: Doppler USS → reversal of flow"
    },
    {
        "id": "fc014", "subject": "Endocrinology",
        "front": "What are the signs of Cushing's syndrome?",
        "back": "Excess cortisol → CUSHINGS:\n\n🔸 C — Central obesity, buffalo hump\n🔸 U — Urinary frequency (DM)\n🔸 S — Skin: striae, easy bruising, thin skin\n🔸 H — Hypertension, Hirsutism\n🔸 I — Infections (immunosuppressed)\n🔸 N — Necrosis (avascular, femoral head)\n🔸 G — Growth retardation (children)\n🔸 S — Secondary amenorrhoea, moon face"
    },
    {
        "id": "fc015", "subject": "Reproductive",
        "front": "What is the management of Pre-eclampsia?",
        "back": "Pre-eclampsia: HTN >140/90 + proteinuria after 20 weeks\n\nManagement:\n• Antihypertensive: Labetalol / Nifedipine / Methyldopa\n• Seizure prophylaxis: Magnesium sulphate (MgSO₄)\n• Fetal monitoring: CTG, USS growth scans\n• Definitive: DELIVERY\n\nEclampsia = Pre-eclampsia + seizures\nHELLP: Haemolysis, ↑LFTs, Low Platelets"
    },
]


# ─────────────────────────────────────────
# MNEMONICS LIBRARY
# ─────────────────────────────────────────
MNEMONICS = [
    {
        "title": "Cranial Nerves (I–XII)",
        "mnemonic": "Oh Oh Oh To Touch And Feel Very Good Velvet... Ahh Heaven!",
        "meaning": "Olfactory, Optic, Oculomotor, Trochlear, Trigeminal, Abducens, Facial, Vestibulocochlear, Glossopharyngeal, Vagus, Accessory, Hypoglossal",
        "subject": "Anatomy",
        "type": "Classic"
    },
    {
        "title": "Brachial Plexus",
        "mnemonic": "Randy Travis Drinks Cold Beer",
        "meaning": "Roots → Trunks → Divisions → Cords → Branches",
        "subject": "Anatomy",
        "type": "Classic"
    },
    {
        "title": "Kawasaki Disease Features",
        "mnemonic": "CRASH and BURN",
        "meaning": "Conjunctivitis, Rash, Adenopathy, Strawberry tongue, Hand/foot changes → BURN (fever >5 days)",
        "subject": "Paediatrics",
        "type": "Classic"
    },
    {
        "title": "Femoral Triangle Contents",
        "mnemonic": "NAVEL (lateral → medial)",
        "meaning": "Nerve, Artery, Vein, Empty space, Lymphatics",
        "subject": "Anatomy",
        "type": "Classic"
    },
    {
        "title": "SLE Diagnostic Criteria",
        "mnemonic": "SOAP BRAIN MD",
        "meaning": "Serositis, Oral ulcers, Arthritis, Photosensitivity, Blood disorders, Renal, ANA, Immunologic, Neurological, Malar rash, Discoid rash",
        "subject": "Rheumatology",
        "type": "Classic"
    },
    {
        "title": "Cushing's Syndrome Features",
        "mnemonic": "CUSHINGS",
        "meaning": "Central obesity, Urinary (DM), Skin changes, Hypertension/Hirsutism, Infections, Necrosis (avascular), Growth issues, Striae/Secondary amenorrhoea",
        "subject": "Endocrinology",
        "type": "Classic"
    },
    {
        "title": "Fat-Soluble Vitamins",
        "mnemonic": "All Dogs Eat Kids",
        "meaning": "Vitamins A, D, E, K are fat-soluble (stored in fat → toxicity risk)",
        "subject": "Biochemistry",
        "type": "Classic"
    },
    {
        "title": "Vitamin B3 Deficiency (Pellagra) — 4 Ds",
        "mnemonic": "4 Ds",
        "meaning": "Dermatitis, Diarrhoea, Dementia, Death",
        "subject": "Biochemistry",
        "type": "Classic"
    },
    {
        "title": "Heart Failure Medications",
        "mnemonic": "ABBA",
        "meaning": "ACE inhibitor, Beta-blocker, (spiro)nolactone, ARNI/ARBs — the four pillars with mortality benefit",
        "subject": "Cardiology",
        "type": "Classic"
    },
    {
        "title": "ACS Immediate Management",
        "mnemonic": "MONA",
        "meaning": "Morphine, Oxygen (if <94%), Nitrates, Aspirin 300mg",
        "subject": "Cardiology",
        "type": "Classic"
    },
    {
        "title": "Stroke Recognition",
        "mnemonic": "FAST",
        "meaning": "Face drooping, Arm weakness, Speech difficulty, Time to call emergency",
        "subject": "Neurology",
        "type": "Classic"
    },
    {
        "title": "Parkinson's Disease",
        "mnemonic": "TRAP",
        "meaning": "Tremor (resting, pill-rolling), Rigidity (cogwheel), Akinesia/bradykinesia, Postural instability",
        "subject": "Neurology",
        "type": "Classic"
    },
    {
        "title": "Causes of Clubbing",
        "mnemonic": "CLUBBING",
        "meaning": "Cancer (lung), Lung suppuration (abscess/empyema), Ulcerative colitis, Bronchiectasis, Bowel (Crohn's), Infective endocarditis, Neuroblastoma, Graves' disease",
        "subject": "General Medicine",
        "type": "Classic"
    },
    {
        "title": "Sepsis-6 Bundle",
        "mnemonic": "Take 3, Give 3",
        "meaning": "TAKE: Blood cultures, Lactate, Urine monitoring | GIVE: Oxygen, IV fluids (30mL/kg), IV antibiotics",
        "subject": "Emergency Medicine",
        "type": "Clinical"
    },
    {
        "title": "Glasgow Coma Scale",
        "mnemonic": "EVM — 4, 5, 6",
        "meaning": "Eyes (max 4), Verbal (max 5), Motor (max 6) = Maximum 15. GCS ≤8 = Intubate",
        "subject": "Emergency Medicine",
        "type": "Clinical"
    },
    {
        "title": "Antibiotic Targets",
        "mnemonic": "Buy AT 30, CELL at 50",
        "meaning": "30S: Aminoglycosides, Tetracyclines | 50S: Chloramphenicol, Erythromycin (macrolides), Lincosamides (clindamycin) | Cell Wall: β-lactams, Vancomycin",
        "subject": "Microbiology",
        "type": "Pharmacology"
    },
    {
        "title": "Types of Shock",
        "mnemonic": "HOOD",
        "meaning": "Hypovolaemic, Obstructive, Obstructive (cardiac tamponade/PE), Distributive (septic/anaphylactic/neurogenic)",
        "subject": "Emergency Medicine",
        "type": "Clinical"
    },
    {
        "title": "DKA vs HHS",
        "mnemonic": "DKA is Dramatic, HHS is Hyperosmolar",
        "meaning": "DKA: Young T1DM, fast onset, ketones, pH<7.3 | HHS: Old T2DM, slow onset, no ketones, glucose >30, very high osmolality",
        "subject": "Endocrinology",
        "type": "Clinical"
    },
]


# ─────────────────────────────────────────
# POMODORO BREAK SUGGESTIONS
# ─────────────────────────────────────────
BREAK_SUGGESTIONS = {
    "short": [  # 5 min break
        "💧 Drink a full glass of water — hydration keeps your brain sharp!",
        "🧘 Do 5 deep breaths: inhale 4 sec, hold 4, exhale 4 (box breathing)",
        "👁️ 20-20-20 rule: look at something 20 feet away for 20 seconds",
        "🚶 Walk to the kitchen and back — move those legs!",
        "🤸 Do 10 neck rolls — left, right, forward, back",
        "😴 Close your eyes for 2 minutes — micro-rest your brain",
        "🌿 Look outside at nature for 5 minutes — proven stress reducer",
        "✋ Shake out your hands — relieve tension from writing",
    ],
    "long": [  # 15–30 min break
        "🍎 Eat a healthy snack — nuts, fruit, or dates (Omani energy boost!)",
        "🚶‍♀️ Take a 10-minute walk outside — fresh air improves memory consolidation",
        "🧘‍♀️ Do a 10-minute guided meditation — reduces cortisol before exams",
        "💬 Call a friend or family member — social connection reduces burnout",
        "🛁 Wash your face with cold water — activates the dive reflex, calms you",
        "📖 Read something non-medical for 15 minutes — let your brain relax",
        "🎵 Listen to your favourite song — music boosts dopamine and motivation",
        "🍵 Make tea/coffee mindfully — a ritual that signals 'break mode'",
    ]
}


# ─────────────────────────────────────────
# MOTIVATIONAL QUOTES
# ─────────────────────────────────────────
MOTIVATIONAL_QUOTES = [
    {"quote": "The art of medicine consists of amusing the patient while nature cures the disease.", "author": "Voltaire"},
    {"quote": "Medicine is not only a science; it is also an art.", "author": "Paracelsus"},
    {"quote": "The doctor of the future will give no medicine, but will interest his patients in the care of the human frame, in diet and in the cause and prevention of disease.", "author": "Thomas Edison"},
    {"quote": "Wherever the art of medicine is loved, there is also a love of humanity.", "author": "Hippocrates"},
    {"quote": "The good physician treats the disease; the great physician treats the patient who has the disease.", "author": "William Osler"},
    {"quote": "Every patient you see is a lesson in much more than the malady from which they suffer.", "author": "William Osler"},
    {"quote": "In medicine, as in statecraft and propaganda, words are sometimes the most powerful drugs we can use.", "author": "Sara Murray Jordan"},
    {"quote": "To study medicine is to study humanity.", "author": "Unknown"},
    {"quote": "Your future patients are counting on you. Study hard today.", "author": "MedStudy Oman"},
    {"quote": "Being a doctor is an honour. What you do today matters for tomorrow.", "author": "MedStudy Oman"},
]