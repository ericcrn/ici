# Autor: Eric Cerna
import os
DIR = os.path.dirname(os.path.realpath(__file__)) + "/"

def leer_archivo(archivo):
    f = open(DIR + archivo, "r")
    datos = f.read()
    f.close()
    return datos

def limpiar_elecciones(elecciones):
    elecciones_limpio = elecciones.split(";")
    coaliciones = {}
    
    for item in elecciones_limpio:
        item = item.split(":")
        partidos = item[1].split("-")
        if item[0] not in coaliciones:
            coaliciones[item[0]] = {}
            for partido in partidos:
                coaliciones[item[0]][partido] = 0
    
    return coaliciones

def contar_votos(votos, elecciones):
    votos = votos.split("$")
    dict = elecciones
    
    for voto in votos:
        for coalicion in dict:
            for partido in dict[coalicion]:
                if partido in voto:
                    dict[coalicion][partido] += 1
    
    return dict

def archivo_salida(votos):
    f = open(DIR + "resultado.txt", "w")
    suma = 0
    
    for coalicion in votos:
        linea = "Coalición: {}\n".format(coalicion)
        f.write(linea)
        for partido in votos[coalicion]:
            suma += votos[coalicion][partido]
            
            linea = "Partido {}: {}\n".format(partido, votos[coalicion][partido])
            f.write(linea)
        f.write("Total de votos: {}\n".format(suma))
        suma = 0
        f.write("\n\n")
    f.close()

if __name__ == "__main__":
    elecciones = leer_archivo("elecciones.txt")
    elecciones = limpiar_elecciones(elecciones)
    votos = leer_archivo("votos.txt")
    votos = contar_votos(votos, elecciones)
    archivo_salida(votos)