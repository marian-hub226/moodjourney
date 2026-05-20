import streamlit as st
from streamlit_drawable_canvas import st_canvas

emotion = st.session_state.get("emotion", "Unknown Emotion")
color = st.session_state.get("color", "#00F5FF")
intensity = st.session_state.get("intensity", 50)

st.markdown(f"""
<div style="
padding:35px;
border-radius:30px;

background:
linear-gradient(
135deg,
rgba(255,255,255,0.08),
rgba(255,255,255,0.03)
);

backdrop-filter:blur(16px);

border:
1px solid rgba(255,255,255,0.12);

box-shadow:
0px 0px 50px {color};

">

<h1 style="
text-align:center;
font-size:3.5rem;
color:{color};
text-shadow:0px 0px 30px {color};
">

🎨 Draw Your Emotion

</h1>

<p style="
text-align:center;
font-size:1.2rem;
color:white;
line-height:1.8;
">

Your selected emotion is:

<b>{emotion}</b>

Express it visually through shapes,
colors and movement.

</p>

</div>
""",
unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== CONTROLS =====

col1, col2 = st.columns(2)

with col1:

    stroke_width = st.slider(
        "🖌 Brush Size",
        1,
        25,
        8
    )

with col2:

    drawing_mode = st.selectbox(
        "✨ Drawing Mode",
        (
            "freedraw",
            "line",
            "rect",
            "circle",
            "transform"
        )
    )

st.markdown("<br>", unsafe_allow_html=True)

# ===== CANVAS =====

st.markdown(f"""
<div style="
padding:20px;
border-radius:25px;

background:
rgba(255,255,255,0.05);

border:
1px solid rgba(255,255,255,0.08);

box-shadow:
0px 0px 40px {color};

">
""",
unsafe_allow_html=True)

canvas_result = st_canvas(
    fill_color="rgba(255,255,255,0.05)",
    stroke_width=stroke_width,
    stroke_color=color,
    background_color="#050816",
    height=550,
    width=900,
    drawing_mode=drawing_mode,
    key="canvas",
)

st.markdown("</div>", unsafe_allow_html=True)

st.session_state["drawing"] = canvas_result.image_data

st.markdown("<br>", unsafe_allow_html=True)

# ===== EMOTION VISUAL =====

glow = intensity + 40

st.markdown(f"""
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

font-size:3rem;
font-weight:bold;

color:white;

box-shadow:
0px 0px {glow}px {color};

">

{emotion}

</div>
""",
unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.success("Your emotional artwork has been saved ✨")
