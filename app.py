import streamlit as st
# Añadir titulo
st.title("Proyecto Final Diploma BI")
# Añadir barra
st.sidebar.title("Parámetros")
# Añadir imagenes
st.image("Python_logo.png", width=300)
# Añadir imagenes EN BARRA
st.sidebar.image("DMC.png", width=100)

st.write("Elaborado por: Geraldine Geronimo")

archivo = st.file_uploader("Cargue el archivo excel o csv")

if archivo is not None:
  if arcivo.name.endswith(".csv"):
    data = pd.read_csv(archivo)
    str.write(data)
  elif archivo.name.enswith(".xlsx"):
    data = pd.read_excel(archivo)
    str.write(data)
  else: 
    str.write("Formato no válido")
  
else:
  st.write("Por favor cargue su archivo")
