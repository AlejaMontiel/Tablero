import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.title('Tablero para dibujar')

# Add canvas component
# Specify canvas parameters in application
drawing_mode = "freedraw"
stroke_width = st.slider('Selecciona el ancho de línea', 1, 30, 15)
stroke_color = '#FFFFFF'  # Set line color to white
bg_color = '#000000'

# Create a canvas component
canvas_result = st_canvas(
    fill_color="rgba(255, 165, 0, 0.3)",  # Fixed fill color with some opacity
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color=bg_color,
    height=200,
    width=200,
    key="canvas",
)

# Sidebar content
st.sidebar.title("Acerca de:")
st.sidebar.text("En este tablero puedes")
st.sidebar.text("dibujar cualquier cosa")
st.sidebar.text("y la app la adivinará")

