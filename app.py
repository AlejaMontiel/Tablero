import streamlit as st
from streamlit_drawable_canvas import st_canvas
from PIL import Image
import numpy as np
import base64
import openai
import os

# Función para codificar la imagen en base64
def encode_image_to_base64(image_path):
    try:
        with open(image_path, "rb") as image_file:
            encoded_image = base64.b64encode(image_file.read()).decode("utf-8")
            return encoded_image
    except FileNotFoundError:
        return "Error: La imagen no se encontró en la ruta especificada."

# Personalizar el título de la aplicación con emojis
st.title('🎨 Tablero de Dibujo Inteligente')

# Añadir una breve descripción bajo el título
st.markdown("""
### ¡Bienvenido al tablero donde tu creatividad se puede desplegar! 😎✨
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

# Ingreso de clave API de OpenAI
api_key = st.text_input('🔑 Ingresa tu Clave de API de OpenAI', type="password")
if api_key:
    os.environ['OPENAI_API_KEY'] = api_key

# Botón para analizar la imagen
if st.button("🔍 Analiza la imagen") and canvas_result.image_data is not None and api_key:
    with st.spinner("Analizando tu dibujo..."):
        # Convertir la imagen del lienzo en un arreglo numpy
        input_numpy_array = np.array(canvas_result.image_data)
        input_image = Image.fromarray(input_numpy_array.astype('uint8'), 'RGBA')
        input_image.save('dibujo.png')

        # Codificar la imagen en base64
        base64_image = encode_image_to_base64('dibujo.png')

        # Descripción solicitada para la API de OpenAI
        prompt_text = "Describe brevemente la imagen en español."

        # Crear el payload para la solicitud a OpenAI
        messages = [
            {
                "role": "user",
                "content": [
                    {"type": "text", "text": prompt_text},
                    {
                        "type": "image_url",
                        "image_url": f"data:image/png;base64,{base64_image}",
                    },
                ],
            }
        ]

        # Realizar la solicitud a OpenAI
        try:
            full_response = ""
            response = openai.Completion.create(
                model="gpt-4o-mini",  # Puedes cambiar el modelo si es necesario
                prompt=prompt_text,
                max_tokens=500,
                n=1,
                stop=None,
                temperature=0.5,
            )
            
            # Mostrar la respuesta
            full_response = response.choices[0].text
            st.write("Descripción de la imagen:", full_response)

        except Exception as e:
            st.error(f"Ocurrió un error al analizar la imagen: {e}")
else:
    st.warning("Por favor, dibuja algo en el lienzo y asegúrate de ingresar tu clave API.")

   
