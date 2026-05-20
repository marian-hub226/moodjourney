import streamlit as st

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

    padding:40px;

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

.preview-box {

    padding:40px;

    border-radius:30px;

    background:
    rgba(255,255,255,0.06);

    backdrop-filter: blur(14px);

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

📖 {t("Write Your Story", "Escribe Tu Historia")}

</h1>

<p style="
text-align:center;
font-size:1.2rem;
color:white;
line-height:1.8;
">

{t(
f'''
Your emotion is <b>{emotion}</b>.

Now transform your feelings into words
and create a personal emotional narrative.
''',
f'''
Tu emoción es <b>{emotion}</b>.

Ahora transforma tus sentimientos en palabras
y crea una narrativa emocional personal.
'''
)}

</p>

</div>
"""

st.markdown(hero_section, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== STORY TITLE =====

title = st.text_input(
    t(
        "✨ Story Title",
        "✨ Título de la Historia"
    )
)

st.markdown("<br>", unsafe_allow_html=True)

# ===== STORY BOX =====

story = st.text_area(
    t(
        "📝 Emotional Story",
        "📝 Historia Emocional"
    ),
    height=300,
    placeholder=t(
        """
Example:

The glowing lights surrounded the silent room while memories slowly faded into the dark...
""",
        """
Ejemplo:

Las luces brillantes rodeaban la habitación silenciosa mientras los recuerdos desaparecían lentamente en la oscuridad...
"""
    )
)

# ===== SAVE DATA =====

st.session_state["title"] = title
st.session_state["story"] = story

st.markdown("<br>", unsafe_allow_html=True)

# ===== STORY PREVIEW =====

preview_title = title if title else t(
    "Your Story Title",
    "El Título de Tu Historia"
)

preview_story = story if story else t(
    "Your emotional story preview will appear here...",
    "La vista previa de tu historia emocional aparecerá aquí..."
)

story_preview = f"""
<div class="preview-box"
style="
box-shadow:0px 0px 40px {color};
">

<h2 style="
color:{color};
font-size:2.2rem;
margin-bottom:20px;
">

{preview_title}

</h2>

<p style="
font-size:1.2rem;
line-height:2;
color:white;
">

{preview_story}

</p>

</div>
"""

st.markdown(story_preview, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== FINAL EMOTION CARD =====

glow = intensity + 40

emotion_card = f"""
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

font-size:2.8rem;
font-weight:bold;

color:white;

box-shadow:
0px 0px {glow}px {color};

">

✨ {emotion} ✨

</div>
"""

st.markdown(emotion_card, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== FINAL MESSAGE =====

st.success(
    t(
        "Your emotional story has been saved ✨",
        "Tu historia emocional ha sido guardada ✨"
    )
)
