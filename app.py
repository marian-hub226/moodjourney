import streamlit as st

st.set_page_config(
    page_title="MoodJourney",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* ===== FONDO GENERAL ===== */

.stApp {
    background:
    linear-gradient(
        135deg,
        #050816 0%,
        #0B1023 50%,
        #120B25 100%
    );

    color: white;
}

/* ===== SIDEBAR ===== */

[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #0B1023,
        #120B25
    );

    border-right: 1px solid rgba(255,255,255,0.08);
}

/* ===== TÍTULOS ===== */

h1 {

    color: #00F5FF;
    text-align: center;
    font-size: 4rem;
    font-weight: 800;

    text-shadow:
    0px 0px 25px #00F5FF;

}

h2, h3 {

    color: #FF00E5;

}

/* ===== TEXTO ===== */

p, li {

    font-size: 1.1rem;
    line-height: 1.8;

}

/* ===== BOTONES ===== */

div.stButton > button {

    background:
    linear-gradient(
        135deg,
        #00F5FF,
        #FF00E5
    );

    color: white;

    border: none;

    border-radius: 14px;

    padding:
    0.6rem 1.2rem;

    font-weight: bold;

    box-shadow:
    0px 0px 20px rgba(0,245,255,0.4);

    transition: 0.3s;
}

div.stButton > button:hover {

    transform: scale(1.05);

    box-shadow:
    0px 0px 30px rgba(255,0,229,0.7);

}

/* ===== CARDS ===== */

.glass-card {

    background:
    rgba(255,255,255,0.08);

    border:
    1px solid rgba(255,255,255,0.12);

    border-radius: 25px;

    padding: 35px;

    backdrop-filter: blur(14px);

    box-shadow:
    0px 0px 30px rgba(0,0,0,0.25);

}

/* ===== INFO BOX ===== */

[data-testid="stAlert"] {

    border-radius: 18px;

}

/* ===== INPUTS ===== */

.stTextInput input,
.stTextArea textarea {

    border-radius: 14px !important;

}

/* ===== SLIDER ===== */

.stSlider {

    padding-top: 20px;

}

</style>
""", unsafe_allow_html=True)

st.markdown("""
<div class="glass-card">

<h1>🎨 MoodJourney</h1>

<h3 style="
text-align:center;
margin-top:-10px;
">
An Interactive Emotional Art Experience
</h3>

<p style="
text-align:center;
font-size:1.2rem;
margin-top:30px;
">

MoodJourney transforms emotions into
colors, drawings and stories through
an immersive artistic experience.

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.info("Use the sidebar to begin your emotional journey ✨")
