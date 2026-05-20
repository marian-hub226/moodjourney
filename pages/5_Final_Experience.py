import streamlit as st
import numpy as np

st.title("🌌 Final Experience")

emotion = st.session_state.get("emotion", "Unknown")
color = st.session_state.get("color", "#00F5FF")
intensity = st.session_state.get("intensity", 50)

story = st.session_state.get("story", "")
title = st.session_state.get("title", "Untitled Story")

drawing = st.session_state.get("drawing", None)

st.write("""
This is the final result of your emotional journey.
""")

st.markdown("---")

st.subheader("🎭 Your Emotion")

st.markdown(f"""
<div style="
height:220px;
border-radius:30px;
background:{color};
display:flex;
justify-content:center;
align-items:center;
font-size:42px;
font-weight:bold;
color:white;
box-shadow:0px 0px {intensity}px {color};
">

{emotion}

</div>
""",
unsafe_allow_html=True)

st.markdown("---")

st.subheader("🎨 Your Emotional Drawing")

if drawing is not None:

    st.image(
        drawing,
        caption="Your artistic emotional expression",
        use_container_width=True
    )

else:

    st.warning("No drawing found.")

st.markdown("---")

st.subheader("📖 Your Story")

st.markdown(f"""
<div style="
padding:35px;
border-radius:25px;
background:rgba(255,255,255,0.08);
backdrop-filter:blur(12px);
border:1px solid rgba(255,255,255,0.15);
">

<h2 style="color:white;">
{title}
</h2>

<p style="
font-size:20px;
line-height:1.8;
color:white;
">
{story}
</p>

</div>
""",
unsafe_allow_html=True)

st.markdown("---")

st.subheader("✨ Emotional Summary")

st.write(f"""
- Emotion selected: **{emotion}**
- Emotional intensity: **{intensity}%**
- Main emotional color: **{color}**
""")

st.markdown("---")

st.success("Your emotional journey is complete ✨")
