import streamlit as st

st.set_page_config(
    page_title="MoodLamp Studio",
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

st.title("🎨 MoodLamp Studio")

st.subheader("Experiencia Artística Multimodal")

st.write("""
MoodLamp Studio transforma emociones, colores y creatividad
en experiencias visuales interactivas.

Explora ambientes digitales, dibujo libre y visualizaciones artísticas.
""")

st.image(
    "https://images.unsplash.com/photo-1519608487953-e999c86e7455"
)

st.info("Usa el menú lateral para navegar por la experiencia ✨")
