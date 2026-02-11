import streamlit as st
import streamlit.components.v1 as components
import base64

# ----------------------------
# PAGE CONFIG
# ----------------------------
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
            width: 550px;
            max-width: 90%;
            position: relative;
            overflow: hidden;
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
            position: relative;
            width: 100%;
            height: 160px;
            margin-bottom: 30px;
        }}

        .yes-btn {{
            background: linear-gradient(135deg, #f093fb 0%, #f5576c 100%);
            color: white;
            border: none;
            padding: 18px 55px;
            font-size: 22px;
            font-weight: 700;
            border-radius: 50px;
            cursor: pointer;
            box-shadow: 0 10px 30px rgba(245, 87, 108, 0.4);
            transition: transform 0.2s ease;
            font-family: 'Poppins', sans-serif;
            position: absolute;
            left: 50%;
            top: 50%;
            transform: translate(-50%, -50%);
        }}

        .yes-btn:hover {{
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
            left: 65%;
            top: 55%;
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
                <button class="yes-btn" id="yesBtn" onclick="sayYes()">Yes</button>
                <button class="no-btn" id="noBtn">No</button>
            </div>

            <p class="message">*The No button has been replaced by extra hugs 🤗💖</p>
        </div>


        <!-- SECOND PAGE -->
        <div id="success" class="success">
            <div class="bear">💖</div>

            <h1>I’m so lucky to have you… my Valentine 💘</h1>

            <h2>YAY! 🎉</h2>

            <!-- AUDIO -->
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

        const noBtn = document.getElementById("noBtn");
        const yesBtn = document.getElementById("yesBtn");
        const buttonsBox = document.querySelector(".buttons");

        let yesSize = 1.0;
        const maxYesSize = 1.35; // LIMIT YES SIZE

        function getRandomPosition() {{
            const boxRect = buttonsBox.getBoundingClientRect();
            const btnRect = noBtn.getBoundingClientRect();

            const maxX = boxRect.width - btnRect.width;
            const maxY = boxRect.height - btnRect.height;

            const randomX = Math.random() * maxX;
            const randomY = Math.random() * maxY;

            return {{ x: randomX, y: randomY }};
        }}

        function moveButton() {{
            const pos = getRandomPosition();

            noBtn.style.left = pos.x + "px";
            noBtn.style.top = pos.y + "px";

            // YES grows but limited
            yesSize += 0.05;
            if (yesSize > maxYesSize) yesSize = maxYesSize;

            yesBtn.style.transform = "translate(-50%, -50%) scale(" + yesSize + ")";
        }}

        // Laptop: move away when cursor comes close
        document.addEventListener("mousemove", function(e) {{
            const btnRect = noBtn.getBoundingClientRect();

            const btnX = btnRect.left + btnRect.width / 2;
            const btnY = btnRect.top + btnRect.height / 2;

            const distance = Math.sqrt(
                Math.pow(e.clientX - btnX, 2) + Math.pow(e.clientY - btnY, 2)
            );

            if (distance < 160) {{
                moveButton();
            }}
        }});

        // Mobile: move away when touched
        noBtn.addEventListener("touchstart", function(e) {{
            e.preventDefault();
            moveButton();
        }});

        function sayYes() {{
            document.getElementById('question').style.display = 'none';
            document.getElementById('success').classList.add('show');

            const audio = document.getElementById("loveAudio");
            audio.play();

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

components.html(valentine_html, height=1000, scrolling=False)
