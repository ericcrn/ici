def abrir_fichero(archivo):
    try:
        # Abre el archivo en modo lectura, en una lista separada por líneas
        f = open(archivo, 'r', encoding='UTF-8')
        guias = f.readlines()
        f.close()
        
        return guias

    except FileNotFoundError:
        print("El archivo no existe")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        
def limpiar_guias(guias):
    # Limpia las guías de saltos de línea y comas
    guias_limpio = []
    for guia in guias:
        guia_temp = guia.strip("\n")
        # Agrega la guía a la lista de guías_limpio separada por comas en una lista
        guias_limpio.append(list(guia_temp.split(",")))
        
    return guias_limpio

def buscar(guias):
    julio_2022 = []
    julio_2023 = []
    for linea in guias:
        fecha = linea[2]
        if fecha[:7] == "2022-07":
            julio_2022.append(linea)
        elif fecha[:7] == "2023-07":
            julio_2023.append(linea)
        
    return julio_2022, julio_2023

def mostrar(extracción):
    print("Julio 2022: {} \n".format(extracción[0]))
    print("Julio 2023: {} \n".format(extracción[1]))
    print("Total de guías: {}\nTotal de guías 2023-07: {}\nTotal de guías 2023-07: {}".format(len(extracción[0]) + len(extracción[1]), len(extracción[0]), len(extracción[1])))

if __name__ == "__main__":
    guias = abrir_fichero("unidad-2/guias.dat")
    guias = limpiar_guias(guias)
    extracion = buscar(guias)
    mostrar(extracion)