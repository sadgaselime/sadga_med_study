"""
ai_chat_page.py — MedStudy Oman 🩺
Phase 7: Floating AI Medical Tutor Panel
Gemini AI · Quick Prompts · Conversation History · Pathophysiology Engine
"""

import streamlit as st
import time
import datetime
import json
import requests


# ─────────────────────────────────────────────────────────────────────────────
# SYSTEM PROMPT  — specialised for Omani medical students
# ─────────────────────────────────────────────────────────────────────────────
SYSTEM_PROMPT = """You are MedBot, an expert AI Medical Tutor built specifically for Omani medical students.

Your expertise covers:
- SQU College of Medicine curriculum (Years 1–6)
- OMSB Part 1 & Part 2 board exam preparation
- USMLE Step 1 & Step 2 CK high-yield content
- MRCP Part 1 & 2 preparation
- MOH Oman clinical guidelines and tropical/Gulf medicine
- Oman-specific epidemiology (diabetes, hypertension, brucellosis, sickle cell, consanguinity disorders)

Your teaching style:
- Start with the mechanism/pathophysiology before clinical features
- Use mnemonics when helpful (mark them with 💡)
- Give clinical pearls for exams (mark with 🎯)
- Highlight Oman/Gulf relevance when applicable (mark with 🇴🇲)
- Use structured formats: Cause → Mechanism → Features → Diagnosis → Management
- Keep answers focused and high-yield
- For drug questions, always mention mechanism, side effects, and contraindications
- For clinical cases, use the SOAP format

Format rules:
- Use **bold** for drug names, diagnoses, and key terms
- Use bullet points for lists
- Use numbered lists for steps/management
- Keep responses concise but complete
- End complex topics with a "🎯 Key Pearl" section

You are NOT a substitute for clinical judgment. Always remind students to consult seniors and guidelines in real clinical scenarios."""


# ─────────────────────────────────────────────────────────────────────────────
# QUICK PROMPTS
# ─────────────────────────────────────────────────────────────────────────────
QUICK_PROMPTS = [
    {
        "icon": "🧬", "label": "Pathophysiology",
        "color": "#e63946",
        "prompt": "Explain the pathophysiology of ",
        "placeholder": "e.g. DKA, heart failure, sepsis…",
    },
    {
        "icon": "💊", "label": "Drug Mechanism",
        "color": "#8b5cf6",
        "prompt": "Explain the mechanism of action, side effects, and clinical uses of ",
        "placeholder": "e.g. metformin, warfarin, furosemide…",
    },
    {
        "icon": "🔍", "label": "Differential Dx",
        "color": "#f97316",
        "prompt": "Give me a structured differential diagnosis for a patient presenting with ",
        "placeholder": "e.g. chest pain, fever + rash, haematuria…",
    },
    {
        "icon": "🏥", "label": "Management",
        "color": "#10b981",
        "prompt": "What is the evidence-based management for ",
        "placeholder": "e.g. STEMI, anaphylaxis, meningitis…",
    },
    {
        "icon": "🧪", "label": "Interpret Results",
        "color": "#0891b2",
        "prompt": "Help me interpret these results: ",
        "placeholder": "e.g. ABG: pH 7.2, pCO2 60, HCO3 24…",
    },
    {
        "icon": "🩺", "label": "OSCE Prep",
        "color": "#ec4899",
        "prompt": "Walk me through how to examine and present a patient with ",
        "placeholder": "e.g. heart failure, thyroid enlargement…",
    },
    {
        "icon": "📝", "label": "MCQ Explain",
        "color": "#d97706",
        "prompt": "Explain why the answer to this MCQ is correct and why the others are wrong: ",
        "placeholder": "Paste your MCQ here…",
    },
    {
        "icon": "🇴🇲", "label": "Oman Context",
        "color": "#16a34a",
        "prompt": "Tell me about ",
        "placeholder": "e.g. brucellosis, sickle cell in Oman, MOH guidelines…",
        "suffix": " in the context of Oman and the Gulf region, including local epidemiology and MOH guidelines.",
    },
]

# Subject context filters
SUBJECT_FILTERS = [
    "General", "Cardiology", "Neurology", "Pulmonology", "Gastroenterology",
    "Nephrology", "Endocrinology", "Haematology", "Infectious Disease",
    "Pharmacology", "Pathology", "Anatomy", "Physiology", "Biochemistry",
    "Psychiatry", "Surgery", "Obstetrics & Gynaecology", "Paediatrics",
    "Radiology", "Emergency Medicine",
]


# ─────────────────────────────────────────────────────────────────────────────
# THEME HELPERS — safe getters for keys that may not exist in all themes
# ─────────────────────────────────────────────────────────────────────────────
def _t(theme: dict, key: str, fallback: str = "") -> str:
    """Safe theme key getter with sensible fallbacks."""
    if key in theme:
        return theme[key]
    fallbacks = {
        "text_muted":  theme.get("subtext", "rgba(255,255,255,0.45)"),
        "shadow_sm":   f"0 2px 8px rgba(0,0,0,0.15)",
        "focus_ring":  f"0 0 0 3px {theme.get('primary', '#06b6d4')}40",
    }
    return fallbacks.get(key, fallback)


# ─────────────────────────────────────────────────────────────────────────────
# GEMINI API CALL
# ─────────────────────────────────────────────────────────────────────────────
def _call_gemini(messages: list, api_key: str) -> str:
    """Call Gemini 1.5 Flash via REST API."""
    url = (
        f"https://generativelanguage.googleapis.com/v1beta/models/"
        f"gemini-1.5-flash:generateContent?key={api_key}"
    )

    # Convert chat history to Gemini format
    contents = []
    for msg in messages:
        role = "user" if msg["role"] == "user" else "model"
        contents.append({"role": role, "parts": [{"text": msg["content"]}]})

    payload = {
        "contents": contents,
        "systemInstruction": {"parts": [{"text": SYSTEM_PROMPT}]},
        "generationConfig": {
            "temperature":     0.7,
            "topP":            0.9,
            "maxOutputTokens": 1500,
        },
    }

    try:
        resp = requests.post(url, json=payload, timeout=30)
        resp.raise_for_status()
        data = resp.json()
        return data["candidates"][0]["content"]["parts"][0]["text"]
    except requests.exceptions.Timeout:
        return "⏱️ Request timed out. Please try again."
    except requests.exceptions.HTTPError as e:
        if resp.status_code == 400:
            return "❌ Invalid API key. Please check your GEMINI_API_KEY in .streamlit/secrets.toml"
        return f"❌ API error ({resp.status_code}). Please try again."
    except Exception as e:
        return f"❌ Error: {str(e)}"


def _get_api_key() -> str | None:
    """Try to get Gemini API key from secrets or existing ai_features module."""
    try:
        return st.secrets.get("GEMINI_API_KEY") or st.secrets.get("gemini_api_key")
    except Exception:
        pass
    # Try from ai_features.py
    try:
        import ai_features
        return getattr(ai_features, "API_KEY", None) or getattr(ai_features, "api_key", None)
    except Exception:
        pass
    return None


# ─────────────────────────────────────────────────────────────────────────────
# SESSION STATE
# ─────────────────────────────────────────────────────────────────────────────
def _init_chat_state():
    if "ai_messages"       not in st.session_state:
        st.session_state.ai_messages = []
    if "ai_subject_filter" not in st.session_state:
        st.session_state.ai_subject_filter = "General"
    if "ai_quick_input"    not in st.session_state:
        st.session_state.ai_quick_input = ""
    if "ai_total_tokens"   not in st.session_state:
        st.session_state.ai_total_tokens = 0
    if "ai_msg_count"      not in st.session_state:
        st.session_state.ai_msg_count = 0


# ─────────────────────────────────────────────────────────────────────────────
# MAIN ENTRY
# ─────────────────────────────────────────────────────────────────────────────
def ai_tutor_page(theme: dict = None):
    """Full AI Medical Tutor chat page — Phase 7."""
    if theme is None:
        from styles import THEMES
        theme = THEMES.get(
            st.session_state.get("theme", "🩺 Clinical Snow"),
            list(THEMES.values())[0]
        )

    _init_chat_state()
    _inject_chat_css(theme)

    api_key = _get_api_key()

    # Resolve potentially missing theme keys once
    text_muted = _t(theme, "text_muted")

    # ── Page header ───────────────────────────────────────────────────────────
    h_col, btn_col = st.columns([5, 2])
    with h_col:
        st.markdown(
            f'<div style="display:flex;align-items:center;gap:14px;margin-bottom:0.4rem;">'
            f'<div style="width:52px;height:52px;border-radius:16px;'
            f'background:linear-gradient(135deg,#06b6d4,#8b5cf6);'
            f'display:flex;align-items:center;justify-content:center;font-size:1.7rem;'
            f'box-shadow:0 4px 20px rgba(139,92,246,0.35);">🤖</div>'
            f'<div>'
            f'<div style="font-family:Syne,sans-serif;font-size:1.8rem;font-weight:900;'
            f'color:{theme["text"]};letter-spacing:-0.03em;">AI Medical Tutor</div>'
            f'<div style="font-size:0.8rem;color:{theme["subtext"]};margin-top:1px;">'
            f'Powered by Gemini · Specialised for Omani medical students · OMSB · USMLE'
            f'</div></div></div>',
            unsafe_allow_html=True,
        )

    with btn_col:
        st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)
        c1, c2 = st.columns(2)
        with c1:
            if st.button("🗑️ Clear", use_container_width=True, key="ai_clear"):
                st.session_state.ai_messages    = []
                st.session_state.ai_msg_count   = 0
                st.session_state.ai_total_tokens = 0
                st.rerun()
        with c2:
            msgs = len(st.session_state.ai_messages)
            st.markdown(
                f'<div style="background:{theme["glass_bg"]};'
                f'border:1px solid {theme["card_border"]};border-radius:12px;'
                f'padding:0.45rem 0.8rem;font-size:0.78rem;color:{text_muted};'
                f'text-align:center;">{msgs // 2} exchanges</div>',
                unsafe_allow_html=True,
            )

    # ── No API key warning ────────────────────────────────────────────────────
    if not api_key:
        st.markdown(f"""
        <div style="background:{theme['warning']}15;border:1.5px solid {theme['warning']}50;
             border-radius:16px;padding:1rem 1.4rem;margin-bottom:1rem;">
            <div style="font-weight:800;color:{theme['warning']};margin-bottom:0.3rem;">
                ⚠️ Gemini API Key Not Found</div>
            <div style="font-size:0.85rem;color:{theme['text']};">
                Add your key to <code>.streamlit/secrets.toml</code>:<br>
                <code>GEMINI_API_KEY = "your-key-here"</code><br>
                Get a free key at
                <strong>aistudio.google.com</strong>
            </div>
        </div>
        """, unsafe_allow_html=True)

    # ── Main layout: Chat | Controls ──────────────────────────────────────────
    col_chat, col_ctrl = st.columns([3, 1.4])

    with col_ctrl:
        _render_controls(theme, api_key)

    with col_chat:
        _render_chat_area(theme)
        _render_input_area(theme, api_key)


# ─────────────────────────────────────────────────────────────────────────────
# CONTROLS PANEL  (right side)
# ─────────────────────────────────────────────────────────────────────────────
def _render_controls(theme: dict, api_key):
    text_muted = _t(theme, "text_muted")

    # Subject context filter
    st.markdown(
        f'<div style="font-size:0.7rem;font-weight:800;color:{theme["subtext"]};'
        f'letter-spacing:0.12em;text-transform:uppercase;margin-bottom:6px;">Subject Context</div>',
        unsafe_allow_html=True,
    )
    subj = st.selectbox(
        "Subject",
        SUBJECT_FILTERS,
        index=SUBJECT_FILTERS.index(st.session_state.ai_subject_filter),
        key="ai_subj_sel",
    )
    if subj != st.session_state.ai_subject_filter:
        st.session_state.ai_subject_filter = subj

    st.markdown(f"<div style='height:0.8rem'></div>", unsafe_allow_html=True)

    # Quick prompts
    st.markdown(
        f'<div style="font-size:0.7rem;font-weight:800;color:{theme["subtext"]};'
        f'letter-spacing:0.12em;text-transform:uppercase;margin-bottom:8px;">Quick Prompts</div>',
        unsafe_allow_html=True,
    )

    for qp in QUICK_PROMPTS:
        col_btn, = st.columns([1])
        st.markdown(
            f'<div style="background:{qp["color"]}12;border:1px solid {qp["color"]}35;'
            f'border-radius:10px;padding:0.5rem 0.8rem;margin-bottom:6px;'
            f'display:flex;align-items:center;gap:8px;">'
            f'<span style="font-size:1.1rem;">{qp["icon"]}</span>'
            f'<span style="font-size:0.8rem;font-weight:700;color:{qp["color"]};">'
            f'{qp["label"]}</span>'
            f'</div>',
            unsafe_allow_html=True,
        )
        if st.button(
            qp["label"],
            key=f"qp_{qp['label']}",
            use_container_width=True,
        ):
            st.session_state.ai_quick_input = qp["prompt"]
            st.rerun()

    st.markdown(f"<div style='height:0.8rem'></div>", unsafe_allow_html=True)

    # Session stats
    msgs  = len(st.session_state.ai_messages)
    turns = msgs // 2
    st.markdown(f"""
    <div style="background:{theme['glass_bg']};border:1px solid {theme['card_border']};
         border-radius:14px;padding:0.9rem;backdrop-filter:blur(10px);">
        <div style="font-size:0.68rem;font-weight:800;color:{theme['subtext']};
             letter-spacing:0.12em;text-transform:uppercase;margin-bottom:0.6rem;">
             Session Stats</div>
        <div style="font-size:0.8rem;color:{text_muted};line-height:2;">
            💬 {turns} exchanges<br>
            📚 {st.session_state.ai_subject_filter}<br>
            {'✅ API Connected' if api_key else '❌ No API Key'}<br>
            🕐 {datetime.datetime.now().strftime('%H:%M')}
        </div>
    </div>
    """, unsafe_allow_html=True)

    # Tips
    st.markdown(f"""
    <div style="background:{theme['primary']}10;border:1px solid {theme['primary']}30;
         border-radius:14px;padding:0.9rem;margin-top:0.8rem;">
        <div style="font-size:0.68rem;font-weight:800;color:{theme['primary']};
             letter-spacing:0.10em;text-transform:uppercase;margin-bottom:0.5rem;">
             💡 Tips</div>
        <div style="font-size:0.75rem;color:{text_muted};line-height:1.7;">
            • Ask about drug mechanisms<br>
            • Request differential diagnoses<br>
            • Get OSCE examination guides<br>
            • Paste MCQs for explanation<br>
            • Ask for Oman-specific context
        </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# CHAT AREA
# ─────────────────────────────────────────────────────────────────────────────
def _render_chat_area(theme: dict):
    shadow_sm = _t(theme, "shadow_sm")

    # Chat container
    st.markdown(
        f'<div style="background:{theme["glass_bg"]};border:1px solid {theme["card_border"]};'
        f'border-radius:20px;padding:1.2rem 1.4rem;backdrop-filter:blur(16px);'
        f'min-height:420px;max-height:520px;overflow-y:auto;" id="chat-container">',
        unsafe_allow_html=True,
    )

    messages = st.session_state.ai_messages

    if not messages:
        # Welcome state
        st.markdown(f"""
        <div style="text-align:center;padding:3rem 2rem;">
            <div style="font-size:3.5rem;margin-bottom:1rem;
                 animation:float 3s ease-in-out infinite;">🤖</div>
            <div style="font-family:Syne,sans-serif;font-size:1.3rem;font-weight:900;
                 color:{theme['text']};margin-bottom:0.5rem;">
                 Hello, Doctor 👋</div>
            <div style="font-size:0.88rem;color:{theme['subtext']};
                 line-height:1.7;max-width:380px;margin:0 auto;">
                 I'm your AI Medical Tutor, specialised for Omani medical students.
                 Ask me anything about pathophysiology, drugs, clinical cases, or OSCE prep.
            </div>
            <div style="margin-top:1.5rem;display:flex;gap:8px;justify-content:center;
                 flex-wrap:wrap;">
                <span style="background:{theme['primary']}15;color:{theme['primary']};
                      border-radius:999px;padding:4px 12px;font-size:0.74rem;font-weight:700;">
                      OMSB Ready</span>
                <span style="background:#10b98115;color:#10b981;border-radius:999px;
                      padding:4px 12px;font-size:0.74rem;font-weight:700;">USMLE Aligned</span>
                <span style="background:#8b5cf615;color:#8b5cf6;border-radius:999px;
                      padding:4px 12px;font-size:0.74rem;font-weight:700;">Gemini AI</span>
            </div>
        </div>
        """, unsafe_allow_html=True)
    else:
        for msg in messages:
            role    = msg["role"]
            content = msg["content"]
            ts      = msg.get("time", "")

            if role == "user":
                st.markdown(f"""
                <div style="display:flex;justify-content:flex-end;margin-bottom:1rem;">
                    <div style="max-width:75%;">
                        <div style="background:{theme['primary']};color:white;
                             border-radius:18px 18px 4px 18px;padding:0.8rem 1.1rem;
                             font-size:0.88rem;line-height:1.6;font-weight:500;
                             box-shadow:0 4px 16px {theme['primary_glow']};">
                             {content}
                        </div>
                        <div style="text-align:right;font-size:0.65rem;
                             color:{theme['subtext']};margin-top:3px;">{ts} · You</div>
                    </div>
                    <div style="width:32px;height:32px;border-radius:50%;
                         background:{theme['primary']};display:flex;align-items:center;
                         justify-content:center;margin-left:8px;flex-shrink:0;
                         font-size:0.9rem;align-self:flex-end;">👤</div>
                </div>
                """, unsafe_allow_html=True)

            else:  # assistant
                st.markdown(f"""
                <div style="display:flex;justify-content:flex-start;margin-bottom:1.2rem;">
                    <div style="width:32px;height:32px;border-radius:50%;
                         background:linear-gradient(135deg,#06b6d4,#8b5cf6);
                         display:flex;align-items:center;justify-content:center;
                         margin-right:8px;flex-shrink:0;font-size:0.9rem;
                         align-self:flex-start;margin-top:4px;
                         box-shadow:0 2px 8px rgba(139,92,246,0.3);">🤖</div>
                    <div style="max-width:80%;">
                        <div style="background:{theme['card_bg']};
                             border:1px solid {theme['card_border']};
                             border-radius:4px 18px 18px 18px;padding:1rem 1.2rem;
                             font-size:0.87rem;line-height:1.7;
                             color:{theme['text']};
                             box-shadow:{shadow_sm};">
                             {_md_to_html(content, theme)}
                        </div>
                        <div style="font-size:0.65rem;color:{theme['subtext']};
                             margin-top:3px;">{ts} · MedBot · {st.session_state.ai_subject_filter}</div>
                    </div>
                </div>
                """, unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)


def _md_to_html(text: str, theme: dict) -> str:
    """Convert basic markdown to HTML for display inside st.markdown."""
    import re

    # Bold
    text = re.sub(r'\*\*(.*?)\*\*', r'<strong>\1</strong>', text)
    # Italic
    text = re.sub(r'\*(.*?)\*', r'<em>\1</em>', text)
    # Code inline
    text = re.sub(r'`(.*?)`',
                  lambda m: f'<code style="background:{theme["surface_raised"]};'
                            f'color:{theme["primary"]};border-radius:4px;'
                            f'padding:1px 5px;font-family:DM Mono,monospace;'
                            f'font-size:0.83em;">{m.group(1)}</code>',
                  text)
    # Numbered list items
    text = re.sub(r'^\d+\.\s+(.+)$',
                  lambda m: f'<div style="display:flex;gap:6px;margin-bottom:3px;">'
                            f'<span style="color:{theme["primary"]};font-weight:700;'
                            f'flex-shrink:0;">•</span><span>{m.group(1)}</span></div>',
                  text, flags=re.MULTILINE)
    # Bullet list items
    text = re.sub(r'^[-•]\s+(.+)$',
                  lambda m: f'<div style="display:flex;gap:6px;margin-bottom:3px;">'
                            f'<span style="color:{theme["primary"]};flex-shrink:0;">›</span>'
                            f'<span>{m.group(1)}</span></div>',
                  text, flags=re.MULTILINE)
    # Headers h3
    text = re.sub(r'^###\s+(.+)$',
                  lambda m: f'<div style="font-family:Syne,sans-serif;font-weight:800;'
                            f'font-size:0.95rem;color:{theme["text"]};margin:0.8rem 0 0.3rem;">'
                            f'{m.group(1)}</div>',
                  text, flags=re.MULTILINE)
    # Headers h2
    text = re.sub(r'^##\s+(.+)$',
                  lambda m: f'<div style="font-family:Syne,sans-serif;font-weight:900;'
                            f'font-size:1rem;color:{theme["primary"]};margin:0.9rem 0 0.4rem;">'
                            f'{m.group(1)}</div>',
                  text, flags=re.MULTILINE)
    # Newlines to br
    text = text.replace('\n\n', '<br><br>').replace('\n', '<br>')
    return text


# ─────────────────────────────────────────────────────────────────────────────
# INPUT AREA
# ─────────────────────────────────────────────────────────────────────────────
def _render_input_area(theme: dict, api_key):
    st.markdown("<div style='height:0.6rem'></div>", unsafe_allow_html=True)

    # Pre-fill from quick prompt
    default_val = st.session_state.get("ai_quick_input", "")

    with st.form("ai_chat_form", clear_on_submit=True):
        user_input = st.text_area(
            "Ask MedBot",
            value=default_val,
            placeholder="Ask about pathophysiology, drugs, clinical cases, OSCE prep, MCQs…",
            height=100,
            key="ai_input_field",
        )

        sc1, sc2, sc3 = st.columns([3, 1, 1])
        with sc1:
            subject_ctx = st.session_state.ai_subject_filter
            st.markdown(
                f'<div style="font-size:0.75rem;color:{theme["subtext"]};padding-top:0.5rem;">'
                f'Context: <strong style="color:{theme["primary"]};">{subject_ctx}</strong></div>',
                unsafe_allow_html=True,
            )
        with sc2:
            submitted = st.form_submit_button(
                "Send 🚀",
                use_container_width=True,
                type="primary",
            )
        with sc3:
            example = st.form_submit_button(
                "💡 Example",
                use_container_width=True,
            )

    # Reset quick input after render
    if st.session_state.get("ai_quick_input"):
        st.session_state.ai_quick_input = ""

    # Handle example button
    if example:
        examples = [
            "Explain the pathophysiology of diabetic ketoacidosis step by step.",
            "What is the mechanism of action of metformin and why is it first-line for T2DM?",
            "Give me a differential diagnosis for a 30-year-old with haemoptysis.",
            "Walk me through STEMI management — door to balloon.",
            "Explain the renin-angiotensin-aldosterone system and where ACE inhibitors work.",
            "What is the difference between nephrotic and nephritic syndrome?",
            "How do I examine the cardiovascular system for an OSCE station?",
            "What are the common causes of brucellosis in Oman and how is it treated?",
        ]
        import random
        ex_msg = random.choice(examples)
        st.session_state.ai_messages.append({
            "role":    "user",
            "content": ex_msg,
            "time":    datetime.datetime.now().strftime("%H:%M"),
        })
        _get_ai_response(ex_msg, api_key, theme)
        st.rerun()

    # Handle submit
    if submitted and user_input.strip():
        user_text = user_input.strip()

        # Add subject context if not General
        if st.session_state.ai_subject_filter != "General":
            ctx_note = f" [Context: {st.session_state.ai_subject_filter}]"
            full_text = user_text + ctx_note
        else:
            full_text = user_text

        st.session_state.ai_messages.append({
            "role":    "user",
            "content": user_text,   # display without context note
            "time":    datetime.datetime.now().strftime("%H:%M"),
        })

        _get_ai_response(full_text, api_key, theme)
        st.rerun()


def _get_ai_response(user_text: str, api_key, theme: dict):
    """Call Gemini and append response to session state."""
    if not api_key:
        # Demo mode — helpful without API key
        demo_responses = [
            "**Demo Mode** 🔑\n\nTo unlock real AI responses, add your Gemini API key to `.streamlit/secrets.toml`:\n\n`GEMINI_API_KEY = \"your-key-here\"`\n\nGet a **free key** at [aistudio.google.com](https://aistudio.google.com)\n\n🎯 **Key Pearl:** Gemini 1.5 Flash is free for up to 15 requests/minute.",
            "**API Key Required** 🔑\n\nI'm MedBot, your AI Medical Tutor — but I need a Gemini API key to answer questions.\n\n**Setup:**\n1. Visit aistudio.google.com\n2. Create a free API key\n3. Add to `.streamlit/secrets.toml`\n4. Restart the app\n\n💡 *Free tier: 15 req/min, 1M tokens/day*",
        ]
        import random
        response = random.choice(demo_responses)
    else:
        # Build messages for API (only last 10 exchanges to stay within context)
        history = st.session_state.ai_messages[-20:]
        api_messages = [
            {"role": "user" if m["role"] == "user" else "assistant",
             "content": m["content"]}
            for m in history[:-1]  # exclude the message we just added
        ]
        api_messages.append({"role": "user", "content": user_text})

        with st.spinner("🤖 MedBot is thinking…"):
            response = _call_gemini(api_messages, api_key)

    st.session_state.ai_messages.append({
        "role":    "assistant",
        "content": response,
        "time":    datetime.datetime.now().strftime("%H:%M"),
    })
    st.session_state.ai_msg_count += 1


# ─────────────────────────────────────────────────────────────────────────────
# CSS
# ─────────────────────────────────────────────────────────────────────────────
def _inject_chat_css(t: dict):
    # Resolve missing keys with safe fallbacks
    text_muted = _t(t, "text_muted")
    focus_ring = _t(t, "focus_ring")

    st.markdown(f"""
    <style>
    /* Chat container scrollable */
    #chat-container {{
        scroll-behavior: smooth;
    }}

    /* AI message prose */
    .ai-message-body strong {{
        color: {t['primary']};
    }}
    .ai-message-body em {{
        color: {text_muted};
    }}

    /* Input area */
    .stTextArea textarea {{
        background:    {t['glass_bg']}  !important;
        border:        1.5px solid {t['card_border']} !important;
        border-radius: 14px !important;
        color:         {t['text']}      !important;
        font-size:     0.9rem           !important;
        resize:        none             !important;
        transition:    border-color 0.2s, box-shadow 0.2s !important;
    }}
    .stTextArea textarea:focus {{
        border-color: {t['primary']}   !important;
        box-shadow:   {focus_ring} !important;
    }}

    /* Quick prompt buttons (controls panel) */
    div[data-testid="column"] .stButton > button {{
        text-align: left !important;
    }}

    /* Floating bubble (decorative, bottom right) */
    .ai-float-bubble {{
        position:      fixed;
        bottom:        24px;
        right:         24px;
        width:         58px;
        height:        58px;
        border-radius: 50%;
        background:    linear-gradient(135deg, #06b6d4, #8b5cf6);
        display:       flex;
        align-items:   center;
        justify-content: center;
        font-size:     1.6rem;
        cursor:        pointer;
        box-shadow:    0 4px 24px rgba(139,92,246,0.45),
                       0 8px 48px rgba(6,182,212,0.20);
        z-index:       9999;
        animation:     bubblePulse 3s ease-in-out infinite;
        transition:    transform 0.25s ease;
    }}
    .ai-float-bubble:hover {{
        transform: scale(1.12);
    }}
    </style>
    """, unsafe_allow_html=True)

    # Floating decorative bubble (visual only)
    if st.session_state.get("page") != "ai_tutor":
        st.markdown(
            '<div class="ai-float-bubble" title="AI Medical Tutor">🤖</div>',
            unsafe_allow_html=True,
        )


def ai_tutor_page(theme: dict = None):
    """Interactive AI Tutor using native Streamlit chat components."""
    from ai_service import get_ai_status, tutor_reply

    if theme is None:
        from styles import THEMES
        theme = THEMES.get(
            st.session_state.get("theme", "🌸 Light Lavender"),
            list(THEMES.values())[0],
        )

    st.markdown(
        f"""
        <div class="glass-card" style="margin-bottom:1rem;">
            <div style="font-family:Syne,sans-serif;font-size:1.55rem;font-weight:900;color:{theme['text']};">
                AI Clinical Medicine Professor
            </div>
            <div style="color:{theme['subtext']};font-size:0.9rem;">
                Encouraging diagnostic reasoning, mechanisms-first explanations, and exam-ready clinical breakdowns.
            </div>
        </div>
        """,
        unsafe_allow_html=True,
    )

    if "ai_chat_history" not in st.session_state:
        st.session_state.ai_chat_history = []

    status = get_ai_status()
    if not status["ready"]:
        st.warning("Add GEMINI_API_KEY or OPENAI_API_KEY to Streamlit secrets to unlock live tutor responses.")

    top_col, clear_col = st.columns([4, 1])
    with top_col:
        st.caption(f"Provider: {status['provider']}")
    with clear_col:
        if st.session_state.ai_chat_history and st.button("Clear", use_container_width=True, key="native_ai_clear"):
            st.session_state.ai_chat_history = []
            st.rerun()

    for message in st.session_state.ai_chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    user_input = st.chat_input("Ask about a symptom, disease, drug, investigation, OSCE case, or MCQ...")
    if user_input:
        st.session_state.ai_chat_history.append({"role": "user", "content": user_input})
        with st.chat_message("user"):
            st.markdown(user_input)
        with st.chat_message("assistant"):
            with st.spinner("Thinking clinically..."):
                response = tutor_reply(st.session_state.ai_chat_history[:-1], user_input)
            st.markdown(response)
        st.session_state.ai_chat_history.append({"role": "assistant", "content": response})
