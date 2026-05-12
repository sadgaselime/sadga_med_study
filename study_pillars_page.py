"""
study_pillars_page.py - four core premium study pillars.
"""

from __future__ import annotations

import html

import streamlit as st

from ai_service import DEFAULT_ERROR, generate_mnemonic, generate_topic_module, get_ai_status, tutor_reply
from medical_data import get_subjects, get_topic, get_topics


def _safe(value) -> str:
    return html.escape(str(value or ""))


def _theme_value(theme: dict, key: str, fallback: str) -> str:
    return theme.get(key, fallback)


def _glass(theme: dict, body: str, border: str | None = None):
    st.markdown(
        f"""
        <div class="glass-card" style="border-left:4px solid {border or theme.get('primary', '#8b5cf6')};">
            {body}
        </div>
        """,
        unsafe_allow_html=True,
    )


def _render_module_tabs(module: dict, theme: dict, prefix: str):
    tabs = st.tabs(["Overview", "Detailed Notes", "High-Yield", "MCQs", "Flashcards"])
    with tabs[0]:
        _glass(theme, f"<p>{_safe(module.get('overview'))}</p>")
    with tabs[1]:
        notes = module.get("detailed_notes") or []
        for note in notes if isinstance(notes, list) else [notes]:
            st.markdown(f"- {_safe(note)}")
    with tabs[2]:
        for point in module.get("high_yield") or []:
            st.success(str(point))
    with tabs[3]:
        for i, mcq in enumerate(module.get("mcqs") or [], start=1):
            question = mcq.get("question") or mcq.get("stem") or f"Question {i}"
            with st.expander(f"Q{i}. {question}"):
                for option in mcq.get("options") or []:
                    st.markdown(f"- {option}")
                st.success(f"Answer: {mcq.get('answer') or mcq.get('correct_option') or mcq.get('correct')}")
                if mcq.get("explanation"):
                    st.caption(mcq["explanation"])
    with tabs[4]:
        for i, card in enumerate(module.get("flashcards") or [], start=1):
            front = card.get("front") or card.get("question") or f"Card {i}"
            with st.expander(front):
                st.write(card.get("back") or card.get("answer") or "")


def _render_static_vault(theme: dict):
    st.markdown("### Static Resource Vault")
    subjects = get_subjects()
    if not subjects:
        st.info("No local medical data is configured yet.")
        return
    col1, col2 = st.columns(2)
    with col1:
        subject = st.selectbox("Subject", subjects, key="vault_subject")
    with col2:
        topic = st.selectbox("Topic", get_topics(subject), key="vault_topic")
    module = get_topic(subject, topic)
    st.caption("Loaded instantly from local medical_data.py")
    _render_module_tabs(module, theme, "vault")


def _render_topic_generator(theme: dict):
    st.markdown("### Dynamic AI Topic Generator")
    status = get_ai_status()
    if not status["ready"]:
        st.warning("Add GEMINI_API_KEY or OPENAI_API_KEY to Streamlit secrets to enable live generation.")
    topic = st.text_input("Medical topic", placeholder="e.g. Acute pancreatitis, nephrotic syndrome, beta-blockers", key="ai_topic_input")
    if st.button("Generate Full Study Module", type="primary", use_container_width=True, key="generate_ai_topic"):
        if not topic.strip():
            st.warning("Type a topic first.")
        else:
            with st.spinner("Building a structured study module..."):
                module, error = generate_topic_module(topic.strip())
            if error:
                st.error(error)
            else:
                st.session_state.generated_topic_module = module
                st.session_state.generated_topic_name = topic.strip()
                st.success("Study module generated.")
    module = st.session_state.get("generated_topic_module")
    if module:
        st.markdown(f"#### {st.session_state.get('generated_topic_name', 'Generated Topic')}")
        _render_module_tabs(module, theme, "generated")


def _render_mnemonics(theme: dict):
    st.markdown("### AI Mnemonic Craftsman")
    facts = st.text_area(
        "Facts, symptoms, criteria, or drug list",
        placeholder="Paste the list you need to memorize, one item per line...",
        height=180,
        key="mnemonic_facts",
    )
    style = st.selectbox(
        "Mnemonic Style",
        ["Professional Academic", "Creative/Story", "Humorous"],
        key="mnemonic_style",
    )
    if st.button("Craft Mnemonic", type="primary", use_container_width=True, key="craft_mnemonic"):
        if not facts.strip():
            st.warning("Paste a list of facts first.")
        else:
            with st.spinner("Crafting a mapped acronym..."):
                st.session_state.crafted_mnemonic = generate_mnemonic(facts.strip(), style)
    result = st.session_state.get("crafted_mnemonic")
    if result:
        if result == DEFAULT_ERROR:
            st.error(result)
        else:
            _glass(theme, html.escape(result).replace("\n", "<br>"), _theme_value(theme, "warning", "#f59e0b"))


def _render_tutor(theme: dict):
    st.markdown("### Interactive AI Tutor")
    if "pillar_tutor_history" not in st.session_state:
        st.session_state.pillar_tutor_history = []
    for message in st.session_state.pillar_tutor_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])
    prompt = st.chat_input("Ask your Clinical Medicine Professor anything...")
    if prompt:
        st.session_state.pillar_tutor_history.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.markdown(prompt)
        with st.chat_message("assistant"):
            with st.spinner("Professor is thinking through the case..."):
                response = tutor_reply(st.session_state.pillar_tutor_history[:-1], prompt)
            st.markdown(response)
        st.session_state.pillar_tutor_history.append({"role": "assistant", "content": response})
    if st.session_state.pillar_tutor_history and st.button("Clear Tutor Chat", use_container_width=True, key="clear_pillar_tutor"):
        st.session_state.pillar_tutor_history = []
        st.rerun()


def study_pillars_page(theme: dict):
    st.markdown('<div class="section-title">Premium Study Pillars</div>', unsafe_allow_html=True)
    st.caption("Static library, on-demand AI modules, mnemonic crafting, and a conversational clinical tutor.")
    tabs = st.tabs(["Resource Vault", "AI Topic Generator", "Mnemonic Craftsman", "AI Tutor"])
    with tabs[0]:
        _render_static_vault(theme)
    with tabs[1]:
        _render_topic_generator(theme)
    with tabs[2]:
        _render_mnemonics(theme)
    with tabs[3]:
        _render_tutor(theme)
