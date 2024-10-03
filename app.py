import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Configurar la barra lateral
st.sidebar.title("Acerca de:")
st.sidebar.write("En esta aplicación veremos la capacidad que ahora tiene una máquina de interpretar un boceto. ¡Dibuja cualquier cosa y ve lo que sucede!")

# Configuración del grosor de la línea y herramienta de dibujo en la barra lateral
stroke_width = st.sidebar.slider('Selecciona el ancho de línea', 1, 30, 5)
drawing_mode = st.sidebar.selectbox("Herramienta de dibujo:", ["freedraw", "line", "rect", "circle", "transform"])

# Elegir color del trazo
st.write("### Color de Trazo")
stroke_color = st.color_picker("Escoge el color", "#000000")

# Crear un lienzo mucho más grande (1200x1200)
canvas_result = st_canvas(
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color="#FFFFFF",  # Fondo blanco
    update_streamlit=True,
    height=1200,  # Altura del lienzo
    width=1200,   # Ancho del lienzo
    drawing_mode=drawing_mode,
    key="canvas",
)

# Botón para analizar la imagen
if st.button("Analiza la imagen"):
    st.write("La imagen ha sido procesada.")
    # Lógica de análisis de imagen podría añadirse aquí

