import streamlit as st
from streamlit_folium import folium_static
import folium
import pandas as pd

st.image('https://github.com/solor5/directorio_oxigeno/raw/main/img_ox.png', use_column_width=True)
st.title('Directorio de puntos de venta de oxígeno medicinal ')
st.write('Esta es una iniciativa sin fines de lucro que busca crear un directorio nacional de puntos de venta de oxígeno. Si deseas agregar una empresa o brindar más detalle de los contactos ya existentes, por favor, haz clic [aquí](https://docs.google.com/forms/d/e/1FAIpQLSeE5uEuDBDtwQIhLZPNuSC5KinHWn5Bx3tU9xbu-DzRZxD6jQ/viewform)')
st.write('Por el momento, solo se cuenta con información de la ciudad de Piura, cada 24 horas se actualizará con la información proporcionada de otras regiones del Perú.')
st.write('Creado por [William Solórzano](https://www.linkedin.com/in/william-solórzano/)')
st.header('**Piura**')

df_nan = pd.read_csv('https://raw.githubusercontent.com/solor5/directorio_oxigeno/main/data.csv')
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

st.subheader('**Mapa con los puntos de venta**')
# call to render Folium map in Streamlit
folium_static(m)

opciones = ['Amazonas', 'Ancash', 'Apurimac', 'Arequipa', 'Ayacucho', 'Cajamarca', 'Cusco', 'Huancavelica',
           'Huánuco', 'Ica', 'Junín', 'La Libertad', 'Lambayeque', 'Lima', 'Loreto', 'Madre de Dios', 'Moquegua', 
           'Pasco', 'Piura', 'Puno', 'San Martín', 'Tacna', 'Tumbes', 'Ucayali']

st.header('**Formulario**')
nombre = st.text_input('Nombre de la empresa o contacto')
telefono1 = st.number_input('Teléfono 1', format="{:,.0f}")
telefono2 = st.number_input('Teléfono 2', format="{:,.0f}")
departamento = st.selectbox('Departamento', opciones)
ciudad = st.text_input('Nombre del distrito o ciudad')
direccion = st.text_input('Dirección de la empresa, puede adjuntar el enlace de Google Maps')
precio = st.number_input('Llene este apartado si posee información del precio del óxigeno', format="{:,.2f}",)

list = [nombre, telefono1, telefono2, departamento, ciudad, direccion, precio]
st.write(list)

