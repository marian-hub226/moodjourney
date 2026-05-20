import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("🎨 Draw Your Emotion")

emotion = st.session_state.get("emotion", "Unknown Emotion")
color = st.session_state.get("color", "#00F5FF")
intensity = st.session_state.get("intensity", 50)

st.write(f"""
You selected the emotion:

### {emotion}

Now express it visually through drawing.
""")

st.markdown("---")

stroke_width = st.slider(
    "Brush size",
    1,
    25,
    8
)

drawing_mode = st.selectbox(
    "Drawing mode",
    (
        "freedraw",
        "line",
        "rect",
        "circle",
        "transform"
    )
)

canvas_result = st_canvas(
    fill_color="rgba(255,255,255,0.1)",
    stroke_width=stroke_width,
    stroke_color=color,
    background_color="#0B1023",
    height=500,
    width=900,
    drawing_mode=drawing_mode,
    key="canvas",
)

st.session_state["drawing"] = canvas_result.image_data

st.markdown("---")

st.markdown(f"""
<div style="
height:180px;
border-radius:25px;
background:{color};
display:flex;
justify-content:center;
align-items:center;
font-size:36px;
font-weight:bold;
color:white;
box-shadow:0px 0px 70px {color};
">

{emotion}

</div>
""",
unsafe_allow_html=True)

st.success("Your emotional drawing has been saved ✨")
