import streamlit as st
import pandas as pd
import numpy as np

juegos = pd.read_csv('datos/games.csv')

st.title('Analisis de Datos Sobre la Industria de los Videojuegos')

st.header('EDA: Analisis exploratorio inicial')

st.subheader('Estructura de los datos')

estructura = juegos.dtypes.reset_index()
estructura.columns = ['Columna', 'Tipo de Dato']
st.write(estructura)

st.dataframe(data = juegos)

st.header('Valores Duplicados')

total_repetidos = juegos.duplicated().sum()
st.write(f'El total de filas repetidas es: {total_repetidos}')

st.header('Valores Ausentes')

valores_ausentes = juegos.isna().sum().sort_values(ascending=False).reset_index()
valores_ausentes.columns = ['Columna', 'Total filas ausentes']

st.dataframe(data = valores_ausentes)

st.subheader('Imputacion de valores faltantes')

juegos['Rating'].fillna('Desconocido', inplace=True)
juegos['Year_of_Release'].fillna(0, inplace=True)

#Interpolacion: Rellenar valores faltantes con ML

juegos['Critic_Score'].interpolate(method='polynomial', order=3, inplace=True)

juegos.loc[juegos['User_Score'] == 'tbd', 'User_Score'] = np.nan

juegos['User_Score'] = juegos['User_Score'].astype('float')

juegos['User_Score'].interpolate(method='polynomial', order=3, inplace=True)

juegos.dropna(inplace=True)

valores_ausentes_despues = juegos.isna().sum().sort_values(ascending=False).reset_index()

st.dataframe(valores_ausentes_despues)

boton_eu = st.button('Ventas EU')
boton_na = st.button('Ventas NA')

if boton_eu:
    ventas = juegos.query('Year_of_Release > 0').groupby('Year_of_Release').agg({'EU_sales': 'sum'})
    st.line_chart(ventas)

if boton_na:
    ventas = juegos.query('Year_of_Release > 0').groupby('Year_of_Release').agg({'NA_sales': 'sum'})
    st.line_chart(ventas)