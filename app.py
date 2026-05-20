import streamlit as st

# ===== LANGUAGE =====

if "language" not in st.session_state:

    st.session_state["language"] = "English"

language = st.sidebar.selectbox(
    "🌍 Language",
    ["English", "Español"],
    index=0 if st.session_state["language"] == "English" else 1
)

st.session_state["language"] = language

# ===== TRANSLATION =====

def t(en, es):

    if st.session_state["language"] == "Español":
        return es

    return en

# ===== PAGE =====

st.set_page_config(
    page_title="MoodJourney",
    page_icon="🌌",
    layout="wide"
)

st.title("🌌 MoodJourney")

st.write(
    t(
        """
Welcome to an immersive emotional and artistic experience.

Use the sidebar to navigate through the journey.
""",
        """
Bienvenida a una experiencia emocional y artística inmersiva.

Usa el menú lateral para navegar por el viaje.
"""
    )
)

st.markdown("---")

st.success(
    t(
        "Choose a page from the sidebar ✨",
        "Escoge una página desde el menú lateral ✨"
    )
)
