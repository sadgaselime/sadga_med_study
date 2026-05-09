"""
shared_notes.py — Shared Note-Taking 📝
Collaborative note editing and sharing
"""

import streamlit as st
from datetime import datetime

# Sample shared notes
SHARED_NOTES = [
    {
        "id": 1,
        "title": "Cardiology Pharmacology Summary",
        "subject": "Cardiology",
        "author": "Dr. Ahmed",
        "collaborators": 8,
        "last_updated": "2024-04-27",
        "content": """
# Cardiology Drug Classes

## Beta Blockers
- **Mechanism:** Block β-adrenergic receptors
- **Uses:** Hypertension, Angina, Arrhythmias
- **Examples:** Metoprolol, Atenolol, Propranolol
- **Side Effects:** Bradycardia, Fatigue, Bronchospasm

## ACE Inhibitors
- **Mechanism:** Block conversion of Angiotensin I to II
- **Uses:** Hypertension, Heart Failure, Post-MI
- **Examples:** Lisinopril, Enalapril, Ramipril
- **Side Effects:** Dry cough, Hyperkalemia, Angioedema
        """,
        "views": 124,
        "public": True,
    },
    {
        "id": 2,
        "title": "Cranial Nerves Mnemonics",
        "subject": "Anatomy",
        "author": "Fatima A.",
        "collaborators": 5,
        "last_updated": "2024-04-26",
        "content": """
# Cranial Nerves Mnemonic

**On Old Olympus Towering Top, A Finn And German Viewed Some Hops**

1. **O**lfactory (I) - Smell
2. **O**ptic (II) - Vision
3. **O**culomotor (III) - Eye movement, pupil constriction
4. **T**rochlear (IV) - Eye movement (down and in)
5. **T**rigeminal (V) - Facial sensation, chewing
6. **A**bducens (VI) - Eye movement (lateral)
7. **F**acial (VII) - Facial expression, taste
8. **A**coustic/Vestibulocochlear (VIII) - Hearing, balance
9. **G**lossopharyngeal (IX) - Taste, swallowing
10. **V**agus (X) - Parasympathetic to organs
11. **S**pinal Accessory (XI) - Shoulder shrug
12. **H**ypoglossal (XII) - Tongue movement
        """,
        "views": 89,
        "public": True,
    },
]

def shared_notes_page(theme, user=None):
    st.markdown(f"<h2 style='color: {theme['text']}'>📝 Shared Notes</h2>", unsafe_allow_html=True)
    st.markdown("Collaborate on study notes with your peers!")
    
    if not user:
        st.warning("🔒 Login to create and edit shared notes")
    
    # Tabs
    tab1, tab2 = st.tabs(["📚 Browse Notes", "➕ Create Note"])
    
    # TAB 1: Browse
    with tab1:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            subject_filter = st.selectbox("Filter by Subject:", 
                ["All", "Cardiology", "Anatomy", "Pharmacology", "Physiology"])
        
        with col2:
            sort_by = st.selectbox("Sort by:", ["Most Recent", "Most Popular", "Most Collaborators"])
        
        # Display notes
        for note in SHARED_NOTES:
            if subject_filter != "All" and note["subject"] != subject_filter:
                continue
            
            st.markdown(f"""
            <div style="
                background: {theme['card_bg']};
                border: 1px solid {theme['card_border']};
                border-radius: 16px;
                padding: 1.5rem;
                margin-bottom: 1rem;
            ">
                <h3 style="color: {theme['text']}; margin: 0 0 0.5rem 0;">
                    📄 {note['title']}
                </h3>
                <div style="color: {theme['subtext']}; margin-bottom: 1rem;">
                    📚 {note['subject']} • 👤 {note['author']} • 👥 {note['collaborators']} collaborators
                    <br>
                    👁️ {note['views']} views • 📅 Updated: {note['last_updated']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3 = st.columns(3)
            with col1:
                if st.button("📖 Read", key=f"read_{note['id']}", use_container_width=True):
                    st.session_state[f'show_note_{note["id"]}'] = True
                    st.rerun()
            with col2:
                if st.button("✏️ Edit", key=f"edit_{note['id']}", use_container_width=True):
                    st.info("Opening collaborative editor...")
            with col3:
                if st.button("💾 Download", key=f"dl_{note['id']}", use_container_width=True):
                    st.success("Downloaded as PDF!")
            
            # Show note content if requested
            if st.session_state.get(f'show_note_{note["id"]}', False):
                st.markdown(f"""
                <div style="
                    background: {theme['card_bg']};
                    border-left: 4px solid {theme['primary']};
                    padding: 1.5rem;
                    margin: 1rem 0;
                    border-radius: 8px;
                ">
                    {note['content'].replace(chr(10), '<br>')}
                </div>
                """, unsafe_allow_html=True)
                
                if st.button("Close", key=f"close_{note['id']}"):
                    st.session_state[f'show_note_{note["id"]}'] = False
                    st.rerun()
    
    # TAB 2: Create Note
    with tab2:
        if not user:
            st.info("Please login to create shared notes")
        else:
            st.markdown("### Create Shared Note")
            
            title = st.text_input("📝 Note Title:", placeholder="e.g., Neurology Study Guide")
            
            subject = st.selectbox("📚 Subject:", 
                ["Cardiology", "Anatomy", "Pharmacology", "Physiology", "Pathology"])
            
            col1, col2 = st.columns(2)
            with col1:
                public = st.checkbox("🌐 Make Public", value=True)
            with col2:
                allow_collab = st.checkbox("👥 Allow Collaborators", value=True)
            
            content = st.text_area("📄 Note Content:", 
                placeholder="Write your notes here... (Markdown supported)",
                height=300)
            
            if st.button("💾 Create Note", type="primary", use_container_width=True):
                if title and content:
                    st.success("✅ Note created successfully!")
                    st.balloons()
                else:
                    st.error("Please fill in title and content")