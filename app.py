import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Configurar el título principal
st.title("🎨 Tablero para dibujar con IA")

# Configurar la barra lateral
st.sidebar.title("Acerca de:")
st.sidebar.write("En esta aplicación veremos la capacidad que ahora tiene una máquina de interpretar un boceto. ¡Dibuja cualquier cosa y ve lo que sucede!")

# Componentes en la barra lateral
stroke_width = st.sidebar.slider('Selecciona el ancho de línea', 1, 30, 5)
drawing_mode = st.sidebar.selectbox("Herramienta de dibujo:", ["freedraw", "line", "rect", "circle", "transform"])

# Elegir color del trazo
st.write("### Color de Trazo")
stroke_color = st.color_picker("Escoge el color", "#000000")

# Crear el lienzo más grande (600x600)
canvas_result = st_canvas(
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color="#FFFFFF",  # Fondo blanco
    update_streamlit=True,
    height=600,  # Altura del lienzo
    width=600,   # Ancho del lienzo
    drawing_mode=drawing_mode,
    key="canvas",
)

# Mensaje después del análisis
st.write("Cuando termines de dibujar, la aplicación interpretará tu imagen.")
