import streamlit as st

# ===== LANGUAGE FUNCTION =====

language = st.session_state.get("language", "English")

def t(en, es):

    if language == "Español":
        return es

    return en

# ===== PAGE =====

st.title(
    t(
        "🎭 Choose Your Emotion",
        "🎭 Escoge Tu Emoción"
    )
)

st.write(
    t(
        """
Every emotion has a color, an energy and a visual identity.

Choose the emotion that represents your current state.
""",
        """
Cada emoción tiene un color, una energía y una identidad visual.

Escoge la emoción que represente tu estado actual.
"""
    )
)

# ===== DEFAULT VALUES =====

if "emotion" not in st.session_state:
    st.session_state["emotion"] = "Joy"

if "color" not in st.session_state:
    st.session_state["color"] = "#00F5FF"

if "intensity" not in st.session_state:
    st.session_state["intensity"] = 50

# ===== INPUTS =====

emotion_options = [
    "Joy",
    "Sadness",
    "Calm",
    "Fear",
    "Excitement",
    "Love",
    "Loneliness"
]

emotion = st.selectbox(
    t(
        "✨ Select your emotion",
        "✨ Selecciona tu emoción"
    ),
    emotion_options,
    index=emotion_options.index(st.session_state["emotion"]),
    key="emotion_select"
)

color = st.color_picker(
    t(
        "🎨 Emotional color",
        "🎨 Color emocional"
    ),
    value=st.session_state["color"],
    key="color_picker"
)

intensity = st.slider(
    t(
        "⚡ Emotional intensity",
        "⚡ Intensidad emocional"
    ),
    0,
    100,
    value=st.session_state["intensity"],
    key="intensity_slider"
)

# ===== SAVE DATA =====

st.session_state["emotion"] = emotion
st.session_state["color"] = color
st.session_state["intensity"] = intensity

st.markdown("<br>", unsafe_allow_html=True)

# ===== GLOW CARD =====

glow = intensity + 30

emotion_card = f"""
<div style='padding:50px; border-radius:35px; background:linear-gradient(135deg,{color},#050816); display:flex; flex-direction:column; justify-content:center; align-items:center; box-shadow:0px 0px {glow}px {color}; border:1px solid rgba(255,255,255,0.12);'>

<h1 style='font-size:4rem; color:white; text-shadow:0px 0px 30px white; margin-bottom:10px;'>

{emotion}

</h1>

<p style='font-size:1.3rem; color:white; opacity:0.9;'>

{t("Intensity Level", "Nivel de Intensidad")}: {intensity}%

</p>

</div>
"""

st.markdown(emotion_card, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== REFLECTION CARD =====

reflection_card = f"""
<div style='padding:35px; border-radius:30px; background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.08); box-shadow:0px 0px 30px rgba(255,255,255,0.05);'>

<h2 style='color:{color};'>
🌌 {t("Emotional Reflection", "Reflexión Emocional")}
</h2>

<p style='font-size:1.15rem; line-height:2; color:white;'>

{t(
'''
Your selected emotion generates a unique visual atmosphere.
The chosen color represents the emotional energy
that will guide the rest of your artistic journey.

Every next step will be influenced by this choice.
''',
'''
La emoción seleccionada genera una atmósfera visual única.
El color elegido representa la energía emocional
que guiará el resto de tu viaje artístico.

Cada siguiente paso estará influenciado por esta elección.
'''
)}

</p>

</div>
"""

st.markdown(reflection_card, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== FINAL MESSAGE =====

st.success(
    t(
        "Emotion captured successfully ✨",
        "Emoción capturada exitosamente ✨"
    )
)
