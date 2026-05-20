import streamlit as st

st.title("🎭 Choose Your Emotion")

st.write("""
Every emotion has a color, an energy and a visual identity.

Choose the emotion that represents your current state.
""")

emotion = st.selectbox(
    "✨ Select your emotion",
    [
        "Joy",
        "Sadness",
        "Calm",
        "Fear",
        "Excitement",
        "Love",
        "Loneliness"
    ]
)

color = st.color_picker(
    "🎨 Emotional color",
    "#00F5FF"
)

intensity = st.slider(
    "⚡ Emotional intensity",
    0,
    100,
    50
)

st.session_state["emotion"] = emotion
st.session_state["color"] = color
st.session_state["intensity"] = intensity

st.markdown("<br>", unsafe_allow_html=True)

glow = intensity + 30

st.markdown(f"""
<div style="
padding:50px;
border-radius:35px;

background:
linear-gradient(
135deg,
{color},
#050816
);

display:flex;
flex-direction:column;
justify-content:center;
align-items:center;

box-shadow:
0px 0px {glow}px {color};

border:
1px solid rgba(255,255,255,0.12);

">

<h1 style="
font-size:4rem;
color:white;
text-shadow:0px 0px 30px white;
margin-bottom:10px;
">

{emotion}

</h1>

<p style="
font-size:1.3rem;
color:white;
opacity:0.9;
">

Intensity Level: {intensity}%

</p>

</div>
""",
unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.markdown(f"""
<div class="glass-card">

<h2 style="color:{color};">
🌌 Emotional Reflection
</h2>

<p style="
font-size:1.15rem;
line-height:2;
">

Your selected emotion generates a unique visual atmosphere.
The chosen color represents the emotional energy
that will guide the rest of your artistic journey.

Every next step will be influenced by this choice.

</p>

</div>
""",
unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.success("Emotion captured successfully ✨")
