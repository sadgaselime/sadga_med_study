"""
tips_page.py — Study Tips & Exam Strategies 💡
"""

import streamlit as st

STUDY_TIPS = {
    "Active Recall": {
        "icon": "🧠",
        "description": "Test yourself frequently rather than re-reading",
        "tips": [
            "Close your notes and write everything you remember",
            "Use flashcards to quiz yourself regularly",
            "Explain concepts out loud without looking at notes",
            "Practice with past exam papers",
        ],
        "color": "#10b981"
    },
    "Spaced Repetition": {
        "icon": "📅",
        "description": "Review material at increasing intervals",
        "tips": [
            "Review new material after 1 day, then 3 days, then 1 week",
            "Use SRS apps like Anki or our Flashcard system",
            "Don't cram - spread your study over time",
            "Focus more on difficult topics",
        ],
        "color": "#8b5cf6"
    },
    "Pomodoro Technique": {
        "icon": "⏱️",
        "description": "Study in focused 25-minute blocks",
        "tips": [
            "Set timer for 25 minutes of focused study",
            "Take 5-minute break after each session",
            "After 4 sessions, take a longer 15-30 minute break",
            "Eliminate all distractions during study time",
        ],
        "color": "#ec4899"
    },
    "Feynman Technique": {
        "icon": "👨‍🏫",
        "description": "Teach concepts to identify knowledge gaps",
        "tips": [
            "Pick a concept and explain it in simple terms",
            "Pretend you're teaching it to a 10-year-old",
            "Identify areas where you struggle to explain",
            "Go back and review those weak areas",
        ],
        "color": "#f59e0b"
    },
    "Mind Mapping": {
        "icon": "🗺️",
        "description": "Visualize connections between concepts",
        "tips": [
            "Start with main topic in center",
            "Branch out to subtopics",
            "Use colors and images",
            "Connect related ideas with lines",
        ],
        "color": "#ef4444"
    },
    "Practice Questions": {
        "icon": "📝",
        "description": "Apply knowledge through active problem-solving",
        "tips": [
            "Do practice questions BEFORE reading solutions",
            "Review incorrect answers thoroughly",
            "Understand why wrong answers are wrong",
            "Redo missed questions after a few days",
        ],
        "color": "#06b6d4"
    }
}

EXAM_STRATEGIES = [
    {
        "title": "Before the Exam",
        "tips": [
            "Get 7-8 hours sleep the night before",
            "Eat a nutritious breakfast",
            "Arrive 15 minutes early",
            "Bring all required materials",
            "Review key concepts briefly, don't cram",
        ]
    },
    {
        "title": "During the Exam",
        "tips": [
            "Read all instructions carefully",
            "Scan entire exam first",
            "Answer easy questions first",
            "Mark difficult questions to revisit",
            "Manage your time per section",
        ]
    },
    {
        "title": "MCQ Strategy",
        "tips": [
            "Read question carefully before options",
            "Eliminate obviously wrong answers",
            "Look for absolute words (always/never)",
            "Check for double negatives",
            "Don't change answers unless certain",
        ]
    },
    {
        "title": "Essay Questions",
        "tips": [
            "Plan your answer before writing",
            "Address all parts of the question",
            "Use clear topic sentences",
            "Support with specific examples",
            "Leave time to review and edit",
        ]
    }
]

def tips_page(theme):
    st.markdown(f"<h2 style='color: {theme['text']}'>💡 Study Tips & Exam Strategies</h2>", unsafe_allow_html=True)
    st.markdown("Evidence-based techniques to maximize your learning")
    
    # Study techniques
    st.markdown("### 📚 Effective Study Techniques")
    
    for technique, data in STUDY_TIPS.items():
        with st.expander(f"{data['icon']} {technique}"):
            st.markdown(f"""
            <div style="
                background: {data['color']}15;
                border-left: 4px solid {data['color']};
                padding: 1.5rem;
                border-radius: 8px;
                margin-bottom: 1rem;
            ">
                <div style="color: {theme['text']}; font-weight: 700; font-size: 1.1rem; margin-bottom: 0.5rem;">
                    {data['description']}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            st.markdown("**How to apply:**")
            for tip in data['tips']:
                st.markdown(f"✓ {tip}")
    
    # Exam strategies
    st.markdown("---")
    st.markdown("### 🎯 Exam Strategies")
    
    cols = st.columns(2)
    for i, strategy in enumerate(EXAM_STRATEGIES):
        with cols[i % 2]:
            st.markdown(f"""
            <div style="
                background: {theme['card_bg']};
                border: 2px solid {theme['primary']};
                border-radius: 16px;
                padding: 1.5rem;
                margin-bottom: 1rem;
            ">
                <h3 style="color: {theme['text']}; margin: 0 0 1rem 0;">{strategy['title']}</h3>
            </div>
            """, unsafe_allow_html=True)
            
            for tip in strategy['tips']:
                st.markdown(f"• {tip}")
            
            st.markdown("<br>", unsafe_allow_html=True)
    
    # Quick tips
    st.markdown("---")
    st.markdown("### ⚡ Quick Tips")
    
    col1, col2, col3 = st.columns(3)
    
    quick_tips = [
        ("🚫 Avoid", ["All-nighters", "Multitasking", "Passive reading", "Studying while tired"], "#ef4444"),
        ("✅ Do", ["Regular breaks", "Active recall", "Sleep well", "Stay hydrated"], "#10b981"),
        ("📱 Tools", ["Pomodoro timer", "Flashcards", "Mind maps", "Study groups"], "#8b5cf6"),
    ]
    
    for col, (title, items, color) in zip([col1, col2, col3], quick_tips):
        with col:
            st.markdown(f"""
            <div style="
                background: {theme['card_bg']};
                border: 2px solid {color};
                border-radius: 12px;
                padding: 1.5rem;
            ">
                <div style="color: {color}; font-weight: 700; font-size: 1.1rem; margin-bottom: 1rem;">
                    {title}
                </div>
            </div>
            """, unsafe_allow_html=True)
            
            for item in items:
                st.markdown(f"• {item}")