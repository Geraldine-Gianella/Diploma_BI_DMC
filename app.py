import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np

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
st.write("Herramienta interactiva para la carga, procesamiento, exploración y "
    "visualización de datos mediante Python y Streamlit.")
st.write("**Elaborado por:** Geraldine Gianella Geronimo Oscanoa")
st.write("**Año:** 2026")
st.markdown("---")


# Crear módulos de vista
st.sidebar.title("Navegación")
modulos = st.sidebar.selectbox("Seleccione un módulo",["🏠 Home","📂 Carga y perfil del dataset",
                                                       "⚙️ Procesamiento de datos","📊 Análisis visual"])
st.sidebar.markdown("---")

st.sidebar.subheader("Información")
if st.session_state.data is not None:
    st.sidebar.success("Dataset cargado: " +  st.session_state.nombre_archivo)
else:
    st.sidebar.info("No hay dataset cargado")
st.sidebar.markdown("---")

st.sidebar.image("DMC.png", width=100)
st.sidebar.subheader("Diploma Business Analyst")
st.sidebar.write("Exploración y Visualización de Datos con Python")

# Añadir imagenes
#st.image("Python_logo.png", width=300)
# Añadir imagenes EN BARRA
#st.sidebar.image("DMC.png", width=100)


if modulos == "🏠 Home" :
  st.subheader("BIENVENIDO A LA APLICACIÓN")
  st.info("Esta aplicación permite cargar, procesar, explorar y visualizar datasets "
    "de forma interactiva para apoyar el análisis y la toma de decisiones.")

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
  st.write("📌 AI Impact on Jobs 2030")
  st.write("Evaluación del impacto de la IA en el mercado laboral, riesgos de reemplazo y salarios.")
    
  st.write("📌 Sample Superstore")
  st.write("Datos de ventas, pedidos y ganancias de una tienda minorista para análisis comercial.")
    
  st.write("📌 Synthetic E-commerce Order Risk")
  st.write("Datos enfocados en la detección de fraudes y riesgos en transacciones electrónicas.")
    
  st.write("📌 Teen Mental Health Dataset")
  st.write("Análisis del impacto de redes sociales y tiempo de pantalla en el bienestar emocional de adolescentes.")
    
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




elif modulos == "📂 Carga y perfil del dataset":
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

    # Información general
    st.subheader("Información general")  
          
    # Dimensiones 
    nfilas, ncolumnas = data.shape 
    
    # Métricas
    total_nulos = data.isnull().sum().sum()
    duplicados = data.duplicated().sum()

    # Tipos de variables
    columnas_numericas = data.select_dtypes(include="number").columns.tolist()
    columnas_categoricas = data.select_dtypes(include=["object", "category"]).columns.tolist()
    columnas_fecha = data.select_dtypes(include=["datetime64[ns]"]).columns.tolist()
    
    # Mostrar dimensiones, tipos de variables y métricas en una tabla
    st.write("- Número de registros:", nfilas)
    st.write("- Número de variables:", ncolumnas)
    st.write("- Variables numéricas identificadas:", len(columnas_numericas))
    st.write("- Variables categóricas identificadas:", len(columnas_categoricas))
    st.write("- Total de valores nulos:", total_nulos)
    st.write("- Total de filas duplicadas:", duplicados)
          
    # Mostrar mensaje si no hay variables de tipo numérica o categórica
    st.subheader("Validación de Variables:")
    if len(columnas_numericas) > 0:
        st.write("- Se identificaron variables numéricas.")
    else:
         st.write("- No se identificaron variables numéricas.")
          
    if len(columnas_categoricas) > 0:
        st.write("- Se identificaron variables categóricas.")
    else:
        st.write("- No se identificaron variables categóricas.")
          
    if len(columnas_fecha) > 0:
        st.write("- Se identificaron variables de fecha.")
    else:
        st.write("- No se identificaron variables de fecha.")
    
      
    # Vista previa del archivo 
    st.subheader("Vista previa del dataset")
    st.write("Primeros registros del dataset cargado.")
    st.dataframe(data.head())
    
    # Columnas y tipos de datos
    st.subheader("Columnas y Tipos de Datos")
    info_columnas = pd.DataFrame({
          "Columna": data.columns,
           "Tipo de dato": data.dtypes.astype(str)
    })
    info_columnas = info_columnas.reset_index(drop=True)
    st.dataframe(info_columnas)

   
    # Selección de variables 
    st.subheader("Selección de Variables")
    columnas_seleccionadas = st.multiselect("Seleccione una o más variables para visualizar su resumen estadístico.",
                                            options=data.columns)
    
    # Mostrar estadísticas desccriptivas de las variables seleccionadas
    if columnas_seleccionadas:
        st.write("Resumen estadístico")
        st.dataframe(data[columnas_seleccionadas].describe(include="all"))
    

elif modulos == "⚙️ Procesamiento de datos":

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
    
        columnas_fecha = data.select_dtypes(include=["datetime64[ns]"]).columns.tolist()

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

elif modulos == "📊 Análisis visual":
    
  if st.session_state.data is not None:
    data = st.session_state.data
    # Establecemos los tab
    tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs([
        "Resumen",
         "Análisis univariado",
         "Análisis bivariado",
         "Análisis multivariado",
         "Análisis temporal",
         "Insights"])
      
    # Tab1 Resumen 
    tab1.subheader("Resumen del Dataset")
    
    # Dimensiones
    nfilas, ncolumnas = data.shape
    
    # Tipos de variables
    columnas_numericas = data.select_dtypes(include="number").columns.tolist()
    columnas_categoricas = data.select_dtypes(include=["object", "category"]).columns.tolist()
    
    # Métricas generales
    nulos = data.isnull().sum().sum()
    duplicados = data.duplicated().sum()
    
    # KPIs con columns 
    col1, col2, col3 = tab1.columns(3)
    col1.metric("Filas", nfilas)
    col2.metric("Columnas", ncolumnas)
    col3.metric("Duplicados", duplicados)
      
    col4, col5, col6 = tab1.columns(3)
    col4.metric("Variables numéricas", len(columnas_numericas))
    col5.metric("Variables categóricas", len(columnas_categoricas))
    col6.metric("Valores nulos", nulos)  
    tab1.markdown("---")  

    # Vista del dataset
    tab1.subheader("Vista previa del dataset")
    tab1.dataframe(data.head())
    
    # Estructura del dataset
    tab1.subheader("Estructura del dataset")    
    info = pd.DataFrame({
        "Columna": data.columns,
        "Tipo de dato": data.dtypes.astype(str)
    }).reset_index(drop=True)   
    tab1.dataframe(info)
    
    # Resumen estadístico
    tab1.subheader("Resumen estadístico")   
    tab1.dataframe(data.describe(include="all"))

    # Tab2 Análisis univariado
    tab2.subheader("Comparación entre Variables")
      
    # Separar variables
    columnas_numericas = data.select_dtypes(include="number").columns.tolist()
    columnas_categoricas = data.select_dtypes(include=["object", 
                                                       "category"]).columns.tolist()
    columnas_categoricas_validas = [
    col for col in columnas_categoricas
    if data[col].nunique() <= 15]
    
    # Gráficos para variables numéricas
    if len(columnas_numericas) > 0:
        tab2.subheader("Distribución de variables numéricas")
        variable_num = tab2.selectbox("Seleccione variable numérica", 
                                      columnas_numericas)
        col1, col2 = tab2.columns(2)
    
        # Histograma
        fig1 = px.histogram(data, x=variable_num, title="Histograma de " + variable_num)
        col1.plotly_chart(fig1)
    
        # Boxplot
        fig2 = px.box(data, y=variable_num, title="Boxplot de " + variable_num)
        col2.plotly_chart(fig2)
    
    else:
        tab2.info("No hay variables numéricas en el dataset.")

    # Gráficos para variables categóricas
    if len(columnas_categoricas_validas) > 0:
        tab2.subheader("Distribución de variables categóricas")
        variable_cat = tab2.selectbox("Seleccione variable categórica",columnas_categoricas_validas)
        conteo = data[variable_cat].value_counts().reset_index()
        conteo.columns = [variable_cat, "cantidad"]
        col1, col2 = tab2.columns(2)
    
        # Gráfico de barras
        fig3 = px.bar(conteo, x=variable_cat, y="cantidad", title="Conteo de " + variable_cat)
        col1.plotly_chart(fig3)
    
        # Gráfico de proporciones
        conteo["proporcion"] = conteo["cantidad"] / conteo["cantidad"].sum()
        fig4 = px.pie(conteo, names=variable_cat, values="cantidad", 
                      title="Proporciones de " + variable_cat)
        col2.plotly_chart(fig4)
    
    else:
        tab2.info("No hay variables categóricas en el dataset.")
      
    # Tab3 Análisis bivariado
    tab3.subheader("Correlaciones")

    # Gráfico: Relación entre variables numéricas
    if len(columnas_numericas) >= 2:
        tab3.subheader("Relación entre variables numéricas")
        col1, col2 = tab3.columns(2)
    
        variable_x = col1.selectbox("Variable X", columnas_numericas, key="x_scatter")
        variable_y = col2.selectbox("Variable Y", columnas_numericas, key="y_scatter")
    
        fig4 = px.scatter(data, x=variable_x, y=variable_y, 
                          title="Relación entre " + variable_x + " y " + variable_y)
        tab3.plotly_chart(fig4)

    else:
        tab3.info("No hay suficientes variables numéricas para scatter plot.") 
        
    # Gráfico: Boxplot por categoría (numérica vs categórica)
    if len(columnas_categoricas_validas) > 0 and len(columnas_numericas) > 0:
        tab3.subheader("Distribución por categoría")
        col1, col2 = tab3.columns(2)
    
        variable_cat = col1.selectbox("Variable categórica", columnas_categoricas_validas,
                                      key="cat_box")
        variable_num = col2.selectbox("Variable numérica", columnas_numericas, 
                                      key="num_box")
    
        fig5 = px.box(data, x=variable_cat, y=variable_num, 
                      title="Distribución de " + variable_num + " por " + variable_cat)
        tab3.plotly_chart(fig5)
    
    else:
        tab3.info("No hay variables suficientes para boxplot por categoría.")

    # Gráfico: Comparación categórica con barras agrupadas
    if len(columnas_categoricas_validas) >= 2:
        tab3.subheader("Comparación entre variables categóricas")
        col1, col2 = tab3.columns(2)
        cat1 = col1.selectbox("Variable categórica 1", columnas_categoricas_validas, key="cat1_bar")
        opciones_cat2 = [c for c in columnas_categoricas_validas if c != cat1]
        cat2 = col2.selectbox("Variable categórica 2", opciones_cat2, key="cat2_bar")
        df_temp = data[[cat1, cat2]].dropna()
    
        tabla = (df_temp.groupby([cat1, cat2]).size().reset_index(name="cantidad"))
    
        fig6 = px.bar(tabla, x=cat1, y="cantidad", color=cat2, barmode="group", 
                      title="Relación entre " + cat1 + " y " + cat2)
        tab3.plotly_chart(fig6)
    
    else:
        tab3.info("No hay suficientes variables categóricas para comparación.")

    # Gráfico: Barras apiladas para combinación de variables categóricas
    if len(columnas_categoricas_validas) >= 2:
        tab3.subheader("Barras apiladas")
        col1, col2 = tab3.columns(2)
    
        cat1 = col1.selectbox("Categoría base", columnas_categoricas_validas, key="stack_cat1")
        opciones_cat2 = [c for c in columnas_categoricas_validas if c != cat1]
        cat2 = col2.selectbox("Segmentación", opciones_cat2, key="stack_cat2")
        tabla = (data[[cat1, cat2]].dropna().groupby([cat1, cat2]).size().reset_index(name="cantidad"))
    
        fig8 = px.bar(tabla, x=cat1, y="cantidad", color=cat2, barmode="stack",
                      title="Barras apiladas: " + cat1 + " vs " + cat2)
        tab3.plotly_chart(fig8)
    
    else:
        tab3.info("No hay suficientes variables categóricas.") 

    # Gráfico: Barras agregadas por una métrica a elección
    tab3.subheader("Métrica agregada por categoría")
    
    if len(columnas_categoricas_validas) > 0 and len(columnas_numericas) > 0:
        col1, col2, col3 = tab3.columns(3)
        variable_cat = col1.selectbox("Variable categórica",columnas_categoricas_validas,
                                      key="bar_cat")
        variable_num = col2.selectbox("Variable numérica",columnas_numericas,key="bar_num")
    
        operacion = col3.selectbox("Agregación",["Suma", "Promedio"])
    
        if operacion == "Suma":
            tabla = (data.groupby(variable_cat)[variable_num].sum().reset_index())
    
        else:
            tabla = (data.groupby(variable_cat)[variable_num].mean().reset_index())
    
        tabla = tabla.sort_values(variable_num,ascending=False)
    
        fig21 = px.bar(tabla,x=variable_cat,y=variable_num,
            title=f"{operacion} de {variable_num} por {variable_cat}")
        tab3.plotly_chart(fig21)
    
    else:
        tab3.info("Se requiere al menos una variable categórica y una numérica.")


    # Gráfico: Ranking Top N
    tab3.subheader("Ranking Top N")
    if len(columnas_categoricas_validas) > 0 and len(columnas_numericas) > 0:
        col1, col2, col3, col4 = tab3.columns(4)
        variable_cat = col1.selectbox("Variable categórica",columnas_categoricas_validas,
                                      key="top_cat")
        variable_num = col2.selectbox("Variable numérica",columnas_numericas,key="top_num")
        operacion = col3.selectbox("Agregación",["Suma", "Promedio"],key="top_agregacion")

        top_n = col4.selectbox("Top",[5, 10, 15, 20],index=1)
    
        if operacion == "Suma": 
            tabla_top = (data.groupby(variable_cat)[variable_num].sum().reset_index())
    
        else:
            tabla_top = (data.groupby(variable_cat)[variable_num].mean().reset_index())
    
        tabla_top = tabla_top.sort_values(variable_num, ascending=False).head(top_n)
        fig22 = px.bar(tabla_top,x=variable_cat,y=variable_num,
                         title=f"Top {top_n} de {variable_cat}")    
        tab3.plotly_chart(fig22)
    
    else:
        tab3.info("Se requiere al menos una variable categórica y una numérica.")

      

    # Tab4 Análisis multivariado
    tab4.subheader("Análisis Multivariado")

    # Gráfico : Correlacion con heatmap 
    if len(columnas_numericas) >= 2:
        tab4.subheader("Correlación entre variables numéricas")
        corr = data[columnas_numericas].corr()
        fig9, ax = plt.subplots()
        sns.heatmap(corr, annot=False, cmap="coolwarm", ax=ax)
        tab4.pyplot(fig9)
    
    else:
        tab4.info("No hay suficientes variables numéricas para correlación.")

    # Gráfico : Scatter multivariado (2 numéricas y 1 categorica)
    if len(columnas_numericas) >= 2 and len(columnas_categoricas_validas) >= 1:
        tab4.subheader("Relación multivariada")
        col1, col2, col3 = tab4.columns(3)
        var_x = col1.selectbox("Variable X", columnas_numericas, key="mv_x")
        var_y = col2.selectbox("Variable Y", columnas_numericas, key="mv_y")
        var_cat = col3.selectbox("Color (categoría)", columnas_categoricas_validas, key="mv_cat")
        fig10 = px.scatter(data, x=var_x, y=var_y, color=var_cat, 
                           title="Relación entre " + var_x + ", " + var_y + " y " + var_cat)
        tab4.plotly_chart(fig10)
    
    else:
        tab4.info("No hay suficientes variables para scatter multivariado.")

    # Gráfico : Segmentación múltiple (1 numerica y 2 categoricas)
    if len(columnas_numericas) >= 1 and len(columnas_categoricas_validas) >= 2:
    
        tab4.subheader("Segmentación multivariada")
    
        col1, col2, col3 = tab4.columns(3)
    
        var_cat1 = col1.selectbox("Categoría 1", columnas_categoricas_validas, key="seg1")
        opciones_cat2 = [c for c in columnas_categoricas_validas if c != var_cat1]
    
        var_cat2 = col2.selectbox("Categoría 2", opciones_cat2, key="seg2")
    
        var_num = col3.selectbox("Variable numérica", columnas_numericas, key="seg_num")
    
        df_temp = data[[var_cat1, var_cat2, var_num]].dropna()
    
        tabla = df_temp.groupby([var_cat1, var_cat2])[var_num].mean().reset_index()
    
        fig11 = px.bar(tabla, x=var_cat1, y=var_num, color=var_cat2, barmode="group",
                       title="Segmentación multivariada de " + var_num)
        tab4.plotly_chart(fig11)
    
    else:
        tab4.info("No hay suficientes variables para segmentación.")

    # Gráfico :  Heatmap de interacción categórica 
    if len(columnas_categoricas_validas) >= 2:
        tab4.subheader("Mapa de interacción categórica")
        cat1 = columnas_categoricas_validas[0]
        cat2 = columnas_categoricas_validas[1]
        tabla = pd.crosstab(data[cat1], data[cat2])
        fig12, ax = plt.subplots()
        sns.heatmap(tabla, cmap="Blues", ax=ax)
        tab4.pyplot(fig12)

    # Scatter multivariado (3 numéricas y 1 categórica)
    if len(columnas_numericas) >= 3 and len(columnas_categoricas_validas) >= 1:
        tab4.subheader("Análisis de Cuatro Variables")  
        col1, col2, col3, col4 = tab4.columns(4)
        
        var_x = col1.selectbox("Variable X", columnas_numericas, key="mv4_x")
        opciones_y = [c for c in columnas_numericas if c != var_x]
        var_y = col2.selectbox("Variable Y", opciones_y, key="mv4_y")
        opciones_size = [c for c in columnas_numericas if c not in [var_x, var_y]]
        var_size = col3.selectbox("Tamaño", opciones_size, key="mv4_size")
        var_cat = col4.selectbox("Color", columnas_categoricas_validas, key="mv4_cat")
        
        fig23 = px.scatter(data,x=var_x,y=var_y,size=var_size,color=var_cat,
                           title=f"{var_x} vs {var_y} segmentado por {var_cat} y tamaño según {var_size}")
        tab4.plotly_chart(fig23)
    
    else:
        tab4.info("Se requieren al menos tres variables numéricas y una categórica.")
    

    # Tab5 Análisis temporal
    tab5.subheader("Análisis Temporal")

    # Convertir las columnas a fecha si lo son 
    for columna in data.columns:
        if "date" in columna:
            data[columna] = pd.to_datetime(data[columna])

    columnas_fecha = data.select_dtypes(include=["datetime64[ns]"]).columns.tolist()
    columnas_numericas = data.select_dtypes(include="number").columns.tolist()
    columnas_categoricas = data.select_dtypes(include=["object", "category"]).columns.tolist()
    
    if len(columnas_fecha) == 0:
        tab5.info("El dataset no contiene variables de fecha.")
    else:
        # Selección de variable fecha
        variable_fecha = tab5.selectbox("Seleccione variable de fecha", columnas_fecha)
        df_temp = data
        df_temp[variable_fecha] = pd.to_datetime(df_temp[variable_fecha], errors="coerce")
        df_temp = df_temp.dropna(subset=[variable_fecha])

        # Crear componentes temporales
        df_temp["anio"] = df_temp[variable_fecha].dt.year
        df_temp["mes"] = df_temp[variable_fecha].dt.month
    
        # Filtros de año y mes
        col1, col2 = tab5.columns(2)  
        anios = sorted(df_temp["anio"].dropna().unique().tolist())
        meses = list(range(1, 13))
        anios_sel = col1.multiselect("Año(s)", anios, default=anios)
        meses_sel = col2.multiselect("Mes(es)", meses, default=meses)
    
        df_temp = df_temp[
            (df_temp["anio"].isin(anios_sel)) &
            (df_temp["mes"].isin(meses_sel))
        ]

        # Selección de métrica
        if len(columnas_numericas) > 0:
            variable_num = tab5.selectbox("Variable numérica (métrica)",columnas_numericas)
    
            #  Agregación temporal
            df_temp["periodo"] = df_temp[variable_fecha].dt.to_period("M").astype(str)
            tabla = df_temp.groupby("periodo")[variable_num].mean().reset_index()
    
            # Gráfico de tendencia
            fig16 = px.line(tabla, x="periodo", y=variable_num, markers=True,
                          title="Evolución de " + variable_num + " en el tiempo")
            tab5.plotly_chart(fig16)
    
        else:
            # Si no hay numéricas 
            df_temp["periodo"] = df_temp[variable_fecha].dt.to_period("M").astype(str)
            tabla = df_temp.groupby("periodo").size().reset_index(name="cantidad")
            fig17 = px.line(tabla, x="periodo", y="cantidad", markers=True,
                            title="Evolución de registros en el tiempo")
            tab5.plotly_chart(fig17)
    
        # Segmentación categórica 
        if len(columnas_categoricas_validas) > 0:
            tab5.subheader("Segmentación por categoría")
        
            # Selección de variable categórica
            variable_cat = tab5.selectbox("Variable categórica", columnas_categoricas_validas)
        
            # Copia del dataset ya filtrado por fecha,mes y año
            df_seg = data
        
            # Crear componentes temporales 
            df_seg["anio"] = df_seg[variable_fecha].dt.year
            df_seg["mes"] = df_seg[variable_fecha].dt.month
        
            # Filtros de año y mes 
            col1, col2 = tab5.columns(2)
            anios2 = sorted(df_seg["anio"].dropna().unique().tolist())
            meses2 = list(range(1, 13))
            anios_sel2 = col1.multiselect("Año(s)", anios2, default=anios2, key="seg_anios")
            meses_sel2 = col2.multiselect("Mes(es)", meses2, default=meses2, key="seg_meses")
        
            df_seg = df_seg[(df_seg["anio"].isin(anios_sel2)) & (df_seg["mes"].isin(meses_sel2))]

            # Agregación
            df_seg["periodo"] = df_seg[variable_fecha].dt.to_period("M").astype(str)
            tabla_seg = df_seg.groupby(["periodo", variable_cat]).size().reset_index(name="cantidad")

            fig20 = px.line(tabla_seg, x="periodo",y="cantidad",color=variable_cat, markers=True,
                            title="Evolución segmentada por " + variable_cat)
        
            tab5.plotly_chart(fig20)
          
    # Tab6 Insights
    tab6.subheader("Insights y Recomendaciones")
    total_nulos = data.isnull().sum().sum()
    duplicados = data.duplicated().sum()

    # Hallazgos Clave
    tab6.markdown("### Hallazgos Clave")
    nfilas, ncolumnas = data.shape
    tab6.write(f"• El dataset contiene {nfilas} registros y {ncolumnas} variables.")

    if total_nulos > 0:
        variable_nulos = data.isnull().sum().idxmax()
        cantidad_nulos = data.isnull().sum().max()
        tab6.write(f"• La variable '{variable_nulos}' presenta la mayor cantidad de valores faltantes ({cantidad_nulos}).")

    if len(columnas_categoricas) > 0:
        variable_cat = columnas_categoricas[0]
        categoria_top = data[variable_cat].value_counts().idxmax()
        frecuencia = data[variable_cat].value_counts().max()
        tab6.write(f"• En la variable '{variable_cat}', la categoría predominante es '{categoria_top}' con {frecuencia} registros.")

    if len(columnas_numericas) > 0:
        dispersion = data[columnas_numericas].std()
        variable_dispersion = dispersion.idxmax()
        tab6.write(f"• La variable '{variable_dispersion}' presenta la mayor variabilidad dentro del dataset.")

    if len(columnas_numericas) >= 2:
        corr = data[columnas_numericas].corr().abs()
        corr = corr.where(~np.eye(corr.shape[0], dtype=bool))
        max_corr = corr.stack().idxmax()
        valor_corr = corr.stack().max()
        tab6.write(f"• La relación más fuerte se observa entre '{max_corr[0]}' y '{max_corr[1]}' (r = {valor_corr:.2f}).")

    # Interpretación
    tab6.markdown("### Interpretación de Resultados")

    if len(columnas_numericas) > 0:
        tab6.info("Las variables numéricas presentan diferentes niveles de dispersión, lo que sugiere la existencia de comportamientos heterogéneos dentro del conjunto de datos.")
    
    if len(columnas_categoricas) > 0:
        tab6.info("La distribución de categorías permite identificar segmentos predominantes que podrían requerir análisis específicos.")
    
    if len(columnas_numericas) >= 2:
        tab6.info("Las relaciones detectadas entre variables pueden contribuir a explicar patrones relevantes para el análisis del negocio.")

    # Recomendaciones para la toma de decisiones
    tab6.markdown("### Recomendaciones")

    if total_nulos > 0:
        tab6.write("• Revisar y tratar los valores faltantes antes de desarrollar análisis predictivos o modelos estadísticos.")
    
    if duplicados > 0:
        tab6.write("• Validar los registros duplicados para evitar sesgos en los resultados.")
    
    if len(columnas_categoricas) > 0:
        tab6.write("• Analizar con mayor detalle las categorías con mayor participación para identificar oportunidades o riesgos.")
    
    if len(columnas_numericas) >= 2:
        tab6.write("• Profundizar el estudio de las variables con mayor correlación para comprender posibles factores asociados.")
    
    tab6.write("• Complementar este análisis exploratorio con técnicas estadísticas o predictivas según los objetivos del negocio.")
    


  else:
    st.warning("Primero debe cargar un dataset.")
          
