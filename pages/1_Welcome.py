import streamlit as st

# ===== LANGUAGE FUNCTION =====

language = st.session_state.get("language", "English")

def t(en, es):

    if language == "Español":
        return es

    return en

# ===== PAGE =====

st.markdown("""
<style>

.hero-title {

    text-align:center;
    font-size:4.5rem;
    font-weight:800;

    color:#00F5FF;

    text-shadow:
    0px 0px 30px #00F5FF;

    margin-bottom:10px;
}

.hero-subtitle {

    text-align:center;
    font-size:1.3rem;

    color:white;

    opacity:0.9;

    line-height:2;
}

.glass-box {

    padding:45px;

    border-radius:35px;

    background:
    rgba(255,255,255,0.06);

    border:
    1px solid rgba(255,255,255,0.12);

    backdrop-filter: blur(14px);

    box-shadow:
    0px 0px 40px rgba(0,245,255,0.2);
}

.feature-card {

    padding:25px;

    border-radius:25px;

    background:
    rgba(255,255,255,0.05);

    border:
    1px solid rgba(255,255,255,0.08);

    margin-top:20px;

    box-shadow:
    0px 0px 20px rgba(255,255,255,0.05);
}

</style>
""", unsafe_allow_html=True)

# ===== HERO =====

hero_section = f"""
<div class="glass-box">

<h1 class="hero-title">

🌌 MoodJourney

</h1>

<p class="hero-subtitle">

{t(
'''
An immersive emotional and artistic experience
where colors, emotions and storytelling merge
into a unique digital journey.
''',
'''
Una experiencia inmersiva emocional y artística
donde los colores, emociones e historias
se unen en un viaje digital único.
'''
)}

</p>

</div>
"""

st.markdown(hero_section, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== EXPERIENCE STEPS =====

step_1 = t(
"Choose an emotion and color",
"Escoge una emoción y un color"
)

step_2 = t(
"Express yourself through drawing",
"Exprésate a través del dibujo"
)

step_3 = t(
"Write a short emotional story",
"Escribe una pequeña historia emocional"
)

step_4 = t(
"Generate your final artistic experience",
"Genera tu experiencia artística final"
)

experience_section = f"""
<div class="glass-box">

<h2 style="
color:#FF00E5;
text-align:center;
margin-bottom:30px;
">

✨ {t("Your Journey", "Tu Viaje")}

</h2>

<div class="feature-card">
<h3>1️⃣ {step_1}</h3>
</div>

<div class="feature-card">
<h3>2️⃣ {step_2}</h3>
</div>

<div class="feature-card">
<h3>3️⃣ {step_3}</h3>
</div>

<div class="feature-card">
<h3>4️⃣ {step_4}</h3>
</div>

</div>
"""

st.markdown(experience_section, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== FINAL MESSAGE =====

st.success(
    t(
        "Ready to begin? Use the sidebar ✨",
        "¿Lista para comenzar? Usa el menú lateral ✨"
    )
)
