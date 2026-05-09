"""
lab_game.py — Lab Values Speed Game ⚗️
"""

import streamlit as st
import random
import time

LAB_VALUES = {
    "Sodium (Na+)": {"range": "135-145", "unit": "mEq/L", "category": "Electrolytes"},
    "Potassium (K+)": {"range": "3.5-5.0", "unit": "mEq/L", "category": "Electrolytes"},
    "Chloride (Cl-)": {"range": "95-105", "unit": "mEq/L", "category": "Electrolytes"},
    "Calcium (Ca2+)": {"range": "8.5-10.5", "unit": "mg/dL", "category": "Electrolytes"},
    "ALT": {"range": "7-56", "unit": "U/L", "category": "LFT"},
    "AST": {"range": "10-40", "unit": "U/L", "category": "LFT"},
    "Alkaline Phosphatase": {"range": "44-147", "unit": "U/L", "category": "LFT"},
    "Total Bilirubin": {"range": "0.3-1.2", "unit": "mg/dL", "category": "LFT"},
    "Creatinine": {"range": "0.6-1.2", "unit": "mg/dL", "category": "RFT"},
    "BUN": {"range": "7-20", "unit": "mg/dL", "category": "RFT"},
    "WBC": {"range": "4.5-11.0", "unit": "×10³/μL", "category": "CBC"},
    "Hemoglobin (M)": {"range": "13.5-17.5", "unit": "g/dL", "category": "CBC"},
    "Hemoglobin (F)": {"range": "12.0-15.5", "unit": "g/dL", "category": "CBC"},
    "Platelets": {"range": "150-400", "unit": "×10³/μL", "category": "CBC"},
    "Fasting Glucose": {"range": "70-100", "unit": "mg/dL", "category": "Glucose"},
    "HbA1c": {"range": "4.0-5.6", "unit": "%", "category": "Glucose"},
    "pH": {"range": "7.35-7.45", "unit": "", "category": "ABG"},
    "PaCO2": {"range": "35-45", "unit": "mmHg", "category": "ABG"},
    "PaO2": {"range": "80-100", "unit": "mmHg", "category": "ABG"},
}

def lab_game_page(theme):
    st.markdown(f"<h2 style='color: {theme['text']}'>⚗️ Lab Values Speed Game</h2>", unsafe_allow_html=True)
    st.markdown("Test your knowledge! 2-minute challenge!")
    
    if "game_active" not in st.session_state:
        st.session_state.game_active = False
        st.session_state.game_score = 0
        st.session_state.game_total = 0
    
    col1, col2 = st.columns(2)
    
    with col1:
        category = st.selectbox("Category:", ["All", "Electrolytes", "LFT", "RFT", "CBC", "Glucose", "ABG"])
    
    with col2:
        if not st.session_state.game_active:
            if st.button("🎮 Start Game", type="primary", use_container_width=True):
                st.session_state.game_active = True
                st.session_state.game_score = 0
                st.session_state.game_total = 0
                st.session_state.game_start = time.time()
                labs = list(LAB_VALUES.keys()) if category == "All" else [k for k,v in LAB_VALUES.items() if v["category"] == category]
                st.session_state.current_lab = random.choice(labs)
                st.rerun()
        else:
            if st.button("⏹️ Stop", use_container_width=True):
                st.session_state.game_active = False
                st.rerun()
    
    if st.session_state.game_active:
        elapsed = int(time.time() - st.session_state.game_start)
        remaining = max(0, 120 - elapsed)
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("⏱️ Time", f"{remaining//60:02d}:{remaining%60:02d}")
        with col2:
            st.metric("✅ Score", st.session_state.game_score)
        with col3:
            st.metric("📝 Total", st.session_state.game_total)
        
        if remaining == 0:
            st.session_state.game_active = False
            st.success(f"🎉 Game Over! Score: {st.session_state.game_score}/{st.session_state.game_total}")
            st.balloons()
            st.rerun()
        
        lab = st.session_state.current_lab
        lab_data = LAB_VALUES[lab]
        
        st.markdown("---")
        st.markdown(f"### 🔬 {lab}")
        st.markdown(f"**Category:** {lab_data['category']} | **Unit:** {lab_data['unit']}")
        
        user_answer = st.text_input("Normal range:", placeholder="e.g., 135-145", key=f"ans_{st.session_state.game_total}")
        
        col1, col2 = st.columns(2)
        with col1:
            if st.button("✅ Submit", type="primary", use_container_width=True):
                if user_answer:
                    if user_answer.strip() == lab_data['range']:
                        st.session_state.game_score += 1
                        st.success("✅ Correct!")
                    else:
                        st.error(f"❌ Answer: {lab_data['range']}")
                    st.session_state.game_total += 1
                    labs = list(LAB_VALUES.keys()) if category == "All" else [k for k,v in LAB_VALUES.items() if v["category"] == category]
                    st.session_state.current_lab = random.choice(labs)
                    time.sleep(0.5)
                    st.rerun()
        
        with col2:
            if st.button("⏭️ Skip", use_container_width=True):
                st.warning(f"Answer: {lab_data['range']}")
                st.session_state.game_total += 1
                labs = list(LAB_VALUES.keys()) if category == "All" else [k for k,v in LAB_VALUES.items() if v["category"] == category]
                st.session_state.current_lab = random.choice(labs)
                time.sleep(0.5)
                st.rerun()
        
        time.sleep(1)
        st.rerun()
    
    else:
        st.markdown("### 📊 Lab Values Reference")
        for lab_name, lab_data in LAB_VALUES.items():
            st.markdown(f"**{lab_name}:** `{lab_data['range']} {lab_data['unit']}` - *{lab_data['category']}*")