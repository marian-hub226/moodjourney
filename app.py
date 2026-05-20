import streamlit as st

st.set_page_config(
    page_title="MoodJourney",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #050816, #0B1023);
    color: white;
}

h1, h2, h3 {
    color: #00F5FF;
    text-align: center;
}

[data-testid="stSidebar"] {
    background-color: #0B1023;
}

div.stButton > button {
    background-color: #00F5FF;
    color: black;
    border-radius: 12px;
    border: none;
    font-weight: bold;
}

div.stButton > button:hover {
    background-color: #FF00E5;
    color: white;
}

</style>
""", unsafe_allow_html=True)

st.title("🎨 MoodJourney")

st.subheader("An Interactive Emotional Art Experience")

st.markdown("---")

st.write("""
MoodJourney is an artistic and multimodal experience where users
explore emotions through:

- colors,
- drawing,
- storytelling,
- and interactive visual expression.

Each step builds a personalized emotional journey.
""")

st.markdown("---")

st.info("Use the sidebar to begin your emotional journey ✨")
