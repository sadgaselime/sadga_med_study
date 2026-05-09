"""
study_groups.py — Study Groups 👥
Create and join study groups, share resources
"""

import streamlit as st
from datetime import datetime
import random

# Sample study groups (in real app, this would be in database)
STUDY_GROUPS = {
    1: {
        "name": "Cardiology Crushers 🫀",
        "members": 12,
        "created": "2024-01-15",
        "description": "Focused on mastering cardiology for final exams",
        "subject": "Cardiology",
        "university": "SQU",
        "active": True,
    },
    2: {
        "name": "Anatomy All-Stars 🦴",
        "members": 8,
        "created": "2024-02-01",
        "description": "Daily anatomy practice and quiz sessions",
        "subject": "Anatomy",
        "university": "SQU",
        "active": True,
    },
    3: {
        "name": "Pharmacology Pros 💊",
        "members": 15,
        "created": "2024-01-20",
        "description": "Drug classifications, mechanisms, and mnemonics",
        "subject": "Pharmacology",
        "university": "All",
        "active": True,
    },
}

def study_groups_page(theme, user=None):
    st.markdown(f"<h2 style='color: {theme['text']}'>👥 Study Groups</h2>", unsafe_allow_html=True)
    
    if not user:
        st.markdown(f"""
        <div style="
            text-align: center;
            padding: 3rem;
            background: linear-gradient(135deg, {theme['primary']}20, {theme['primary']}05);
            border-radius: 20px;
        ">
            <div style="font-size: 4rem; margin-bottom: 1rem;">🔒</div>
            <h3 style="color: {theme['text']}">Login Required</h3>
            <p style="color: {theme['subtext']}">Please login to join study groups</p>
        </div>
        """, unsafe_allow_html=True)
        return
    
    # Tabs for different views
    tab1, tab2, tab3 = st.tabs(["🔍 Browse Groups", "➕ Create Group", "👥 My Groups"])
    
    # TAB 1: Browse Groups
    with tab1:
        st.markdown("### Available Study Groups")
        
        col1, col2 = st.columns(2)
        with col1:
            subject_filter = st.selectbox("Filter by Subject:", ["All", "Cardiology", "Anatomy", "Pharmacology", "Physiology"])
        with col2:
            uni_filter = st.selectbox("Filter by University:", ["All", "SQU", "Dhofar University", "OMC"])
        
        # Display groups
        for group_id, group in STUDY_GROUPS.items():
            if subject_filter != "All" and group["subject"] != subject_filter:
                continue
            if uni_filter != "All" and group["university"] != "All" and group["university"] != uni_filter:
                continue
            
            st.markdown(f"""
            <div style="
                background: {theme['card_bg']};
                border: 2px solid {theme['card_border']};
                border-radius: 16px;
                padding: 1.5rem;
                margin-bottom: 1rem;
            ">
                <div style="display: flex; justify-content: space-between; align-items: start;">
                    <div>
                        <h3 style="color: {theme['text']}; margin: 0 0 0.5rem 0;">{group['name']}</h3>
                        <p style="color: {theme['subtext']}; margin: 0 0 0.5rem 0;">{group['description']}</p>
                        <div style="color: {theme['primary']}; font-size: 0.9rem;">
                            👥 {group['members']} members • 📚 {group['subject']} • 🏫 {group['university']}
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns([1, 1, 2])
            with col1:
                if st.button(f"➕ Join", key=f"join_{group_id}", use_container_width=True):
                    st.success(f"✅ Joined {group['name']}!")
                    st.balloons()
            with col2:
                if st.button(f"👁️ View", key=f"view_{group_id}", use_container_width=True):
                    st.info(f"Viewing group details...")
    
    # TAB 2: Create Group
    with tab2:
        st.markdown("### Create New Study Group")
        
        group_name = st.text_input("📝 Group Name:", placeholder="e.g., Neurology Ninjas 🧠")
        
        col1, col2 = st.columns(2)
        with col1:
            subject = st.selectbox("📚 Subject:", ["Cardiology", "Anatomy", "Pharmacology", "Physiology", "Pathology", "Biochemistry"])
        with col2:
            university = st.selectbox("🏫 University:", ["SQU", "All Universities", "Dhofar University", "OMC"])
        
        description = st.text_area("📄 Description:", placeholder="What will your group focus on?")
        
        col1, col2 = st.columns([1, 3])
        with col1:
            if st.button("✨ Create Group", type="primary", use_container_width=True):
                if group_name and description:
                    st.success(f"🎉 Created {group_name}!")
                    st.balloons()
                else:
                    st.error("Please fill in all fields")
    
    # TAB 3: My Groups
    with tab3:
        st.markdown("### My Study Groups")
        
        # Show joined groups (sample)
        my_groups = [STUDY_GROUPS[1], STUDY_GROUPS[3]]
        
        for group in my_groups:
            st.markdown(f"""
            <div style="
                background: linear-gradient(135deg, {theme['primary']}20, {theme['primary']}05);
                border: 2px solid {theme['primary']};
                border-radius: 16px;
                padding: 1.5rem;
                margin-bottom: 1rem;
            ">
                <h3 style="color: {theme['text']}; margin: 0 0 0.5rem 0;">{group['name']}</h3>
                <p style="color: {theme['subtext']}; margin: 0;">
                    👥 {group['members']} members • Last active: Today
                </p>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("💬 Chat", key=f"chat_{group['name']}", use_container_width=True):
                    st.info("Group chat opening...")
            with col2:
                if st.button("📚 Resources", key=f"res_{group['name']}", use_container_width=True):
                    st.info("Shared resources...")
            with col3:
                if st.button("🚪 Leave", key=f"leave_{group['name']}", use_container_width=True):
                    st.warning("Left group")