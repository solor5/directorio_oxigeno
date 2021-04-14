import streamlit as st

from conection import MySQL


class ControllerCompany(object):
        def __init__(self):
                self.connection = MySQL(st)
                self.data = self.connection.get_all_data()
                if self.data['state']:
                        self.df_nan = self.data['response']
                else:
                        st.error('Error al traer los datos, recarge la páguina')

        def get_data_for_table(self):
                data_necesari = []
                for fila in self.df_nan:
                        data_necesari.append([fila[0],fila[1],fila[2],fila[3],fila[4],fila[5]])
                return data_necesari

        def get_data_for_map(self):
                data_necesari = []
                for fila in self.df_nan:
                        data_necesari.append([fila[0],fila[6],fila[7]])
                return data_necesari

        def add_company(self,company_name, celphone1, celphone2, address, price,aparment_id, city):
                try:
                        self.connection.add_data(company_name, celphone1, celphone2, address, price,aparment_id, city)
                except:
                        st.error('Error al guardar data, Intente nuevamente')
                        return False
                return True