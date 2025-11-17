import streamlit as st
from PIL import Image

st.set_page_config(page_title="youtube", page_icon=":alien:", layout="wide")

menu = st.sidebar.radio("Navegación", ["Inicio", "Youtube", "Los polinesios", "videos", "¿Quienes somos?"])

if menu == "Inicio":
    st.title("Bienvenido a mi sitio web")
    st.header("Bienvenido a mi aplicacion de streamlit:upside_down_face:")
    st.subheader("¿En que consiste?")
    st.image("lpss.jpg")
    st.text("Esta aplicacion consite en saber quienes son los polinesios, aqui averiguaras sus videos, su musica y saber quienes son ellos. Te invito a saber mucho mas de esto")
    st.image("Youtube-PNG-Photo.png", use_container_width=True)
    
elif menu == "Youtube":
    st.title("Youtube")
    st.header("¿Que es youtube?")
    st.subheader("youtube es una aplicacion la cual hay distintos youtubers que muestran distintos contenidos")
    st.text("En este sitio web hablare sobre Los Polinesios")
    st.audio("noncopyright-music-pianos-295174.mp3")
    st.video("https://www.youtube.com/watch?v=pIDDHYxxBbE")
    st.video("https://www.youtube.com/watch?v=0CTp1a-aCUM")
    st.video("https://www.youtube.com/watch?v=NG5w1IGULEw")
    
elif menu == "Los polinesios":
    st.title("Los polinesios:teddy_bear:")
    st.header("Aqui encontraras quienes son y su musica")
    st.subheader("Los polinesios son unos youtubers el cual consiste en tres hermanos, ellos son creadores de contenido haciendo distintos retos y challenge")
    st.audio("intro-music-black-box-saxy-blasts-12574.mp3")
    st.video("https://www.youtube.com/watch?v=BfX2qAMp5ac")
    st.video("https://www.youtube.com/watch?v=w9Wkp3ygJmk&list=RDw9Wkp3ygJmk&start_radio=1")
    st.video("https://www.youtube.com/watch?v=hLzgZsCIYhE&list=RDhLzgZsCIYhE&start_radio=1")
    
elif menu == "videos":
    st.title("Los polinesios")
    st.image("imagelp.jpg")
    st.header("En este canal encontraras a los tres integrantes pero con contenido de su vida rutinaria o contestando preguntas de sus fans")
    st.video("https://www.youtube.com/watch?v=3bTER3G6YlI")
    st.title("Musas")
    st.image("musas.jpg")
    st.header("En este canal podremos encontrar a solo dos integrantes de este grupo, lo que hacen es contenido de maquillaje, recetas de comida, podcast, etc.")
    st.video("https://www.youtube.com/watch?v=b0M8P-67yJU")
    st.title("ExtraPolinesios")
    st.image("extra.jpg")
    st.header("En este canal se encuentran los tres integrantes pero con contenidos de retos o challenge")
    st.video("https://www.youtube.com/watch?v=1VUVJ5oBLw4")
    
elif menu == "¿Quienes somos?":
    st.image("telefono.jpg")
    st.title("¿Quienes somos?:monocle:")
    st.header("soy antonia y este es mi sitio web, cree este sitio para que conozcan la vida de youtube y sus grandes youtubers que para mi parecer son los polinesios")
    st.write("""
    ### Equipo stio web:
    - **CEO:** [ANTONIA]  
    - **Product Manager:** [ANTONIA]  
      
    Email: youtube.lpp@gmail.com  
    """)

    st.image("ytb.png")
    st.audio("cooking-food-music-247352.mp3")
    
