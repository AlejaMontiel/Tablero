import streamlit as st
from streamlit_drawable_canvas import st_canvas
st.title('Tablero para pintar')

st.sidebar.title("Acerca de:")
st.sidebar.write("En este tablero puede dibujar cualquier cosa y nuestra app adivinará qué es")

# Sidebar components
stroke_width = st.sidebar.slider('Selecciona el ancho de línea', 1, 30, 5)
drawing_mode = st.sidebar.selectbox("Herramienta de dibujo:", ["freedraw", "line", "rect", "circle", "transform"])

# Main interface
st.write("### Color de Trazo")

stroke_color = st.color_picker("Escoge el color", "#000000")

# Create canvas
canvas_result = st_canvas(
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color="#FFFFFF",  # Background color white
    update_streamlit=True,
    height=400,
    width=700,
    drawing_mode=drawing_mode,
    key="canvas",
)
   
