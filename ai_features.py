"""
ai_features.py — All AI-powered features using Google Gemini API.
Handles: AI Tutor, AI Quiz Generator, AI Flashcard Generator,
AI Mnemonic Generator, AI Concept Explainer with diagrams.
"""

import streamlit as st
import json
import re

# ── Try to import Gemini ──
try:
    import google.generativeai as genai
    GEMINI_AVAILABLE = True
except ImportError:
    GEMINI_AVAILABLE = False


# ══════════════════════════════════════════════════════
# SETUP GEMINI
# ══════════════════════════════════════════════════════
def get_gemini_model():
    """
    Initialises and returns Gemini model.
    API key is stored in .streamlit/secrets.toml
    """
    if not GEMINI_AVAILABLE:
        return None

    try:
        api_key = st.secrets.get("GEMINI_API_KEY", "")
        if not api_key:
            return None
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel(
            model_name="gemini-1.5-flash",
            generation_config={
                "temperature": 0.7,
                "max_output_tokens": 1500,
            }
        )
        return model
    except Exception as e:
        st.error(f"Gemini setup error: {e}")
        return None


def call_gemini(prompt, system_context=""):
    """
    Calls Gemini API with a prompt.
    Returns response text or None on failure.
    """
    model = get_gemini_model()
    if not model:
        return None

    try:
        full_prompt = f"{system_context}\n\n{prompt}" if system_context else prompt
        response = model.generate_content(full_prompt)
        return response.text
    except Exception as e:
        st.error(f"AI error: {str(e)}")
        return None


# ══════════════════════════════════════════════════════
# AI TUTOR — CHAT INTERFACE
# ══════════════════════════════════════════════════════

TUTOR_SYSTEM_PROMPT = """
You are Dr. Aisha, a brilliant, warm, and experienced Senior Medical Consultant 
and Educator at Sultan Qaboos University Hospital (SQUH) in Muscat, Oman.

Your role is to help Omani medical students (primarily from SQU) understand 
medicine deeply and pass their exams.

Your teaching style:
- Always explain the PATHOPHYSIOLOGY first (why does this happen?)
- Use clinical cases and relatable examples
- Connect theory to real Omani clinical practice
- Reference local context (SQUH protocols, common Omani diseases like Brucellosis, Sickle cell)
- Use analogies to make complex topics simple
- Always end with HIGH-YIELD exam tips
- Format your responses clearly with sections
- Be encouraging and motivating — medical school is hard!
- If asked to draw diagrams, create them using ASCII art or clear text-based representations
- Include mnemonics whenever helpful
- Keep responses focused and clinically relevant

When explaining anatomy: use body landmarks and clinical correlations
When explaining physiology: use step-by-step mechanisms
When explaining pathology: explain what goes wrong at cellular level first
When explaining pharmacology: always cover mechanism, indication, side effects

You are NOT just a chatbot — you are their personal medical mentor.
"""

def ai_tutor_page():
    """Renders the AI Tutor chat page."""
    t = _get_theme()

    st.markdown(f'<h1 style="color:{t["text"]}">🤖 AI Senior Consultant — Dr. Aisha</h1>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:{t["subtext"]}">Your personal medical mentor, available 24/7 — Powered by Gemini AI</p>', unsafe_allow_html=True)

    # Check API setup
    if not _check_api():
        _show_api_setup_instructions()
        return

    # Initialise chat history
    if "ai_chat_history" not in st.session_state:
        st.session_state.ai_chat_history = []

    # Suggested questions
    if not st.session_state.ai_chat_history:
        st.markdown("### 💡 Try asking Dr. Aisha:")
        suggestions = [
            "Explain the pathophysiology of heart failure with a diagram",
            "What are the ECG changes in hyperkalaemia?",
            "Give me a mnemonic for the causes of clubbing",
            "Explain how ACE inhibitors work step by step",
            "What's the difference between Crohn's disease and UC?",
            "How does the kidney regulate blood pressure?",
            "Explain sepsis pathophysiology like I'm a 3rd year student",
            "What are the Omani-specific diseases I must know for finals?",
        ]
        cols = st.columns(2)
        for i, sug in enumerate(suggestions):
            with cols[i % 2]:
                if st.button(f"💬 {sug}", key=f"sug_{i}", use_container_width=True):
                    st.session_state.ai_chat_history.append({"role": "user", "content": sug})
                    with st.spinner("Dr. Aisha is thinking... 🩺"):
                        response = _get_tutor_response(sug, st.session_state.ai_chat_history[:-1])
                    if response:
                        st.session_state.ai_chat_history.append({"role": "assistant", "content": response})
                    st.rerun()

    # Display chat history
    chat_container = st.container()
    with chat_container:
        for msg in st.session_state.ai_chat_history:
            if msg["role"] == "user":
                with st.chat_message("user", avatar="🧑‍⚕️"):
                    st.markdown(msg["content"])
            else:
                with st.chat_message("assistant", avatar="👩‍⚕️"):
                    st.markdown(msg["content"])

    # Chat input
    if user_input := st.chat_input("Ask Dr. Aisha anything about medicine..."):
        st.session_state.ai_chat_history.append({"role": "user", "content": user_input})

        with st.chat_message("user", avatar="🧑‍⚕️"):
            st.markdown(user_input)

        with st.chat_message("assistant", avatar="👩‍⚕️"):
            with st.spinner("Dr. Aisha is thinking... 🩺"):
                response = _get_tutor_response(user_input, st.session_state.ai_chat_history[:-1])
            if response:
                st.markdown(response)
                st.session_state.ai_chat_history.append({"role": "assistant", "content": response})
            else:
                st.error("Sorry, I couldn't get a response. Please check your API key.")

    # Clear chat button
    if st.session_state.ai_chat_history:
        col1, col2, col3 = st.columns([1, 1, 1])
        with col2:
            if st.button("🗑️ Clear Chat", use_container_width=True):
                st.session_state.ai_chat_history = []
                st.rerun()


def _get_tutor_response(user_message, history):
    """Gets AI tutor response considering chat history."""
    # Build conversation context from history
    history_text = ""
    for msg in history[-6:]:  # Last 3 exchanges for context
        role = "Student" if msg["role"] == "user" else "Dr. Aisha"
        history_text += f"{role}: {msg['content']}\n\n"

    prompt = f"""
{TUTOR_SYSTEM_PROMPT}

Previous conversation:
{history_text}

Student's question: {user_message}

Please provide a thorough, educational response as Dr. Aisha.
"""
    return call_gemini(prompt)


# ══════════════════════════════════════════════════════
# AI QUIZ GENERATOR
# ══════════════════════════════════════════════════════

def ai_quiz_page():
    """Renders the AI Quiz Generator page."""
    t = _get_theme()

    st.markdown(f'<h1 style="color:{t["text"]}">🧪 AI Quiz Generator</h1>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:{t["subtext"]}">Generate custom MCQs on ANY medical topic instantly</p>', unsafe_allow_html=True)

    if not _check_api():
        _show_api_setup_instructions()
        return

    col1, col2, col3 = st.columns(3)
    with col1:
        topic = st.text_input("📚 Topic", placeholder="e.g. Aortic stenosis, DKA, Malaria")
    with col2:
        difficulty = st.selectbox("🎯 Difficulty", ["Medical Student", "Intern Level", "Registrar Level"])
    with col3:
        num_questions = st.selectbox("🔢 Number of Questions", [1, 3, 5])

    subject = st.selectbox("📋 Subject (optional)", [
        "Any", "Cardiology", "Respiratory", "Neurology", "Gastroenterology",
        "Endocrinology", "Anatomy", "Physiology", "Pharmacology",
        "Microbiology", "Pathology", "Emergency Medicine", "Paediatrics",
        "Obstetrics", "Psychiatry", "Musculoskeletal"
    ])

    if st.button("⚡ Generate Quiz", type="primary", use_container_width=True):
        if not topic:
            st.warning("Please enter a topic first!")
            return

        with st.spinner(f"🤖 Generating {num_questions} question(s) on {topic}..."):
            questions = _generate_mcq_questions(topic, subject, difficulty, num_questions)

        if questions:
            st.session_state.ai_generated_quiz = questions
            st.session_state.ai_quiz_topic = topic
            st.session_state.ai_quiz_answered = [None] * len(questions)
            st.session_state.ai_quiz_submitted = [False] * len(questions)
            st.rerun()

    # Display generated quiz
    if "ai_generated_quiz" in st.session_state and st.session_state.ai_generated_quiz:
        st.markdown("---")
        st.markdown(f"### 📝 Quiz: {st.session_state.get('ai_quiz_topic', 'Custom Topic')}")

        for i, q in enumerate(st.session_state.ai_generated_quiz):
            st.markdown(f"""
            <div class="glass-card">
                <div style="font-weight:700; margin-bottom:1rem; color:{t['text']}">
                    Q{i+1}: {q.get('question', '')}
                </div>
            </div>
            """, unsafe_allow_html=True)

            answered = st.session_state.ai_quiz_answered[i]
            submitted = st.session_state.ai_quiz_submitted[i]

            if not submitted:
                selected = st.radio(
                    f"Select answer for Q{i+1}:",
                    q.get('options', []),
                    key=f"ai_q_{i}",
                    index=None,
                    label_visibility="collapsed"
                )
                if selected and st.button(f"✅ Submit Q{i+1}", key=f"sub_{i}"):
                    st.session_state.ai_quiz_answered[i] = selected
                    st.session_state.ai_quiz_submitted[i] = True
                    st.rerun()
            else:
                correct_idx = q.get('correct_index', 0)
                correct_ans = q['options'][correct_idx] if correct_idx < len(q.get('options', [])) else q.get('correct', '')
                user_ans = answered

                for j, opt in enumerate(q.get('options', [])):
                    if j == correct_idx:
                        st.markdown(f'<div style="background:rgba(16,185,129,0.15); border:2px solid #10b981; border-radius:10px; padding:0.7rem; margin:0.3rem 0; color:{t["text"]}">✅ {opt}</div>', unsafe_allow_html=True)
                    elif opt == user_ans and j != correct_idx:
                        st.markdown(f'<div style="background:rgba(239,68,68,0.15); border:2px solid #ef4444; border-radius:10px; padding:0.7rem; margin:0.3rem 0; color:{t["text"]}">❌ {opt}</div>', unsafe_allow_html=True)
                    else:
                        st.markdown(f'<div style="background:{t["card_bg"]}; border:1px solid {t["card_border"]}; border-radius:10px; padding:0.7rem; margin:0.3rem 0; color:{t["subtext"]}">{opt}</div>', unsafe_allow_html=True)

                with st.expander("📖 Explanation", expanded=True):
                    st.markdown(q.get('explanation', 'No explanation provided.'))
                    if q.get('tip'):
                        st.markdown(f"""
                        <div class="mnemonic-card">
                            🩺 <b>Senior Tip:</b> {q['tip']}
                        </div>
                        """, unsafe_allow_html=True)

        if all(st.session_state.ai_quiz_submitted):
            correct = sum(
                1 for i, q in enumerate(st.session_state.ai_generated_quiz)
                if st.session_state.ai_quiz_answered[i] == q['options'][q.get('correct_index', 0)]
            )
            total = len(st.session_state.ai_generated_quiz)
            pct = round(correct / total * 100) if total > 0 else 0

            st.markdown(f"""
            <div class="glass-card" style="text-align:center; margin-top:1rem">
                <div style="font-size:2rem">{'🏆' if pct >= 80 else '👍' if pct >= 60 else '📚'}</div>
                <div style="font-size:1.5rem; font-weight:800; color:{t['primary']}">{correct}/{total} — {pct}%</div>
                <div style="color:{t['subtext']}">AI Quiz Complete!</div>
            </div>
            """, unsafe_allow_html=True)

            if st.button("🔄 Generate New Quiz", type="primary", use_container_width=True):
                del st.session_state.ai_generated_quiz
                st.rerun()


def _generate_mcq_questions(topic, subject, difficulty, num):
    """Generates MCQ questions using Gemini."""
    prompt = f"""
You are a medical exam question writer for {difficulty} level.
Generate exactly {num} high-quality MCQ(s) about: "{topic}"
Subject area: {subject}

For EACH question, return ONLY valid JSON in this exact format (no extra text, no markdown):

[
  {{
    "question": "The full clinical scenario question here",
    "options": ["Option A here", "Option B here", "Option C here", "Option D here"],
    "correct_index": 0,
    "explanation": "Detailed explanation of why the correct answer is right and why others are wrong",
    "tip": "A senior doctor exam tip or clinical pearl"
  }}
]

Rules:
- Make questions clinical and scenario-based (not just factual)
- Include realistic patient presentations with age, gender, symptoms
- All 4 options should be plausible (no obviously wrong answers)
- correct_index is 0-based (0=A, 1=B, 2=C, 3=D)
- Explanation should cover pathophysiology
- Tip should be a high-yield clinical pearl
- For {difficulty}: {'basic mechanisms and common presentations' if 'Student' in difficulty else 'complex differentials and management decisions' if 'Registrar' in difficulty else 'clinical management and complications'}

Return ONLY the JSON array, nothing else.
"""
    response = call_gemini(prompt)
    if not response:
        return None

    try:
        # Clean response — remove markdown if present
        clean = re.sub(r'```json\s*|\s*```', '', response).strip()
        questions = json.loads(clean)
        return questions if isinstance(questions, list) else None
    except json.JSONDecodeError:
        # Try to extract JSON from response
        try:
            match = re.search(r'\[.*\]', response, re.DOTALL)
            if match:
                return json.loads(match.group())
        except:
            pass
        st.error("Failed to parse AI response. Please try again.")
        return None


# ══════════════════════════════════════════════════════
# AI FLASHCARD GENERATOR
# ══════════════════════════════════════════════════════

def ai_flashcards_page():
    """Renders the AI Flashcard Generator page."""
    t = _get_theme()

    st.markdown(f'<h1 style="color:{t["text"]}">✨ AI Flashcard Generator</h1>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:{t["subtext"]}">Generate custom Anki-style flashcards on any medical topic</p>', unsafe_allow_html=True)

    if not _check_api():
        _show_api_setup_instructions()
        return

    col1, col2 = st.columns(2)
    with col1:
        topic = st.text_input("📚 Topic", placeholder="e.g. Beta-blockers, Brachial plexus, DKA")
    with col2:
        num_cards = st.selectbox("🔢 Number of Cards", [3, 5, 8, 10])

    style = st.radio("Card Style", ["Question & Answer", "Fill in the Blank", "Clinical Scenario"], horizontal=True)

    if st.button("✨ Generate Flashcards", type="primary", use_container_width=True):
        if not topic:
            st.warning("Please enter a topic!")
            return

        with st.spinner(f"🤖 Generating {num_cards} flashcards on {topic}..."):
            cards = _generate_flashcards(topic, num_cards, style)

        if cards:
            st.session_state.ai_flashcards = cards
            st.session_state.ai_fc_topic = topic
            st.session_state.ai_fc_index = 0
            st.session_state.ai_fc_show = False
            st.rerun()

    # Display flashcards
    if "ai_flashcards" in st.session_state and st.session_state.ai_flashcards:
        cards = st.session_state.ai_flashcards
        idx = st.session_state.ai_fc_index
        show = st.session_state.ai_fc_show

        if idx >= len(cards):
            idx = 0
            st.session_state.ai_fc_index = 0

        card = cards[idx]
        topic_name = st.session_state.get("ai_fc_topic", "Custom")

        st.markdown("---")
        st.markdown(f"**Topic:** {topic_name} — Card {idx + 1} of {len(cards)}")
        st.progress((idx + 1) / len(cards))

        if not show:
            st.markdown(f"""
            <div class="flashcard">
                <div>
                    <div style="font-size:0.8rem; color:{t['subtext']}; text-transform:uppercase; letter-spacing:2px; margin-bottom:0.8rem">
                        ❓ {style}
                    </div>
                    <div style="font-size:1.1rem; font-weight:600; color:{t['text']}">
                        {card.get('front', '')}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)
            col1, col2, col3 = st.columns([1, 2, 1])
            with col2:
                if st.button("👁️ Reveal Answer", type="primary", use_container_width=True):
                    st.session_state.ai_fc_show = True
                    st.rerun()
        else:
            back_html = card.get('back', '').replace('\n', '<br>')
            st.markdown(f"""
            <div class="flashcard" style="border-color:{t['primary']}">
                <div style="width:100%">
                    <div style="font-size:0.8rem; color:{t['primary']}; text-transform:uppercase; letter-spacing:2px; margin-bottom:0.5rem; font-weight:700">
                        ✅ Answer
                    </div>
                    <div style="font-size:0.85rem; text-align:left; color:{t['text']}; line-height:1.8">
                        {back_html}
                    </div>
                </div>
            </div>
            """, unsafe_allow_html=True)

            col1, col2, col3, col4 = st.columns(4)
            def next_ai_card():
                st.session_state.ai_fc_index = (idx + 1) % len(cards)
                st.session_state.ai_fc_show = False

            with col1:
                if st.button("❌ Again", use_container_width=True): next_ai_card(); st.rerun()
            with col2:
                if st.button("😕 Hard", use_container_width=True): next_ai_card(); st.rerun()
            with col3:
                if st.button("👍 Good", use_container_width=True): next_ai_card(); st.rerun()
            with col4:
                if st.button("⭐ Easy", use_container_width=True): next_ai_card(); st.rerun()

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🗑️ Generate New Cards", use_container_width=True):
                del st.session_state.ai_flashcards
                st.rerun()
        with col2:
            if st.button("🔀 Shuffle", use_container_width=True):
                import random
                random.shuffle(st.session_state.ai_flashcards)
                st.session_state.ai_fc_index = 0
                st.session_state.ai_fc_show = False
                st.rerun()


def _generate_flashcards(topic, num, style):
    """Generates flashcards using Gemini."""
    style_instruction = {
        "Question & Answer": "Create clear Q&A pairs about the topic",
        "Fill in the Blank": "Create fill-in-the-blank statements where key terms are removed",
        "Clinical Scenario": "Create short clinical scenario on front, diagnosis/management on back"
    }.get(style, "Create Q&A pairs")

    prompt = f"""
You are a medical flashcard creator for medical students.
{style_instruction}.
Topic: "{topic}"
Number of cards: {num}

Return ONLY valid JSON in this exact format (no other text):

[
  {{
    "front": "The question, blank, or clinical scenario",
    "back": "The complete answer with key points, mechanisms, and mnemonics if helpful"
  }}
]

Make cards:
- Clinically relevant and high-yield
- Use bullet points on the back for clarity
- Include mechanisms where relevant
- Include mnemonics if helpful
- Each card should focus on ONE main concept

Return ONLY the JSON array.
"""
    response = call_gemini(prompt)
    if not response:
        return None
    try:
        clean = re.sub(r'```json\s*|\s*```', '', response).strip()
        cards = json.loads(clean)
        return cards if isinstance(cards, list) else None
    except:
        try:
            match = re.search(r'\[.*\]', response, re.DOTALL)
            if match:
                return json.loads(match.group())
        except:
            pass
        st.error("Couldn't parse flashcards. Try again.")
        return None


# ══════════════════════════════════════════════════════
# AI MNEMONIC GENERATOR
# ══════════════════════════════════════════════════════

def ai_mnemonics_page():
    """Renders the AI Mnemonic Generator page."""
    t = _get_theme()

    st.markdown(f'<h1 style="color:{t["text"]}">💡 AI Mnemonic Generator</h1>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:{t["subtext"]}">Generate memorable, funny, or creative mnemonics for any medical concept</p>', unsafe_allow_html=True)

    if not _check_api():
        _show_api_setup_instructions()
        return

    col1, col2 = st.columns(2)
    with col1:
        topic = st.text_input("📚 What do you need to remember?",
                              placeholder="e.g. Causes of clubbing, Cranial nerves, COPD management")
    with col2:
        mnem_style = st.selectbox("🎨 Mnemonic Style", [
            "Classic Acronym",
            "Funny/Memorable Story",
            "Rhyme or Poem",
            "Arabic/English Mix",
            "Visual/Spatial",
            "Multiple Options"
        ])

    if st.button("✨ Generate Mnemonic", type="primary", use_container_width=True):
        if not topic:
            st.warning("Enter a topic first!")
            return

        with st.spinner(f"🤖 Creating mnemonics for: {topic}..."):
            result = _generate_mnemonic(topic, mnem_style)

        if result:
            st.session_state.ai_mnemonic = result
            st.session_state.ai_mnemonic_topic = topic
            st.rerun()

    # Display mnemonic
    if "ai_mnemonic" in st.session_state:
        st.markdown("---")
        topic_display = st.session_state.get("ai_mnemonic_topic", "")
        st.markdown(f"### 💡 Mnemonic for: {topic_display}")
        st.markdown(f"""
        <div class="glass-card" style="border-left: 4px solid {t['primary']};">
            {st.session_state.ai_mnemonic.replace(chr(10), '<br>')}
        </div>
        """, unsafe_allow_html=True)

        col1, col2 = st.columns(2)
        with col1:
            if st.button("🔄 Generate Another Version", use_container_width=True):
                with st.spinner("Creating a different mnemonic..."):
                    result = _generate_mnemonic(topic_display, mnem_style)
                if result:
                    st.session_state.ai_mnemonic = result
                    st.rerun()
        with col2:
            if st.button("🗑️ Clear", use_container_width=True):
                del st.session_state.ai_mnemonic
                st.rerun()

    # Example suggestions
    st.markdown("---")
    st.subheader("💡 Try These Topics:")
    example_topics = [
        "12 cranial nerves",
        "Causes of hypercalcaemia",
        "Heart failure medications",
        "Causes of metabolic acidosis",
        "Side effects of steroids",
        "Causes of secondary hypertension",
    ]
    cols = st.columns(3)
    for i, eg in enumerate(example_topics):
        with cols[i % 3]:
            if st.button(eg, key=f"eg_{i}", use_container_width=True):
                with st.spinner(f"Creating mnemonic for {eg}..."):
                    result = _generate_mnemonic(eg, mnem_style)
                if result:
                    st.session_state.ai_mnemonic = result
                    st.session_state.ai_mnemonic_topic = eg
                    st.rerun()


def _generate_mnemonic(topic, style):
    """Generates a mnemonic using Gemini."""
    style_prompts = {
        "Classic Acronym": "Create a classic acronym where each letter stands for an item to remember",
        "Funny/Memorable Story": "Create a funny, absurd, or dramatic story that helps remember the items",
        "Rhyme or Poem": "Create a rhyme, poem, or song-like verse to remember the items",
        "Arabic/English Mix": "Create a mnemonic mixing Arabic and English words that Omani students will find memorable",
        "Visual/Spatial": "Describe a vivid visual scene or journey through a familiar location where each stop represents an item",
        "Multiple Options": "Create 3 different types of mnemonics (acronym, story, and rhyme) so the student can choose the best one"
    }

    style_instruction = style_prompts.get(style, style_prompts["Classic Acronym"])

    prompt = f"""
You are a creative medical mnemonic expert helping Omani medical students at SQU.
Topic: "{topic}"
Style: {style_instruction}

Create an excellent, memorable mnemonic. Format your response clearly with:
1. The MNEMONIC itself (make it stand out)
2. What each part MEANS (the medical content)
3. A HIGH-YIELD clinical tip about why this is important

Make it:
- Easy to remember (vivid, funny, or catchy)
- Medically accurate
- Clinically relevant
- Include ALL important items for this topic

Be creative and make it genuinely helpful for exam preparation!
"""
    return call_gemini(prompt)


# ══════════════════════════════════════════════════════
# AI CONCEPT EXPLAINER WITH DIAGRAMS
# ══════════════════════════════════════════════════════

def ai_explain_page():
    """Renders the AI Concept Explainer page."""
    t = _get_theme()

    st.markdown(f'<h1 style="color:{t["text"]}">🔬 AI Concept Explainer</h1>', unsafe_allow_html=True)
    st.markdown(f'<p style="color:{t["subtext"]}">Get AI to explain ANY medical concept with diagrams, analogies, and step-by-step breakdowns</p>', unsafe_allow_html=True)

    if not _check_api():
        _show_api_setup_instructions()
        return

    col1, col2 = st.columns(2)
    with col1:
        concept = st.text_input("🔬 What concept do you want explained?",
                               placeholder="e.g. How ACE inhibitors work, Cardiac action potential")
    with col2:
        explain_level = st.selectbox("🎓 Explain at level of...", [
            "Total Beginner (Year 1)",
            "Pre-clinical Student (Year 2-3)",
            "Clinical Student (Year 4-5)",
            "Intern / Junior Doctor"
        ])

    include_options = st.multiselect(
        "📋 Include in explanation:",
        ["ASCII Diagram/Flowchart", "Step-by-step mechanism", "Clinical analogy",
         "Common exam questions", "Clinical relevance", "Mnemonic"],
        default=["Step-by-step mechanism", "Clinical analogy", "Mnemonic"]
    )

    if st.button("🔬 Explain This!", type="primary", use_container_width=True):
        if not concept:
            st.warning("Enter a concept to explain!")
            return

        with st.spinner(f"🤖 Building explanation for: {concept}..."):
            explanation = _explain_concept(concept, explain_level, include_options)

        if explanation:
            st.session_state.ai_explanation = explanation
            st.session_state.ai_explained_concept = concept
            st.rerun()

    if "ai_explanation" in st.session_state:
        st.markdown("---")
        st.markdown(f"### 🔬 {st.session_state.get('ai_explained_concept', 'Concept')}")
        st.markdown(st.session_state.ai_explanation)

        if st.button("🗑️ Clear Explanation", use_container_width=True):
            del st.session_state.ai_explanation
            st.rerun()

    # Quick explain topics
    st.markdown("---")
    st.subheader("🚀 Quick Explains:")
    quick_explains = [
        ("🫀", "Cardiac action potential"),
        ("💊", "How beta-blockers work"),
        ("🧠", "Blood-brain barrier"),
        ("🫁", "V/Q mismatch"),
        ("🔬", "Complement cascade"),
        ("💉", "DKA vs HHS differences"),
    ]
    cols = st.columns(3)
    for i, (icon, topic) in enumerate(quick_explains):
        with cols[i % 3]:
            if st.button(f"{icon} {topic}", key=f"qe_{i}", use_container_width=True):
                with st.spinner(f"Explaining {topic}..."):
                    exp = _explain_concept(topic, explain_level, include_options)
                if exp:
                    st.session_state.ai_explanation = exp
                    st.session_state.ai_explained_concept = topic
                    st.rerun()


def _explain_concept(concept, level, includes):
    """Generates concept explanation using Gemini."""
    includes_str = ", ".join(includes) if includes else "step-by-step mechanism"

    prompt = f"""
You are Dr. Aisha, Senior Consultant at SQUH, Oman. Explain the following medical concept
to a student at {level} level.

Concept: "{concept}"

Please include: {includes_str}

Format your response with clear headings and sections. If asked for ASCII diagram/flowchart,
create one using text characters like:
→ ← ↑ ↓ ├ ─ │ └ ┌ ┐ ┘ ┤ ┬ ┴ ┼ ═ ║ ╔ ╗ ╚ ╝

Make your explanation:
- Appropriate for the specified student level
- Include pathophysiology (WHY things happen)
- Connect to clinical practice (WHAT do we do about it?)
- Use memorable analogies (like explaining to a friend)
- Include a high-yield exam pearl at the end
- Reference Omani clinical context where relevant

Be thorough but clear. Use markdown formatting for structure.
"""
    return call_gemini(prompt)


# ══════════════════════════════════════════════════════
# HELPER FUNCTIONS
# ══════════════════════════════════════════════════════

def _get_theme():
    """Gets current theme colors."""
    try:
        from styles import THEMES
        theme_name = st.session_state.get("theme", "🧠 Neural Purple")
        return THEMES.get(theme_name, THEMES["🧠 Neural Purple"])
    except:
        return {
            "text": "#e2e8f0", "subtext": "#94a3b8",
            "primary": "#8b5cf6", "card_bg": "rgba(139,92,246,0.08)",
            "card_border": "rgba(139,92,246,0.25)", "gradient": "linear-gradient(135deg, #8b5cf6, #6d28d9)"
        }


def _check_api():
    """Returns True if API is configured."""
    try:
        key = st.secrets.get("GEMINI_API_KEY", "")
        return bool(key) and GEMINI_AVAILABLE
    except:
        return False


def _show_api_setup_instructions():
    """Shows instructions for setting up Gemini API."""
    t = _get_theme()

    st.markdown(f"""
    <div class="glass-card" style="border-left: 4px solid {t['primary']}">
        <h3 style="color:{t['text']}">🔑 Setup Gemini AI — 3 Easy Steps</h3>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("""
    ### Step 1 — Get Your FREE Gemini API Key
    1. Go to: **https://aistudio.google.com/**
    2. Sign in with your Google account
    3. Click **"Get API Key"** → **"Create API Key"**
    4. Copy the key (starts with `AIza...`)
    """)

    st.markdown("""
    ### Step 2 — Create the Secrets File in VS Code
    1. In your `medStudy_oman` folder, create a new folder called `.streamlit`
    2. Inside that folder, create a new file called `secrets.toml`
    3. Paste this into the file:
    ```toml
    GEMINI_API_KEY = "paste-your-key-here"
    ```
    """)

    st.markdown("""
    ### Step 3 — Install Gemini Library
    In your VS Code terminal:
    ```bash
    pip install google-generativeai
    ```
    Then restart your app:
    ```bash
    streamlit run app.py
    ```
    """)

    st.success("✅ Once done, all AI features will unlock automatically!")

    st.markdown("""
    ### 📁 Your Folder Structure Should Look Like:
    ```
    medStudy_oman/
    ├── .streamlit/
    │   └── secrets.toml    ← New file with your API key
    ├── app.py
    ├── ai_features.py      ← New AI file
    ├── database.py
    ├── styles.py
    ├── content.py
    ├── mcq_bank.py         ← New MCQ bank
    └── requirements.txt
    ```
    """)