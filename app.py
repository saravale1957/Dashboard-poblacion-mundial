import pandas as pd
import streamlit as st
import numpy as np

st.set_page_config(page_title="Poblacion Mundial", layout="wide")
st.title("Análisis de la poblacion mundial")
st.write("Aquí tenemos los 10 paises mas poblados del mundo")

archivo = st.file_uploader("Selecciona el archivo csv", type="csv")

if archivo:
     datos = pd.read_csv(archivo)

     top10 = datos.sort_values(
     "2022 Population",
     ascending = False
    ).head(10)

     paises = top10["Country/Territory"].to_numpy()

     poblacion_2015 = top10["2015 Population"].to_numpy()
     poblacion_2020 = top10["2020 Population"].to_numpy()
     poblacion_2022 = top10["2022 Population"].to_numpy()

     total = np.sum(poblacion_2022)
     promedio = np.mean(poblacion_2022)
     mediana = np.median(poblacion_2022)
     minimo = np.min(poblacion_2022)
     maximo = np.max(poblacion_2022)

     st.subheader("Estadisticas de la poblacion de 2022")
     col1,col2,col3,col4,col5 = st.columns(5)

     col1.metric("Poblacion total",f"{total/1000000:,.2f}millones")
     col2.metric("Promedio de la poblacion",f"{promedio/1000000:,.2f}millones")
     col3.metric("Mediana de la poblacion",f"{mediana/1000000:,.2f}millones")
     col4.metric("Poblacion minima",f"{minimo/1000000:,.2f}millones")
     col5.metric("Poblacion maxima",f"{maximo/1000000:,.2f}millones")
     st.subheader("Comparacion de la poblacion por pais")


     grafico = top10.set_index("Country/Territory")[[
     "2015 Population",
     "2020 Population",
     "2022 Population"

]]/1000000

     st.bar_chart(grafico)

     st.subheader("Datos de los 10 paises")

     st.dataframe(top10[[
        "Country/Territory",
        "2015 Population",
        "2020 Population",
        "2022 Population"
    ]])


else:
     st.info("Primero debes cargar el dataset")