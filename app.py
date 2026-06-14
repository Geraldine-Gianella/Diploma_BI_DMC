import streamlit as st
import pandas as pd

# TÍTULOS E IDENTIFICACIÓN
# Añadir titulo
st.title("APLICACIÓN ANALIZADORA DE DATASETS CON STREAMLIT")
# Añadir barra
st.sidebar.title("Parámetros")
# Añadir imagenes
#st.image("Python_logo.png", width=300)
# Añadir imagenes EN BARRA
#st.sidebar.image("DMC.png", width=100)

st.write("Elaborado por: Geraldine Gianella Geronimo Oscanoa")
st.write("**Año:** 2026")
st.markdown("---")



# Crear módulos de vista
modulos = st.sidebar.selectbox("Seleccione un módulo", ["Home", "Carga y perfil del dataset", "Procesamiento de datos", "Análisis visual"])

if modulos == "Home" :
  st.write("Bienvenido a la aplicación")
    # DETALLES DEL PROYECTO
    
  st.subheader("Objetivo y Alcance")
  st.write(
        "El objetivo de este proyecto es proveer una herramienta interactiva para "
        "la carga, exploración y análisis visual de datos. El alcance incluye el "
        "diagnóstico descriptivo inicial y la generación de gráficos estadísticos "
        "para apoyar la toma de decisiones como Business Analyst."
    )
    
  st.markdown("---")
    
  st.subheader("Datasets Disponibles")
  st.write("**1. AI Impact on Jobs 2030:** Evaluación del impacto de la IA en el mercado laboral, riesgos de reemplazo y salarios.")
  st.write("**2. Sample - Superstore:** Datos de ventas, pedidos y ganancias de una tienda minorista para análisis comercial.")
  st.write("**3. Synthetic E-commerce Order Risk:** Datos enfocados en la detección de fraudes y riesgos en transacciones electrónicas.")
  st.write("**4. Teen Mental Health Dataset:** Análisis del impacto de redes sociales y tiempo de pantalla en el bienestar emocional de adolescentes.")
    
  st.markdown("---")
    
  st.subheader("Tecnologías Usadas")
  st.write("- **Lenguaje:** Python")
  st.write("- **Manipulación de Datos:** Pandas")
  st.write("- **Interfaz de Usuario:** Streamlit")
  st.write("- **Gráficos e Interactividad:** Plotly, Matplotlib y Seaborn")
  st.write("- **Control de Versiones:** GitHub")
    
  st.markdown("---")
    
    # NOTA DE USO RESPONSABLE
    
  st.warning(
        "**Nota de uso responsable:** Los resultados presentados en esta app son "
        "estrictamente exploratorios y no reemplazan una validación técnica o profesional."
    )


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

  # Vista previa del archivo 
  st.header("Vista previa del dataset")
  st.dataframe(data.head())

  # Dimensiones 
  nfilas, ncolumnas = data.shape
  st.header("Dimensiones del DataFrame")  
  st.write("Número de filas:", nfilas)
  st.write("Número de columnas:", ncolumnas)

  # Tipos de variables
  columnas_numericas = data.select_dtypes(
      include="number"
  ).columns.tolist()
  
  columnas_categoricas = data.select_dtypes(
      include=["object", "category"]
  ).columns.tolist()
  
  columnas_fecha = data.select_dtypes(
      include=["datetime64[ns]"]
  ).columns.tolist()
    
  
  
  
else :
  st.write("Por favor cargue su archivo")
