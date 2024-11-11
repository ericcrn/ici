# Autor(es): Eric Cerna Lizama - 22127660-4 - Ingenieria Civil Informatica
# Tomás Díaz Morales - 21332335-0 - Ingenieria Civil Informatica

def lectura_datos (archivo):
    # Función que lee los datos de un archivo de texto
    datos = []
    f = open("./" + archivo, "r", encoding="ascii")
    txt = f.readlines()
    for linea in txt:
        linea = linea.replace("\n", "") 
        # Quita espacios.
        linea = linea.split(" ") 
        # Divide cada linea separada por espacios.
        if linea == ['']:
            pass
        else:
            for item in linea:
                if item != "": # Nos aseguramos que no contenga espacios vacios.
                    datos.append(int(item))
    f.close()
    
    return datos


def eliminar_ceros_repetidos(datos):
    # Función que elimina ceros consecutivos de la lista.
    indice = 0
    anterior = None
    
    while indice < len(datos):
        if datos[indice] == 0:
            if anterior == 0:
                datos.pop(indice)
                # Recorre la lista "datos" en busca de ceros, si se encuentran dos ceros seguidos se elimina uno de ellos.
                indice -= 1
            else:
                anterior = 0
        else:
            anterior = datos[indice]
        indice += 1
        # Al no haber ceros consecutivos en la lista resultante se devuelve la lista "datos" sin ceros consecutivos.
        
    return datos


def extraer_secuencias(datos):
    # Función que separa la lista en secuencias separadas por ceros.
    secuencias = []
    secuencia = []
    
    for dato in datos:
        if dato != 0:
            # Al encontrar un numero distinto de 0 lo agrega a una secuencia temporal.
            secuencia.append(dato)
        else:
            secuencias.append(secuencia)
            # Al encontrar un 0 agrega la secuencia a la lista "secuencias" y empieza nuevamente el proceso.
            secuencia = []

    return secuencias

def eliminar_secuencias_cortas(secuencias, largo):
    # Función que elimina secuencias menores a un numero establecido, (menores a 3 en este caso).
    indice = 0
    while indice < len(secuencias):
        if len(secuencias[indice]) < largo:
            # Si la secuencia tiene menor longitud que el largo de esta, se elmina.
            secuencias.pop(indice)
            indice -= 1
        indice += 1
    
    return secuencias


def encontrar_cimas(secuencia):
    # Función que se encarga de encontrar las cimas en las secuencias numericas.
    cimas = []
    indice = 1
    repetidos = 1
    en_repeticion = False

    while (indice < len(secuencia) - 1):
        # Recorre las secuencias para encontrar numeros repetidos.
        if (secuencia[indice] == secuencia[indice + 1]):
            if en_repeticion == False:
                en_repeticion = True
                repetidos = 2
            else:
                repetidos += 1
        elif (secuencia[indice] > secuencia[indice + 1]):
            if en_repeticion:
                if (secuencia[indice - repetidos] < secuencia[indice]) and (secuencia[indice] > secuencia[indice + 1]):
                    # Si se encuentra una cima se agrega a la lista cimas en donde seran definidas por posición y cuantas veces se repite este valor de posición.
                    cimas.append([(indice + 1) - (repetidos - 1), repetidos])
                    en_repeticion = False
                    repetidos = 1
                else:
                    en_repeticion = False
            elif secuencia[indice - 1] < secuencia[indice]:
                cimas.append([indice + 1, repetidos])
        else: 
            en_repeticion = False
            repetidos = 1
        indice += 1
    
    return cimas


def genera_archivo(secuencias):
    # Funcion que genera el archvio "cimas.txt" el cual contiene todas las cimas de cada secuencia.
    f = open("cimas.txt", "w", encoding="ascii")
    
    for secuencia in secuencias:
        cimas = encontrar_cimas(secuencia)
        for cima in cimas:
            f.write(str(cima[0]) + " " + str(cima[1]) + "\n")
            # Escribe las posiciones y cantidades de las cimas en el archivo.
        f.write("***\n")
        # Después de procesar una secuencia genera "***" para indicar el fin de dicha secuencia.
    f.close()


if __name__ == "__main__":
    datos = lectura_datos("datos.txt")
    datos = eliminar_ceros_repetidos(datos)
    secuencias = extraer_secuencias(datos)
    #secuencias = eliminar_secuencias_cortas(secuencias, 3)
    
    genera_archivo(secuencias)