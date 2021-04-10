
def get_data_for_table(data):
    data_necesari = []
    for fila in data:
            data_necesari.append([fila[0],fila[1],fila[2],fila[3]])
    return data_necesari

def get_data_for_map(data):
    data_necesari = []
    for fila in data:
            data_necesari.append([fila[0],fila[4],fila[5]])
    return data_necesari