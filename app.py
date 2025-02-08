import streamlit as st
import pandas as pd
import plotly.express as px

# Título de la aplicación
st.title("Análisis de Vehículos en EE.UU.")
st.header("Exploración de Precios de Vehículos")

# Leer el archivo CSV
df = pd.read_csv('vehicles_us.csv')

# Mostrar los primeros datos
st.write("Vista previa de los datos:", df.head())

# Casilla de verificación para el histograma
if st.checkbox('Mostrar Histograma de Precios'):
    fig = px.histogram(df, x='price', nbins=50, title='Distribución de Precios de Vehículos')
    st.plotly_chart(fig)

# Casilla de verificación para el gráfico de dispersión
if st.checkbox('Mostrar Dispersión Año vs Precio'):
    fig2 = px.scatter(df, x='model_year', y='price', color='condition',
                      title='Precio vs Año del Modelo por Condición')
    st.plotly_chart(fig2)