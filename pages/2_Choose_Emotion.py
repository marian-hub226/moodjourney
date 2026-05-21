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

# =====================================================
# LED RING EXPERIENCE
# =====================================================

effects = {

    "Joy": {
        "effect_en": "Rainbow Cycle",
        "effect_es": "Ciclo Arcoíris",
        "description_en":
        "A vibrant rainbow animation representing happiness and energy.",
        "description_es":
        "Una animación arcoíris vibrante que representa felicidad y energía."
    },

    "Sadness": {
        "effect_en": "Blue Breathing",
        "effect_es": "Respiración Azul",
        "description_en":
        "A slow blue pulse symbolizing emotional depth and silence.",
        "description_es":
        "Un pulso azul lento que simboliza profundidad emocional y silencio."
    },

    "Calm": {
        "effect_en": "Soft Cyan Glow",
        "effect_es": "Brillo Cyan Suave",
        "description_en":
        "A stable cyan glow creating peace and serenity.",
        "description_es":
        "Un brillo cyan estable que crea paz y serenidad."
    },

    "Fear": {
        "effect_en": "Purple Flash",
        "effect_es": "Destello Púrpura",
        "description_en":
        "Fast flashes expressing tension and uncertainty.",
        "description_es":
        "Destellos rápidos que expresan tensión e incertidumbre."
    },

    "Excitement": {
        "effect_en": "Fast Spin",
        "effect_es": "Giro Rápido",
        "description_en":
        "Rapid moving lights representing adrenaline and emotion.",
        "description_es":
        "Luces rápidas en movimiento que representan adrenalina y emoción."
    },

    "Love": {
        "effect_en": "Pink Pulse",
        "effect_es": "Pulso Rosa",
        "description_en":
        "A soft pulsing pink light inspired by affection and warmth.",
        "description_es":
        "Una suave luz rosa pulsante inspirada en afecto y calidez."
    },

    "Loneliness": {
        "effect_en": "Single Dim Light",
        "effect_es": "Luz Individual Tenue",
        "description_en":
        "A lonely fading light surrounded by darkness.",
        "description_es":
        "Una luz tenue y solitaria rodeada por oscuridad."
    }

}

selected_effect = effects.get(emotion)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# LED EXPERIENCE CARD
# =====================================================

led_card = f"""
<div style='padding:40px; border-radius:30px; background:linear-gradient(135deg,rgba(255,255,255,0.08),rgba(255,255,255,0.03)); backdrop-filter:blur(14px); border:1px solid rgba(255,255,255,0.10); box-shadow:0px 0px 40px {color};'>

<h1 style='
text-align:center;
font-size:3rem;
color:{color};
text-shadow:0px 0px 20px {color};
'>

🌈 {t("LED Ring Experience", "Experiencia LED Ring")}

</h1>

<h2 style='
text-align:center;
color:white;
margin-top:20px;
'>

{selected_effect["effect_es"] if language == "Español" else selected_effect["effect_en"]}

</h2>

<p style='
text-align:center;
font-size:1.15rem;
line-height:2;
color:white;
opacity:0.9;
margin-top:20px;
'>

{selected_effect["description_es"] if language == "Español" else selected_effect["description_en"]}

</p>

</div>
"""

st.markdown(led_card, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# =====================================================
# WOKWI LINK
# =====================================================

wokwi_url = "https://wokwi.com/projects/464581491904789505"

st.markdown(f"""
<div style='
text-align:center;
margin-top:25px;
'>

<a href="{wokwi_url}" target="_blank"
style='
background:{color};
padding:16px 28px;
border-radius:16px;
text-decoration:none;
font-size:1.1rem;
font-weight:bold;
color:white;
box-shadow:0px 0px 25px {color};
display:inline-block;
'>

🚀 {t("Open Wokwi LED Simulation", "Abrir Simulación LED en Wokwi")}

</a>

<p style='
margin-top:25px;
font-size:1.1rem;
line-height:1.8;
color:white;
opacity:0.9;
'>

{t(
"""
Click the Wokwi link, press the Play button
and type any of these emotions inside the Serial Monitor:

<b>JOY</b>, <b>SADNESS</b>, <b>LOVE</b>,
<b>FEAR</b>, <b>CALM</b> or <b>EXCITEMENT</b>.
""",
"""
Da click en el link de Wokwi, presiona el botón Play
y escribe cualquiera de estas emociones dentro del Serial Monitor:

<b>JOY</b>, <b>SADNESS</b>, <b>LOVE</b>,
<b>FEAR</b>, <b>CALM</b> o <b>EXCITEMENT</b>.
"""
)}

</p>

</div>
""", unsafe_allow_html=True)
