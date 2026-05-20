import streamlit as st

# ===== INITIAL LANGUAGE =====

if "language" not in st.session_state:

    st.session_state["language"] = "English"

# ===== LANGUAGE SELECTOR =====

language = st.sidebar.selectbox(
    "🌍 Language",
    ["English", "Español"],
    index=0 if st.session_state["language"] == "English" else 1
)

st.session_state["language"] = language

def t(en, es):

    if st.session_state["language"] == "Español":
        return es

    return en

st.set_page_config(
    page_title="MoodJourney",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* ===== FONDO ANIMADO ===== */

.stApp {

    background:
    radial-gradient(circle at top left, #120B25, #050816);

    overflow-x:hidden;

}

/* ===== PARTÍCULAS ===== */

.particles {

    position: fixed;

    width: 100%;
    height: 100%;

    top: 0;
    left: 0;

    z-index: -1;

    overflow: hidden;
}

.particle {

    position: absolute;

    width: 4px;
    height: 4px;

    background: rgba(255,255,255,0.8);

    border-radius: 50%;

    animation: float 20s infinite linear;
}

@keyframes float {

    from {

        transform:
        translateY(100vh);

        opacity: 0;

    }

    10% {

        opacity: 1;

    }

    90% {

        opacity: 1;

    }

    to {

        transform:
        translateY(-10vh);

        opacity: 0;

    }

}

/* ===== SIDEBAR ===== */

[data-testid="stSidebar"] {

    background:
    linear-gradient(
        180deg,
        #0B1023,
        #120B25
    );

    border-right:
    1px solid rgba(255,255,255,0.08);
}

/* ===== TITLES ===== */

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

/* ===== TEXT ===== */

p, li {

    font-size: 1.1rem;

    line-height: 1.8;

    color: white;

}

/* ===== BUTTONS ===== */

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

/* ===== GLASS CARD ===== */

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

</style>

<div class="particles">

<div class="particle" style="left:10%; animation-delay:0s;"></div>
<div class="particle" style="left:20%; animation-delay:2s;"></div>
<div class="particle" style="left:30%; animation-delay:4s;"></div>
<div class="particle" style="left:40%; animation-delay:1s;"></div>
<div class="particle" style="left:50%; animation-delay:3s;"></div>
<div class="particle" style="left:60%; animation-delay:5s;"></div>
<div class="particle" style="left:70%; animation-delay:2s;"></div>
<div class="particle" style="left:80%; animation-delay:4s;"></div>
<div class="particle" style="left:90%; animation-delay:1s;"></div>

</div>

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

Explore emotions through colors,
drawing and storytelling
inside an immersive digital experience.

</p>

</div>
""", unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.info("Use the sidebar to begin your emotional journey ✨")
