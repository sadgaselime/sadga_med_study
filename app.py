            rows  = "".join(
                f'<div style="font-size:0.84rem;color:{theme["text"]};padding:0.4rem 0;'
                f'border-bottom:1px solid {theme["card_border"]};">● {e}</div>'
                for e in exams
            )
            st.markdown(
                f'<div style="background:{theme["glass_bg"]};border:1px solid {theme["glass_border"]};'
                f'border-radius:18px;padding:1.4rem;backdrop-filter:blur(12px);">'
                f'<div style="font-size:0.65rem;font-weight:800;color:{theme["primary"]};'
                f'letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.6rem;">Target Exams</div>'
                f'{rows}</div>',
                unsafe_allow_html=True,
            )

# ═════════════════════════════════════════════════════════════════════════════
# ROUTING
# ═════════════════════════════════════════════════════════════════════════════
page = st.session_state.page

if page == "auth":
    auth_page(theme, login_user, signup_user)

elif page == "home":
    home_page(theme, tr, MOTIVATIONAL_QUOTES)

elif page == "subjects":
    if "subjects_page" in globals():
        subjects_page(theme)
    else:
        _render_unavailable("Subjects", "subjects_page")

elif page == "flashcards":
    flashcards_page(theme)

elif page == "mnemonics":
    if "mnemonics_page" in globals():
        mnemonics_page(theme)
    else:
        _render_unavailable("Mnemonics", "mnemonics_page")

elif page == "mcq_quiz":
    mcq_quiz_page(theme)

elif page == "dashboard":
    db_stats = {}
    if st.session_state.logged_in:
        db_stats = get_user_stats(st.session_state.user["id"]) or {}
    else:
        st.info("📊 Showing demo data — login to see your personal analytics.")
    if "dashboard_page" in globals():
        dashboard_page(theme, db_stats)
    else:
        _render_unavailable("Dashboard", "dashboard_page")

elif page == "pomodoro":
    _render_pomodoro()

elif page == "osce_timer":
    if "osce_timer_page" in globals():
        osce_timer_page(theme)
    else:
        timer_page(theme)


elif page == "ai_tutor":
    ai_chat_tutor_page(theme)


elif page == "voice_ai":
    _page_header("🎤", tr("voice_ai"), "Hands-free studying powered by speech recognition")
    st.info("🎤 Voice AI — coming soon!")

elif page == "lab_game":
    if "lab_game_page" in globals():
        lab_game_page(theme)
    else:
        _render_unavailable("Lab Game", "lab_game")

elif page == "anatomy_3d":
    if "anatomy_3d_page" in globals():
        anatomy_3d_page(theme)
    else:
        _render_unavailable("3D Anatomy", "anatomy_3d")

elif page == "resources":
    if "resources_page" in globals():
        resources_page(theme)
    else:
        _render_unavailable("Resources", "resources_page")

elif page == "progress":
    if not st.session_state.logged_in:
        _require_login("progress")
    elif "progress_tracker_page" in globals():
        progress_tracker_page(theme, get_user_stats(st.session_state.user["id"]))
    else:
        _render_unavailable("Progress", "progress_tracker")

elif page == "study_groups":
    if "study_groups_page" in globals():
        study_groups_page(theme,
            st.session_state.user if st.session_state.logged_in else None)
    else:
        _render_unavailable("Study Groups", "study_groups")

elif page == "discussion":
    if "discussion_page" in globals():
        discussion_page(theme,
            st.session_state.user if st.session_state.logged_in else None)
    else:
        _render_unavailable("Forums", "discussion")

elif page == "shared_notes":
    if "shared_notes_page" in globals():
        shared_notes_page(theme,
            st.session_state.user if st.session_state.logged_in else None)
    else:
        _render_unavailable("Shared Notes", "shared_notes")

elif page == "leaderboards":
    if "leaderboards_page" in globals():
        leaderboards_page(theme,
            st.session_state.user if st.session_state.logged_in else None)
    else:
        _render_unavailable("Leaderboards", "leaderboards")

elif page == "tips":
    if "tips_page" in globals():
        tips_page(theme)
    else:
        _render_unavailable("Study Tips", "tips_page")

elif page == "profile":
    if not st.session_state.logged_in:
        _require_login("profile")
    else:
        _page_header("👤", tr("profile"),
                     f"Dr. {st.session_state.user['name']} · Academic Analytics")
        _render_profile()

elif page == "about":
    about_page(theme)

else:
    st.session_state.page = "home"
    st.rerun()

render_bottom_nav(theme)






