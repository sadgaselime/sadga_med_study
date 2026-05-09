"""
resources_page.py — MedStudy Oman 🩺
Phase 3: Resources Hub — extracted from app.py into its own clean module.
Tabs: Textbooks · Question Banks · Apps · Websites · Videos · Oman Resources
+ Save to Vault functionality
"""

import streamlit as st


def resources_page(theme: dict):
    """Render the full Resources Hub page."""

    st.markdown(f"""
    <div style="display:flex;align-items:center;gap:14px;margin-bottom:0.5rem;">
        <div style="width:46px;height:46px;border-radius:14px;background:{theme['gradient']};
             display:flex;align-items:center;justify-content:center;font-size:1.5rem;">📖</div>
        <div>
            <div style="font-family:'Syne',sans-serif;font-size:1.7rem;font-weight:800;
                 color:{theme['text']};">Resources Hub</div>
            <div style="font-size:0.82rem;color:{theme['subtext']};">
                 Curated · WFME · WDOMS · SQU-COM · USMLE · OMSB aligned</div>
        </div>
    </div>
    """, unsafe_allow_html=True)

    res_tabs = st.tabs([
        "📚 Textbooks",
        "📝 Question Banks",
        "📱 Apps",
        "🌐 Websites",
        "🎥 Videos",
        "🇴🇲 Oman Context",
    ])

    # ── helper: save-to-vault button ─────────────────────────────────────────
    def vault_btn(key: str, title: str, icon: str = "📌", rtype: str = "Resource"):
        if st.button(f"🏦 Save", key=f"vault_{key}", help="Save to My Vault"):
            if "vault_items" not in st.session_state:
                st.session_state.vault_items = []
            item = {"title": title, "icon": icon, "type": rtype}
            if item not in st.session_state.vault_items:
                st.session_state.vault_items.append(item)
                st.toast(f"✅ Saved '{title}' to vault!", icon="🏦")

    # ────────────────────────────────────────────────────────────────────────
    # TAB 0 — TEXTBOOKS
    # ────────────────────────────────────────────────────────────────────────
    with res_tabs[0]:
        st.markdown(f"<h3 style='color:{theme['text']}'>📚 Essential Medical Textbooks</h3>",
                    unsafe_allow_html=True)

        BOOKS = {
            "🔬 Preclinical (Years 1–2)": [
                ("Gray's Anatomy", "40th Ed", "Drake, Vogl, Mitchell",
                 "Gold standard anatomy text; comprehensive regional and systemic anatomy", "📗"),
                ("Guyton & Hall Medical Physiology", "14th Ed", "Hall & Hall",
                 "The definitive physiology textbook worldwide", "📗"),
                ("Robbins & Cotran Pathologic Basis", "10th Ed", "Kumar, Abbas, Aster",
                 "The Bible of Pathology; essential for USMLE and OMSB", "📗"),
                ("Harper's Illustrated Biochemistry", "32nd Ed", "Rodwell et al.",
                 "Comprehensive biochemistry; clinical relevance throughout", "📗"),
                ("Lippincott's Pharmacology", "8th Ed", "Whalen et al.",
                 "Visual summary format; USMLE Step 1 favourite", "📗"),
                ("Murray's Medical Microbiology", "9th Ed", "Rosenthal, Pfaller",
                 "Standard microbiology reference", "📗"),
                ("Langman's Medical Embryology", "14th Ed", "Sadler",
                 "Standard embryology text", "📗"),
                ("First Aid USMLE Step 1", "2024 Ed", "Le, Bhushan",
                 "Must-have USMLE Step 1 review book; used globally", "📕"),
            ],
            "🏥 Clinical (Years 3–6)": [
                ("Harrison's Principles of Internal Medicine", "21st Ed", "Longo et al.",
                 "The definitive internal medicine textbook worldwide", "📘"),
                ("Davidson's Principles & Practice", "24th Ed", "Ralston et al.",
                 "Widely used in UK/Commonwealth/Oman; concise clinical medicine", "📘"),
                ("Oxford Handbook of Clinical Medicine", "10th Ed", "Longmore et al.",
                 "Essential pocket reference for clinical years", "📘"),
                ("Bailey & Love's Surgery", "28th Ed", "Williams et al.",
                 "The surgery bible for Commonwealth countries", "📘"),
                ("Williams Obstetrics", "26th Ed", "Cunningham et al.",
                 "Gold standard obstetrics text", "📘"),
                ("Nelson Textbook of Pediatrics", "21st Ed", "Kliegman et al.",
                 "The definitive paediatrics reference", "📘"),
                ("First Aid USMLE Step 2 CK", "12th Ed", "Le, Bhushan",
                 "USMLE Step 2 Clinical Knowledge review", "📕"),
            ],
            "🇴🇲 Oman & Middle East Specific": [
                ("OMSB Part 1 & 2 Past Papers", "Various", "Oman Medical Specialty Board",
                 "Essential for OMSB board exams", "📙"),
                ("MOH Oman Clinical Guidelines", "Latest", "Ministry of Health Oman",
                 "MOH Oman clinical guidelines for primary care", "📙"),
                ("SQU Medical Journal (SQUMJ)", "Ongoing", "Sultan Qaboos University",
                 "Peer-reviewed journal with Oman-specific research", "📙"),
            ],
        }

        for category, books in BOOKS.items():
            with st.expander(category, expanded=True):
                for title, edition, authors, desc, icon in books:
                    c1, c2 = st.columns([5, 1])
                    with c1:
                        st.markdown(f"""
                        <div class="resource-card" style="margin-bottom:0.6rem;">
                            <div class="rc-header">
                                <span style="font-size:1.3rem;">{icon}</span>
                                <div>
                                    <div style="font-weight:700;color:{theme['text']};
                                         font-size:0.9rem;">{title}</div>
                                    <div style="font-size:0.73rem;color:{theme['subtext']};">
                                         ✍️ {authors} ·
                                         <span style="background:{theme['primary']}20;
                                               color:{theme['primary']};border-radius:6px;
                                               padding:1px 7px;">{edition}</span>
                                    </div>
                                </div>
                            </div>
                            <div class="rc-body">
                                <div style="font-size:0.8rem;color:{theme['subtext']};
                                     font-style:italic;">{desc}</div>
                            </div>
                        </div>
                        """, unsafe_allow_html=True)
                    with c2:
                        vault_btn(f"book_{title}", title, icon, "Textbook")

    # ────────────────────────────────────────────────────────────────────────
    # TAB 1 — QUESTION BANKS
    # ────────────────────────────────────────────────────────────────────────
    with res_tabs[1]:
        st.markdown(f"<h3 style='color:{theme['text']}'>📝 Question Banks & Exam Prep</h3>",
                    unsafe_allow_html=True)

        QBANKS = [
            ("🥇 UWorld",          "uworld.com",          "#ef4444", "USMLE",        "Paid",
             "Gold standard question bank. 3,000+ Step 1 questions with detailed explanations."),
            ("🥈 AMBOSS",           "amboss.com",           "#8b5cf6", "USMLE/Clinical","Paid",
             "Comprehensive medical knowledge platform with 5,000+ USMLE questions + library."),
            ("🎯 Kaplan Qbank",     "kaptest.com",          "#f59e0b", "USMLE",        "Paid",
             "Kaplan USMLE question bank with test-taking strategies. 2,000+ per step."),
            ("📚 Pastest",          "pastest.co.uk",        "#0891b2", "MRCP/PLAB",    "Paid",
             "Leading UK question bank for MRCP Part 1 & 2, PLAB."),
            ("🔬 OnExamination",    "onexamination.com",    "#16a34a", "MRCP/MRCS",    "Paid",
             "BMJ Learning question bank for MRCP, MRCOG, MRCS, MRCPCH."),
            ("🆓 Osmosis Q&A",      "osmosis.org",          "#10b981", "Pre-clinical", "Free+",
             "Free and paid medical question practice with spaced repetition."),
            ("🧪 Pathoma",          "pathoma.com",          "#ec4899", "Pathology",    "Paid",
             "Dr. Sattar's pathology video course with accompanying questions."),
            ("📖 Anki",             "apps.ankiweb.net",     "#0ea5e9", "All subjects", "Free",
             "Spaced repetition flashcards. Use Zanki, Lightyear, Brosencephalon decks."),
            ("🇴🇲 OMSB Resources",  "omsb.gov.om",          "#16a34a", "OMSB Boards",  "Free",
             "Official OMSB exam guidelines, syllabi, and resources."),
        ]

        cols = st.columns(2)
        for i, (name, url, color, qtype, cost, desc) in enumerate(QBANKS):
            with cols[i % 2]:
                c1, c2 = st.columns([4, 1])
                with c1:
                    free_color = "#10b981" if "Free" in cost else "#f59e0b"
                    st.markdown(f"""
                    <div style="background:{theme['card_bg']};border:2px solid {color}30;
                         border-top:4px solid {color};border-radius:16px;
                         padding:1.1rem;margin-bottom:0.9rem;">
                        <div style="font-weight:700;color:{theme['text']};font-size:0.9rem;">
                             {name}</div>
                        <div style="display:flex;gap:6px;margin:0.4rem 0;">
                            <span style="background:{color}20;color:{color};border-radius:6px;
                                  padding:2px 8px;font-size:0.72rem;">{qtype}</span>
                            <span style="background:{free_color}20;color:{free_color};
                                  border-radius:6px;padding:2px 8px;font-size:0.72rem;">{cost}</span>
                        </div>
                        <div style="font-size:0.79rem;color:{theme['subtext']};line-height:1.5;">
                             {desc}</div>
                        <div style="color:{color};font-size:0.73rem;margin-top:0.3rem;">
                             🌐 {url}</div>
                    </div>
                    """, unsafe_allow_html=True)
                with c2:
                    vault_btn(f"qb_{name}", name, "📝", "Question Bank")

    # ────────────────────────────────────────────────────────────────────────
    # TAB 2 — APPS
    # ────────────────────────────────────────────────────────────────────────
    with res_tabs[2]:
        st.markdown(f"<h3 style='color:{theme['text']}'>📱 Essential Medical Apps</h3>",
                    unsafe_allow_html=True)

        APPS = {
            "📖 Study & Learning": [
                ("Anki",       "iOS/Android", "Free",     "#0ea5e9",
                 "Spaced repetition. Best study tool. Use Zanki/Lightyear decks."),
                ("Osmosis",    "iOS/Android", "Free+",    "#10b981",
                 "Visual medical education. Excellent for visual learners."),
                ("Sketchy",    "iOS/Android", "Paid",     "#f97316",
                 "Story mnemonics for micro/pharmacology/pathology."),
                ("Amboss",     "iOS/Android", "Free+",    "#8b5cf6",
                 "Medical knowledge library + question bank."),
                ("Lecturio",   "iOS/Android", "Paid",     "#ec4899",
                 "Full medical curriculum video lectures."),
            ],
            "🏥 Clinical Reference": [
                ("UpToDate",   "iOS/Android", "Subscription", "#dc2626",
                 "#1 clinical decision support. Available at SQUH."),
                ("Medscape",   "iOS/Android", "Free",     "#0891b2",
                 "Drug reference, disease monographs, medical calculators."),
                ("MDCalc",     "iOS/Android", "Free",     "#16a34a",
                 "700+ validated medical calculators. CURB-65, GRACE, Wells…"),
                ("Epocrates",  "iOS/Android", "Free+",    "#f59e0b",
                 "Drug reference and interactions."),
            ],
            "🔬 Specialty Apps": [
                ("Radiopaedia","iOS/Android", "Free+",    "#64748b",
                 "Radiology cases and reference articles."),
                ("ECG Guide",  "iOS/Android", "Free",     "#ef4444",
                 "Comprehensive ECG learning with interactive examples."),
                ("Visible Body","iOS/Android","Paid",     "#ef4444",
                 "3D interactive anatomy atlas."),
            ],
        }

        for cat, apps in APPS.items():
            st.markdown(f"#### {cat}")
            cols = st.columns(3)
            for i, (name, platform, cost, color, desc) in enumerate(apps):
                with cols[i % 3]:
                    c1, c2 = st.columns([3, 1])
                    with c1:
                        st.markdown(f"""
                        <div style="background:{theme['card_bg']};border:1px solid {color}40;
                             border-top:3px solid {color};border-radius:12px;
                             padding:0.9rem;margin-bottom:0.7rem;">
                            <div style="font-weight:700;color:{theme['text']};font-size:0.88rem;">
                                 📱 {name}</div>
                            <div style="font-size:0.73rem;color:{theme['subtext']};margin:0.2rem 0;">
                                 {platform} ·
                                 <span style="color:{'#10b981' if 'Free' in cost else '#f59e0b'}">
                                 {cost}</span></div>
                            <div style="font-size:0.77rem;color:{theme['subtext']};line-height:1.4;">
                                 {desc}</div>
                        </div>
                        """, unsafe_allow_html=True)
                    with c2:
                        vault_btn(f"app_{name}", name, "📱", "App")

    # ────────────────────────────────────────────────────────────────────────
    # TAB 3 — WEBSITES
    # ────────────────────────────────────────────────────────────────────────
    with res_tabs[3]:
        st.markdown(f"<h3 style='color:{theme['text']}'>🌐 Essential Medical Websites</h3>",
                    unsafe_allow_html=True)

        SITES = {
            "📚 Learning Platforms": [
                ("Khan Academy Medicine", "khanacademy.org", "Free",
                 "Free medical education covering MCAT and basic science."),
                ("OnlineMedEd",          "onlinemeded.org",  "Free+",
                 "Clinical medicine videos. Popular for Step 2 CK prep."),
                ("Geeky Medics",         "geekymedics.com",  "Free",
                 "OSCE guides, clinical examination tutorials, mnemonics."),
                ("TeachMe Anatomy",      "teachmeanatomy.info","Free",
                 "Detailed anatomy articles with illustrations."),
            ],
            "🔎 Evidence-Based Medicine": [
                ("PubMed",          "pubmed.ncbi.nlm.nih.gov","Free",
                 "30M+ biomedical citations. Primary medical literature."),
                ("Cochrane Library", "cochranelibrary.com",   "Free",
                 "Systematic reviews and meta-analyses. Gold standard EBM."),
                ("NICE Guidelines",  "nice.org.uk/guidance",  "Free",
                 "UK National Institute for Health & Care Excellence."),
                ("WHO Guidelines",   "who.int/publications",  "Free",
                 "World Health Organization clinical guidelines."),
            ],
            "🩺 Radiology": [
                ("Radiopaedia",         "radiopaedia.org",    "Free+",
                 "Best radiology learning. Thousands of teaching cases."),
                ("The Radiology Asst.", "radiologyassistant.nl","Free",
                 "Radiology teaching articles with cases."),
            ],
        }

        for cat, sites in SITES.items():
            st.markdown(f"#### {cat}")
            for name, url, cost, desc in sites:
                c1, c2 = st.columns([5, 1])
                with c1:
                    st.markdown(f"""
                    <div style="background:{theme['card_bg']};border:1px solid {theme['card_border']};
                         border-radius:10px;padding:0.7rem 1rem;margin-bottom:0.35rem;">
                        <b style="color:{theme['text']};font-size:0.88rem;">🌐 {name}</b>
                        <span style="color:{'#10b981' if 'Free' in cost else '#f59e0b'};
                              font-size:0.73rem;margin-left:7px;">[{cost}]</span>
                        <div style="color:{theme['subtext']};font-size:0.77rem;margin-top:0.15rem;">
                             {desc}</div>
                        <div style="color:{theme['primary']};font-size:0.72rem;margin-top:0.1rem;">
                             🔗 {url}</div>
                    </div>
                    """, unsafe_allow_html=True)
                with c2:
                    vault_btn(f"site_{name}", name, "🌐", "Website")

    # ────────────────────────────────────────────────────────────────────────
    # TAB 4 — VIDEOS
    # ────────────────────────────────────────────────────────────────────────
    with res_tabs[4]:
        st.markdown(f"<h3 style='color:{theme['text']}'>🎥 Video Learning Channels</h3>",
                    unsafe_allow_html=True)

        VIDS = [
            ("🩺 Armando Hasudungan", "YouTube", "Free", "#ef4444",
             "Hand-drawn pathophysiology and pharmacology. Excellent for visual learners."),
            ("🧬 Dr. Najeeb Lectures", "YouTube/Web", "Free+", "#8b5cf6",
             "Longest medical lecture series. Detailed basic sciences."),
            ("🔬 Pathoma",            "pathoma.com", "Paid", "#ec4899",
             "The best pathology video course for USMLE Step 1."),
            ("📊 Boards & Beyond",    "boardsbeyond.com", "Paid", "#0891b2",
             "Dr. Jason Ryan's USMLE Step 1 videos."),
            ("🎓 OnlineMedEd",        "onlinemeded.org", "Free+", "#16a34a",
             "Outstanding for Step 2 CK and clinical rotations."),
            ("💊 Sketchy",            "sketchy.com", "Paid", "#f97316",
             "Story-based visual learning for micro, pharmacology, pathology."),
            ("⚡ Speed Pharmacology", "YouTube", "Free", "#f59e0b",
             "Concise pharmacology videos. Great for quick drug class revision."),
            ("🧠 Dirty Medicine",     "YouTube", "Free", "#dc2626",
             "High-yield USMLE Step 1 review videos."),
            ("🔎 Geeky Medics",       "YouTube", "Free", "#0d9488",
             "Clinical examination guides, OSCE videos."),
        ]

        cols = st.columns(2)
        for i, (name, platform, cost, color, desc) in enumerate(VIDS):
            with cols[i % 2]:
                c1, c2 = st.columns([4, 1])
                with c1:
                    st.markdown(f"""
                    <div style="background:{theme['card_bg']};border:1px solid {color}35;
                         border-left:4px solid {color};border-radius:12px;
                         padding:0.9rem 1rem;margin-bottom:0.7rem;">
                        <div style="font-weight:700;color:{theme['text']};font-size:0.88rem;">
                             🎥 {name}</div>
                        <div style="font-size:0.73rem;color:{theme['subtext']};margin:0.2rem 0;">
                             {platform} ·
                             <span style="color:{'#10b981' if 'Free' in cost else '#f59e0b'}">
                             {cost}</span></div>
                        <div style="font-size:0.79rem;color:{theme['subtext']};line-height:1.4;">
                             {desc}</div>
                    </div>
                    """, unsafe_allow_html=True)
                with c2:
                    vault_btn(f"vid_{name}", name, "🎥", "Video Channel")

    # ────────────────────────────────────────────────────────────────────────
    # TAB 5 — OMAN CONTEXT
    # ────────────────────────────────────────────────────────────────────────
    with res_tabs[5]:
        st.markdown(f"<h3 style='color:{theme['text']}'>🇴🇲 Oman Medical Context</h3>",
                    unsafe_allow_html=True)

        # Universities
        st.markdown("#### 🎓 Medical Universities in Oman")
        UNIS = [
            ("SQU College of Medicine & Health Sciences",
             "squ.edu.om", "Muscat",
             "Premier medical school, est. 1986. 6-year MBBS. WFME accredited.", "#16a34a"),
            ("Oman Medical College",
             "omc.edu.om", "Muscat & Sohar",
             "Private; MD in collaboration with West Virginia University School of Medicine.", "#0891b2"),
            ("Sohar University — Faculty of Medicine",
             "soharuni.edu.om", "Sohar",
             "Growing clinical network in Northern Oman.", "#8b5cf6"),
        ]
        for uni, url, city, desc, color in UNIS:
            st.markdown(f"""
            <div style="background:{theme['card_bg']};border:1px solid {color}40;
                 border-left:4px solid {color};border-radius:12px;
                 padding:1rem 1.2rem;margin-bottom:0.6rem;">
                <b style="color:{theme['text']};font-size:0.9rem;">🏥 {uni}</b>
                <div style="color:{color};font-size:0.77rem;margin:0.15rem 0;">
                     📍 {city} · 🌐 {url}</div>
                <div style="color:{theme['subtext']};font-size:0.79rem;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)

        # OMSB
        st.markdown("---")
        st.markdown("#### 🏛️ OMSB Board Exams")
        st.markdown(f"""
        <div style="background:{theme['card_bg']};border:2px solid {theme['primary']}40;
             border-radius:16px;padding:1.4rem;">
            <div style="font-weight:700;color:{theme['text']};margin-bottom:0.7rem;">
                 Oman Medical Specialty Board · omsb.gov.om</div>
            <div style="font-size:0.83rem;color:{theme['subtext']};line-height:2;">
                📋 <b>Part 1:</b> Basic sciences + clinical (after internship)<br>
                📋 <b>Part 2:</b> Clinical specialty exam<br>
                📋 <b>Fellowships:</b> 20+ specialties including IM, Surgery, Paeds, O&G<br>
                📋 <b>Recognition:</b> Equivalent to MRCP/MRCS Part 1 for comparison purposes<br>
                📋 <b>Best Prep:</b> Davidson's + Kumar & Clark + Pastest/OnExamination
            </div>
        </div>
        """, unsafe_allow_html=True)

        # Health stats
        st.markdown("---")
        st.markdown("#### 📊 Oman Health Statistics")
        s_cols = st.columns(4)
        om_stats = [
            ("4.97M", "Population (2023)", "#0891b2"),
            ("77.1 yrs", "Life Expectancy", "#16a34a"),
            ("2.8", "Doctors / 1,000", "#8b5cf6"),
            ("1.9", "Hospital Beds / 1,000", "#ef4444"),
        ]
        for col, (val, label, color) in zip(s_cols, om_stats):
            with col:
                st.markdown(f"""
                <div class="stat-card" style="border-top:3px solid {color};">
                    <div style="font-family:'Syne',sans-serif;font-size:1.6rem;
                         font-weight:800;color:{color};">{val}</div>
                    <div style="font-size:0.75rem;color:{theme['subtext']};">{label}</div>
                </div>
                """, unsafe_allow_html=True)

        # Priority conditions
        st.markdown("---")
        st.markdown("#### 🌡️ Priority Conditions in Oman")
        CONDITIONS = [
            ("Diabetes Mellitus Type 2", "~20% adult prevalence", "Very High", "#ef4444"),
            ("Hypertension",             "~30% adult prevalence", "Very High", "#ef4444"),
            ("Ischaemic Heart Disease",  "Leading cause of death","Very High", "#dc2626"),
            ("Sickle Cell / Thalassaemia","Inherited; common in Oman","High",  "#f97316"),
            ("Brucellosis",              "Camel/goat dairy contact","Moderate","#f59e0b"),
            ("Heat-related Illness",     "Extreme summer temps",   "High (seasonal)","#ef4444"),
            ("Dengue Fever",             "Dhofar monsoon season",  "Moderate","#f59e0b"),
            ("Consanguinity disorders",  "Autosomal recessive↑",   "High",    "#8b5cf6"),
        ]
        for cond, detail, priority, color in CONDITIONS:
            st.markdown(f"""
            <div style="background:{theme['card_bg']};border:1px solid {color}30;
                 border-radius:8px;padding:0.5rem 1rem;margin-bottom:0.25rem;
                 display:flex;justify-content:space-between;align-items:center;">
                <div>
                    <b style="color:{theme['text']};font-size:0.84rem;">{cond}</b>
                    <div style="font-size:0.73rem;color:{theme['subtext']};">{detail}</div>
                </div>
                <span style="background:{color}20;color:{color};border-radius:6px;
                      padding:2px 9px;font-size:0.71rem;white-space:nowrap;">{priority}</span>
            </div>
            """, unsafe_allow_html=True)