import streamlit as st
import pandas as pd

juegos = pd.read_csv('datos/games.csv')

st.title('Analisis de Datos Sobre la Industria de los Videojuegos')

st.header('EDA: Analisis exploratorio inicial')

st.dataframe(data = juegos)


