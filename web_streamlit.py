"""
Hacer comentarios aquí
"""

import streamlit as st
from PIL import Image

# Crear aplicación
st.set_page_config(page_title="Santiago Danielli",
                   layout="centered")

# Variables de Texto

descripcion_personal = """
Como Data Analyst me especializo en brindar servicios de consultoría analítica e implementar soluciones de 
business intelligence. Tengo conocimiento y experiencia en las más importantes tecnologías para aportar a la 
toma de decisiones a partir de la explotación de los datos.
"""

concepto_ad = """
El análisis de datos es un proceso integral que implica examinar, limpiar y modelar datos con el objetivo de 
descubrir patrones, tendencias y obtener información significativa. Este enfoque se utiliza en diversas 
disciplinas, desde la investigación científica hasta la toma de decisiones empresariales. En primer lugar, 
implica la recopilación y organización de datos brutos provenientes de diversas fuentes, como encuestas, 
sensores o bases de datos. Posteriormente, se aplican técnicas estadísticas y algoritmos de aprendizaje 
automático para identificar relaciones, correlaciones y generar insights valiosos. El análisis de datos 
se ha convertido en una herramienta esencial para la toma de decisiones informadas, ya que proporciona una 
comprensión profunda de los fenómenos estudiados y facilita la anticipación de tendencias futuras.

En el ámbito empresarial, el análisis de datos se emplea para optimizar operaciones, mejorar la eficiencia y 
desarrollar estrategias comerciales más efectivas. A través de la visualización de datos, los analistas 
pueden comunicar de manera clara y accesible los hallazgos, permitiendo a las organizaciones tomar decisiones 
basadas en evidencia. En resumen, el análisis de datos es una herramienta poderosa que permite convertir 
grandes cantidades de información en conocimiento significativo, desempeñando un papel crucial en la toma de 
decisiones en diversos campos.
"""

# Variables de imagenes

data_viz_1 = Image.open("data_viz_3.png")
data_viz_2 = Image.open("data_viz_4.png")

# Encabezado y primera parte
st.write("Santiago Danielli")
colum1, colum2 = st.columns(2)
with colum1:
    st.header("Transformando datos en conocimiento")
    st.markdown(descripcion_personal)
with colum2:
    st.image(data_viz_1)

st.markdown("------")

# Segunda parte
st.header("¿Qué es el análisis de datos?")
st.markdown(concepto_ad)


st.markdown("------")

columna1, columna2 = st.columns(2)
with columna1:
    st.subheader("Podes encontrarme en:")
    st.link_button(":briefcase: Perfil de Linkedin", "https://www.linkedin.com/in/santiago-danielli-3a6859b2/")
    st.link_button(":computer: Github - Proyectos", "https://github.com/santiagodanielli")
    st.link_button(":page_facing_up: Curriculum Vitae", "https://santiagodanielli-cv.streamlit.app/")
with columna2:
    st.image(data_viz_2)

st.markdown("------")

# Formulario para mails
formulario_contacto = """
<form action="https://formsubmit.co/santiagodanielli0@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Tu nombre" required>
     <input type="email" name="email" placeholder="Tu correo electrónico" required>
     <textarea name="message" placeholder="Escribe tu mensaje a continuación"></textarea>
     <button type="submit">Enviar</button>
</form>
"""
st.subheader("También podes enviarme un correo electrónico:")
st.markdown(formulario_contacto, unsafe_allow_html=True)

# Usar css file
def local_css(file_name):
    with open(file_name)as f:
        st.markdown(f"<style>{f.read()}</style", unsafe_allow_html=True)

local_css("style/style.css")



