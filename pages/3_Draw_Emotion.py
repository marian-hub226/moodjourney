import streamlit as st
from streamlit_drawable_canvas import st_canvas

# ===== LANGUAGE FUNCTION =====

language = st.session_state.get("language", "English")

def t(en, es):

    if language == "Español":
        return es

    return en

# ===== SESSION DATA =====

emotion = st.session_state.get("emotion", "Unknown Emotion")
color = st.session_state.get("color", "#00F5FF")
intensity = st.session_state.get("intensity", 50)

# ===== STYLES =====

st.markdown("""
<style>

.glass-box {

    padding:35px;

    border-radius:30px;

    background:
    linear-gradient(
    135deg,
    rgba(255,255,255,0.08),
    rgba(255,255,255,0.03)
    );

    backdrop-filter: blur(16px);

    border:
    1px solid rgba(255,255,255,0.12);
}

.canvas-box {

    padding:20px;

    border-radius:25px;

    background:
    rgba(255,255,255,0.05);

    border:
    1px solid rgba(255,255,255,0.08);
}

</style>
""", unsafe_allow_html=True)

# ===== HERO SECTION =====

hero_section = f"""
<div class="glass-box"
style="
box-shadow:0px 0px 50px {color};
">

<h1 style="
text-align:center;
font-size:3.5rem;
color:{color};
text-shadow:0px 0px 30px {color};
">

🎨 {t("Draw Your Emotion", "Dibuja Tu Emoción")}

</h1>

<p style="
text-align:center;
font-size:1.2rem;
color:white;
line-height:1.8;
">

{t(
'''
Your selected emotion is:
''',
'''
Tu emoción seleccionada es:
'''
)}

<br><br>

<b style="font-size:1.5rem;">
{emotion}
</b>

<br><br>

{t(
'''
Express it visually through shapes,
colors and movement.
''',
'''
Exprésala visualmente a través de formas,
colores y movimiento.
'''
)}

</p>

</div>
"""

st.markdown(hero_section, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== CONTROLS =====

col1, col2 = st.columns(2)

with col1:

    stroke_width = st.slider(
        t(
            "🖌 Brush Size",
            "🖌 Tamaño del Pincel"
        ),
        1,
        25,
        8
    )

with col2:

    drawing_mode = st.selectbox(
        t(
            "✨ Drawing Mode",
            "✨ Modo de Dibujo"
        ),
        (
            "freedraw",
            "line",
            "rect",
            "circle",
            "transform"
        )
    )

st.markdown("<br>", unsafe_allow_html=True)

# ===== CANVAS =====

canvas_html = f"""
<div class="canvas-box"
style="
box-shadow:0px 0px 40px {color};
">
</div>
"""

st.markdown(canvas_html, unsafe_allow_html=True)

canvas_result = st_canvas(
    fill_color="rgba(255,255,255,0.05)",
    stroke_width=stroke_width,
    stroke_color=color,
    background_color="#050816",
    height=550,
    width=900,
    drawing_mode=drawing_mode,
    key="canvas",
)

# ===== SAVE DRAWING =====

st.session_state["drawing"] = canvas_result.image_data

st.markdown("<br>", unsafe_allow_html=True)

# ===== EMOTIONAL VISUAL =====

glow = intensity + 40

emotion_visual = f"""
<div style="
height:220px;
border-radius:30px;

background:
radial-gradient(
circle,
{color},
#050816
);

display:flex;
justify-content:center;
align-items:center;

font-size:3rem;
font-weight:bold;

color:white;

box-shadow:
0px 0px {glow}px {color};

">

{emotion}

</div>
"""

st.markdown(emotion_visual, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== FINAL MESSAGE =====

st.success(
    t(
        "Your emotional artwork has been saved ✨",
        "Tu obra emocional ha sido guardada ✨"
    )
)
