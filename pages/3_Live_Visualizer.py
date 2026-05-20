import streamlit as st

st.title("🌈 Live Visualizer")

st.write("""
Transforma emociones en ambientes visuales interactivos.
""")

mood = st.selectbox(
    "Selecciona tu mood actual",
    [
        "🌙 Relax",
        "🔥 Energetic",
        "💙 Melancholy",
        "🎉 Party",
        "🎯 Focus"
    ]
)

primary_color = st.color_picker(
    "Color principal",
    "#00F5FF"
)

secondary_color = st.color_picker(
    "Color secundario",
    "#FF00E5"
)

intensity = st.slider(
    "Intensidad visual",
    0,
    100,
    70
)

blur = 100 - intensity

st.markdown("---")

st.subheader("Visualización generada")

st.markdown(f"""
<div style="
height:450px;
border-radius:30px;
background:
linear-gradient(
135deg,
{primary_color},
{secondary_color}
);
display:flex;
justify-content:center;
align-items:center;
font-size:42px;
font-weight:bold;
color:white;
box-shadow:0px 0px {blur}px {primary_color};
">

{mood}

</div>
""",
unsafe_allow_html=True)

st.markdown("---")

st.metric(
    label="Nivel de intensidad",
    value=f"{intensity}%"
)

st.success("Ambiente visual generado correctamente ✨")
