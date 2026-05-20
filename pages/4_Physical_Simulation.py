import streamlit as st

st.title("🖥️ Physical Simulation")

st.write("""
MoodLamp Studio también integra interacción con hardware
simulado usando ESP32 y WOKWI.
""")

st.markdown("---")

st.subheader("🔌 Componentes Utilizados")

col1, col2 = st.columns(2)

with col1:

    st.markdown("""
    ### Hardware
    - ESP32
    - LED RGB
    - Simulación WOKWI
    - Conexión WiFi virtual
    """)

with col2:

    st.markdown("""
    ### Software
    - Streamlit
    - Python
    - WOKWI
    - GitHub
    """)

st.markdown("---")

st.subheader("🎨 Funcionamiento")

st.write("""
El usuario interactúa con MoodLamp Studio mediante:

- selección de colores,
- dibujo libre,
- controles visuales,
- ambientes interactivos.

Estas interacciones representan emociones y estados de ánimo,
los cuales pueden reflejarse físicamente mediante iluminación RGB
simulada en WOKWI.
""")

st.markdown("---")

st.subheader("🌈 Simulación RGB")

selected_color = st.color_picker(
    "Selecciona un color de simulación",
    "#00F5FF"
)

st.markdown(f"""
<div style="
height:250px;
border-radius:25px;
background:{selected_color};
display:flex;
justify-content:center;
align-items:center;
font-size:36px;
font-weight:bold;
color:white;
box-shadow:0px 0px 80px {selected_color};
">

RGB Simulation

</div>
""",
unsafe_allow_html=True)

st.markdown("---")

st.subheader("🧠 Arquitectura del Sistema")

st.code("""
Usuario
   ↓
MoodLamp Studio (Streamlit)
   ↓
Visualización Artística
   ↓
Simulación Física WOKWI
   ↓
ESP32 + LED RGB
""")

st.success("Simulación física integrada correctamente ✨")
