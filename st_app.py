import streamlit as st
import folium
import pandas as pd

from  streamlit_folium import folium_static
from views.components.hero import hero
from controller.company import ControllerCompany

controller = ControllerCompany()
#Hero


# Table
df_data_pd = pd.DataFrame(controller.get_data_for_table(),columns=(['Empresa','Telefono1','Telefono2','Departamento','Ciudad','Precio']))
st.table(df_data_pd)

# Map
df_data_pd_map = pd.DataFrame(controller.get_data_for_map(),columns=(['Empresa','Latitud','Longitud']))
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

aparment_id = {'Amazonas':4, 'Ancash':14, 'Apurimac':24, 'Arequipa':34, 'Ayacucho':44, 'Cajamarca':54, 'Cusco':64, 'Huancavelica':74,
           'Huánuco':84, 'Ica':94, 'Junín':104, 'La Libertad':114, 'Lambayeque':124, 'Lima':134, 'Loreto':144, 'Madre de Dios':154,
            'Moquegua':164,'Pasco':174, 'Piura':184, 'Puno':194, 'San Martín':204, 'Tacna':214, 'Tumbes':224, 'Ucayali':234}
st.header('**Formulario**')
company_name = st.text_input('Nombre de la empresa o contacto')
celphone1 = st.text_input('Teléfono 1')
celphone2 = st.text_input('Teléfono 2')
aparment = st.selectbox('Departamento', opciones)
city = st.text_input('Ciudad')
address = st.text_input('Dirección de la empresa, puede adjuntar el enlace de Google Maps')
price = st.number_input('Llene este apartado si posee información del precio del óxigeno', format="%.2f")

if st.button('Enviar'):
  response = controller.add_company(company_name, celphone1, celphone2, address, price,aparment_id[aparment],city )
  if response :
      st.success("Gracias por compartir :). Se guardo la data exitosamente")
