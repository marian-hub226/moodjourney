import streamlit as st

st.title("🎭 Choose Your Emotion")

emotion = st.selectbox(
    "Select your current emotion",
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
    "Choose a color that represents your emotion",
    "#00F5FF"
)

intensity = st.slider(
    "Emotional intensity",
    0,
    100,
    50
)

st.session_state["emotion"] = emotion
st.session_state["color"] = color
st.session_state["intensity"] = intensity

st.markdown("---")

st.markdown(f"""
<div style="
height:300px;
border-radius:30px;
background:{color};
display:flex;
justify-content:center;
align-items:center;
font-size:40px;
font-weight:bold;
color:white;
box-shadow:0px 0px 60px {color};
">

{emotion}

</div>
""",
unsafe_allow_html=True)

st.success("Emotion saved successfully ✨")
