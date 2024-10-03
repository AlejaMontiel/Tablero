import streamlit as st
from streamlit_drawable_canvas import st_canvas

st.sidebar.title("Acerca de:")
st.sidebar.write("En esta aplicación veremos la capacidad que ahora tiene una máquina de interpretar un boceto.")

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
    height=200,
    width=200,
    drawing_mode=drawing_mode,
    key="canvas",
)

# Input and button for image analysis
clave = st.text_input("Ingresa tu Clave")
if st.button("Analiza la imagen"):
    if clave:
        st.write(f"La clave ingresada es: {clave}")
        st.write("La imagen ha sido procesada.")

