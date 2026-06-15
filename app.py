import streamlit as st
import pandas as pd
import plotly.express as px

# CONFIGURACIÓN DE SESSION STATE
# Guardamos el dataset cargado
if "data" not in st.session_state:
    st.session_state.data = None

# Guardamos el nombre del archivo cargado
if "nombre_archivo" not in st.session_state:
    st.session_state.nombre_archivo = None
  
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
  st.subheader("BIENVENIDO A LA APLICACIÓN")
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

  if st.session_state.data is not None:
        st.success(f"Dataset cargado: {st.session_state.nombre_archivo}")
  else:
        st.info("Aún no se ha cargado ningún dataset.")



elif modulos == "Carga y perfil del dataset":
  # Crear un cargador de archivos
  archivo = st.file_uploader("Cargue el archivo Excel o CSV", type=["csv", "xlsx"])
  
  if archivo is not None :

    # Guardamos el nombre del archivo en session_state
    st.session_state.nombre_archivo = archivo.name
    
    if archivo.name.endswith(".csv"):
        st.session_state.data = pd.read_csv(archivo)

    elif archivo.name.endswith(".xlsx"):
        st.session_state.data = pd.read_excel(archivo)

  else:
    st.write("Por favor cargue su archivo")

  # Mostrar información si ya existe una data cargada
  if st.session_state.data is not None:   
    data = st.session_state.data
    st.success("Dataset cargado: " + st.session_state.nombre_archivo)
      
    # Estandarizar el nombre las columnas, todas a minúsculas
    data.columns = data.columns.str.lower()
    
    # Cambiar el espacio en blanco de las columnas por un subguion 
    st.session_state.data.columns = st.session_state.data.columns.str.lower().str.replace(" ", "_")
          
    # Vista previa del archivo 
    st.subheader("Vista previa del dataset")
    st.dataframe(data.head())
    
    # Columnas y tipos de datos
    st.subheader("Columnas y Tipos de Datos")
    info_columnas = pd.DataFrame({
          "Columna": data.columns,
           "Tipo de dato": data.dtypes.astype(str)
    })
    info_columnas = info_columnas.reset_index(drop=True)
    st.dataframe(info_columnas)

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
          
    # Mostrar mensaje si no hay variables de tipo numérica o categórica
    st.write("**Validación de Variables:**")
    if len(columnas_numericas) > 0:
        st.write("- Se identificaron variables numéricas en el dataset.")
    else:
         st.write("- No se identificaron variables numéricas en el dataset.")
          
    if len(columnas_categoricas) > 0:
        st.write("- Se identificaron variables categóricas en el dataset.")
    else:
        st.write("- No se identificaron variables categóricas en el dataset.")
          
    if len(columnas_fecha) > 0:
        st.write("- Se identificaron variables de fecha en el dataset.")
    else:
        st.write("- No se identificaron variables de fecha en el dataset.")
    
    # Información general
    st.subheader("Información general")  
          
    # Dimensiones 
    nfilas, ncolumnas = data.shape 
    
    # Métricas
    total_nulos = data.isnull().sum().sum()
    duplicados = data.duplicated().sum()
    
    # Mostrar dimensiones, tipos de variables y métricas en una tabla
    st.write("- Número de registros:", nfilas)
    st.write("- Número de variables:", ncolumnas)
    st.write("- Variables numéricas identificadas:", len(columnas_numericas))
    st.write("- Variables categóricas identificadas:", len(columnas_categoricas))
    st.write("- Total de valores nulos:", total_nulos)
    st.write("- Total de filas duplicadas:", duplicados)
    
    # Selección de variables 
    st.subheader("Selección de Variables")
    columnas_seleccionadas = st.multiselect("Seleccione una o más columnas",
                                            options=data.columns)
    
    # Mostrar estadísticas desccriptivas de las variables seleccionadas
    if columnas_seleccionadas:
        st.write("Resumen estadístico")
        st.dataframe(data[columnas_seleccionadas].describe(include="all"))
    

elif modulos == "Procesamiento de datos":

  if st.session_state.data is not None:
        data = st.session_state.data
        # Estandarizar data: el nombre de las columanas de la data a minusculas (Se realió en Modulo2)
        data.columns = data.columns.str.lower()
    
        # Estandarizar data: cambiar el espacio en blanco de las columnas por un subguion (Se realizó en Modulo2)
        data.columns = data.columns.str.lower().str.replace(" ", "_")
    
        # Convertir las columnas a fecha si lo son 
        for columna in data.columns:
          if "date" in columna:
              data[columna] = pd.to_datetime(data[columna])
    
        columnas_fecha = data.select_dtypes(
              include=["datetime64[ns]"]
          ).columns.tolist()

        # Mencionar si hay variables tipo fecha y mostrarlas
        st.subheader("Variables de tipo Fecha")
        if len(columnas_fecha) > 0:
            st.write("**Se identificaron las siguientes variables de tipo fecha:**")
            for columna in columnas_fecha:
                st.write("-", columna)
        else:
            st.write("No se identificaron variables de fecha.")

        # Variables numéricas y categóricas
        # Función para identificar variables numéricas
        def obtener_variables_numericas(data):
            return data.select_dtypes(
                include="number"
            ).columns.tolist()
            
        # Función para identificar variables categóricas
        def obtener_variables_categoricas(data):
            return data.select_dtypes(
                include=["object", "category"]
            ).columns.tolist()

        columnas_numericas = obtener_variables_numericas(data)
        columnas_categoricas = obtener_variables_categoricas(data)

        st.subheader("Variables Numéricas")
        for columna in columnas_numericas:
            st.write("- ", columna)
            
        st.subheader("Variables Categóricas")  
        for columna in columnas_categoricas:
            st.write("- ", columna)

        # Valores faltantes por columna
        nulos = data.isnull().sum()
        
        # Porcentaje de nulos
        porcentaje_nulos = (data.isnull().sum() / len(data)) * 100
        
        # Mostramos los valores faltantes y los porcentajes nulos en una tabla
        resumen_nulos = pd.DataFrame({
            "Variable": data.columns,
            "Valores nulos": nulos.values,
            "Porcentaje (%)": porcentaje_nulos.values.round(2)
        })

        st.subheader("Valores Faltantes por Columna")
        st.dataframe(resumen_nulos)

        # Detectar duplicados y reportar su cantidad.
        duplicados = data.duplicated().sum()
        st.subheader("Detección de Duplicados")
        
        if duplicados > 0:
            st.write("Se identificaron", duplicados, "filas duplicadas en el dataset.")
        else:
            st.write("No se identificaron filas duplicadas en el dataset.")

        # Outliers en variables numéricas usando IQR o boxplots.
      
        st.subheader("Detección de Outliers en Variables Numéricas")
        if len(columnas_numericas) > 0:
            fig1 = px.box( data[columnas_numericas], title="Boxplots de Variables Numéricas")
            st.plotly_chart(fig1)     
        else:
            st.write( "No se identificaron variables numéricas en el dataset.")

        # Permitir filtros dinámicos por categorías, rangos numéricos o fechas cuando apliquen
        st.subheader("Filtros Dinámicos")
        data_filtrada = data
        # Filtro categórico
        if len(columnas_categoricas) > 0:
            variable_cat = st.selectbox("Variable categórica", columnas_categoricas)
            categorias = st.multiselect("Seleccione categorías", 
                                        data[variable_cat].dropna().unique())
        
            if categorias:
                data_filtrada = data_filtrada[data_filtrada[variable_cat].isin(categorias)]

            # Filtro numérico 
            if len(columnas_numericas) > 0:           
                variable_num = st.selectbox("Variable numérica", columnas_numericas)
                minimo = float(data[variable_num].min())
                maximo = float(data[variable_num].max())
                rango = st.slider("Seleccione rango", minimo, maximo, (minimo, maximo))           
                data_filtrada = data_filtrada[
                    (data_filtrada[variable_num] >= rango[0]) &
                    (data_filtrada[variable_num] <= rango[1])]

                # Filtros por fechas 
                if len(columnas_fecha) > 0:
                    variable_fecha = st.selectbox("Variable fecha", columnas_fecha)
                    fecha_min = data[variable_fecha].min()
                    fecha_max = data[variable_fecha].max()
                    fechas = st.date_input("Seleccione rango de fechas",
                        value=(fecha_min, fecha_max))

                    # Mostrar resultado
                    st.subheader("Dataset Filtrado")
                    st.write("Número de registros:", len(data_filtrada))     
                    st.dataframe(data_filtrada)

        # Evitar que la app se detenga por errores; usar validaciones y mensajes con st.warning(), st.info() o st.error().

            
          
else :
  st.write("Formato no válido")
