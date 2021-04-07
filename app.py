import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd

st.image('https://github.com/solor5/directorio_oxigeno/raw/main/img_ox.png', use_column_width=True)
st.title('Directorio de puntos de venta de oxígeno medicinal ')
st.write('Esta es una iniciativa sin fines de lucro que busca crear un directorio nacional de puntos de venta de oxígeno. Si deseas agregar una empresa o brindar más detalle de los contactos ya existentes, por favor, haz clic [aquí](https://docs.google.com/forms/d/e/1FAIpQLSeE5uEuDBDtwQIhLZPNuSC5KinHWn5Bx3tU9xbu-DzRZxD6jQ/viewform)')
st.write('Creado por [William Solórzano](https://www.linkedin.com/in/william-solórzano/)')
st.header('Piura')

df_nan = pd.read_excel('https://github.com/solor5/directorio_oxigeno/raw/a58a41722d2ed4494db1871b4f6f777fadae7f92/Excel.xlsx')
st.table(df_nan[['Empresa','Teléfonos']])

df = df_nan.dropna(axis = 0).reset_index(drop = True)

# center on Piura
m = folium.Map(location=[-5.19449, -80.63282], zoom_start=12)

# add marker for Piura
count = 0 
for i in range(0,df.shape[0],1):
  folium.Marker(
      [df['Latitud'][count], df['Longitud'][count]], popup=df['Empresa'][count], tooltip=df['Empresa'][count]
  ).add_to(m)
  count += 1

# call to render Folium map in Streamlit
folium_static(m)
