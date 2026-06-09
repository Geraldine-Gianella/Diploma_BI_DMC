import streamlit as st
import pandas as pd

# Añadir titulo
st.title("Proyecto Final Diploma BI")
# Añadir barra
st.sidebar.title("Parámetros")
# Añadir imagenes
st.image("Python_logo.png", width=300)
# Añadir imagenes EN BARRA
st.sidebar.image("DMC.png", width=100)

st.write("Elaborado por: Geraldine Geronimo")

# Crear módulos de vista
modulos = st.sidebar.selectbox("Seleccione un módulo", ["Home", "Carga y perfil del dataset", "Procesamiento de datos", "Análisis visual"])

if modulos == "Home" :
  st.write("Bienvenido a la aplicación")

elif modulos == "Carga y perfil del dataset":
  # Crear un cargador de archivos
  archivo = st.file_uploader("Cargue el archivo excel o csv")
  
  if archivo is not None :
    
    if archivo.name.endswith(".csv"):
      data = pd.read_csv(archivo)
      st.write(data)
    elif archivo.name.endswith(".xlsx"):
      data = pd.read_excel(archivo)
    st.write(data)
  else:
    st.write("Formato no válido")
  
else :
  st.write("Por favor cargue su archivo")
