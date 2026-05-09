"""
osce_timer.py — OSCE Clinical Timer 🩺
"""

import streamlit as st
import time

OSCE_STATIONS = {
    "CVS Examination": {
        "duration": 8,
        "checklist": [
            "Introduce yourself and wash hands",
            "Position patient at 45 degrees",
            "Inspect for JVP, chest deformities",
            "Palpate apex beat and heaves",
            "Auscultate heart sounds (4 areas)",
            "Check for radiation and murmurs",
            "Examine peripheral pulses",
            "Thank patient and summarize"
        ]
    },
    "Respiratory Examination": {
        "duration": 8,
        "checklist": [
            "Introduce and wash hands",
            "Inspect chest shape and breathing",
            "Palpate chest expansion",
            "Percuss all zones",
            "Auscultate all zones",
            "Check vocal resonance",
            "Thank patient"
        ]
    },
    "Abdominal Examination": {
        "duration": 8,
        "checklist": [
            "Introduce and wash hands",
            "Inspect abdomen",
            "Palpate (light then deep)",
            "Palpate organs (liver, spleen, kidneys)",
            "Percuss abdomen",
            "Auscultate bowel sounds",
            "Thank patient"
        ]
    },
    "History Taking": {
        "duration": 10,
        "checklist": [
            "Introduce yourself",
            "Chief complaint",
            "History of presenting illness",
            "Past medical history",
            "Drug history",
            "Family history",
            "Social history",
            "Summarize and thank"
        ]
    },
    "Venepuncture": {
        "duration": 5,
        "checklist": [
            "Introduce and explain procedure",
            "Check patient details",
            "Assemble equipment",
            "Apply tourniquet",
            "Clean site",
            "Insert needle",
            "Collect sample",
            "Apply pressure and dispose safely"
        ]
    }
}

def osce_timer_page(theme):
    st.markdown(f"<h2 style='color: {theme['text']}'>🩺 OSCE Clinical Timer</h2>", unsafe_allow_html=True)
    st.markdown("Practice OSCE stations with built-in checklists!")
    
    if "osce_active" not in st.session_state:
        st.session_state.osce_active = False
        st.session_state.osce_checks = {}
    
    col1, col2 = st.columns([2, 1])
    
    with col1:
        station = st.selectbox("Choose OSCE Station:", list(OSCE_STATIONS.keys()))
    
    with col2:
        if not st.session_state.osce_active:
            if st.button("▶️ Start Station", type="primary", use_container_width=True):
                st.session_state.osce_active = True
                st.session_state.osce_station = station
                st.session_state.osce_start = time.time()
                st.session_state.osce_checks = {i: False for i in range(len(OSCE_STATIONS[station]["checklist"]))}
                st.rerun()
        else:
            if st.button("⏹️ Stop", use_container_width=True):
                st.session_state.osce_active = False
                st.rerun()
    
    if st.session_state.osce_active:
        station_data = OSCE_STATIONS[st.session_state.osce_station]
        elapsed = int(time.time() - st.session_state.osce_start)
        remaining = max(0, station_data["duration"] * 60 - elapsed)
        
        # Timer display
        mins = remaining // 60
        secs = remaining % 60
        
        st.markdown(f"""
        <div style="
            text-align: center;
            padding: 2rem;
            background: linear-gradient(135deg, {theme['primary']}20, {theme['primary']}05);
            border-radius: 20px;
            margin: 1rem 0;
        ">
            <div style="font-size: 4rem; font-weight: 900; color: {theme['primary']}; font-family: monospace;">
                {mins:02d}:{secs:02d}
            </div>
            <div style="font-size: 1.2rem; color: {theme['text']}; margin-top: 0.5rem;">
                {st.session_state.osce_station}
            </div>
        </div>
        """, unsafe_allow_html=True)
        
        if remaining == 0:
            st.session_state.osce_active = False
            completed = sum(st.session_state.osce_checks.values())
            total = len(station_data["checklist"])
            st.success(f"⏰ Time's up! Completed: {completed}/{total} items")
            st.balloons()
            st.rerun()
        
        # Checklist
        st.markdown("### ✅ Checklist")
        for i, item in enumerate(station_data["checklist"]):
            checked = st.checkbox(item, value=st.session_state.osce_checks.get(i, False), key=f"check_{i}")
            st.session_state.osce_checks[i] = checked
        
        completed = sum(st.session_state.osce_checks.values())
        total = len(station_data["checklist"])
        st.progress(completed / total)
        st.markdown(f"**Progress:** {completed}/{total} completed ({completed/total*100:.0f}%)")
        
        time.sleep(1)
        st.rerun()
    
    else:
        st.markdown("### 📋 Available Stations")
        for station_name, station_data in OSCE_STATIONS.items():
            with st.expander(f"{station_name} ({station_data['duration']} min)"):
                for item in station_data["checklist"]:
                    st.markdown(f"- {item}")