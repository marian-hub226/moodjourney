import streamlit as st

st.set_page_config(
    page_title="MoodLamp",
    page_icon="🎨",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

.stApp {
    background-color: #050816;
    color: white;
}

h1, h2, h3 {
    color: #00F5FF;
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

st.title("🎨 MoodLamp")

st.subheader("Sistema Artístico Multimodal Interactivo")

st.write("""
MoodLamp transforma emociones y ambientes en experiencias lumínicas interactivas.

Explora colores, moods y visualizaciones artísticas en tiempo real.
""")

st.image(
    "https://images.unsplash.com/photo-1519608487953-e999c86e7455"
)

st.info("Usa el menú lateral para navegar entre páginas ✨")
