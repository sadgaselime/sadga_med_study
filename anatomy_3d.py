"""
anatomy_3d.py — 3D Anatomy Viewer 🫁
"""

import streamlit as st

ANATOMY_MODELS = {
    "Heart": {
        "description": "Detailed 3D model of the human heart showing chambers, valves, and major vessels",
        "systems": ["Cardiovascular"],
        "url": "https://sketchfab.com/models/06d5a80a04fc43679e86ac0179a8e773/embed"
    },
    "Brain": {
        "description": "Complete brain anatomy including cerebral hemispheres, cerebellum, and brain stem",
        "systems": ["Nervous"],
        "url": "https://sketchfab.com/models/9e2b4d1a0e5f4b8c9a7f6e5d4c3b2a10/embed"
    },
    "Lungs": {
        "description": "Respiratory system showing trachea, bronchi, and lung lobes",
        "systems": ["Respiratory"],
        "url": "https://sketchfab.com/models/a3b2c1d0e9f8g7h6i5j4k3l2m1n0o9p8/embed"
    },
    "Skeleton": {
        "description": "Complete human skeletal system with all major bones",
        "systems": ["Skeletal"],
        "url": "https://sketchfab.com/models/b4c3d2e1f0g9h8i7j6k5l4m3n2o1p0q9/embed"
    },
    "Liver": {
        "description": "Liver anatomy showing lobes, blood vessels, and bile ducts",
        "systems": ["Digestive"],
        "url": "https://sketchfab.com/models/c5d4e3f2g1h0i9j8k7l6m5n4o3p2q1r0/embed"
    }
}

def anatomy_3d_page(theme):
    st.markdown(f"<h2 style='color: {theme['text']}'>🫁 3D Anatomy Viewer</h2>", unsafe_allow_html=True)
    st.markdown("Interactive 3D models of human anatomy")
    
    # Model selection
    col1, col2 = st.columns([2, 1])
    
    with col1:
        selected_model = st.selectbox("Choose Anatomical Structure:", list(ANATOMY_MODELS.keys()))
    
    with col2:
        system_filter = st.selectbox("System:", ["All", "Cardiovascular", "Nervous", "Respiratory", "Skeletal", "Digestive"])
    
    model_data = ANATOMY_MODELS[selected_model]
    
    # Display model info
    st.markdown(f"""
    <div style="
        background: {theme['card_bg']};
        border: 1px solid {theme['card_border']};
        border-radius: 16px;
        padding: 1.5rem;
        margin: 1rem 0;
    ">
        <h3 style="color: {theme['text']}; margin: 0 0 0.5rem 0;">{selected_model}</h3>
        <p style="color: {theme['subtext']}; margin: 0;">{model_data['description']}</p>
        <p style="color: {theme['primary']}; margin: 0.5rem 0 0 0;">
            <strong>System:</strong> {', '.join(model_data['systems'])}
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # 3D Model Embed (placeholder since we can't embed real 3D models without proper URLs)
    st.markdown(f"""
    <div style="
        background: linear-gradient(135deg, {theme['primary']}15, {theme['primary']}05);
        border: 2px solid {theme['primary']};
        border-radius: 20px;
        padding: 3rem;
        text-align: center;
        margin: 2rem 0;
    ">
        <div style="font-size: 5rem; margin-bottom: 1rem;">🫀</div>
        <h3 style="color: {theme['text']}; margin: 0 0 1rem 0;">3D Model: {selected_model}</h3>
        <p style="color: {theme['subtext']}; margin: 0;">
            Interactive 3D model viewer would appear here<br>
            <em>Rotate • Zoom • Explore anatomy layers</em>
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Controls guide
    st.markdown("### 🎮 Controls")
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div style="background: {theme['card_bg']}; padding: 1rem; border-radius: 12px; text-align: center;">
            <div style="font-size: 2rem;">🖱️</div>
            <div style="color: {theme['text']}; font-weight: 700;">Rotate</div>
            <div style="color: {theme['subtext']}; font-size: 0.9rem;">Left click + drag</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col2:
        st.markdown(f"""
        <div style="background: {theme['card_bg']}; padding: 1rem; border-radius: 12px; text-align: center;">
            <div style="font-size: 2rem;">🔍</div>
            <div style="color: {theme['text']}; font-weight: 700;">Zoom</div>
            <div style="color: {theme['subtext']}; font-size: 0.9rem;">Scroll wheel</div>
        </div>
        """, unsafe_allow_html=True)
    
    with col3:
        st.markdown(f"""
        <div style="background: {theme['card_bg']}; padding: 1rem; border-radius: 12px; text-align: center;">
            <div style="font-size: 2rem;">👆</div>
            <div style="color: {theme['text']}; font-weight: 700;">Pan</div>
            <div style="color: {theme['subtext']}; font-size: 0.9rem;">Right click + drag</div>
        </div>
        """, unsafe_allow_html=True)
    
    # Quiz mode
    st.markdown("---")
    st.markdown("### 🧠 Quiz Mode")
    
    if st.button("Start Anatomy Quiz", type="primary"):
        st.info("Quiz feature coming soon! Test your knowledge of anatomical structures.")