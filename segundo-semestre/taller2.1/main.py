import os

def leer_archivo(archivo):
    DIR = os.path.dirname(os.path.realpath(__file__)) + "/"
    datos = []
    f = open(DIR + archivo, "r", encoding= "UTF-8")
    
    for linea in f:
        datos.append(linea.rstrip("\n"))
    f.close()
    
    return datos

def limpiar_archivo(archivo):
    datos_temp = []
    datos = []
    
    for linea in archivo:
        if linea != "":
            if "Récord" not in linea:
                if "Record" not in linea:
                    if "Mejores marcas de 2024" not in linea:
                        datos_temp.append(linea)
    
    for linea in datos_temp:
        linea = linea.split("-")
        datos.append(linea)
    
    return datos

def records(archivo):
    i = 0
    record_olimpico = None
    record_mundial = None
    datos = []
    
    for lista in archivo:
        if i == 0:
            record_mundial = lista
        if i == 1:
            record_olimpico = lista
        i += 1
    
    for linea in archivo:
        if linea != record_mundial:
            if linea != record_olimpico:
                datos.append(linea)
    
    return record_mundial, record_olimpico, datos

def exportar_lista(archivo):
    lista_datos = []
    
    record_mundial, record_olimpico, datos = records(archivo)
    
    for listas in datos:
        for lista in listas:
            i = 0
            
            in_pais = False
            
            
            for char in lista[0]:
                if char == "(":
                    nombre = lista[0][:i-1]
                    i_temp = i
                    in_pais = True
                if in_pais:
                    if char == ")":
                        pais = lista[0]
                        pais = pais[i_temp+1:i]
                        in_pais = False
                i += 1
                
            tiempo = float(lista[1])
            lista_datos.append([2024, nombre, pais, tiempo])

    return record_mundial, record_olimpico, lista_datos

def primero_segundo(lista):
    list_primero_segundo = [[None, None, None, 0], [None, None, None, 0]]
    
    for item in lista:
        if item[3] > list_primero_segundo[0][3]:
            list_primero_segundo[1] = list_primero_segundo[0]
            list_primero_segundo[0] = item
        elif item[3] > list_primero_segundo[1][3]:
            list_primero_segundo[1] = item
    
    return list_primero_segundo

def media(lista):
    suma = 0
    
    for item in lista:
        suma += item[3]
    
    return suma / len(lista)

def clear_record(record):
    i = 0
    checker = False
    
    for char in record[0]:
        if char == "(":
            i_nombre = i
            nombre = record[0][:i_nombre-1]
        if char.isnumeric() and checker == False:
            checker = True
            i_pais = i
            pais = record[0][i_nombre+1:i_pais-1]
        if char.isnumeric() and checker == True:
            ano = record[0][i_pais:i+1]
        tiempo = float(record[1])
        
        i += 1
    list = [ano, nombre, pais, tiempo]
                
    return list


def salida(record_mundial, record_olimpico, titulo, lista_datos):
    columns = os.get_terminal_size().columns
    linea = '-' * columns
    list_primero_segundo = primero_segundo(lista_datos)
    i = 2
    
    print(f"{titulo} \n")
    print(f"{"Año":<6} {"id":<6} {"Atleta":<32} {"Pais":<24} {"Tiempo":<12}")
    
    print(linea)
    
    wr = clear_record(record_mundial)
    print(f"{wr[0]:<6} {"wr":<6} {wr[1]:<32} {wr[2]:<24} {wr[3]:<12}")
    wo = clear_record(record_olimpico)
    print(f"{wo[0]:<6} {"wo":<6} {wo[1]:<32} {wo[2]:<24} {wo[3]:<12}")
    
    for item in list_primero_segundo:
        print(f"{item[0]:<6} {i:<6} {item[1]:<32} {item[2]:<24} {item[3]:<12}")
        i -= 1
    print(f"{"-":<6} {"-":<6} {"Dif. Media de tiempo:":<32} {"-":<24} {media(lista_datos):<12}")
    
    print(linea)


if __name__ == "__main__":
    wr100 = limpiar_archivo(leer_archivo("wr100.txt"))
    record_mundial, record_olimpico, lista_datos = exportar_lista(records(wr100))
    salida(record_mundial, record_olimpico, "Marcas 100M planos:", lista_datos)
    
    wr200 = limpiar_archivo(leer_archivo("wr200.txt"))
    record_mundial1, record_olimpico1, lista_datos1 = exportar_lista(records(wr200))
    salida(record_mundial1, record_olimpico1, "Marcas 200M planos:", lista_datos1)