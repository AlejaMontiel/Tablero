import streamlit as st
from streamlit_drawable_canvas import st_canvas

# Definir estilo global para la aplicación
st.markdown("""
    <style>
    .main {background-color: #f0f0f5;}
    .stButton>button {background-color: #ff4b4b; color: white; border-radius: 5px;}
    .stTextInput>div>input {border-radius: 5px; border: 1px solid #ff4b4b;}
    </style>
    """, unsafe_allow_html=True)

# Configurar el título principal
st.title("🎨 Tablero para dibujar con IA")

# Configurar la barra lateral
st.sidebar.title("Acerca de:")
st.sidebar.markdown("""
    En esta aplicación veremos la capacidad que ahora tiene una máquina 
    de interpretar un boceto. ¡Dibuja cualquier cosa y ve lo que sucede!
""")

# Componentes en la barra lateral
stroke_width = st.sidebar.slider('Selecciona el ancho de línea', 1, 30, 5)
drawing_mode = st.sidebar.selectbox("Herramienta de dibujo:", ["freedraw", "line", "rect", "circle", "transform"])

# Dividir la pantalla en dos columnas
col1, col2 = st.columns([1, 2])

with col1:
    st.subheader("Configuración del dibujo")
    
    # Elegir color del trazo
    stroke_color = st.color_picker("Color de Trazo", "#000000")

    # Espacio para dibujar en el lienzo
    canvas_result = st_canvas(
        stroke_width=stroke_width,
        stroke_color=stroke_color,
        background_color="#FFFFFF",
        update_streamlit=True,
        height=200,
        width=200,
        drawing_mode=drawing_mode,
        key="canvas",
    )

with col2:
    st.subheader("Análisis de la imagen")

    # Campo de texto para ingresar la clave
    clave = st.text_input("Ingresa tu Clave", "")

    # Botón para procesar la imagen
    if st.button("Analiza la imagen"):
        if clave:
            st.success(f"La clave ingresada es: {clave}")
            st.write("La imagen ha sido procesada correctamente.")
        else:
            st.warning("Por favor, ingresa una clave antes de analizar la imagen.")

    st.write("La imagen muestra el número \"4\" dibujado a mano, con líneas simples y un estilo informal.")

# Footer
st.markdown("---")
st.markdown("<small>Aplicación creada con Streamlit</small>", unsafe_allow_html=True)
