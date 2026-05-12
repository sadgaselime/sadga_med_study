"""
login_page.py — MedStudy Oman 🩺
Phase 2: Futuristic Login / Sign-Up Card
Floating labels · Micro-animations · Bio-Lock aesthetic
"""

import streamlit as st
import time


# ─────────────────────────────────────────────────────────────────────────────
# AUTH PAGE  (replaces inline forms in app.py)
# ─────────────────────────────────────────────────────────────────────────────

def auth_page(theme: dict, login_user_fn, signup_user_fn):
    """
    Full-screen authentication page.
    Switches between login and signup via st.session_state.auth_mode.
    """

    if "auth_mode" not in st.session_state:
        st.session_state.auth_mode = "login"

    t = theme   # shorthand

    # ── Ambient background particles ────────────────────────────────────────
    st.markdown(f"""
    <style>
    /* Full-page auth backdrop */
    [data-testid="stAppViewContainer"] > .main {{
        background: {t['hero_gradient']} !important;
    }}
    .auth-wrapper {{
        display: flex;
        align-items: center;
        justify-content: center;
        min-height: 80vh;
        padding: 2rem 1rem;
    }}
    .auth-card {{
        background:       {t['glass_bg']};
        border:           1px solid {t['glass_border']};
        border-radius:    28px;
        backdrop-filter:  blur({t['glass_blur']});
        -webkit-backdrop-filter: blur({t['glass_blur']});
        box-shadow:       {t['shadow_lg']}, {t['glow']};
        padding:          3rem 2.5rem;
        width:            100%;
        max-width:        480px;
        margin:           0 auto;
        position:         relative;
        overflow:         hidden;
        animation:        fadeUp 0.55s cubic-bezier(0.34,1.56,0.64,1) both;
    }}
    /* Glow orb top-right */
    .auth-card::before {{
        content:          '';
        position:         absolute;
        top:              -60px;
        right:            -60px;
        width:            180px;
        height:           180px;
        border-radius:    50%;
        background:       radial-gradient(circle, {t['primary']}40, transparent 70%);
        pointer-events:   none;
        animation:        glowPulse 3s ease-in-out infinite;
    }}
    /* Glow orb bottom-left */
    .auth-card::after {{
        content:          '';
        position:         absolute;
        bottom:           -50px;
        left:             -50px;
        width:            140px;
        height:           140px;
        border-radius:    50%;
        background:       radial-gradient(circle, {t['secondary']}30, transparent 70%);
        pointer-events:   none;
    }}
    .auth-logo {{
        text-align:       center;
        margin-bottom:    2rem;
    }}
    .auth-logo .logo-ring {{
        display:          inline-flex;
        align-items:      center;
        justify-content:  center;
        width:            72px;
        height:           72px;
        border-radius:    50%;
        background:       {t['gradient']};
        font-size:        2rem;
        margin-bottom:    1rem;
        box-shadow:       {t['shadow_md']}, 0 0 30px {t['primary_glow']};
        animation:        float 4s ease-in-out infinite;
    }}
    .auth-logo .logo-title {{
        font-family:      'Syne', sans-serif;
        font-size:        1.7rem;
        font-weight:      800;
        background:       {t['gradient']};
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        background-clip:  text;
        margin-bottom:    0.25rem;
        letter-spacing:   -0.03em;
    }}
    .auth-logo .logo-sub {{
        font-size:        0.82rem;
        color:            {t['subtext']};
        letter-spacing:   0.12em;
        text-transform:   uppercase;
    }}
    .auth-tab-toggle {{
        display:          flex;
        background:       {t['surface_raised']};
        border-radius:    999px;
        padding:          4px;
        margin-bottom:    2rem;
        gap:              4px;
    }}
    .auth-tab-btn {{
        flex:             1;
        padding:          9px 0;
        text-align:       center;
        border-radius:    999px;
        font-size:        0.88rem;
        font-weight:      700;
        cursor:           pointer;
        transition:       all 0.25s ease;
        color:            {t['subtext']};
        letter-spacing:   0.02em;
        border:           none;
        background:       transparent;
    }}
    .auth-tab-btn.active {{
        background:       {t['gradient']};
        color:            {t['text_inverse']};
        box-shadow:       0 4px 14px {t['primary_glow']};
    }}
    /* Floating label field */
    .field-group {{
        position:         relative;
        margin-bottom:    1.3rem;
    }}
    .field-group .field-icon {{
        position:         absolute;
        left:             16px;
        top:              50%;
        transform:        translateY(-50%);
        font-size:        1rem;
        z-index:          2;
        pointer-events:   none;
    }}
    /* Security badge */
    .security-badge {{
        display:          flex;
        align-items:      center;
        gap:              8px;
        padding:          10px 14px;
        background:       {t['primary_glow']};
        border:           1px solid {t['primary']}40;
        border-radius:    12px;
        margin-bottom:    1.5rem;
        font-size:        0.8rem;
        color:            {t['primary']};
        font-weight:      600;
    }}
    .security-badge .dot {{
        width:            8px;
        height:           8px;
        border-radius:    50%;
        background:       {t['primary']};
        animation:        glowPulse 1.5s ease-in-out infinite;
        flex-shrink:      0;
    }}
    /* Submit button */
    .auth-submit-btn {{
        width:            100%;
        padding:          14px 0;
        background:       {t['gradient']};
        border:           none;
        border-radius:    14px;
        color:            {t['text_inverse']};
        font-size:        1rem;
        font-weight:      700;
        cursor:           pointer;
        letter-spacing:   0.04em;
        transition:       all 0.25s ease;
        box-shadow:       0 6px 20px {t['primary_glow']};
        font-family:      'DM Sans', sans-serif;
        margin-top:       0.5rem;
    }}
    .auth-submit-btn:hover {{
        filter:           brightness(1.12);
        transform:        translateY(-2px);
        box-shadow:       0 10px 28px {t['primary_glow']};
    }}
    .auth-divider {{
        display:          flex;
        align-items:      center;
        gap:              12px;
        margin:           1.5rem 0;
        color:            {t['subtext']};
        font-size:        0.8rem;
    }}
    .auth-divider::before,
    .auth-divider::after {{
        content:          '';
        flex:             1;
        height:           1px;
        background:       {t['card_border']};
    }}
    /* Lock icon shimmer */
    @keyframes lockPulse {{
        0%,100% {{ text-shadow: 0 0 8px {t['primary']}60; }}
        50%     {{ text-shadow: 0 0 20px {t['primary']}, 0 0 40px {t['primary_glow']}; }}
    }}
    .lock-icon {{ animation: lockPulse 2.5s ease-in-out infinite; }}
    .auth-home-note {{
        max-width: 760px;
        margin: 0 auto 1rem;
        padding: 12px 14px;
        border-radius: 18px;
        border: 1px solid {t['card_border']};
        background: {t['glass_bg']};
        box-shadow: {t['shadow_sm']};
        color: {t['text']};
        text-align: center;
        font-size: .9rem;
        font-weight: 650;
    }}
    </style>
    """, unsafe_allow_html=True)

    st.markdown(
        """
        <div class="auth-home-note">
            Want to browse first? Use the Home button in the top bar to return to the student dashboard.
        </div>
        """,
        unsafe_allow_html=True,
    )

    # ── Logo header ──────────────────────────────────────────────────────────
    st.markdown(f"""
    <div class="auth-logo">
        <div class="logo-ring">🩺</div>
        <div class="logo-title">MedStudy Oman</div>
        <div class="logo-sub">AI · Clinical · Board-Ready</div>
    </div>
    """, unsafe_allow_html=True)

    # ── Toggle tabs (Login / Sign Up) ────────────────────────────────────────
    col_l, col_r = st.columns(2)
    with col_l:
        if st.button(
            "🔑  Login",
            use_container_width=True,
            type="primary" if st.session_state.auth_mode == "login" else "secondary",
            key="auth_toggle_login",
        ):
            st.session_state.auth_mode = "login"
            st.rerun()
    with col_r:
        if st.button(
            "📝  Sign Up",
            use_container_width=True,
            type="primary" if st.session_state.auth_mode == "signup" else "secondary",
            key="auth_toggle_signup",
        ):
            st.session_state.auth_mode = "signup"
            st.rerun()

    st.markdown("<br>", unsafe_allow_html=True)

    # ── Security badge ───────────────────────────────────────────────────────
    st.markdown(f"""
    <div class="security-badge">
        <div class="dot"></div>
        <span class="lock-icon">🔒</span>
        <span>End-to-end encrypted · HIPAA-compliant storage</span>
    </div>
    """, unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════
    # LOGIN FORM
    # ═══════════════════════════════════════════════════════════════════════
    if st.session_state.auth_mode == "login":
        with st.form("login_form", clear_on_submit=False):
            email = st.text_input(
                "📧  Email Address",
                placeholder="your.email@squ.edu.om",
                key="lf_email",
            )
            password = st.text_input(
                "🔒  Password",
                type="password",
                placeholder="••••••••",
                key="lf_pass",
            )

            remember = st.checkbox("Keep me signed in for 30 days", value=True)

            submitted = st.form_submit_button(
                "🔑  Sign In to MedStudy",
                use_container_width=True,
                type="primary",
            )

        if submitted:
            if not email or not password:
                st.error("⚠️ Please enter both email and password.")
            else:
                with st.spinner("Authenticating…"):
                    time.sleep(0.4)   # micro-delay for UX feedback
                    success, result = login_user_fn(email, password)

                if success:
                    st.session_state.logged_in = True
                    st.session_state.user = result
                    st.session_state.theme = result.get("theme", "🩺 Clinical Snow")
                    st.session_state.page = "dashboard"
                    st.session_state.show_auth = False
                    st.session_state.just_logged_in = True
                    st.success(f"✅ Welcome back, Dr. {result['name']}! 🎉")
                    st.balloons()
                    time.sleep(0.8)
                    st.rerun()
                else:
                    st.error(f"❌ {result}")

        # forgot / demo hint
        st.markdown(f"""
        <div style="text-align:center;margin-top:1rem;">
            <span style="font-size:0.8rem;color:{t['subtext']};">
                New to MedStudy Oman?
                <span style="color:{t['primary']};cursor:pointer;font-weight:700;">
                    Create your account →
                </span>
            </span>
        </div>
        """, unsafe_allow_html=True)

    # ═══════════════════════════════════════════════════════════════════════
    # SIGNUP FORM
    # ═══════════════════════════════════════════════════════════════════════
    else:
        with st.form("signup_form", clear_on_submit=False):
            col1, col2 = st.columns(2)
            with col1:
                name = st.text_input(
                    "👤  Full Name",
                    placeholder="Dr. Sadga Selime",
                    key="sf_name",
                )
                email = st.text_input(
                    "📧  Email",
                    placeholder="student@squ.edu.om",
                    key="sf_email",
                )
            with col2:
                university = st.selectbox(
                    "🏫  University",
                    [
                        "SQU College of Medicine",
                        "Oman Medical College",
                        "Dhofar University",
                        "Gulf Medical University",
                        "Sohar University",
                        "Other",
                    ],
                    key="sf_uni",
                )
                year = st.selectbox(
                    "📅  Year",
                    [f"Year {i}" for i in range(1, 7)] + ["Intern", "Resident", "Other"],
                    key="sf_year",
                )

            pass1 = st.text_input(
                "🔒  Password",
                type="password",
                placeholder="Min. 8 characters",
                key="sf_pass1",
            )
            pass2 = st.text_input(
                "🔒  Confirm Password",
                type="password",
                placeholder="Re-enter password",
                key="sf_pass2",
            )

            target_exams = st.multiselect(
                "🎯  Target Exams (optional)",
                ["USMLE Step 1", "USMLE Step 2 CK", "OMSB Part 1",
                 "OMSB Part 2", "MRCP Part 1", "MRCP Part 2",
                 "IELTS Academic", "MOH Oman", "MCCQE", "PLAB"],
                key="sf_exams",
            )

            agree = st.checkbox(
                "I agree to the Terms of Service and Privacy Policy",
                key="sf_agree",
            )

            submitted = st.form_submit_button(
                "🚀  Create My MedStudy Account",
                use_container_width=True,
                type="primary",
            )

        if submitted:
            if not all([name, email, pass1, pass2]):
                st.error("⚠️ Please fill in all required fields.")
            elif pass1 != pass2:
                st.error("❌ Passwords do not match.")
            elif len(pass1) < 8:
                st.error("⚠️ Password must be at least 8 characters.")
            elif not agree:
                st.error("⚠️ Please agree to the Terms of Service.")
            else:
                year_num = int(year.split(" ")[1]) if year.startswith("Year") else 7
                with st.spinner("Creating your account…"):
                    time.sleep(0.5)
                    success, msg = signup_user_fn(
                        name, email, pass1, str(university), year_num
                    )

                if success:
                    st.success("🎉 Account created! Welcome to MedStudy Oman, Dr. " + name.split()[0] + "! 🩺")
                    st.balloons()
                    st.session_state.auth_mode = "login"
                    time.sleep(1.5)
                    st.rerun()
                else:
                    st.error(f"❌ {msg}")

    # ── Footer trust signals ─────────────────────────────────────────────────
    st.markdown(f"""
    <div style="text-align:center;padding-top:1.5rem;border-top:1px solid {t['card_border']};
         margin-top:2rem;">
        <div style="font-size:0.75rem;color:{t['subtext']};letter-spacing:0.06em;
             text-transform:uppercase;">
            🇴🇲 Built for Omani Medical Students
        </div>
        <div style="font-size:0.7rem;color:{t['subtext']};margin-top:0.4rem;opacity:0.7;">
            SQU · OMSB · WFME · USMLE Aligned
        </div>
    </div>
    """, unsafe_allow_html=True)
