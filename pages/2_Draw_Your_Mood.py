import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title("🎨 Draw Your Mood")

st.write("""
Expresa tus emociones a través del dibujo y el color.
""")

stroke_width = st.slider(
    "Tamaño del pincel",
    1,
    25,
    8
)

stroke_color = st.color_picker(
    "Color del pincel",
    "#00F5FF"
)

bg_color = st.color_picker(
    "Color de fondo",
    "#0B1023"
)

drawing_mode = st.selectbox(
    "Modo de dibujo",
    (
        "freedraw",
        "line",
        "rect",
        "circle",
        "transform"
    )
)

st.markdown("---")

canvas_result = st_canvas(
    fill_color="rgba(255, 255, 255, 0.1)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=500,
    width=900,
    drawing_mode=drawing_mode,
    key="canvas",
)

st.markdown("---")

st.success("Tu arte representa tu mood actual ✨")
