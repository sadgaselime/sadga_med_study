"""
discussion.py — Discussion Forums 💬
Q&A forums by subject with upvoting
"""

import streamlit as st
from datetime import datetime

# Sample forum posts
FORUM_POSTS = [
    {
        "id": 1,
        "subject": "Cardiology",
        "title": "Best way to memorize heart murmurs?",
        "question": "I'm struggling with differentiating between systolic and diastolic murmurs. Any tips or mnemonics?",
        "author": "Ahmed S.",
        "date": "2024-04-25",
        "upvotes": 12,
        "answers": 5,
        "tags": ["murmurs", "cardiology", "mnemonics"],
    },
    {
        "id": 2,
        "subject": "Pharmacology",
        "title": "ACE inhibitors vs ARBs - when to use which?",
        "question": "Can someone explain the clinical scenarios where you'd choose one over the other?",
        "author": "Fatima A.",
        "date": "2024-04-26",
        "upvotes": 8,
        "answers": 3,
        "tags": ["pharmacology", "hypertension"],
    },
    {
        "id": 3,
        "subject": "Anatomy",
        "title": "Brachial plexus - easiest way to remember?",
        "question": "The roots, trunks, divisions, cords arrangement is confusing. Help!",
        "author": "Ali M.",
        "date": "2024-04-27",
        "upvotes": 15,
        "answers": 7,
        "tags": ["anatomy", "nervous system", "mnemonics"],
    },
]

def discussion_page(theme, user=None):
    st.markdown(f"<h2 style='color: {theme['text']}'>💬 Discussion Forums</h2>", unsafe_allow_html=True)
    st.markdown("Ask questions, share knowledge, help your peers!")
    
    if not user:
        st.warning("🔒 Login to post questions and answers")
    
    # Tabs
    tab1, tab2 = st.tabs(["📋 Browse Questions", "➕ Ask Question"])
    
    # TAB 1: Browse
    with tab1:
        col1, col2 = st.columns([2, 1])
        
        with col1:
            subject_filter = st.selectbox("Filter by Subject:", 
                ["All", "Cardiology", "Anatomy", "Pharmacology", "Physiology", "Pathology"])
        
        with col2:
            sort_by = st.selectbox("Sort by:", ["Most Recent", "Most Upvoted", "Most Answers"])
        
        # Display posts
        for post in FORUM_POSTS:
            if subject_filter != "All" and post["subject"] != subject_filter:
                continue
            
            st.markdown(f"""
            <div style="
                background: {theme['card_bg']};
                border: 1px solid {theme['card_border']};
                border-radius: 16px;
                padding: 1.5rem;
                margin-bottom: 1rem;
            ">
                <div style="display: flex; gap: 1rem;">
                    <div style="text-align: center; min-width: 60px;">
                        <div style="font-size: 1.5rem; color: {theme['primary']}; font-weight: 900;">
                            {post['upvotes']}
                        </div>
                        <div style="font-size: 0.8rem; color: {theme['subtext']};">votes</div>
                        <div style="font-size: 1.2rem; color: {theme['text']}; font-weight: 700; margin-top: 0.5rem;">
                            {post['answers']}
                        </div>
                        <div style="font-size: 0.8rem; color: {theme['subtext']};">answers</div>
                    </div>
                    <div style="flex: 1;">
                        <h3 style="color: {theme['text']}; margin: 0 0 0.5rem 0;">
                            {post['title']}
                        </h3>
                        <p style="color: {theme['subtext']}; margin: 0 0 1rem 0;">
                            {post['question']}
                        </p>
                        <div style="display: flex; gap: 0.5rem; flex-wrap: wrap; margin-bottom: 0.5rem;">
                            {' '.join([f'<span style="background: {theme["primary"]}20; color: {theme["primary"]}; padding: 0.25rem 0.5rem; border-radius: 6px; font-size: 0.8rem;">#{tag}</span>' for tag in post['tags']])}
                        </div>
                        <div style="color: {theme['subtext']}; font-size: 0.85rem;">
                            📚 {post['subject']} • 👤 {post['author']} • 📅 {post['date']}
                        </div>
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            col1, col2, col3, col4 = st.columns(4)
            with col1:
                if st.button("👍 Upvote", key=f"up_{post['id']}", use_container_width=True):
                    st.success("Upvoted!")
            with col2:
                if st.button("💬 Answer", key=f"ans_{post['id']}", use_container_width=True):
                    st.info("Opening answer editor...")
            with col3:
                if st.button("👁️ View", key=f"view_{post['id']}", use_container_width=True):
                    st.info("View full discussion...")
            with col4:
                if st.button("🔖 Save", key=f"save_{post['id']}", use_container_width=True):
                    st.success("Saved to bookmarks!")
    
    # TAB 2: Ask Question
    with tab2:
        if not user:
            st.info("Please login to ask questions")
        else:
            st.markdown("### Ask a Question")
            
            subject = st.selectbox("📚 Subject:", 
                ["Cardiology", "Anatomy", "Pharmacology", "Physiology", "Pathology", "Biochemistry"])
            
            title = st.text_input("📝 Question Title:", placeholder="e.g., How to differentiate between...")
            
            question = st.text_area("❓ Your Question:", 
                placeholder="Provide details about what you're asking...",
                height=150)
            
            tags = st.text_input("🏷️ Tags (comma separated):", 
                placeholder="e.g., mnemonics, differential diagnosis")
            
            if st.button("📤 Post Question", type="primary", use_container_width=True):
                if title and question:
                    st.success("✅ Question posted successfully!")
                    st.balloons()
                else:
                    st.error("Please fill in title and question")