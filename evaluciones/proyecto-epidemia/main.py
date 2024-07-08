# Autor(es): Eric Cerna Lizama - Pablo Cofré González
# Introducción a la Computación - INF113 - secc:S1
import matplotlib.pyplot as plt

def lectura_datos (archivo):
    # Función que lee los datos de un archivo de texto y los almacena en una lista
    datos = []
    f = open("./" + archivo, "r")
    # Recorre las lineas del archivo y las almacena en la lista
    for linea in f:
        linea = datos.append(linea.rstrip("\n").split(","))
    return datos

def lista_regiones(datos):
    # Función que crea una lista de regiones
    regiones = []
    for dato in datos:
        if [dato[3],0] not in regiones:
            regiones.append([dato[3], 0]) # Formato: [[region, 0], [region, 0], ...]
    return regiones

def fuction_a(datos):
    # Función que cuenta la cantidad de casos de secuencia H5N1 por región
    contador_regiones = lista_regiones(datos)
    for dato in datos: 
        for region in contador_regiones:
            if dato[3] == region[0]:
                if dato[8] == "H5N1":
                    region[1] += 1
    return contador_regiones

def fuction_b(datos):
    # Función que cuenta la cantidad de casos negativos para el mes de abril del año 2023
    negativos_ab_23 = 0
    for dato in datos:
        if dato [2][3:] == "04-2023":
            if dato[9] == "Negativo":
                negativos_ab_23 += 1
    return negativos_ab_23

def fuction_c(datos):
    # Función que cuenta la cantidad de yuncos negativos
    yuncus_neg = 0
    for dato in datos:
        if dato[5] == "Yunco":
            if dato[9] == "Negativo":
                yuncus_neg += 1
    return yuncus_neg

def fuction_d(datos):
    # Función que cuenta la cantidad de liles negativos en junio del 2023
    lile_neg_jun23 = 0
    for dato in datos:
        if dato[5] == "Lile":
            if dato[2][3:] == "06-2023":
                if dato[9] == "Negativo":
                    lile_neg_jun23 += 1
    return lile_neg_jun23

def cantidad_casos_neg(datos):
    # Función que cuenta la cantidad de casos negativos
    casos_neg = [
        ["Gaviota", 0],
        ["Piquero", 0],
        ["Salteador", 0],
        ["Pelicano", 0],
        ["Guanay", 0]]
    for dato in datos:
        for caso in casos_neg:
            if dato[5] == caso[0] or dato[5] == "Salteador chileno":
                if dato[9] == "Negativo":
                    caso[1] += 1
    return casos_neg

def crear_grafico(etiquetas, datos, colores):
    # Crear el gráfico de barras con color
    barras = plt.bar(etiquetas, datos, color=colores)
    # Agregar cuadriculas al gráfico
    ax = plt.gca()
    # Deja las cuadriculas por debajo
    ax.grid(True, color = "black", linestyle = "-", linewidth=0.5)
    for bar in barras:
        # Pone las barras sobre la cuadricula
        bar.set_zorder(10)
    # Agregar título y etiquetas al eje X e Y
    plt.title("Cantidad de casos negativos de algunas especies.")
    plt.xlabel("Especies de las aves")
    plt.ylabel("Casos negativos (-)")
    # Mostrar el gráfico
    plt.show()

def fuction_e(datos):
    # Función que crea un gráfico de barras con la cantidad de casos negativos
    colores = ["blue", "purple", "darkgoldenrod", "limegreen", "darkslategrey"]
    lista_casos_neg = cantidad_casos_neg(datos)
    x = []
    y = []
    # Recorre la lista de casos negativos y los almacena en las listas x e y
    for caso in lista_casos_neg:
        x.append(caso[0])
        y.append(caso[1])
    crear_grafico(x, y, colores)

def genera_salida(a, b, c, d):
    # Función que genera el archivo de salida
    f = open("resultadoS3.txt", "w")
    f.write("Autor(es): Eric Cerna Lizama - Pablo Cofré González\n\n")
    f.write("Cantidad de casos de secuenciación por región:\n\n")
    
    for region in a:
        f.write("\t" + region[0] + ": " + str(region[1]) + "\n\n")
        
    f.write("\nCasos negativos mes abril del año 2023: " + str(b) + "\n\n")
    f.write("Casos negativo especie Yunco: " + str(c) + "\n\n")
    f.write('Incidencias 06/2023 del “Lile”: ' + str(d))



if __name__ == "__main__":
    datos = lectura_datos("protocolo_vigilancia.txt") # Lectura de los datos del archivo
    a = fuction_a(datos)  # Respuesta al punto a de la tarea
    b = fuction_b(datos)  # Respuesta al punto b de la tarea
    c = fuction_c(datos)  # Respuesta al punto c de la tarea
    d = fuction_d(datos)  # Respuesta al punto d de la tarea
    e = fuction_e(datos)  # Respuesta al punto e de la tarea
    genera_salida(a, b, c, d)