"""
enhanced_login.py — Beautiful login page with theme previews
"""

def get_enhanced_login_page_html(themes_dict, current_theme_name):
    """
    Creates a stunning login page with live theme previews.
    
    Args:
        themes_dict: Dictionary of all available themes
        current_theme_name: Currently selected theme name
    
    Returns:
        HTML string for enhanced login page
    """
    
    current_theme = themes_dict.get(current_theme_name, list(themes_dict.values())[0])
    
    # Generate theme preview cards
    theme_cards_html = ""
    for i, (name, theme) in enumerate(themes_dict.items()):
        is_active = (name == current_theme_name)
        theme_cards_html += f"""
        <div style="
            background: linear-gradient(135deg, {theme['primary']}22, {theme['secondary']}11);
            border: {'3px solid ' + theme['primary'] if is_active else '1px solid ' + theme['card_border']};
            border-radius: 16px;
            padding: 1rem;
            margin: 0.5rem;
            cursor: pointer;
            transition: all 0.3s ease;
            box-shadow: {'0 0 30px ' + theme['glow'] if is_active else 'none'};
            min-width: 200px;
        ">
            <div style="font-weight: 700; color: {theme['text']}; margin-bottom: 0.5rem; font-size: 0.9rem;">
                {name}
            </div>
            <div style="
                display: flex;
                gap: 8px;
                margin-bottom: 0.5rem;
            ">
                <div style="width: 30px; height: 30px; border-radius: 8px; background: {theme['primary']};"></div>
                <div style="width: 30px; height: 30px; border-radius: 8px; background: {theme['secondary']};"></div>
                <div style="width: 30px; height: 30px; border-radius: 8px; background: {theme['accent']};"></div>
            </div>
            <div style="
                height: 6px;
                background: {theme['gradient']};
                border-radius: 100px;
                margin-top: 0.5rem;
            "></div>
            {'<div style="color: ' + theme['primary'] + '; font-size: 0.7rem; margin-top: 0.5rem; font-weight: 700;">✓ ACTIVE</div>' if is_active else ''}
        </div>
        """
    
    html = f"""
    <style>
        @keyframes fadeInUp {{
            from {{
                opacity: 0;
                transform: translateY(30px);
            }}
            to {{
                opacity: 1;
                transform: translateY(0);
            }}
        }}
        
        @keyframes float {{
            0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
            50% {{ transform: translateY(-20px) rotate(5deg); }}
        }}
        
        @keyframes pulse-glow {{
            0%, 100% {{ box-shadow: 0 0 20px {current_theme['glow']}, 0 0 40px {current_theme['glow']}55; }}
            50% {{ box-shadow: 0 0 40px {current_theme['glow']}, 0 0 60px {current_theme['glow']}88; }}
        }}
        
        @keyframes shimmer {{
            0% {{ background-position: -1000px 0; }}
            100% {{ background-position: 1000px 0; }}
        }}
        
        .login-hero {{
            animation: fadeInUp 0.8s ease-out;
        }}
        
        .float-icon {{
            animation: float 3s ease-in-out infinite;
        }}
        
        .pulse-border {{
            animation: pulse-glow 2s ease-in-out infinite;
        }}
        
        .shimmer-text {{
            background: linear-gradient(
                90deg,
                {current_theme['primary']} 0%,
                {current_theme['accent']} 50%,
                {current_theme['primary']} 100%
            );
            background-size: 1000px 100%;
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            background-clip: text;
            animation: shimmer 3s linear infinite;
        }}
        
        .theme-selector {{
            display: flex;
            overflow-x: auto;
            gap: 1rem;
            padding: 1rem 0;
            scroll-behavior: smooth;
        }}
        
        .theme-selector::-webkit-scrollbar {{
            height: 6px;
        }}
        
        .theme-selector::-webkit-scrollbar-track {{
            background: {current_theme['card_bg']};
            border-radius: 10px;
        }}
        
        .theme-selector::-webkit-scrollbar-thumb {{
            background: {current_theme['primary']};
            border-radius: 10px;
        }}
    </style>
    
    <div style="
        min-height: 100vh;
        background: linear-gradient(135deg, {current_theme['bg_start']}, {current_theme['bg_end']});
        padding: 2rem;
        position: relative;
        overflow: hidden;
    ">
        <!-- Animated background particles -->
        <div style="
            position: absolute;
            width: 500px;
            height: 500px;
            border-radius: 50%;
            background: radial-gradient(circle, {current_theme['primary']}22, transparent);
            top: -200px;
            right: -200px;
            animation: float 6s ease-in-out infinite;
        "></div>
        <div style="
            position: absolute;
            width: 400px;
            height: 400px;
            border-radius: 50%;
            background: radial-gradient(circle, {current_theme['secondary']}15, transparent);
            bottom: -150px;
            left: -150px;
            animation: float 8s ease-in-out infinite reverse;
        "></div>
        
        <!-- Main content -->
        <div style="position: relative; z-index: 10; max-width: 1400px; margin: 0 auto;">
            
            <!-- Hero Section -->
            <div class="login-hero" style="text-align: center; margin-bottom: 3rem;">
                <div class="float-icon" style="font-size: 6rem; margin-bottom: 1rem;">
                    🩺
                </div>
                <h1 class="shimmer-text" style="
                    font-size: clamp(2.5rem, 6vw, 5rem);
                    font-weight: 900;
                    margin: 0 0 1rem;
                    line-height: 1.1;
                ">
                    MedStudy Oman
                </h1>
                <div style="
                    color: {current_theme['subtext']};
                    font-size: 1.2rem;
                    max-width: 600px;
                    margin: 0 auto 2rem;
                    line-height: 1.6;
                ">
                    Welcome, Future Doctor! 👨‍⚕️ Your complete AI-powered study companion awaits
                </div>
                
                <!-- Stats badges -->
                <div style="
                    display: flex;
                    gap: 1rem;
                    justify-content: center;
                    flex-wrap: wrap;
                    margin-top: 2rem;
                ">
                    <div style="
                        background: {current_theme['card_bg']};
                        border: 1px solid {current_theme['card_border']};
                        border-radius: 100px;
                        padding: 0.5rem 1.5rem;
                        font-size: 0.85rem;
                        backdrop-filter: blur(10px);
                    ">
                        <span style="color: {current_theme['primary']}; font-weight: 800;">60+</span>
                        <span style="color: {current_theme['subtext']}"> MCQs</span>
                    </div>
                    <div style="
                        background: {current_theme['card_bg']};
                        border: 1px solid {current_theme['card_border']};
                        border-radius: 100px;
                        padding: 0.5rem 1.5rem;
                        font-size: 0.85rem;
                        backdrop-filter: blur(10px);
                    ">
                        <span style="color: {current_theme['primary']}; font-weight: 800;">5</span>
                        <span style="color: {current_theme['subtext']}"> AI Tools</span>
                    </div>
                    <div style="
                        background: {current_theme['card_bg']};
                        border: 1px solid {current_theme['card_border']};
                        border-radius: 100px;
                        padding: 0.5rem 1.5rem;
                        font-size: 0.85rem;
                        backdrop-filter: blur(10px);
                    ">
                        <span style="color: {current_theme['primary']}; font-weight: 800;">24</span>
                        <span style="color: {current_theme['subtext']}"> Subjects</span>
                    </div>
                    <div style="
                        background: {current_theme['card_bg']};
                        border: 1px solid {current_theme['card_border']};
                        border-radius: 100px;
                        padding: 0.5rem 1.5rem;
                        font-size: 0.85rem;
                        backdrop-filter: blur(10px);
                    ">
                        <span style="color: {current_theme['primary']}; font-weight: 800;">10</span>
                        <span style="color: {current_theme['subtext']}"> Themes</span>
                    </div>
                </div>
            </div>
            
            <!-- Theme Selector Section -->
            <div style="margin: 3rem 0;">
                <h3 style="
                    color: {current_theme['text']};
                    text-align: center;
                    margin-bottom: 1.5rem;
                    font-size: 1.5rem;
                ">
                    🎨 Choose Your Study Vibe
                </h3>
                <div class="theme-selector">
                    {theme_cards_html}
                </div>
            </div>
            
            <!-- Features Preview -->
            <div style="
                display: grid;
                grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                gap: 1.5rem;
                margin-top: 3rem;
            ">
                <div class="pulse-border" style="
                    background: {current_theme['card_bg']};
                    border: 2px solid {current_theme['card_border']};
                    border-radius: 20px;
                    padding: 2rem;
                    backdrop-filter: blur(20px);
                ">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">🤖</div>
                    <h4 style="color: {current_theme['text']}; margin: 0 0 0.5rem;">AI Tutor - Dr. Aisha</h4>
                    <p style="color: {current_theme['subtext']}; margin: 0; line-height: 1.6;">
                        Chat with your personal AI medical consultant. Ask anything, get detailed explanations with diagrams!
                    </p>
                </div>
                
                <div style="
                    background: {current_theme['card_bg']};
                    border: 2px solid {current_theme['card_border']};
                    border-radius: 20px;
                    padding: 2rem;
                    backdrop-filter: blur(20px);
                ">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">🎤</div>
                    <h4 style="color: {current_theme['text']}; margin: 0 0 0.5rem;">Voice AI</h4>
                    <p style="color: {current_theme['subtext']}; margin: 0; line-height: 1.6;">
                        Speak your questions, get audio responses. Perfect for hands-free studying!
                    </p>
                </div>
                
                <div style="
                    background: {current_theme['card_bg']};
                    border: 2px solid {current_theme['card_border']};
                    border-radius: 20px;
                    padding: 2rem;
                    backdrop-filter: blur(20px);
                ">
                    <div style="font-size: 3rem; margin-bottom: 1rem;">⏱️</div>
                    <h4 style="color: {current_theme['text']}; margin: 0 0 0.5rem;">Medical Timer</h4>
                    <p style="color: {current_theme['subtext']}; margin: 0; line-height: 1.6;">
                        5 animated timer styles with medical instruments. Make studying fun!
                    </p>
                </div>
            </div>
            
            <!-- Call to action -->
            <div style="
                text-align: center;
                margin-top: 4rem;
                padding: 3rem 2rem;
                background: linear-gradient(135deg, {current_theme['primary']}22, {current_theme['secondary']}11);
                border: 2px solid {current_theme['primary']}44;
                border-radius: 24px;
                backdrop-filter: blur(20px);
            ">
                <h2 style="color: {current_theme['text']}; margin: 0 0 1rem;">
                    Ready to Transform Your Medical Studies?
                </h2>
                <p style="color: {current_theme['subtext']}; margin: 0 0 2rem; font-size: 1.1rem;">
                    Join hundreds of Omani medical students already using MedStudy! 🇴🇲
                </p>
                <div style="
                    display: inline-block;
                    background: {current_theme['gradient']};
                    border-radius: 100px;
                    padding: 1rem 3rem;
                    font-size: 1.2rem;
                    font-weight: 700;
                    color: white;
                    box-shadow: 0 10px 40px {current_theme['glow']};
                    cursor: pointer;
                ">
                    ⬇️ Sign Up / Login Below to Enter
                </div>
            </div>
        </div>
    </div>
    """
    
    return html


def get_welcome_animation_html(theme_colors, user_name):
    """
    Creates a welcome animation that plays after successful login.
    
    Args:
        theme_colors: Current theme colors
        user_name: Name of the logged-in user
    
    Returns:
        HTML string with welcome animation
    """
    return f"""
    <style>
        @keyframes welcome-zoom {{
            0% {{
                opacity: 0;
                transform: scale(0.5);
            }}
            50% {{
                opacity: 1;
                transform: scale(1.1);
            }}
            100% {{
                opacity: 1;
                transform: scale(1);
            }}
        }}
        
        @keyframes confetti {{
            0% {{ transform: translateY(-100vh) rotate(0deg); opacity: 1; }}
            100% {{ transform: translateY(100vh) rotate(720deg); opacity: 0; }}
        }}
        
        .welcome-container {{
            position: fixed;
            top: 0;
            left: 0;
            width: 100%;
            height: 100vh;
            background: linear-gradient(135deg, {theme_colors['bg_start']}, {theme_colors['bg_end']});
            display: flex;
            align-items: center;
            justify-content: center;
            z-index: 9999;
            animation: welcome-zoom 1.5s ease-out;
        }}
        
        .confetti-piece {{
            position: absolute;
            width: 10px;
            height: 10px;
            animation: confetti 3s linear;
        }}
    </style>
    
    <div class="welcome-container">
        <!-- Confetti pieces -->
        <div class="confetti-piece" style="left: 10%; background: {theme_colors['primary']}; animation-delay: 0s;"></div>
        <div class="confetti-piece" style="left: 20%; background: {theme_colors['secondary']}; animation-delay: 0.2s;"></div>
        <div class="confetti-piece" style="left: 30%; background: {theme_colors['accent']}; animation-delay: 0.4s;"></div>
        <div class="confetti-piece" style="left: 40%; background: {theme_colors['primary']}; animation-delay: 0.6s;"></div>
        <div class="confetti-piece" style="left: 50%; background: {theme_colors['secondary']}; animation-delay: 0.8s;"></div>
        <div class="confetti-piece" style="left: 60%; background: {theme_colors['accent']}; animation-delay: 1s;"></div>
        <div class="confetti-piece" style="left: 70%; background: {theme_colors['primary']}; animation-delay: 1.2s;"></div>
        <div class="confetti-piece" style="left: 80%; background: {theme_colors['secondary']}; animation-delay: 1.4s;"></div>
        <div class="confetti-piece" style="left: 90%; background: {theme_colors['accent']}; animation-delay: 1.6s;"></div>
        
        <div style="text-align: center;">
            <div style="font-size: 8rem; margin-bottom: 2rem;">🎉</div>
            <h1 style="
                font-size: 3rem;
                font-weight: 900;
                background: {theme_colors['gradient']};
                -webkit-background-clip: text;
                -webkit-text-fill-color: transparent;
                background-clip: text;
                margin: 0 0 1rem;
            ">
                Welcome, Dr. {user_name}!
            </h1>
            <p style="
                color: {theme_colors['text']};
                font-size: 1.5rem;
                margin: 0;
            ">
                Let's make today count! 🩺
            </p>
        </div>
    </div>
    
    <script>
        setTimeout(() => {{
            document.querySelector('.welcome-container').style.display = 'none';
        }}, 3000);
    </script>
    """