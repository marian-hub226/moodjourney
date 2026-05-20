import streamlit as st

# ===== LANGUAGE FUNCTION =====

language = st.session_state.get("language", "English")

def t(en, es):

    if language == "Español":
        return es

    return en

# ===== SESSION DATA =====

emotion = st.session_state.get("emotion", "Unknown")
color = st.session_state.get("color", "#00F5FF")
intensity = st.session_state.get("intensity", 50)

story = st.session_state.get("story", "")
title = st.session_state.get("title", "Untitled Story")

drawing = st.session_state.get("drawing", None)

# ===== HERO SECTION =====

hero_section = f"""
<div style='padding:40px; border-radius:30px; background:linear-gradient(135deg,rgba(255,255,255,0.08),rgba(255,255,255,0.03)); border:1px solid rgba(255,255,255,0.12); box-shadow:0px 0px 50px {color};'>

<h1 style='text-align:center; font-size:4rem; color:{color}; text-shadow:0px 0px 30px {color};'>

{emotion}

</h1>

<p style='text-align:center; font-size:1.3rem; color:white; margin-top:-10px;'>

{t(
"Your emotional journey has been completed.",
"Tu viaje emocional ha sido completado."
)}

</p>

</div>
"""

st.markdown(hero_section, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== DRAWING SECTION =====

drawing_title = f"""
<div style='padding:35px; border-radius:30px; background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.08);'>

<h2 style='color:{color};'>

🎨 {t("Emotional Expression", "Expresión Emocional")}

</h2>

</div>
"""

st.markdown(drawing_title, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

if drawing is not None:

    st.image(
        drawing,
        use_container_width=True
    )

else:

    st.warning(
        t(
            "No drawing available.",
            "No hay dibujo disponible."
        )
    )

st.markdown("<br>", unsafe_allow_html=True)

# ===== STORY SECTION =====

story_title = title if title else t(
    "Untitled Story",
    "Historia Sin Título"
)

story_content = story if story else t(
    "No story available.",
    "No hay historia disponible."
)

story_section = f"""
<div style='padding:35px; border-radius:30px; background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.08); box-shadow:0px 0px 40px {color};'>

<h2 style='color:{color}; font-size:2.2rem; margin-bottom:20px;'>

📖 {story_title}

</h2>

<p style='font-size:1.2rem; line-height:2; color:white;'>

{story_content}

</p>

</div>
"""

st.markdown(story_section, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== SUMMARY =====

summary_section = f"""
<div style='padding:35px; border-radius:30px; background:rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.08);'>

<h2 style='color:white;'>

✨ {t("Emotional Summary", "Resumen Emocional")}

</h2>

<ul style='font-size:1.2rem; line-height:2; color:white;'>

<li>
<b>{t("Emotion", "Emoción")}:</b> {emotion}
</li>

<li>
<b>{t("Intensity", "Intensidad")}:</b> {intensity}%
</li>

<li>
<b>{t("Main Color", "Color Principal")}:</b> {color}
</li>

</ul>

</div>
"""

st.markdown(summary_section, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== FINAL VISUAL =====

glow = intensity + 50

final_visual = f"""
<div style='height:300px; border-radius:30px; background:radial-gradient(circle,{color},#050816); display:flex; justify-content:center; align-items:center; font-size:3rem; font-weight:bold; color:white; box-shadow:0px 0px {glow}px {color};'>

✨ {emotion} ✨

</div>
"""

st.markdown(final_visual, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== EXPORT EXPERIENCE =====

export_text = f"""
MOODJOURNEY — EMOTIONAL EXPERIENCE

Emotion:
{emotion}

Intensity:
{intensity}%

Main Color:
{color}

Story Title:
{title}

Story:
{story}
"""

st.download_button(
    label=t(
        "⬇ Download Emotional Experience",
        "⬇ Descargar Experiencia Emocional"
    ),
    data=export_text,
    file_name="moodjourney_experience.txt",
    mime="text/plain"
)

st.markdown("<br>", unsafe_allow_html=True)

# ===== FINAL MESSAGE =====

st.success(
    t(
        "Your emotional artwork is complete ✨",
        "Tu obra emocional está completa ✨"
    )
)
