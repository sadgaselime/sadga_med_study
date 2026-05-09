"""
mnemonics_page.py — Medical Mnemonics Library 💡
Memory aids for medical students
"""

import streamlit as st

MNEMONICS_LIBRARY = {
    "Cranial Nerves": {
        "mnemonic": "On Old Olympus Towering Top, A Finn And German Viewed Some Hops",
        "breakdown": [
            "O - Olfactory (I)",
            "O - Optic (II)",
            "O - Oculomotor (III)",
            "T - Trochlear (IV)",
            "T - Trigeminal (V)",
            "A - Abducens (VI)",
            "F - Facial (VII)",
            "A - Auditory/Vestibulocochlear (VIII)",
            "G - Glossopharyngeal (IX)",
            "V - Vagus (X)",
            "S - Spinal Accessory (XI)",
            "H - Hypoglossal (XII)"
        ],
        "category": "Anatomy"
    },
    "Carpal Bones": {
        "mnemonic": "Some Lovers Try Positions That They Can't Handle",
        "breakdown": [
            "S - Scaphoid",
            "L - Lunate",
            "T - Triquetrum",
            "P - Pisiform",
            "T - Trapezium",
            "T - Trapezoid",
            "C - Capitate",
            "H - Hamate"
        ],
        "category": "Anatomy"
    },
    "Heart Murmurs Timing": {
        "mnemonic": "PASS - Pulmonic, Aortic, Systolic | PAID - Pulmonic, Aortic, Diastolic",
        "breakdown": [
            "Systolic: Pulmonic stenosis, Aortic stenosis, Systolic regurg (MR, TR)",
            "Diastolic: Pulmonic regurg, Aortic regurg, Diastolic stenosis (MS, TS)"
        ],
        "category": "Cardiology"
    },
    "ECG Lead Placement": {
        "mnemonic": "Ride Your Green Bike - All Leads Face Toward London",
        "breakdown": [
            "R - Right arm (white)",
            "Y - Left arm (Yellow)",
            "G - Right leg (Green)",
            "B - Left leg (Black)",
        ],
        "category": "Cardiology"
    },
    "Hypercalcemia Causes": {
        "mnemonic": "CHIMPANZEES",
        "breakdown": [
            "C - Calcium supplementation",
            "H - Hyperparathyroidism/Hyperthyroidism",
            "I - Iatrogenic/Immobilization",
            "M - Multiple myeloma/Milk-alkali syndrome",
            "P - Paget's disease",
            "A - Addison's disease",
            "N - Neoplasm",
            "Z - Zollinger-Ellison syndrome",
            "E - Excess vitamin D",
            "E - Excess vitamin A",
            "S - Sarcoidosis"
        ],
        "category": "Medicine"
    },
    "Diabetes Medications": {
        "mnemonic": "Diabetes MEDS",
        "breakdown": [
            "M - Metformin",
            "E - Extra insulin (exogenous)",
            "D - DPP-4 inhibitors",
            "S - Sulfonylureas, SGLT2 inhibitors"
        ],
        "category": "Pharmacology"
    },
    "Signs of Shock": {
        "mnemonic": "SHOCK",
        "breakdown": [
            "S - Skin (cold, clammy)",
            "H - Hypotension",
            "O - Oliguria (decreased urine)",
            "C - Confusion",
            "K - Kalemia (electrolyte imbalance)"
        ],
        "category": "Emergency Medicine"
    },
    "Causes of Clubbing": {
        "mnemonic": "CLUBBING",
        "breakdown": [
            "C - Cyanotic heart disease",
            "L - Lung cancer",
            "U - Ulcerative colitis",
            "B - Bronchiectasis",
            "B - Bacterial endocarditis",
            "I - Interstitial lung disease",
            "N - No reason (idiopathic)",
            "G - GI (cirrhosis, IBD)"
        ],
        "category": "Medicine"
    }
}

def mnemonics_page(theme):
    st.markdown(f"<h2 style='color: {theme['text']}'>💡 Medical Mnemonics</h2>", unsafe_allow_html=True)
    st.markdown("Memory aids to help you remember complex medical concepts")
    
    # Category filter
    categories = ["All"] + sorted(set(m['category'] for m in MNEMONICS_LIBRARY.values()))
    selected_category = st.selectbox("📚 Filter by Category:", categories)
    
    # Search
    search = st.text_input("🔍 Search mnemonics...", placeholder="e.g., cranial nerves")
    
    # Display mnemonics
    filtered_mnemonics = {}
    for name, data in MNEMONICS_LIBRARY.items():
        if selected_category != "All" and data['category'] != selected_category:
            continue
        if search and search.lower() not in name.lower() and search.lower() not in data['mnemonic'].lower():
            continue
        filtered_mnemonics[name] = data
    
    if not filtered_mnemonics:
        st.info("No mnemonics found. Try different filters!")
    
    for name, data in filtered_mnemonics.items():
        with st.expander(f"💡 {name} ({data['category']})"):
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, {theme['primary']}20, {theme['primary']}05);
                border-left: 4px solid {theme['primary']};
                padding: 1.5rem;
                border-radius: 12px;
                margin-bottom: 1rem;
            ">
                <div style="font-size: 1.3rem; font-weight: 700; color: {theme['text']}; margin-bottom: 1rem;">
                    "{data['mnemonic']}"
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("**Breakdown:**")
            for item in data['breakdown']:
                st.markdown(f"- {item}")
            
            col1, col2 = st.columns(2)
            with col1:
                if st.button(f"🔖 Bookmark", key=f"bm_{name}"):
                    st.success(f"Bookmarked: {name}")
            with col2:
                if st.button(f"✅ Mastered", key=f"master_{name}"):
                    st.success(f"Marked as mastered!")
    
    # Add your own section
    st.markdown("---")
    st.markdown("### ➕ Add Your Own Mnemonic")
    
    col1, col2 = st.columns(2)
    with col1:
        custom_name = st.text_input("Topic:", placeholder="e.g., Bone Types")
    with col2:
        custom_category = st.selectbox("Category:", ["Anatomy", "Cardiology", "Pharmacology", "Medicine", "Other"])
    
    custom_mnemonic = st.text_input("Mnemonic phrase:", placeholder="Enter your mnemonic...")
    custom_breakdown = st.text_area("Breakdown (one per line):", placeholder="A - First item\nB - Second item")
    
    if st.button("💾 Save Mnemonic", type="primary"):
        if custom_name and custom_mnemonic:
            st.success(f"✅ Saved: {custom_name}")
            st.balloons()
        else:
            st.error("Please fill in all fields")