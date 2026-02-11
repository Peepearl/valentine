import streamlit as st
import streamlit.components.v1 as components
import base64

# Page config
st.set_page_config(
    page_title="💖 Will You Be My Valentine?",
    page_icon="💖",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Hide Streamlit branding
st.markdown("""
<style>
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}
    .stDeployButton {display: none;}
</style>
""", unsafe_allow_html=True)


# ----------------------------
# LOAD AUDIO AS BASE64
# ----------------------------
def load_audio_base64(path):
    with open(path, "rb") as f:
        data = f.read()
    return base64.b64encode(data).decode("utf-8")


audio_base64 = load_audio_base64("assets/audio1.mp3")


# ----------------------------
# HTML CONTENT
# ----------------------------
valentine_html = f"""
<!DOCTYPE html>
<html>
<head>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600;700&display=swap');
        
        * {{
            margin: 0;
            padding: 0;
            box-sizing: border-box;
        }}
        
        body {{
            font-family: 'Poppins', sans-serif;
            background: linear-gradient(135deg, #ffecd2 0%, #fcb69f 100%);
            min-height: 100vh;
            display: flex;
            justify-content: center;
            align-items: center;
            overflow: hidden;
        }}
        
        .container {{
            background: white;
            padding: 60px 80px;
            border-radius: 30px;
            box-shadow: 0 20px 60px rgba(0, 0, 0, 0.2);
            text-align: center;
            max-width: 550px;
            position: relative;
        }}
        
        .bear {{
            font-size: 120px;
            margin-bottom: 20px;
            animation: float 3s ease-in-out infinite;
        }}
        
        @keyframes float {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-20px); }}
        }}
        
        h1 {{
            font-size: 28px;
            color: #333;
            margin-bottom: 40px;
            font-weight: 600;
        }}
        
        .buttons {{
            display: flex;
            justify-content: center;
            align-items: center;
            gap: 30px;
            margin-bottom: 30px;
            position: relative;
            height: 120px;
        }}
        
        .yes-btn {{
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            border: none;
            padding: 20px 60px;
            font-size: 24px;
            font-weight: 700;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 10px 30px rgba(245, 87, 108, 0.4);
            transition: all 0.3s ease;
            font-family: 'Poppins', sans-serif;
        }}
        
        .yes-btn:hover {{
            transform: scale(1.1);
            box-shadow: 0 15px 40px rgba(245, 87, 108, 0.6);
        }}
        
        .no-btn {{
            background: #f0f0f0;
            color: #666;
            border: 2px solid #ddd;
            padding: 12px 30px;
            font-size: 16px;
            font-weight: 600;
            border-radius: 50px;
            cursor: pointer;
            font-family: 'Poppins', sans-serif;
            position: absolute;
            transition: none !important;
        }}

        .no-btn:hover {{
            background: #e0e0e0;
        }}
        
        .message {{
            color: #999;
            font-size: 14px;
            font-style: italic;
        }}
        
        .success {{
            display: none;
        }}
        
        .success.show {{
            display: block;
            animation: zoomIn 0.5s ease-out;
        }}
        
        @keyframes zoomIn {{
            from {{
                opacity: 0;
                transform: scale(0.5);
            }}
            to {{
                opacity: 1;
                transform: scale(1);
            }}
        }}
        
        .success h2 {{
            font-size: 48px;
            color: #f5576c;
            margin-bottom: 20px;
        }}
        
        .success img {{
            max-width: 100%;
            border-radius: 20px;
            margin-top: 20px;
            box-shadow: 0 10px 30px rgba(0, 0, 0, 0.2);
        }}
        
        .confetti {{
            position: fixed;
            width: 10px;
            height: 10px;
            border-radius: 50%;
            pointer-events: none;
        }}
    </style>
</head>

<body>
    <div class="container">

        <!-- FIRST PAGE -->
        <div id="question" class="question">
            <div class="bear">💖</div>
            <h1><span id="name">Hello babe</span> will you be my valentine?</h1>
            
            <div class="buttons">
                <button class="yes-btn" onclick="sayYes()">Yes</button>
                <button class="no-btn" id="noBtn" onmousemove="moveButton()">No</button>
            </div>
            
            <p class="message">*The No button has been replaced by extra hugs. 🤗💖</p>
        </div>
        

        <!-- SECOND PAGE -->
        <div id="success" class="success">
            <div class="bear">💖</div>

            <h1>I’m so lucky to have you… my Valentine 💘</h1>

            <h2>YAY! 🎉</h2>

            <!-- AUDIO (hidden) -->
            <audio id="loveAudio">
                <source src="data:audio/mpeg;base64,{audio_base64}" type="audio/mpeg">
            </audio>

            <!-- GIF -->
            <img src="https://eventstodayz.com/wp-content/uploads/2024/01/i-love-you-so-much-2024-gif-images.gif" 
                 alt="Celebration" width="100%">
        </div>

    </div>


    <script>
        const name = 'Hello babe';
        document.getElementById('name').textContent = name;

        function getRandomPosition() {{
            const container = document.querySelector('.container');
            const button = document.getElementById('noBtn');
            const containerRect = container.getBoundingClientRect();
            const buttonRect = button.getBoundingClientRect();

            const maxX = containerRect.width - buttonRect.width - 50;
            const maxY = 120;

            const randomX = Math.random() * maxX - maxX/2;
            const randomY = Math.random() * maxY - maxY/2;

            return {{ x: randomX, y: randomY }};
        }}

        // MOVE NO BUTTON FAST
        function moveButton() {{
            const button = document.getElementById('noBtn');
            const pos = getRandomPosition();

            button.style.transform = `translate(${{pos.x}}px, ${{pos.y}}px)`;
        }}

        function sayYes() {{
            document.getElementById('question').style.display = 'none';
            document.getElementById('success').classList.add('show');

            // PLAY AUDIO ONLY ON SECOND PAGE
            const audio = document.getElementById("loveAudio");
            audio.play();

            // CONFETTI
            for (let i = 0; i < 150; i++) {{
                setTimeout(() => createConfetti(), i * 30);
            }}
        }}

        function createConfetti() {{
            const confetti = document.createElement('div');
            confetti.className = 'confetti';
            confetti.style.backgroundColor = ['#ff6b6b', '#f093fb', '#feca57', '#48dbfb', '#ff9ff3', '#1dd1a1'][Math.floor(Math.random() * 6)];
            confetti.style.left = Math.random() * window.innerWidth + 'px';
            confetti.style.top = '-10px';

            document.body.appendChild(confetti);

            const fall = confetti.animate([
                {{
                    transform: 'translateY(0) rotate(0deg)',
                    opacity: 1
                }},
                {{
                    transform: `translateY(${{window.innerHeight + 10}}px) rotate(${{Math.random() * 720}}deg)`,
                    opacity: 0
                }}
            ], {{
                duration: Math.random() * 2000 + 1500,
                easing: 'cubic-bezier(0.25, 0.46, 0.45, 0.94)'
            }});

            fall.onfinish = () => confetti.remove();
        }}
    </script>
</body>
</html>
"""

# Display Valentine app
components.html(valentine_html, height=1000, scrolling=False)
