"""
voice_ai.py — Voice-enabled AI Tutor
Features: Speech-to-text input, Text-to-speech output
Uses: Google Speech Recognition + gTTS
"""

import streamlit as st
from pathlib import Path
import base64

# Try to import voice libraries
try:
    import speech_recognition as sr
    SPEECH_RECOGNITION_AVAILABLE = True
except ImportError:
    SPEECH_RECOGNITION_AVAILABLE = False

try:
    from gtts import gTTS
    import tempfile
    TTS_AVAILABLE = True
except ImportError:
    TTS_AVAILABLE = False


def get_audio_input():
    """
    Captures audio from microphone and converts to text.
    Returns: (success: bool, text: str or error message)
    """
    if not SPEECH_RECOGNITION_AVAILABLE:
        return False, "Speech recognition not installed. Run: pip install SpeechRecognition PyAudio"
    
    recognizer = sr.Recognizer()
    
    try:
        with sr.Microphone() as source:
            st.info("🎤 Listening... Speak now!")
            # Adjust for ambient noise
            recognizer.adjust_for_ambient_noise(source, duration=0.5)
            # Listen for audio
            audio = recognizer.listen(source, timeout=10, phrase_time_limit=30)
            
        # Convert speech to text using Google Speech Recognition
        st.info("🔄 Processing your speech...")
        text = recognizer.recognize_google(audio)
        return True, text
        
    except sr.WaitTimeoutError:
        return False, "No speech detected. Please try again."
    except sr.UnknownValueError:
        return False, "Sorry, I couldn't understand what you said. Please speak clearly."
    except sr.RequestError as e:
        return False, f"Could not connect to speech recognition service: {e}"
    except Exception as e:
        return False, f"Error: {str(e)}"


def text_to_speech(text, lang='en'):
    """
    Converts text to speech and returns audio file.
    
    Args:
        text: Text to convert to speech
        lang: Language code ('en' for English, 'ar' for Arabic)
    
    Returns:
        (success: bool, audio_file_path or error message)
    """
    if not TTS_AVAILABLE:
        return False, "Text-to-speech not installed. Run: pip install gtts"
    
    try:
        # Create speech
        tts = gTTS(text=text, lang=lang, slow=False)
        
        # Save to temporary file
        with tempfile.NamedTemporaryFile(delete=False, suffix='.mp3') as fp:
            tts.save(fp.name)
            return True, fp.name
            
    except Exception as e:
        return False, f"Error generating speech: {str(e)}"


def create_audio_player(audio_file_path):
    """
    Creates an HTML audio player for the generated speech.
    
    Args:
        audio_file_path: Path to the MP3 file
    
    Returns:
        HTML string with audio player
    """
    try:
        with open(audio_file_path, 'rb') as audio_file:
            audio_bytes = audio_file.read()
            audio_base64 = base64.b64encode(audio_bytes).decode()
        
        audio_html = f"""
        <audio controls autoplay style="width: 100%; margin: 1rem 0;">
            <source src="data:audio/mp3;base64,{audio_base64}" type="audio/mp3">
            Your browser does not support the audio element.
        </audio>
        """
        return audio_html
    except Exception as e:
        return f"<p>Error playing audio: {str(e)}</p>"


def voice_ai_tutor_interface(theme_colors, on_question_callback):
    """
    Renders the voice AI interface with microphone button and audio playback.
    
    Args:
        theme_colors: Dict with theme color values
        on_question_callback: Function to call with the transcribed question
            Should return the AI's text response
    
    Returns:
        None (renders Streamlit UI)
    """
    st.markdown(f"""
    <div style="
        background: {theme_colors['card_bg']};
        border: 2px solid {theme_colors['card_border']};
        border-radius: 20px;
        padding: 2rem;
        text-align: center;
        margin: 1rem 0;
    ">
        <h3 style="color: {theme_colors['text']}; margin-top: 0;">
            🎤 Voice-Enabled AI Tutor
        </h3>
        <p style="color: {theme_colors['subtext']}; margin-bottom: 1.5rem;">
            Click the microphone and ask your question out loud!
        </p>
    </div>
    """, unsafe_allow_html=True)
    
    # Check if libraries are available
    if not SPEECH_RECOGNITION_AVAILABLE:
        st.error("""
        ⚠️ **Voice input not available**
        
        To enable voice features, install these libraries:
        ```bash
        pip install SpeechRecognition PyAudio gtts
        ```
        
        On Mac, you may also need:
        ```bash
        brew install portaudio
        pip install pyaudio
        ```
        """)
        return
    
    col1, col2, col3 = st.columns([1, 2, 1])
    
    with col2:
        # Voice input button
        if st.button("🎤 Start Voice Input", type="primary", use_container_width=True, key="voice_btn"):
            with st.spinner("🎤 Listening..."):
                success, result = get_audio_input()
            
            if success:
                # Show transcribed question
                st.success(f"✅ You said: **{result}**")
                
                # Get AI response
                with st.spinner("🤖 Dr. Aisha is thinking..."):
                    ai_response = on_question_callback(result)
                
                if ai_response:
                    # Display text response
                    st.markdown(f"""
                    <div style="
                        background: {theme_colors['card_bg']};
                        border-left: 4px solid {theme_colors['primary']};
                        border-radius: 12px;
                        padding: 1.5rem;
                        margin: 1rem 0;
                    ">
                        <div style="color: {theme_colors['primary']}; font-weight: 700; margin-bottom: 0.5rem;">
                            👩‍⚕️ Dr. Aisha says:
                        </div>
                        <div style="color: {theme_colors['text']}; line-height: 1.8;">
                            {ai_response[:500]}...
                        </div>
                    </div>
                    """, unsafe_allow_html=True)
                    
                    # Generate speech response
                    if TTS_AVAILABLE:
                        with st.spinner("🔊 Generating audio response..."):
                            # Limit text length for TTS (max 500 chars for better performance)
                            tts_text = ai_response[:500]
                            success_audio, audio_result = text_to_speech(tts_text)
                        
                        if success_audio:
                            st.markdown("### 🔊 Listen to Response:")
                            audio_html = create_audio_player(audio_result)
                            st.markdown(audio_html, unsafe_allow_html=True)
                        else:
                            st.warning(f"Could not generate audio: {audio_result}")
                    else:
                        st.info("💡 Install `gtts` for audio responses: `pip install gtts`")
                else:
                    st.error("Sorry, I couldn't generate a response. Please try again.")
            else:
                st.error(f"❌ {result}")
    
    # Instructions
    st.markdown(f"""
    <div style="
        background: {theme_colors['card_bg']};
        border: 1px solid {theme_colors['card_border']};
        border-radius: 12px;
        padding: 1rem;
        margin-top: 1.5rem;
        font-size: 0.85rem;
        color: {theme_colors['subtext']};
    ">
        <b>💡 Tips for best results:</b><br>
        • Speak clearly and at normal speed<br>
        • Ask specific medical questions<br>
        • Avoid background noise<br>
        • Wait for the microphone indicator before speaking<br>
        • Example: "Explain the pathophysiology of heart failure"
    </div>
    """, unsafe_allow_html=True)


def check_voice_dependencies():
    """
    Checks if voice dependencies are installed.
    Returns: Dict with status of each dependency
    """
    return {
        "speech_recognition": SPEECH_RECOGNITION_AVAILABLE,
        "text_to_speech": TTS_AVAILABLE,
        "all_available": SPEECH_RECOGNITION_AVAILABLE and TTS_AVAILABLE
    }


def get_voice_setup_instructions():
    """Returns installation instructions for voice features."""
    return """
# 🎤 Voice AI Setup Instructions

## For Mac Users:
```bash
# Install PortAudio first
brew install portaudio

# Install Python libraries
pip install SpeechRecognition PyAudio gtts
```

## For Windows Users:
```bash
# Install Python libraries
pip install SpeechRecognition PyAudio gtts
```

## For Linux Users:
```bash
# Install system dependencies
sudo apt-get install portaudio19-dev python3-pyaudio

# Install Python libraries
pip install SpeechRecognition PyAudio gtts
```

## Troubleshooting:

**"No module named 'pyaudio'"**
→ On Mac: Run `brew install portaudio` first, then `pip install pyaudio`
→ On Windows: Download PyAudio wheel from https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio

**Microphone not working**
→ Check system permissions (System Preferences → Security & Privacy → Microphone)
→ Make sure your microphone is selected as default input device

**"Request error" when using speech recognition**
→ Check your internet connection (Google Speech Recognition requires internet)
→ Try again after a few seconds
"""