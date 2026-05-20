import streamlit as st

emotion = st.session_state.get("emotion", "Unknown Emotion")
color = st.session_state.get("color", "#00F5FF")
intensity = st.session_state.get("intensity", 50)

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
font-size:3.5rem;
color:{color};
text-shadow:0px 0px 30px {color};
">

📖 Write Your Story

</h1>

<p style="
text-align:center;
font-size:1.2rem;
color:white;
line-height:1.8;
">

Your emotion is <b>{emotion}</b>.

Now transform your feelings into words
and create a personal emotional narrative.

</p>

</div>
""",
unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== STORY TITLE =====

title = st.text_input(
    "✨ Story Title"
)

st.markdown("<br>", unsafe_allow_html=True)

# ===== STORY BOX =====

story = st.text_area(
    "📝 Emotional Story",
    height=300,
    placeholder="""
Example:

The glowing lights surrounded the silent room while memories slowly faded into the dark...
"""
)

st.session_state["title"] = title
st.session_state["story"] = story

st.markdown("<br>", unsafe_allow_html=True)

# ===== STORY PREVIEW =====

st.markdown(f"""
<div style="
padding:40px;
border-radius:30px;

background:
rgba(255,255,255,0.06);

backdrop-filter:blur(14px);

border:
1px solid rgba(255,255,255,0.08);

box-shadow:
0px 0px 40px {color};

">

<h2 style="
color:{color};
font-size:2.2rem;
margin-bottom:20px;
">

{title if title else "Your Story Title"}

</h2>

<p style="
font-size:1.2rem;
line-height:2;
color:white;
">

{story if story else "Your emotional story preview will appear here..."}

</p>

</div>
""",
unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# ===== FINAL EMOTIONAL CARD =====

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

font-size:2.8rem;
font-weight:bold;

color:white;

box-shadow:
0px 0px {glow}px {color};

">

✨ {emotion} ✨

</div>
""",
unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

st.success("Your emotional story has been saved ✨")
