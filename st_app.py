import streamlit as st
import folium
import pandas as pd

from  streamlit_folium import folium_static
from views.components.hero import hero
from controller.company import get_data_for_table
from controller.company import get_data_for_map
from conection import MySQL

connection = MySQL(st)
data = connection.get_all_data()

#Hero
hero(st)

df_nan = data['response']
# Table
df_data_pd = pd.DataFrame(get_data_for_table(df_nan),columns=(['Empresa','Telefono1','Telefono2','Ciudad']))
st.table(df_data_pd)

# Map
df_data_pd_map = pd.DataFrame(get_data_for_map(df_nan),columns=(['Empresa','Latitud','Longitud']))
df = df_data_pd_map.dropna(axis = 0).reset_index(drop = True)

## center on Piura
m = folium.Map(location=[-5.19449, -80.63282], zoom_start=12)

## add marker for Piura
count = 0
for i in range(0,df.shape[0],1):
  folium.Marker(
      [df['Latitud'][count], df['Longitud'][count]], popup=df['Empresa'][count], tooltip=df['Empresa'][count]
  ).add_to(m)
  count += 1

st.subheader('**Mapa con los puntos de venta**')
# call to render Folium map in Streamlit
folium_static(m)

opciones = ['Amazonas', 'Ancash', 'Apurimac', 'Arequipa', 'Ayacucho', 'Cajamarca', 'Cusco', 'Huancavelica',
           'Huánuco', 'Ica', 'Junín', 'La Libertad', 'Lambayeque', 'Lima', 'Loreto', 'Madre de Dios', 'Moquegua', 
           'Pasco', 'Piura', 'Puno', 'San Martín', 'Tacna', 'Tumbes', 'Ucayali']

st.header('**Formulario**')
nombre = st.text_input('Nombre de la empresa o contacto')
telefono1 = st.number_input('Teléfono 1', format="%.0f")
telefono2 = st.number_input('Teléfono 2', format="%.0f")
departamento = st.selectbox('Departamento', opciones)
ciudad = st.text_input('Nombre del distrito o ciudad')
direccion = st.text_input('Dirección de la empresa, puede adjuntar el enlace de Google Maps')
precio = st.number_input('Llene este apartado si posee información del precio del óxigeno', format="%.2f")

if st.button('Enviar'):
  st.write('Gracias por compartir :)')
  list = [nombre, telefono1, telefono2, departamento, ciudad, direccion, precio]
  st.write(list)
