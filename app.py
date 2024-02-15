import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
from sklearn.linear_model import LinearRegression
import streamlit as st

st.title('Menú cíclico')

st.header('Autor: Gabriel Barragán')

data = pd.DataFrame({
  'Presion atmosferica': [993,994,997,1003,1004,1000,994,942,1006,942,986,983,940,966,982],
  'Velocidad viento': [50,60,45,45,40,55,55,105,40,120,50,70,120,100,55]
})
data.description = '''Hurricanes: The data represent the atmospheric
pressure p (in millibars) and the wind speed w (in knots)
measured during various tropical systems in the Atlantic
Ocean'''

option = st.radio('Seleccione una opción: ', ['Visualización','Resumen','Descripción'])

if option == 'Visualización':
  plt.scatter(data['Presion atmosferica'], data['Velocidad viento'])
  plt.xlabel='Presión atmosférica'
  st.pyplot(plt)
elif option == 'Resumen':
  st.write(data.describe())
elif option == 'Descripción':
  st.write(data.description)

