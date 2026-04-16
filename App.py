import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.set_page_config(
    page_title="Tablero de dibujo libre",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.title("Tablero para dibujar")
image = Image.open('pollito.jpg')

with st.sidebar:
    st.subheader("customizar el Tablero")

    # Canvas dimensions (moved to the top)
    st.subheader("tamaño del Tablero")
    canvas_width = st.slider("Ancho del tablero", 300, 700, 500, 50)
    canvas_height = st.slider("Alto del tablero", 200, 600, 300, 50)

    # Drawing mode selector
    drawing_mode = st.selectbox(
        "tipo de pincel:",
        ("freedraw", "line", "rect", "circle", "transform", "polygon", "point"),
    )

    # Stroke width slider
    stroke_width = st.slider("ancho de la línea", 1, 30, 15)

    # Stroke color picker
    stroke_color = st.color_picker("Color del pincel", "#FFFFFF")

    # Background color
    bg_color = st.color_picker("Color de fondo", "#000000")

# Create a canvas component with dynamic key
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=canvas_height,
    width=canvas_width,
    drawing_mode=drawing_mode,
    key=f"canvas_{canvas_width}_{canvas_height}",  # Dynamic key based on dimensions
)
