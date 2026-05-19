import streamlit as st

st.title("🎨 Mood Creator")

st.write("Diseña un ambiente emocional interactivo.")

mood = st.selectbox(
    "Selecciona un mood",
    [
        "🌙 Relax",
        "😊 Happy",
        "🎯 Focus",
        "🎉 Party",
        "💙 Sad"
    ]
)

color = st.color_picker(
    "Color principal",
    "#00F5FF"
)

intensity = st.slider(
    "Intensidad de luz",
    0,
    100,
    50
)

message = st.text_input(
    "Describe tu ambiente ideal"
)

st.markdown("---")

st.subheader("Vista previa")

st.markdown(
    f"""
    <div style="
        background-color:{color};
        padding:40px;
        border-radius:20px;
        text-align:center;
        color:black;
        font-size:28px;
        font-weight:bold;
    ">
        {mood}
    </div>
    """,
    unsafe_allow_html=True
)

st.write(f"✨ Intensidad: {intensity}%")

if st.button("Activar Mood"):
    st.success(f"{mood} activado correctamente ✨")
