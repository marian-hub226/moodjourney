import streamlit as st

st.title("🌌 Final Experience")

emotion = st.session_state.get("emotion", "Unknown")
color = st.session_state.get("color", "#00F5FF")
intensity = st.session_state.get("intensity", 50)

story = st.session_state.get("story", "")
title = st.session_state.get("title", "Untitled Story")

drawing = st.session_state.get("drawing", None)

st.markdown(f"""
<div style="
padding:40px;
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
font-size:4rem;
color:{color};
text-shadow:0px 0px 30px {color};
">
{emotion}
</h1>

<p style="
text-align:center;
font-size:1.3rem;
color:white;
margin-top:-10px;
">
Your emotional journey has been completed.
</p>

</div>
""",
unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== DRAWING =====

st.markdown("""
<div class="glass-card">
<h2>🎨 Emotional Expression</h2>
</div>
""", unsafe_allow_html=True)

if drawing is not None:

    st.image(
        drawing,
        use_container_width=True
    )

else:

    st.warning("No drawing available.")

st.markdown("<br>", unsafe_allow_html=True)

# ===== STORY =====

st.markdown(f"""
<div class="glass-card">

<h2 style="
color:{color};
">
📖 {title}
</h2>

<p style="
font-size:1.2rem;
line-height:2;
color:white;
">
{story}
</p>

</div>
""",
unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== SUMMARY =====

st.markdown(f"""
<div class="glass-card">

<h2>✨ Emotional Summary</h2>

<ul style="
font-size:1.2rem;
line-height:2;
">

<li><b>Emotion:</b> {emotion}</li>

<li><b>Intensity:</b> {intensity}%</li>

<li><b>Main Color:</b> {color}</li>

</ul>

</div>
""",
unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== FINAL VISUAL =====

st.markdown(f"""
<div style="
height:300px;
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
0px 0px 80px {color};

animation:pulse 3s infinite;
">

✨ {emotion} ✨

</div>
""",
unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.success("Your emotional artwork is complete ✨")
