import streamlit as st

st.title("📊 Live Dashboard")

st.write("Visualización en tiempo real de MoodLamp.")

col1, col2, col3 = st.columns(3)

col1.metric(
    "Estado",
    "ON"
)

col2.metric(
    "Mood",
    "Relax"
)

col3.metric(
    "Intensidad",
    "50%"
)

st.markdown("---")

st.subheader("Visualización artística")

st.markdown("""
<div style="
    height:300px;
    border-radius:20px;
    background: linear-gradient(135deg, #00F5FF, #FF00E5);
    display:flex;
    align-items:center;
    justify-content:center;
    font-size:40px;
    font-weight:bold;
    color:white;
">
MoodLamp Active
</div>
""", unsafe_allow_html=True)

st.markdown("---")

st.info("Conexión ESP32: Simulada en WOKWI")
