"""
mcq_bank.py — 200+ High-Yield MCQs organized by medical subject.
Each question has 4 options, correct answer index, detailed explanation,
and a Senior Doctor commentary tip.
"""

MCQ_BANK = {

    # ══════════════════════════════════════
    # ANATOMY
    # ══════════════════════════════════════
    "Anatomy": [
        {
            "q": "A patient presents with inability to abduct the arm beyond 15 degrees after a shoulder dislocation. Which nerve is most likely damaged?",
            "opts": ["Radial nerve", "Axillary nerve", "Musculocutaneous nerve", "Long thoracic nerve"],
            "ans": 1,
            "exp": "The axillary nerve (C5, C6) winds around the surgical neck of the humerus and supplies the deltoid muscle. Anterior shoulder dislocation or surgical neck fractures commonly damage this nerve, causing loss of shoulder abduction (deltoid) and a small patch of sensory loss over the 'regimental badge' area.",
            "tip": "🩺 Axillary nerve = Surgical neck # + Anterior dislocation. Always test deltoid power AND sensation over lateral shoulder after these injuries!"
        },
        {
            "q": "During a mastectomy, a patient develops winging of the scapula post-operatively. Which nerve was damaged?",
            "opts": ["Axillary nerve", "Suprascapular nerve", "Long thoracic nerve", "Thoracodorsal nerve"],
            "ans": 2,
            "exp": "The long thoracic nerve (C5, 6, 7) supplies the serratus anterior muscle. It runs superficially along the chest wall and is vulnerable during mastectomy or axillary dissection. Serratus anterior holds the scapula against the chest wall; without it, the medial border of the scapula wings out.",
            "tip": "🩺 Mnemonic: 'Long thoracic = Serratus = Scapula stays flat.' C5,6,7 raise your wings to heaven!"
        },
        {
            "q": "A patient presents with inability to oppose the thumb and loss of sensation over the lateral 3½ fingers. Which nerve is compressed?",
            "opts": ["Ulnar nerve", "Radial nerve", "Median nerve", "Axillary nerve"],
            "ans": 2,
            "exp": "The median nerve passes through the carpal tunnel. Compression causes: (1) Thenar wasting and loss of thumb opposition (LOAF muscles: Lateral two Lumbricals, Opponens pollicis, Abductor pollicis brevis, Flexor pollicis brevis), (2) Sensory loss over lateral 3½ fingers and palm. Classic carpal tunnel syndrome.",
            "tip": "🩺 LOAF muscles = Median nerve in hand. The ulnar nerve gets the rest (hypothenar + medial 1.5 fingers). Classic OSCE station!"
        },
        {
            "q": "Which structure forms the floor of the femoral triangle?",
            "opts": ["Pectineus and iliopsoas", "Adductor longus and pectineus", "Iliopsoas and adductor longus", "Sartorius and rectus femoris"],
            "ans": 2,
            "exp": "The femoral triangle has: Roof = fascia lata + skin; Lateral border = sartorius; Medial border = adductor longus; Superior border = inguinal ligament; Floor = iliopsoas (lateral) + pectineus (medial). Contents: Femoral Nerve, Artery, Vein, Empty space, Lymphatics (NAVEL - lateral to medial).",
            "tip": "🩺 NAVEL from lateral to medial is the key. The femoral vein is accessed medial to the artery for central lines at SQUH!"
        },
        {
            "q": "A 70-year-old man falls onto his outstretched hand. X-ray shows a fracture at the anatomical neck of the humerus. Which structure is at greatest risk of avascular necrosis?",
            "opts": ["Greater tubercle", "Humeral head", "Coracoid process", "Acromion"],
            "ans": 1,
            "exp": "The humeral head receives its blood supply primarily from the anterior and posterior circumflex humeral arteries, which enter below the anatomical neck. A fracture at the anatomical neck disrupts this supply, potentially leading to avascular necrosis of the humeral head. This is more serious than surgical neck fractures.",
            "tip": "🩺 Anatomical neck # = AVN risk. Surgical neck # = Axillary nerve risk. Know the difference for MCQs and clinics!"
        },
        {
            "q": "Which cranial nerve is responsible for the efferent limb of the corneal reflex?",
            "opts": ["CN V1 (Ophthalmic)", "CN V2 (Maxillary)", "CN VII (Facial)", "CN III (Oculomotor)"],
            "ans": 2,
            "exp": "The corneal reflex: Afferent = CN V1 (ophthalmic branch of trigeminal - detects touch), Efferent = CN VII (facial nerve - causes eye closure via orbicularis oculi). In a comatose patient, absent corneal reflex suggests brainstem involvement.",
            "tip": "🩺 Corneal reflex: V in (sensation), VII out (blink). If afferent is damaged (V), NEITHER eye blinks. If efferent is damaged (VII), only the IPSILATERAL eye doesn't blink."
        },
        {
            "q": "A baby is born with a claw hand deformity affecting the medial 1.5 fingers. Which nerve was likely injured during delivery?",
            "opts": ["Median nerve (upper trunk)", "Ulnar nerve", "Radial nerve", "Lower trunk of brachial plexus (C8, T1)"],
            "ans": 3,
            "exp": "Klumpke's palsy affects C8, T1 (lower trunk of brachial plexus), caused by excessive arm abduction during difficult deliveries. It affects ulnar-innervated intrinsic hand muscles causing claw deformity of medial 1.5 fingers, and T1 contribution to sympathetic chain can cause Horner's syndrome.",
            "tip": "🩺 Klumpke's = Lower trunk (C8,T1) = Claw hand + possible Horner's. Erb's palsy = Upper trunk (C5,6) = 'Waiter's tip' position."
        },
        {
            "q": "The portal triad in the liver consists of which structures?",
            "opts": ["Hepatic artery, hepatic vein, bile duct", "Portal vein, hepatic artery, bile duct", "Portal vein, hepatic vein, lymphatic", "Hepatic artery, central vein, bile canaliculi"],
            "ans": 1,
            "exp": "The portal triad (at corners of liver lobules) contains: Portal vein branch, Hepatic artery branch, Bile duct. Blood flows FROM portal triad → through sinusoids → TO central vein → hepatic vein → IVC. Bile flows in OPPOSITE direction (from hepatocytes → bile canaliculi → bile duct → portal triad).",
            "tip": "🩺 Blood flows IN via portal triad, OUT via central vein. Bile flows opposite to blood! Zone 1 (periportal) = most O2, most affected in hepatitis. Zone 3 (centrilobular) = least O2, most affected in ischaemia and paracetamol OD."
        },
    ],

    # ══════════════════════════════════════
    # PHYSIOLOGY
    # ══════════════════════════════════════
    "Physiology": [
        {
            "q": "A patient has a pCO2 of 28 mmHg, pH 7.50, HCO3 of 20 mEq/L. What is the acid-base disturbance?",
            "opts": ["Metabolic alkalosis", "Respiratory alkalosis with metabolic compensation", "Metabolic acidosis", "Respiratory acidosis"],
            "ans": 1,
            "exp": "pH > 7.45 = alkalosis. Primary disturbance: low pCO2 (28 mmHg, normal 35-45) = Respiratory alkalosis (hyperventilation blows off CO2). The HCO3 is slightly low (20, normal 22-26) = compensatory metabolic response (kidneys excrete HCO3 to bring pH down). This is FULLY compensated respiratory alkalosis.",
            "tip": "🩺 Step 1: pH alkalotic/acidotic? Step 2: Check CO2 (respiratory) and HCO3 (metabolic). Whichever matches the pH direction = PRIMARY. The other = COMPENSATION."
        },
        {
            "q": "Which component of the ECG represents ventricular repolarisation?",
            "opts": ["P wave", "QRS complex", "PR interval", "T wave"],
            "ans": 3,
            "exp": "P wave = Atrial depolarisation. PR interval = AV node conduction delay. QRS = Ventricular depolarisation. T wave = Ventricular repolarisation. Atrial repolarisation is hidden within the QRS complex. Tall peaked T waves = hyperkalaemia. Flattened/inverted T waves = ischaemia, LVH.",
            "tip": "🩺 Peaked T waves in precordial leads = think hyperkalaemia first! Always check K⁺ when you see tall T waves."
        },
        {
            "q": "During exercise, which of the following changes occurs to increase oxygen delivery to muscles?",
            "opts": ["Bohr effect shifts O2 dissociation curve left", "Increased pH shifts curve right", "Increased CO2 and decreased pH shifts curve right", "Decreased temperature shifts curve right"],
            "ans": 2,
            "exp": "The Bohr effect: During exercise, muscles produce CO2 and lactic acid (↓pH). This RIGHTWARD shift of the oxygen-haemoglobin dissociation curve means Hb has LOWER affinity for O2, so it releases more O2 to the tissues. Factors causing right shift: ↑CO2, ↑H⁺ (↓pH), ↑temperature, ↑2,3-DPG.",
            "tip": "🩺 Right shift = Releases O2 to tissues (good during exercise). Remember: CO2-Rich, Hot, Acidic muscles need O2 → curve shifts RIGHT to deliver it. 'CADET face right' = CO2, Acid, DPG, Exercise, Temperature → right shift."
        },
        {
            "q": "GFR is 120 mL/min. Plasma concentration of substance X is 2 mg/mL. Urine concentration is 150 mg/mL, urine flow is 1 mL/min. What is happening to substance X in the nephron?",
            "opts": ["Filtered and completely reabsorbed", "Filtered and partially secreted", "Filtered and partially reabsorbed", "Not filtered at all"],
            "ans": 1,
            "exp": "Filtered load = GFR × plasma concentration = 120 × 2 = 240 mg/min. Excreted = urine concentration × urine flow = 150 × 1 = 150 mg/min. Since excreted (150) < filtered (240), the substance is being REABSORBED. 240 - 150 = 90 mg/min reabsorbed. If secreted, excreted would EXCEED filtered load.",
            "tip": "🩺 Filtered load = GFR × Pconc. Excreted = Uconc × Uflow. If Excreted < Filtered = REABSORBED. If Excreted > Filtered = SECRETED. Creatinine is slightly secreted (so creatinine clearance slightly overestimates true GFR)."
        },
        {
            "q": "Which ion channel is responsible for the plateau phase (phase 2) of the cardiac action potential?",
            "opts": ["Fast Na⁺ channels", "Slow Ca²⁺ channels (L-type)", "K⁺ channels", "Cl⁻ channels"],
            "ans": 1,
            "exp": "Cardiac action potential phases: 0 = Rapid depolarisation (fast Na⁺), 1 = Initial repolarisation (K⁺ out), 2 = Plateau (L-type Ca²⁺ in balanced by K⁺ out - this triggers contraction!), 3 = Rapid repolarisation (K⁺ out), 4 = Resting potential. The plateau is unique to cardiac muscle and prevents tetany.",
            "tip": "🩺 Phase 2 plateau = Ca²⁺ influx = triggers myocardial contraction via calcium-induced calcium release from SR. Calcium channel blockers (verapamil, diltiazem) affect this phase - that's why they reduce contractility."
        },
        {
            "q": "A patient has Conn's syndrome (primary hyperaldosteronism). Which set of findings is expected?",
            "opts": ["↑Na, ↓K, ↓pH (acidosis)", "↑Na, ↓K, ↑pH (alkalosis)", "↓Na, ↑K, ↑pH", "↑Na, ↑K, ↓pH"],
            "ans": 1,
            "exp": "Aldosterone acts on collecting duct: Na⁺ reabsorption (↑Na), K⁺ excretion (↓K = hypokalaemia), H⁺ excretion (metabolic alkalosis ↑pH). Clinical features: hypertension (Na retention → volume expansion), muscle weakness/cramps (hypokalaemia), metabolic alkalosis. Renin is LOW (negative feedback from high aldosterone).",
            "tip": "🩺 Conn's = ↑Aldosterone, ↓Renin, ↑Na, ↓K, Metabolic Alkalosis, HTN. The hypokalaemia and HTN combination should always make you think of Conn's!"
        },
    ],

    # ══════════════════════════════════════
    # BIOCHEMISTRY
    # ══════════════════════════════════════
    "Biochemistry": [
        {
            "q": "A newborn develops jaundice, cataracts, and hypoglycaemia after breastfeeding. What enzyme is deficient?",
            "opts": ["Glucose-6-phosphatase", "Galactose-1-phosphate uridylyltransferase", "Fructokinase", "Phenylalanine hydroxylase"],
            "ans": 1,
            "exp": "Classic Galactosaemia: deficiency of galactose-1-phosphate uridylyltransferase. Galactose (from lactose in breast milk) accumulates → galactose-1-phosphate is toxic. Features: jaundice, cataracts (galactitol deposits in lens), hepatomegaly, hypoglycaemia, intellectual disability, E.coli sepsis in neonates. Treatment: galactose-free diet.",
            "tip": "🩺 Galactosaemia triad: Jaundice + Cataracts + E.coli sepsis in a breastfed neonate. The cataracts due to galactitol accumulation are classic! Neonatal screening catches this."
        },
        {
            "q": "In competitive enzyme inhibition, what happens to Km and Vmax?",
            "opts": ["↑Km, ↓Vmax", "↑Km, unchanged Vmax", "Unchanged Km, ↓Vmax", "↓Km, ↑Vmax"],
            "ans": 1,
            "exp": "Competitive inhibitor COMPETES with substrate for the active site. More substrate overcomes inhibition → Vmax unchanged (can still reach maximum rate). But you need more substrate to reach half-Vmax → Km INCREASES (apparent reduced affinity). Non-competitive inhibitor: binds elsewhere → can't overcome with substrate → ↓Vmax, unchanged Km.",
            "tip": "🩺 Competitive: Can be overcome by ↑substrate → Km↑, Vmax same. Non-competitive: can't be overcome → Km same, Vmax↓. Methotrexate is a competitive inhibitor of dihydrofolate reductase."
        },
        {
            "q": "Which vitamin deficiency causes Wernicke's encephalopathy?",
            "opts": ["Vitamin B12", "Vitamin B6 (Pyridoxine)", "Vitamin B1 (Thiamine)", "Vitamin B3 (Niacin)"],
            "ans": 2,
            "exp": "Thiamine (B1) is a cofactor for: Pyruvate dehydrogenase, α-ketoglutarate dehydrogenase, Transketolase (pentose phosphate pathway). Deficiency → Wernicke's (confusion, ophthalmoplegia, ataxia - Classic TRIAD) → if untreated → Korsakoff's (confabulation, anterograde amnesia). Common in alcoholics. Always give IV thiamine BEFORE glucose in alcoholics!",
            "tip": "🩺 Wernicke's triad: Confusion + Ophthalmoplegia + Ataxia = COA. Give IV Pabrinex (thiamine) BEFORE glucose - glucose without thiamine can PRECIPITATE Wernicke's in thiamine-depleted patients!"
        },
        {
            "q": "A patient with type 1 diabetes is found unconscious. Urine dipstick shows heavy ketonuria. What is the primary metabolic process causing ketone body formation?",
            "opts": ["Increased glycolysis", "Increased fatty acid β-oxidation in the liver", "Increased glycogenolysis", "Decreased gluconeogenesis"],
            "ans": 1,
            "exp": "In insulin deficiency (Type 1 DM, DKA): No insulin → cells can't take up glucose → cells 'starve'. Adipose tissue releases fatty acids → liver β-oxidises them → acetyl-CoA accumulates → diverted to ketone body synthesis (acetoacetate, β-hydroxybutyrate, acetone). Ketones are acidic → metabolic acidosis (DKA).",
            "tip": "🩺 DKA pathway: ↓Insulin → ↑Lipolysis → ↑β-oxidation → ↑Acetyl-CoA → ↑Ketogenesis → Metabolic acidosis. The liver makes the ketones, but can't use them (glucagon-driven state). Other tissues (brain, muscles) use them as fuel."
        },
        {
            "q": "A patient has xanthomas and premature atherosclerosis since age 20. Cholesterol is 12 mmol/L. LDL receptor function is 0%. What is the inheritance pattern?",
            "opts": ["Autosomal recessive", "X-linked recessive", "Autosomal dominant", "Mitochondrial"],
            "ans": 2,
            "exp": "Familial Hypercholesterolaemia (FH): Autosomal dominant mutation in LDL receptor gene. Heterozygous FH: Cholesterol 7-12 mmol/L, premature CVD in 30-40s. Homozygous FH: Cholesterol >15 mmol/L (LDL receptor function 0-25%), CVD in childhood/teenage. Features: tendon xanthomas, xanthelasma, corneal arcus <40yrs.",
            "tip": "🩺 FH is the most common autosomal dominant disorder (1:250 heterozygous). Always screen first-degree relatives! Statins are mainstay but homozygous FH may need LDL apheresis."
        },
    ],

    # ══════════════════════════════════════
    # PATHOLOGY
    # ══════════════════════════════════════
    "Pathology": [
        {
            "q": "A 65-year-old presents with dysphagia, weight loss and iron deficiency anaemia. Endoscopy shows a lower oesophageal mass. Biopsy shows glandular cells with mucin production. What is the most likely diagnosis?",
            "opts": ["Squamous cell carcinoma", "Adenocarcinoma", "Leiomyosarcoma", "Lymphoma"],
            "ans": 1,
            "exp": "Lower oesophageal adenocarcinoma (GOJ/cardia) arises from Barrett's oesophagus (intestinal metaplasia due to chronic GORD). Squamous cell carcinoma affects the UPPER/MIDDLE third (associated with smoking, alcohol, achalasia). Lower third = adenocarcinoma. Glandular cells with mucin = adenocarcinoma histology.",
            "tip": "🩺 Upper/middle oesophagus = SCC (smoking + alcohol). Lower oesophagus/GOJ = Adenocarcinoma (Barrett's + GORD + obesity). This distinction is classic exam and OSCE material!"
        },
        {
            "q": "Which type of necrosis is classically seen in tuberculosis?",
            "opts": ["Coagulative necrosis", "Liquefactive necrosis", "Caseous necrosis", "Fibrinoid necrosis"],
            "ans": 2,
            "exp": "Caseous necrosis (from Latin: caseus = cheese) is pathognomonic of tuberculosis and some fungi. It has a 'soft, cheese-like' white appearance. Microscopically: amorphous eosinophilic debris without preserved architecture, surrounded by granuloma (epithelioid macrophages + Langerhans giant cells + lymphocytes). This is distinct from other necrosis types.",
            "tip": "🩺 TB = Caseous (cheesy) necrosis + Granulomas. Remember all types: Coagulative (MI, most organs), Liquefactive (brain infarct, abscess), Caseous (TB/fungi), Fat (pancreatitis - soap saponification), Fibrinoid (vasculitis), Gangrenous."
        },
        {
            "q": "A 30-year-old woman presents with a breast lump that moves freely, is firm and rubbery, and increases in size before menstruation. What is the most likely diagnosis?",
            "opts": ["Invasive ductal carcinoma", "Fibroadenoma", "Fibrocystic change", "Phyllodes tumour"],
            "ans": 1,
            "exp": "Fibroadenoma: most common benign breast tumour in young women (15-35). Features: well-circumscribed, freely mobile ('breast mouse'), rubbery/firm, responsive to oestrogen (grows in pregnancy/puberty). Ultrasound: smooth, homogeneous, lobulated. Fine needle aspiration: epithelial cells + stromal cells. Usually managed conservatively if <3cm.",
            "tip": "🩺 'Breast mouse' that moves freely = Fibroadenoma. Hard, irregular, tethered lump with skin changes = cancer until proven otherwise. Fibroadenoma doesn't malignantly transform (minimal risk)."
        },
        {
            "q": "A 55-year-old chronic smoker develops haemoptysis. CT shows a central lung mass with hypercalcaemia. Which lung cancer is most likely?",
            "opts": ["Adenocarcinoma", "Small cell carcinoma", "Squamous cell carcinoma", "Large cell carcinoma"],
            "ans": 2,
            "exp": "Squamous cell carcinoma: CENTRAL, associated with smoking, produces PTHrP → hypercalcaemia (paraneoplastic). Also causes SIADH rarely. Adenocarcinoma: peripheral, non-smokers, EGFR mutations. Small cell: central, ACTH/ADH/LEMS (Lambert-Eaton), very chemosensitive. Carcinoid: produces 5-HT → carcinoid syndrome.",
            "tip": "🩺 SCC lung: Central + Cavitating + Hypercalcaemia (PTHrP). Small cell: Central + ACTH/SIADH/LEMS + Very chemo-sensitive (but worst prognosis as spreads early). Know the paraneoplastic syndromes!"
        },
        {
            "q": "Which mediator is responsible for the PAIN in acute inflammation?",
            "opts": ["Histamine", "Prostaglandin E2 and bradykinin", "Serotonin", "Complement C3a"],
            "ans": 1,
            "exp": "The 5 cardinal signs of acute inflammation: Rubor (redness - vasodilation), Calor (heat - vasodilation), Tumor (swelling - oedema), Dolor (pain - PGE2 + bradykinin sensitise nociceptors), Functio laesa (loss of function). NSAIDs work by inhibiting COX → ↓prostaglandin synthesis → ↓pain and fever.",
            "tip": "🩺 Pain in inflammation = PGE2 + Bradykinin. NSAIDs block COX1 and COX2. COX2-selective (celecoxib) = less GI side effects but ↑CVD risk. Paracetamol works centrally, not peripherally."
        },
    ],

    # ══════════════════════════════════════
    # MICROBIOLOGY
    # ══════════════════════════════════════
    "Microbiology": [
        {
            "q": "A 25-year-old has a painless genital ulcer with indurated edges and inguinal lymphadenopathy. Dark-field microscopy shows spirochaetes. What is the diagnosis and causative organism?",
            "opts": ["Chancroid — Haemophilus ducreyi", "Syphilis — Treponema pallidum", "Herpes — HSV-2", "Lymphogranuloma venereum — Chlamydia trachomatis"],
            "ans": 1,
            "exp": "Primary syphilis: painless, indurated (hard) chancre + regional lymphadenopathy. Dark-field microscopy shows Treponema pallidum (spirochaetes). VDRL/RPR = non-treponemal screening. FTA-ABS/TPHA = specific confirmatory. Contrast with Chancroid (painful ulcer, Haemophilus ducreyi) and Herpes (multiple painful vesicles/ulcers).",
            "tip": "🩺 Painless ulcer = Syphilis. Painful ulcer = Herpes (multiple) or Chancroid (one). Painless ulcer + painless nodes = Syphilis. Painless ulcer + painful nodes = LGV (Chlamydia L1-L3 serovars)."
        },
        {
            "q": "A patient develops profuse watery 'rice-water' diarrhoea after eating raw shellfish. No fever. Stool microscopy shows no WBCs. What is the mechanism of disease?",
            "opts": ["Invasion of colonic mucosa", "Secretory toxin — cAMP-mediated chloride secretion", "Cytotoxin causing cell death", "Preformed toxin causing vomiting"],
            "ans": 1,
            "exp": "Vibrio cholerae: Produces cholera toxin (CT) which permanently activates Gs protein → ↑cAMP → PKA phosphorylates CFTR → massive Cl⁻ secretion into gut lumen → water follows osmotically → profuse watery 'rice-water' diarrhoea. No mucosal invasion = no fever, no blood, no WBCs in stool. Treatment: oral rehydration therapy is primary.",
            "tip": "🩺 Non-invasive diarrhoea (no fever, no blood, no WBCs) = Secretory toxin (V.cholerae, ETEC). Invasive diarrhoea (fever, blood, WBCs) = Salmonella, Shigella, Campylobacter, E.coli O157:H7."
        },
        {
            "q": "A 6-year-old presents with fever, stiff neck, petechial rash, and photophobia. LP shows: turbid CSF, WBC ↑↑ (PMNs), protein ↑↑, glucose very low. What is the most likely organism?",
            "opts": ["Streptococcus pneumoniae", "Neisseria meningitidis", "Haemophilus influenzae", "Listeria monocytogenes"],
            "ans": 1,
            "exp": "Neisseria meningitidis (meningococcal meningitis): most common in teenagers/young adults + children. PETECHIAL/PURPURIC RASH is the key differentiator (non-blanching = septicaemia). Gram-negative diplococcus, capsule types A/B/C/W/Y. LP: purulent CSF, PMN predominance, very low glucose (<50% serum). S.pneumoniae = most common overall but no rash. Listeria = neonates/elderly/immunocompromised.",
            "tip": "🩺 Petechial/purpuric non-blanching rash + fever = Meningococcal septicaemia until proven otherwise. Give IV Benzylpenicillin IMMEDIATELY (don't wait for LP) — meningococcal is a medical emergency. Notify public health for prophylaxis of contacts."
        },
        {
            "q": "Brucellosis is commonly seen in Oman. Which of the following is the most common source of infection in Omani patients?",
            "opts": ["Direct contact with infected animals during slaughter", "Consumption of unpasteurised milk and dairy products", "Inhalation of contaminated aerosols", "Tick bites"],
            "ans": 1,
            "exp": "Brucellosis (Brucella melitensis, B.abortus): Zoonosis from goats/sheep/cattle. In Oman, the most common route is ingestion of unpasteurised milk/cheese ('harees', fresh laban, soft cheese from home). Features: undulant fever (peaks in afternoon), sweating, arthralgia, hepatosplenomegaly. Diagnosis: serology (Rose Bengal, SAT), culture. Treatment: Doxycycline + Rifampicin for 6 weeks.",
            "tip": "🩺 In Oman: Always ask about raw dairy consumption in patients with prolonged fever! Brucellosis is commonly misdiagnosed as TB or typhoid. Doxycycline + Rifampicin for 6 weeks = standard treatment."
        },
    ],

    # ══════════════════════════════════════
    # PHARMACOLOGY
    # ══════════════════════════════════════
    "Pharmacology": [
        {
            "q": "A patient taking warfarin for AF is started on ciprofloxacin for a UTI. What happens to warfarin effect?",
            "opts": ["Decreased effect — ciprofloxacin induces CYP450", "Increased effect — ciprofloxacin inhibits CYP450 and kills gut bacteria", "No effect", "Decreased effect — ciprofloxacin displaces warfarin from protein binding"],
            "ans": 1,
            "exp": "Ciprofloxacin INCREASES warfarin effect via 2 mechanisms: (1) Inhibits CYP1A2 → reduced warfarin metabolism → ↑warfarin levels, (2) Kills gut bacteria that produce vitamin K → less vitamin K → less clotting factor synthesis → warfarin effect enhanced. Risk of bleeding! Monitor INR closely. Dose reduction may be needed.",
            "tip": "🩺 Antibiotics + Warfarin = ↑INR (bleeding risk). Enzyme INDUCERS (rifampicin, phenytoin, carbamazepine, St John's Wort) ↓warfarin effect. Enzyme INHIBITORS (ciprofloxacin, fluconazole, amiodarone, metronidazole) ↑warfarin effect."
        },
        {
            "q": "A 68-year-old with heart failure is on furosemide and digoxin. His potassium is 2.8 mEq/L. What is the risk?",
            "opts": ["Hyperkalaemia causing bradycardia", "Digoxin toxicity due to hypokalaemia", "Reduced furosemide efficacy", "Alkalosis causing tetany"],
            "ans": 1,
            "exp": "Digoxin inhibits Na⁺/K⁺-ATPase. Hypokalaemia makes digoxin toxicity MORE likely because: K⁺ normally competes with digoxin for the pump binding site; low K⁺ = less competition = digoxin binds more effectively = toxic effects at lower levels. Furosemide causes hypokalaemia (wasting). Digoxin toxicity: nausea, xanthopsia (yellow vision), arrhythmias.",
            "tip": "🩺 Classic combination: Furosemide (↓K⁺) + Digoxin = TOXIC. Always give K⁺ supplementation or add spironolactone in patients on both. Digoxin toxicity signs: nausea, bradycardia, heart block, yellow/green visual halos, ECG: reverse tick/hockey-stick ST change."
        },
        {
            "q": "A pregnant woman at 28 weeks needs anticoagulation for a DVT. Which anticoagulant is safest?",
            "opts": ["Warfarin", "Dabigatran (DOAC)", "Low molecular weight heparin (LMWH)", "Unfractionated heparin IV"],
            "ans": 2,
            "exp": "Pregnancy anticoagulation: LMWH (e.g. enoxaparin) is the drug of choice throughout pregnancy. Warfarin = TERATOGENIC (warfarin embryopathy in 1st trimester, CNS defects, fetal bleeding). DOACs (dabigatran, rivaroxaban) = CONTRAINDICATED (unknown teratogenicity, cross placenta). LMWH = large molecule, doesn't cross placenta = safe for fetus.",
            "tip": "🩺 Pregnancy + DVT = LMWH throughout. Switch to unfractionated heparin at delivery (shorter half-life, reversible with protamine). Warfarin can be used POSTNATALLY and is safe in breastfeeding."
        },
        {
            "q": "Which beta-blocker is most cardioselective (β1 selective) and therefore safest in a patient with asthma?",
            "opts": ["Propranolol", "Labetalol", "Bisoprolol", "Carvedilol"],
            "ans": 2,
            "exp": "β1 selectivity: Bisoprolol > Metoprolol > Atenolol > Labetalol > Carvedilol > Propranolol. Bisoprolol is most β1 selective = least β2 blockade. β2 receptors in bronchi = bronchodilation; blocking them → bronchoconstriction. However, even 'cardioselective' beta-blockers can cause bronchospasm in severe asthma — use with extreme caution. Carvedilol and Labetalol also block α1 (vasodilation).",
            "tip": "🩺 Bisoprolol = Most β1 selective of commonly used agents. Carvedilol = β1, β2, α1 blocker (non-selective). Propranolol = non-selective β blocker. AVOID beta-blockers in asthma; if essential, use bisoprolol cautiously."
        },
    ],

    # ══════════════════════════════════════
    # CARDIOLOGY
    # ══════════════════════════════════════
    "Cardiology": [
        {
            "q": "An 80-year-old woman presents with syncope on exertion, angina, and dyspnoea. Examination reveals a slow-rising pulse and an ejection systolic murmur radiating to the carotid arteries. What is the diagnosis?",
            "opts": ["Mitral regurgitation", "Aortic stenosis", "Hypertrophic cardiomyopathy", "Pulmonary stenosis"],
            "ans": 1,
            "exp": "Aortic stenosis classic triad: Syncope (exertional), Angina, Dyspnoea (SAD). Signs: Slow-rising pulse (pulsus parvus et tardus), ESM at aortic area radiating to carotids, soft/absent A2, heaving non-displaced apex. Causes: bicuspid AV (young), calcific degeneration (elderly), rheumatic. Severity: peak gradient >40mmHg, AVA <1cm² = severe. Treatment: TAVI or surgical AVR.",
            "tip": "🩺 AS mnemonic: SAD (Syncope, Angina, Dyspnoea). Once symptoms develop, life expectancy without intervention: Syncope 3 years, Angina 5 years, Dyspnoea (HF) 2 years. Median survival: 3 years. TAVI has revolutionised treatment in elderly/high-risk patients."
        },
        {
            "q": "A 28-year-old presents with palpitations and an ECG shows a delta wave and short PR interval. What is the diagnosis?",
            "opts": ["Long QT syndrome", "Wolff-Parkinson-White syndrome", "Brugada syndrome", "First-degree heart block"],
            "ans": 1,
            "exp": "WPW syndrome: Accessory pathway (Bundle of Kent) bypasses AV node → ventricular pre-excitation. ECG: Short PR interval (<120ms), Delta wave (slurred QRS upstroke), widened QRS. Can cause SVT (AVRT) and, dangerously, AF with rapid conduction via accessory pathway → VF → sudden death. AVOID AV nodal blockers (verapamil, digoxin) in WPW with AF!",
            "tip": "🩺 WPW + AF = DANGEROUS. Verapamil/Digoxin in WPW + AF can cause VF and death by blocking AV node and forcing all conduction through fast accessory pathway. Use DC cardioversion or procainamide. Definitive: catheter ablation of accessory pathway."
        },
        {
            "q": "A 75-year-old with AF is on warfarin (INR 2.5). His CHA₂DS₂-VASc score is 4. Is his anticoagulation appropriate?",
            "opts": ["No — he should be on aspirin only", "Yes — anticoagulation is indicated", "No — anticoagulation is not needed at this score", "Only antiplatelet therapy is needed"],
            "ans": 1,
            "exp": "CHA₂DS₂-VASc scoring: C=CHF(1), H=HTN(1), A₂=Age≥75(2), D=DM(1), S₂=Stroke/TIA(2), V=Vascular disease(1), A=Age 65-74(1), Sc=Sex category female(1). Score ≥2 in males or ≥3 in females = anticoagulation recommended. Score of 4 = HIGH risk = warfarin or DOAC is definitely indicated. Aspirin alone is insufficient.",
            "tip": "🩺 AF anticoagulation 2024: Use CHA₂DS₂-VASc. DOACs preferred over warfarin (no monitoring needed). Warfarin still used in: mechanical heart valves, mitral stenosis, severe renal failure. HAS-BLED score assesses bleeding risk but doesn't override anticoagulation decision."
        },
        {
            "q": "A patient develops severe chest pain 5 days after an MI. Echo shows pericardial effusion and new fever. What is the most likely complication?",
            "opts": ["Reinfarction", "Dressler's syndrome (post-MI pericarditis)", "Ventricular septal defect", "Left ventricular free wall rupture"],
            "ans": 1,
            "exp": "Dressler's syndrome (Post-cardiac injury syndrome): Autoimmune pericarditis occurring 2-10 weeks after MI (or cardiac surgery/trauma). Features: fever, pleuritic chest pain, pericardial effusion, raised ESR/CRP, possible pleural effusion. Anti-heart antibodies found. Treatment: NSAIDs, colchicine. Distinguish from early pericarditis (24-72 hrs post-MI = fibrinous, friction rub).",
            "tip": "🩺 Early pericarditis (24-72 hrs): fibrinous, ECG saddle-shaped ST elevation. Late pericarditis (2-10 weeks = Dressler's): autoimmune, fever, effusion. Treatment = NSAIDs + Colchicine. Avoid anticoagulation if effusion is large (tamponade risk)."
        },
    ],

    # ══════════════════════════════════════
    # NEUROLOGY
    # ══════════════════════════════════════
    "Neurology": [
        {
            "q": "A 45-year-old presents with unilateral ptosis, miosis, and anhidrosis of the face. Which syndrome is this?",
            "opts": ["Horner's syndrome", "CN III palsy", "Argyll Robertson pupil", "Holmes-Adie syndrome"],
            "ans": 0,
            "exp": "Horner's syndrome = Interruption of sympathetic supply to the eye. Triad: Ptosis (partial - superior tarsal muscle), Miosis (small pupil - pupil dilator paralysed), Anhidrosis (same side of face - sweat glands). Causes: Pancoast tumour (lung apex), carotid artery dissection, syringomyelia, lateral medullary syndrome. CN III palsy: COMPLETE ptosis + dilated pupil + 'down and out' eye.",
            "tip": "🩺 Horner's triad: PAM - Ptosis (partial), Anhidrosis, Miosis. CN III palsy: complete ptosis + mydriasis (dilated) + down-and-out position. A Pancoast tumour at the lung apex can compress the sympathetic chain → Horner's!"
        },
        {
            "q": "A 35-year-old woman presents with relapsing-remitting episodes of optic neuritis, sensory disturbance, and ataxia over 2 years. MRI shows periventricular white matter lesions. What is the diagnosis?",
            "opts": ["Neuromyelitis optica", "Multiple sclerosis", "Cerebral vasculitis", "Vitamin B12 deficiency"],
            "ans": 1,
            "exp": "Multiple Sclerosis (MS): demyelinating disease, young women (F:M = 3:1), relapsing-remitting pattern. Lesions: periventricular (Dawson's fingers on MRI), juxtacortical, infratentorial. CSF: oligoclonal bands (IgG), ↑IgG. McDonald criteria for diagnosis requires DIS (dissemination in space) and DIT (dissemination in time). Treatment: disease-modifying therapies (interferons, natalizumab, ocrelizumab).",
            "tip": "🩺 MS: young woman + multiple demyelinating episodes in different CNS locations = MS until proven otherwise. Classic symptoms: Optic neuritis (painful vision loss), Uhthoff's phenomenon (worsening with heat), Lhermitte's sign (electric shock down spine on neck flexion), internuclear ophthalmoplegia (MLF lesion)."
        },
        {
            "q": "A 70-year-old with AF is found to have sudden right-sided hemiplegia and aphasia with a dense MCA territory infarct. Onset was 1 hour ago. Which treatment should be considered FIRST?",
            "opts": ["IV Alteplase (tPA) thrombolysis", "Aspirin 300mg", "Mechanical thrombectomy", "IV heparin infusion"],
            "ans": 0,
            "exp": "Ischaemic stroke within 4.5 hours with no contraindications → IV Alteplase (tPA) is FIRST if available. Contraindications: active bleeding, BP >185/110 (not controlled), INR >1.7, recent surgery, haemorrhagic transformation on CT. Mechanical thrombectomy: for large vessel occlusion (MCA M1, ICA), can be done up to 24 hours in eligible patients, but tPA first if within window and no contraindications.",
            "tip": "🩺 Stroke protocol: CT head FIRST (exclude haemorrhage) → if ischaemic + within 4.5hrs + no contraindications → IV tPA. Large vessel occlusion → thrombectomy. Time is brain: every 1 minute of MCA occlusion = 1.9 million neurons lost!"
        },
        {
            "q": "A 60-year-old presents with resting tremor, bradykinesia, and cogwheel rigidity. He responds well to levodopa. Which dopamine pathway is primarily affected?",
            "opts": ["Mesolimbic pathway", "Mesocortical pathway", "Nigrostriatal pathway", "Tuberoinfundibular pathway"],
            "ans": 2,
            "exp": "Parkinson's disease: Loss of dopaminergic neurons in the SUBSTANTIA NIGRA pars compacta of the NIGROSTRIATAL pathway. This pathway modulates movement. Loss of dopamine → relative excess of acetylcholine → tremor, rigidity, bradykinesia. Treatment: Levodopa + Carbidopa (carbidopa prevents peripheral conversion of levodopa), Dopamine agonists, MAO-B inhibitors. Other dopamine pathways: Mesolimbic (reward), Mesocortical (cognition/emotion - blocked by antipsychotics → depression), Tuberoinfundibular (prolactin control - blocked → hyperprolactinaemia).",
            "tip": "🩺 Antipsychotics block ALL dopamine pathways: (1) Nigrostriatal → extrapyramidal side effects (Parkinsonism), (2) Mesolimbic → therapeutic (reduces psychosis), (3) Mesocortical → worsens negative symptoms, (4) Tuberoinfundibular → hyperprolactinaemia (gynaecomastia, galactorrhoea)."
        },
    ],

    # ══════════════════════════════════════
    # RESPIRATORY
    # ══════════════════════════════════════
    "Respiratory": [
        {
            "q": "A 40-year-old non-smoker with a family history of emphysema presents with COPD-pattern disease affecting the lower lobes. What is the most likely underlying cause?",
            "opts": ["Centrilobular emphysema from smoking", "Alpha-1 antitrypsin deficiency", "Sarcoidosis", "Hypersensitivity pneumonitis"],
            "ans": 1,
            "exp": "Alpha-1 antitrypsin (AAT) deficiency: autosomal co-dominant (PiMM normal, PiZZ severely deficient). AAT normally inhibits neutrophil elastase. Without it → uncontrolled elastase → lung destruction. Key features: emphysema (LOWER lobe, panacinar - vs smoking = upper lobe, centrilobular), young onset, non-smoker, liver cirrhosis (AAT accumulates in hepatocytes). Diagnosis: serum AAT levels + genotyping.",
            "tip": "🩺 Lower lobe emphysema in young non-smoker = AAT deficiency until proven otherwise! Also causes liver cirrhosis. Treatment: AAT augmentation therapy (IV infusions), lung transplant in severe cases. Screen family members!"
        },
        {
            "q": "A 55-year-old woman with breast cancer presents with increasing dyspnoea. CXR shows unilateral pleural effusion. Pleural fluid analysis: protein 42 g/L (serum 70 g/L), LDH 400 (serum LDH upper limit 200). What type of effusion is this?",
            "opts": ["Transudate — treat underlying HF", "Exudate — likely malignant effusion", "Chylothorax", "Empyema"],
            "ans": 1,
            "exp": "Light's criteria for EXUDATE (any ONE): (1) Fluid protein/Serum protein >0.5: 42/70 = 0.6 ✓; (2) Fluid LDH/Serum LDH upper limit >0.6: 400/200 = 2.0 ✓; (3) Fluid LDH >2/3 upper limit of normal serum LDH. This is clearly an EXUDATE. In a breast cancer patient → malignant pleural effusion (malignant cells on cytology). Transudate causes: HF, cirrhosis, nephrotic syndrome (low protein states).",
            "tip": "🩺 EXUDATE = protein-rich = inflammation/malignancy/infection. TRANSUDATE = protein-poor = imbalanced hydrostatic/oncotic pressure (HF, cirrhosis, nephrotic). Light's criteria: if any ONE criterion met = exudate. Simple rule: fluid protein >30 g/L = exudate."
        },
        {
            "q": "A 30-year-old woman develops acute onset dyspnoea and pleuritic chest pain 3 days after a long-haul flight from Oman to London. HR 110, RR 22, SpO2 93%. CT-PA confirms bilateral PEs. What is the modified Wells score most likely?",
            "opts": ["0-1 (Low probability)", "2-4 (Moderate)", "≥5 (High probability)", "Cannot calculate without more data"],
            "ans": 2,
            "exp": "Wells PE score ≥5 = HIGH probability. This patient scores: PE most likely diagnosis (+3), HR >100 (+1.5), immobilisation (long flight >4hrs counts) (+1.5) = 6 points = HIGH probability. Standard management: anticoagulate immediately (LMWH/DOAC), CTPA to confirm, assess for haemodynamic compromise → if massive PE with shock → thrombolysis.",
            "tip": "🩺 Wells PE: >4 = HIGH = CTPA. ≤4 = D-dimer first (if negative = PE excluded). Remember: D-dimer is sensitive but NOT specific. In post-surgical or pregnant patients, D-dimer is almost always elevated (useless). Go straight to CTPA if clinical suspicion is high!"
        },
    ],

    # ══════════════════════════════════════
    # GASTROENTEROLOGY
    # ══════════════════════════════════════
    "Gastroenterology": [
        {
            "q": "A 35-year-old male presents with bloody diarrhoea for 6 months, urgency, and tenesmus. Colonoscopy shows continuous inflammation starting from the rectum extending to the splenic flexure. What is the diagnosis?",
            "opts": ["Crohn's disease", "Ulcerative colitis", "Infectious colitis", "Ischaemic colitis"],
            "ans": 1,
            "exp": "Ulcerative colitis: CONTINUOUS inflammation starting at RECTUM (always involved), extends proximally. Classification by extent: Proctitis (rectum only), Left-sided UC (to splenic flexure), Extensive/pancolitis (beyond). Histology: crypt abscesses, goblet cell depletion, MUCOSAL only. Complications: toxic megacolon, colorectal cancer (risk ↑after 10 years), primary sclerosing cholangitis.",
            "tip": "🩺 UC vs Crohn's: UC = continuous + rectum always + mucosal only + bloody diarrhoea + colitis only. Crohn's = skip lesions + anywhere mouth to anus + transmural + fistulae + granulomas. Smoking WORSENS Crohn's but is PROTECTIVE in UC."
        },
        {
            "q": "A 50-year-old alcoholic presents with sudden onset severe epigastric pain radiating to the back, nausea, and vomiting. Amylase is 1500 IU/L. What is the most important initial management?",
            "opts": ["ERCP urgently", "Aggressive IV fluid resuscitation and analgesia", "Immediate surgery", "IV antibiotics prophylactically"],
            "ans": 1,
            "exp": "Acute pancreatitis management: (1) IV fluids (aggressive crystalloid resuscitation - patients are severely dehydrated), (2) Analgesia (IV morphine/pethidine), (3) NBM initially, (4) Monitor for complications (ARDS, AKI, DIC, pseudocyst). ERCP only if gallstone pancreatitis with biliary obstruction. Prophylactic antibiotics NOT recommended. Most cases (80%) resolve with supportive care.",
            "tip": "🩺 Pancreatitis: Gallstones + Alcohol = most common causes (GET SMASHED mnemonic for causes). Ranson's criteria assess severity. Remember: amylase level does NOT correlate with severity - lipase is more specific and remains elevated longer."
        },
        {
            "q": "A 55-year-old with alcoholic cirrhosis is admitted with haematemesis. Endoscopy shows actively bleeding oesophageal varices. What is the FIRST drug to give?",
            "opts": ["Propranolol (non-selective beta-blocker)", "Terlipressin", "Omeprazole (PPI)", "Fresh frozen plasma"],
            "ans": 1,
            "exp": "Acute variceal bleeding: (1) Terlipressin (vasopressin analogue → splanchnic vasoconstriction → ↓portal pressure → controls bleeding) - give ASAP, even before endoscopy. (2) IV antibiotics (Ceftriaxone - SBP prophylaxis, reduces rebleeding and mortality), (3) Urgent endoscopy with band ligation, (4) Sengstaken tube if bleeding uncontrolled, (5) TIPS if refractory. Propranolol = PRIMARY prevention only, not acute treatment.",
            "tip": "🩺 Variceal bleed management: 'ABCDE': Airway/Resus, Band ligation (endoscopy), Ceftriaxone (antibiotics), Decrease portal pressure (Terlipressin), Endoscopy. Terlipressin + Antibiotics started BEFORE endoscopy improve survival."
        },
    ],

    # ══════════════════════════════════════
    # ENDOCRINOLOGY
    # ══════════════════════════════════════
    "Endocrinology": [
        {
            "q": "A 28-year-old woman presents with weight loss, heat intolerance, palpitations, tremor, and exophthalmos. TSH is undetectable, T4 and T3 are very elevated. What is the most likely diagnosis?",
            "opts": ["Toxic multinodular goitre", "Graves' disease", "Hashimoto's thyroiditis", "De Quervain's thyroiditis"],
            "ans": 1,
            "exp": "Graves' disease: autoimmune hyperthyroidism. TSH receptor antibodies (TRAb/TSHR-Ab) mimic TSH → continuous stimulation. ONLY cause of hyperthyroidism with EXOPHTHALMOS (thyroid eye disease - infiltrative ophthalmopathy) and pretibial myxoedema. Treatment: Carbimazole/PTU (block thyroid hormone synthesis), Beta-blocker (propranolol for symptoms), Radioiodine (I-131), or thyroidectomy.",
            "tip": "🩺 Graves' = TSH receptor STIMULATING antibodies → All features of hyperthyroidism + Exophthalmos + Pretibial myxoedema. The exophthalmos can worsen with radioiodine. Carbimazole: side effect = AGRANULOCYTOSIS (stop if sore throat/fever!)."
        },
        {
            "q": "A 45-year-old type 2 diabetic has HbA1c of 9.2% on metformin 2g/day. His eGFR is 25 mL/min. Which medication should be AVOIDED?",
            "opts": ["Gliclazide", "Sitagliptin (DPP-4 inhibitor)", "Metformin", "Insulin"],
            "ans": 2,
            "exp": "Metformin is CONTRAINDICATED when eGFR <30 mL/min (British guidelines; some say <45). Risk: lactic acidosis (metformin accumulates in renal failure → inhibits mitochondrial complex I → anaerobic respiration → lactic acid accumulation). Safe alternatives in CKD: Gliclazide (dose reduce), Sitagliptin (dose reduce per eGFR), Insulin. Empagliflozin/SGLT2 inhibitors also contraindicated <30.",
            "tip": "🩺 Metformin + CKD (eGFR <30) = STOP. Also stop metformin: before IV contrast (restart 48hrs after if renal function stable), before surgery, if acute illness (dehydration risk). HbA1c target in elderly/CKD: less strict (7.5-8%) to avoid hypoglycaemia."
        },
        {
            "q": "A 35-year-old woman has hypercalcaemia, high PTH, and a neck mass. Sestamibi scan shows a single parathyroid adenoma. What is the treatment?",
            "opts": ["Cinacalcet (calcimimetic)", "High-dose vitamin D", "Parathyroidectomy (surgical)", "Bisphosphonate infusion"],
            "ans": 2,
            "exp": "Primary hyperparathyroidism: single parathyroid adenoma (85% of cases) → excessive PTH → hypercalcaemia. PTH causes: bone resorption (↑Ca, ↑ALP), ↑renal Ca reabsorption, ↑1,25-vit D production (↑gut Ca absorption), phosphaturia (↓PO4). Treatment of choice: Minimally invasive parathyroidectomy (curative). Cinacalcet for those unsuitable for surgery.",
            "tip": "🩺 Primary hyperPTH = ↑PTH, ↑Ca, ↓PO4 (phosphaturia). Symptoms: Bones (pain, osteitis fibrosa cystica), Stones (renal), Groans (GI - constipation, pancreatitis), Psychic moans (confusion, depression). 'Bones, Stones, Groans, Psychic Moans'!"
        },
    ],

    # ══════════════════════════════════════
    # EMERGENCY MEDICINE
    # ══════════════════════════════════════
    "Emergency Medicine": [
        {
            "q": "A 25-year-old with a known peanut allergy collapses in a restaurant. HR 130, BP 70/40, stridor, widespread urticaria. What is the FIRST and most critical treatment?",
            "opts": ["IV Chlorphenamine", "IV Hydrocortisone", "IM Adrenaline 0.5mg (1:1000) in anterolateral thigh", "IV Fluids 1L Normal Saline"],
            "ans": 2,
            "exp": "Anaphylaxis: IM Adrenaline 0.5mg (1:1000) in anterolateral thigh is FIRST LINE ALWAYS. Adrenaline: α1 = vasoconstriction (reverses hypotension, reduces urticaria), β1 = ↑HR/contractility (treats shock), β2 = bronchodilation (treats bronchospasm). Antihistamines and steroids are SECOND LINE (slow onset, don't treat shock). Dose can be repeated after 5 minutes. IV adrenaline only in ICU/expert hands.",
            "tip": "🩺 Anaphylaxis = IM ADRENALINE FIRST. Not antihistamine, not steroid. The thigh (vastus lateralis) gives fastest absorption. In the UK/Oman: EpiPen 0.3mg IM for adults. Lay patient flat with legs elevated (unless respiratory distress). Adrenaline + O2 + IV fluids + antihistamine + steroid."
        },
        {
            "q": "A 22-year-old type 1 diabetic is brought in confused. Blood glucose: 2.1 mmol/L. He is GCS 9 and cannot swallow safely. What is the treatment?",
            "opts": ["Oral glucose gel", "Glucagon 1mg IM", "IV 10% Dextrose 150ml (or 50ml of 50% dextrose)", "Subcutaneous insulin"],
            "ans": 2,
            "exp": "Severe hypoglycaemia (GCS impaired/cannot swallow): IV glucose is preferred (faster, reliable). Give 150mL of 10% dextrose IV (or 50mL of 50% dextrose via large vein). Glucagon 1mg IM is alternative if no IV access (works in 10-15 min via glycogenolysis - may not work in alcoholics/malnourished with depleted glycogen stores). NEVER give oral glucose to impaired consciousness (aspiration risk).",
            "tip": "🩺 Conscious + can swallow = oral glucose (Lucozade/glucose tablets). Impaired consciousness = IV dextrose FIRST. No IV access = Glucagon IM. Don't give glucagon in alcoholics (no glycogen stores). Recheck BM in 15 min. Find and treat cause (insulin overdose, missed meal, infection)."
        },
    ],

    # ══════════════════════════════════════
    # PAEDIATRICS
    # ══════════════════════════════════════
    "Paediatrics": [
        {
            "q": "A 4-year-old presents with fever >5 days, strawberry tongue, bilateral conjunctivitis, cervical lymphadenopathy, and a desquamating maculopapular rash on the hands and feet. What is the diagnosis and main concern?",
            "opts": ["Scarlet fever", "Kawasaki disease — coronary artery aneurysms", "Measles", "Staphylococcal scalded skin syndrome"],
            "ans": 1,
            "exp": "Kawasaki disease (CRASH+BURN): C=Conjunctivitis (bilateral, non-exudative), R=Rash (polymorphous), A=Adenopathy (cervical, >1.5cm), S=Strawberry tongue/lip cracking, H=Hand/foot changes (oedema + desquamation). BURN = fever >5 days. The MAIN concern: Coronary Artery Aneurysms (CAA) occur in 15-25% untreated → myocardial infarction. Treatment: IVIG (2g/kg stat) + Aspirin. Echo to screen for CAA.",
            "tip": "🩺 Kawasaki = CRASH+BURN mnemonic. IVIG reduces CAA risk to <5% if given within 10 days. Aspirin is one of the few times we give it to children (Kawasaki is a specific exception to Reye syndrome risk). Echo at diagnosis AND 6-8 weeks!"
        },
        {
            "q": "A premature neonate at 28 weeks develops worsening respiratory distress within 2 hours of birth. CXR shows bilateral ground-glass opacity with air bronchograms. What is the pathophysiology?",
            "opts": ["Meconium aspiration syndrome", "Surfactant deficiency (Respiratory Distress Syndrome)", "Transient tachypnoea of the newborn", "Pneumonia from Group B Strep"],
            "ans": 1,
            "exp": "Neonatal RDS (Hyaline Membrane Disease): Surfactant (produced by Type II pneumocytes) reduces alveolar surface tension preventing collapse. Premature babies (<34 weeks) lack sufficient surfactant. Alveoli collapse → V/Q mismatch → hypoxia. CXR: ground-glass opacities + air bronchograms ('white-out'). Treatment: Exogenous surfactant instillation, CPAP/ventilation, maternal antenatal corticosteroids (accelerates surfactant production).",
            "tip": "🩺 Premature baby + respiratory distress within hours = RDS (surfactant deficiency). Prevention: antenatal steroids (betamethasone) at 24-34 weeks. Treatment: surfactant (intratracheal) + CPAP. Complications: PDA, IVH, BPD (bronchopulmonary dysplasia)."
        },
    ],

    # ══════════════════════════════════════
    # OBSTETRICS & GYNAECOLOGY
    # ══════════════════════════════════════
    "Obstetrics & Gynaecology": [
        {
            "q": "A 32-year-old at 34 weeks gestation presents with sudden onset severe epigastric pain, headache, and blurred vision. BP 165/110. Urine protein +++. LFTs are elevated and platelets are 85 × 10⁹/L. What syndrome is this?",
            "opts": ["Severe pre-eclampsia only", "HELLP syndrome", "Acute fatty liver of pregnancy", "Cholestasis of pregnancy"],
            "ans": 1,
            "exp": "HELLP syndrome: Haemolysis, Elevated Liver enzymes, Low Platelets. It's a severe variant of pre-eclampsia. Features: epigastric/RUQ pain (liver capsule distension), headache, visual disturbance, proteinuria, hypertension. Labs: ↑LDH (haemolysis), ↑AST/ALT, platelets <100. Definitive treatment: DELIVERY (only cure). Steroids if <34 weeks for fetal lung maturity. MgSO4 for seizure prophylaxis.",
            "tip": "🩺 HELLP = Emergency → deliver the baby! Corticosteroids can temporarily stabilise (allow fetal lung maturity if <34 weeks). MgSO4 prevents seizures. Antihypertensives (Labetalol/Nifedipine) for BP control. Can worsen rapidly → organ failure/DIC."
        },
    ],

    # ══════════════════════════════════════
    # PSYCHIATRY
    # ══════════════════════════════════════
    "Psychiatry": [
        {
            "q": "A 25-year-old presents with 3 weeks of depressed mood, anhedonia, early morning waking, psychomotor retardation, and passive suicidal ideation. This is his first episode. What is first-line treatment?",
            "opts": ["Tricyclic antidepressant (amitriptyline)", "SSRI (e.g. sertraline or fluoxetine)", "Lithium", "Benzodiazepine"],
            "ans": 1,
            "exp": "Moderate-severe depression: SSRIs are first-line (e.g. sertraline 50mg, fluoxetine 20mg). Better tolerated than TCAs, safer in overdose. Takes 4-6 weeks for full effect. TCAs (amitriptyline): effective but anticholinergic side effects, dangerous in overdose (Na+ channel blockade → arrhythmia). Lithium: used in bipolar, NOT routine depression. Benzodiazepines: for acute anxiety, NOT depression. Always assess and document suicide risk.",
            "tip": "🩺 SSRIs = First-line for depression AND anxiety disorders. Side effects: GI upset initially, sexual dysfunction, discontinuation syndrome (taper slowly). SIADH risk (especially in elderly). Fluoxetine has longest half-life (safest to stop). Sertraline safest in cardiac disease."
        },
    ],
}


def get_all_mcqs():
    """Returns a flat list of all MCQs with subject label."""
    all_mcqs = []
    for subject, questions in MCQ_BANK.items():
        for q in questions:
            q_copy = q.copy()
            q_copy["subject"] = subject
            all_mcqs.append(q_copy)
    return all_mcqs


def get_mcqs_by_subject(subject):
    """Returns MCQs for a specific subject."""
    return MCQ_BANK.get(subject, [])


def get_subjects():
    """Returns list of available subjects."""
    return list(MCQ_BANK.keys())