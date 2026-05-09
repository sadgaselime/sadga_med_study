"""
progress_tracker.py — Advanced Progress Tracking 📈
"""

import streamlit as st
from datetime import datetime, timedelta
import random

def progress_tracker_page(theme, user_stats):
    st.markdown(f"<h2 style='color: {theme['text']}'>📈 Advanced Progress Tracker</h2>", unsafe_allow_html=True)
    
    # Overall stats
    st.markdown("### 📊 Overall Performance")
    
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #10b98130, #10b98110); border: 2px solid #10b981; border-radius: 16px; padding: 1.5rem; text-align: center;">
            <div style="font-size: 3rem;">⏱️</div>
            <div style="font-size: 2.5rem; font-weight: 900; color: #10b981;">{user_stats['study_hours']}h</div>
            <div style="color: {theme['text']}; font-weight: 600;">Study Hours</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #8b5cf630, #8b5cf610); border: 2px solid #8b5cf6; border-radius: 16px; padding: 1.5rem; text-align: center;">
            <div style="font-size: 3rem;">📅</div>
            <div style="font-size: 2.5rem; font-weight: 900; color: #8b5cf6;">{user_stats['sessions']}</div>
            <div style="color: {theme['text']}; font-weight: 600;">Sessions</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #ec489930, #ec489910); border: 2px solid #ec4899; border-radius: 16px; padding: 1.5rem; text-align: center;">
            <div style="font-size: 3rem;">📝</div>
            <div style="font-size: 2.5rem; font-weight: 900; color: #ec4899;">{user_stats['mcq_percent']}%</div>
            <div style="color: {theme['text']}; font-weight: 600;">MCQ Score</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col4:
        streak = random.randint(1, 15)  # Placeholder
        st.markdown(f"""
        <div style="background: linear-gradient(135deg, #f59e0b30, #f59e0b10); border: 2px solid #f59e0b; border-radius: 16px; padding: 1.5rem; text-align: center;">
            <div style="font-size: 3rem;">🔥</div>
            <div style="font-size: 2.5rem; font-weight: 900; color: #f59e0b;">{streak}</div>
            <div style="color: {theme['text']}; font-weight: 600;">Day Streak</div>
        </div>
        """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Study calendar heatmap (simplified)
    st.markdown("### 📅 Study Calendar")
    
    st.markdown(f"""
    <div style="background: {theme['card_bg']}; border: 1px solid {theme['card_border']}; border-radius: 16px; padding: 2rem;">
        <div style="text-align: center; padding: 2rem;">
            <div style="font-size: 3rem; margin-bottom: 1rem;">📊</div>
            <div style="color: {theme['text']}; font-size: 1.2rem; margin-bottom: 0.5rem;">
                Study Heatmap Calendar
            </div>
            <div style="color: {theme['subtext']};">
                Visual representation of your daily study activity
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Subject progress
    st.markdown("### 📚 Subject Mastery")
    
    subjects = [
        ("Anatomy", random.randint(60, 95)),
        ("Physiology", random.randint(60, 95)),
        ("Biochemistry", random.randint(60, 95)),
        ("Pharmacology", random.randint(60, 95)),
        ("Pathology", random.randint(60, 95)),
        ("Microbiology", random.randint(60, 95)),
    ]
    
    for subject, progress in subjects:
        st.markdown(f"**{subject}**")
        st.progress(progress / 100)
        st.markdown(f"<small style='color: {theme['subtext']}'>{progress}% mastery</small>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)
    
    # Achievements
    st.markdown("### 🏆 Achievements")
    
    achievements = [
        ("🔥", "7-Day Streak", "Study 7 days in a row", True),
        ("📚", "Subject Expert", "Complete 10 subjects", False),
        ("🎯", "Perfect Score", "Get 100% on MCQ quiz", False),
        ("⏱️", "Time Master", "Complete 50 pomodoro sessions", True),
        ("🧠", "Knowledge King", "Answer 500 questions correctly", False),
    ]
    
    cols = st.columns(5)
    for i, (emoji, title, desc, unlocked) in enumerate(achievements):
        with cols[i]:
            opacity = "1.0" if unlocked else "0.3"
            st.markdown(f"""
            <div style="background: {theme['card_bg']}; border: 1px solid {theme['card_border']}; border-radius: 12px; padding: 1rem; text-align: center; opacity: {opacity};">
                <div style="font-size: 2.5rem; margin-bottom: 0.5rem;">{emoji}</div>
                <div style="color: {theme['text']}; font-weight: 700; font-size: 0.9rem; margin-bottom: 0.3rem;">{title}</div>
                <div style="color: {theme['subtext']}; font-size: 0.75rem;">{desc}</div>
            </div>
            """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # Weekly goals
    st.markdown("### 🎯 Weekly Goals")
    
    goals = [
        ("Study 10 hours", 7, 10),
        ("Complete 5 MCQ quizzes", 3, 5),
        ("Practice 3 OSCE stations", 2, 3),
    ]
    
    for goal, current, target in goals:
        st.markdown(f"**{goal}**")
        st.progress(current / target)
        st.markdown(f"<small style='color: {theme['subtext']}'>{current}/{target} completed</small>", unsafe_allow_html=True)
        st.markdown("<br>", unsafe_allow_html=True)