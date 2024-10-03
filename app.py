import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Personalizar el título de la aplicación con emojis
st.title('🎨 Tablero de Dibujo Inteligente')

# Añadir una breve descripción bajo el título
st.markdown("""
### ¡Bienvenido al tablero donde tu creatividad se puede desplegar. 😎✨
""")

# Configurar la barra lateral con colores y una estructura organizada
st.sidebar.title("🖌️ Configuraciones de Dibujo")
st.sidebar.write("Personaliza tu experiencia de dibujo.")

# Configuración del grosor de la línea y la herramienta de dibujo
stroke_width = st.sidebar.slider('Selecciona el ancho de línea', 1, 30, 5)
drawing_mode = st.sidebar.selectbox("Herramienta de dibujo:", ["freedraw", "line", "rect", "circle", "transform"])

# Elegir color del trazo con un subtítulo explicativo
st.sidebar.write("### 🎨 Selecciona el color de trazo")
stroke_color = st.sidebar.color_picker("Escoge el color", "#000000")

# Crear un lienzo personalizado (tamaño 700x1000)
st.write("### 🖼️ Tu Lienzo de Arte")
canvas_result = st_canvas(
    stroke_width=stroke_width,
    stroke_color=stroke_color,
    background_color="#F0F8FF",  # Un color de fondo suave y agradable (AliceBlue)
    update_streamlit=True,
    height=600,  # Aumentar la altura del lienzo
    width=1000,  # Aumentar el ancho del lienzo
    drawing_mode=drawing_mode,
    key="canvas",
)

# Añadir un mensaje debajo del lienzo
st.write("🖌️ **¡Empieza a dibujar y deja volar tu imaginación!**")

# Estilo adicional: cambiar el fondo de la aplicación (solo CSS)
st.markdown("""
<style>
    .reportview-container {
        background-color: #FAF3E0;
        padding: 20px;
    }
    .sidebar .sidebar-content {
        background-color: #FFEDCC;
    }
</style>
""", unsafe_allow_html=True)

   
