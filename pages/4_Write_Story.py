import streamlit as st

st.title("📖 Write Your Story")

emotion = st.session_state.get("emotion", "Unknown Emotion")
color = st.session_state.get("color", "#00F5FF")
intensity = st.session_state.get("intensity", 50)

st.write(f"""
Your journey so far:

- Emotion: {emotion}
- Emotional intensity: {intensity}%
- Main color: {color}

Now transform your emotions into words.
""")

st.markdown("---")

story = st.text_area(
    "Write a short emotional story",
    height=250,
    placeholder="""
Example:

The blue lights surrounded me while silence filled the room...
"""
)

title = st.text_input(
    "Give your story a title"
)

st.session_state["story"] = story
st.session_state["title"] = title

st.markdown("---")

st.markdown(f"""
<div style="
padding:30px;
border-radius:25px;
background:{color};
color:white;
box-shadow:0px 0px 60px {color};
">

<h2>{title if title else "Your Story Title"}</h2>

<p style="font-size:20px;">
{story if story else "Your emotional story will appear here..."}
</p>

</div>
""",
unsafe_allow_html=True)

st.success("Your emotional story has been saved ✨")
