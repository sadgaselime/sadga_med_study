"""
leaderboards.py — Anonymous Leaderboards 🏆
Rankings by quiz scores, study time, streaks
"""

import streamlit as st
import random

# Sample leaderboard data
def generate_leaderboard(category, count=10):
    """Generate sample leaderboard data"""
    names = ["Medical Student", "Future Doctor", "Study Champion", "Quiz Master", 
             "Knowledge Seeker", "Med Star", "Academic Achiever", "Learning Pro",
             "Study Warrior", "Brain Surgeon", "Med Genius", "Scholar"]
    
    universities = ["SQU", "Dhofar University", "OMC", "GMU"]
    
    data = []
    for i in range(count):
        if category == "mcq":
            score = random.randint(70, 100)
            total = random.randint(50, 200)
        elif category == "study_time":
            score = random.randint(10, 150)
            total = "hours"
        elif category == "streak":
            score = random.randint(1, 45)
            total = "days"
        
        data.append({
            "rank": i + 1,
            "name": f"{random.choice(names)} #{random.randint(1000, 9999)}",
            "university": random.choice(universities),
            "score": score,
            "total": total,
        })
    
    return sorted(data, key=lambda x: x['score'], reverse=True)

def leaderboards_page(theme, user=None):
    st.markdown(f"<h2 style='color: {theme['text']}'>🏆 Leaderboards</h2>", unsafe_allow_html=True)
    st.markdown("Anonymous rankings - compete with students across Oman!")
    
    # Category tabs
    tab1, tab2, tab3, tab4 = st.tabs([
        "📝 MCQ Quiz",
        "⏱️ Study Time",
        "🔥 Study Streaks",
        "📊 Overall"
    ])
    
    # Helper function to display leaderboard
    def show_leaderboard(data, category_type):
        for entry in data[:10]:  # Top 10
            rank = entry['rank']
            
            # Medal for top 3
            medal = ""
            border_color = theme['card_border']
            if rank == 1:
                medal = "🥇"
                border_color = "#FFD700"  # Gold
            elif rank == 2:
                medal = "🥈"
                border_color = "#C0C0C0"  # Silver
            elif rank == 3:
                medal = "🥉"
                border_color = "#CD7F32"  # Bronze
            
            score_display = f"{entry['score']}%"
            if category_type == "study_time":
                score_display = f"{entry['score']}h"
            elif category_type == "streak":
                score_display = f"{entry['score']} days"
            
            st.markdown(f"""
            <div style="
                background: {theme['card_bg']};
                border: 2px solid {border_color};
                border-radius: 12px;
                padding: 1rem 1.5rem;
                margin-bottom: 0.75rem;
                display: flex;
                align-items: center;
                gap: 1rem;
            ">
                <div style="
                    font-size: 2rem;
                    font-weight: 900;
                    color: {theme['primary']};
                    min-width: 50px;
                    text-align: center;
                ">
                    {medal} #{rank}
                </div>
                <div style="flex: 1;">
                    <div style="color: {theme['text']}; font-weight: 700; font-size: 1.1rem;">
                        {entry['name']}
                    </div>
                    <div style="color: {theme['subtext']}; font-size: 0.9rem;">
                        🏫 {entry['university']}
                    </div>
                </div>
                <div style="
                    font-size: 1.5rem;
                    font-weight: 900;
                    color: {theme['primary']};
                    text-align: right;
                ">
                    {score_display}
                </div>
            </div>
            """, unsafe_allow_html=True)
    
    # TAB 1: MCQ Quiz Rankings
    with tab1:
        st.markdown("### 📝 Top MCQ Quiz Performers")
        st.markdown("Ranked by quiz accuracy and completion rate")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            subject = st.selectbox("Filter by Subject:", 
                ["All Subjects", "Cardiology", "Anatomy", "Pharmacology", "Physiology"],
                key="mcq_subject")
        with col2:
            timeframe = st.selectbox("Timeframe:", ["This Month", "This Week", "All Time"], key="mcq_time")
        
        data = generate_leaderboard("mcq", 10)
        show_leaderboard(data, "mcq")
    
    # TAB 2: Study Time Rankings
    with tab2:
        st.markdown("### ⏱️ Top Study Time Leaders")
        st.markdown("Ranked by total study hours")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            period = st.selectbox("Period:", ["This Month", "This Week", "All Time"], key="time_period")
        with col2:
            uni = st.selectbox("University:", ["All", "SQU", "Dhofar University", "OMC"], key="time_uni")
        
        data = generate_leaderboard("study_time", 10)
        show_leaderboard(data, "study_time")
    
    # TAB 3: Study Streaks
    with tab3:
        st.markdown("### 🔥 Longest Study Streaks")
        st.markdown("Ranked by consecutive days of study")
        
        data = generate_leaderboard("streak", 10)
        show_leaderboard(data, "streak")
        
        st.markdown(f"""
        <div style="
            background: linear-gradient(135deg, {theme['primary']}20, {theme['primary']}05);
            border: 1px solid {theme['primary']};
            border-radius: 12px;
            padding: 1.5rem;
            margin-top: 2rem;
            text-align: center;
        ">
            <div style="font-size: 2rem; margin-bottom: 0.5rem;">💡</div>
            <div style="color: {theme['text']}; font-weight: 700; margin-bottom: 0.5rem;">
                Keep Your Streak Alive!
            </div>
            <div style="color: {theme['subtext']};">
                Study for at least 15 minutes each day to maintain your streak
            </div>
        </div>
        """, unsafe_allow_html=True)
    
    # TAB 4: Overall Rankings
    with tab4:
        st.markdown("### 📊 Overall Performance Rankings")
        st.markdown("Combined score based on all activities")
        
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Your Rank", "#42", "↑ 5")
        with col2:
            st.metric("Overall Score", "87%", "↑ 3%")
        with col3:
            st.metric("Percentile", "Top 15%", "")
        
        st.markdown("<br>", unsafe_allow_html=True)
        
        data = generate_leaderboard("mcq", 10)
        show_leaderboard(data, "overall")
        
        st.info("💡 Overall score = (MCQ % × 40%) + (Study Hours × 30%) + (Streak × 30%)")
    
    # Privacy notice
    st.markdown("---")
    st.markdown(f"""
    <div style="
        background: {theme['card_bg']};
        border: 1px solid {theme['card_border']};
        border-radius: 8px;
        padding: 1rem;
        text-align: center;
    ">
        <small style="color: {theme['subtext']};">
            🔒 All rankings are anonymous. Your name is never displayed publicly.
        </small>
    </div>
    """, unsafe_allow_html=True)