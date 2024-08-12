# Autor: Eric Cerna Lizama
import os

DIR = os.path.dirname(os.path.realpath(__file__)) + "/"
NUM_CASO = "3688580-4"
GUIA = "ITEM\t\t\tCANTIDAD\tPRECIO UNITARIO"

def lectura_datos(archivo): # Lee los datos del archivo
    datos = []
    f = open(DIR + archivo, "r")
    for linea in f:
        datos.append(linea.rstrip("\n"))
    return datos

def isPar(n): # Determina si un numero es par
    if n % 2 == 0:
        return True
    return False

def extraer_parrafo(datos): # Extrae el parrafo del caso
    i = 0
    en_parrafo = False
    parrafo = []
    
    for linea in datos:
        if linea == ("CASO " + NUM_CASO) or en_parrafo:
            if linea == "":
                if i == 2:
                    return parrafo
                else: 
                    i += 1
                    parrafo.append(linea)
            else:
                parrafo.append(linea)
                en_parrafo = True
    return parrafo

def limpar_parrafo(parrafo): # Limpia el parrafo
    en_parrafo = False
    cant_precio = []
    
    for linea in parrafo:
        if linea == GUIA or en_parrafo:
            en_parrafo = True
            if linea == "":
                return cant_precio
            else:
                if linea == GUIA:
                    pass
                else:
                    cant_precio.append(linea)
    return cant_precio

def limpiar_cant_precio(cant_precio): # Limpia la cantidad y precio
    cant_precio_limpio = []
    for linea in cant_precio:
        linea = linea.split("\t")
        for item in linea:
            item = item.replace(" ", "")
            if item != "":
                cant_precio_limpio.append(item)

    for item in cant_precio_limpio:
        if not item.isnumeric():
            cant_precio_limpio.remove(item)
    return cant_precio_limpio

def calcular_total(cant_precio_limpio): # Calcula el total
    cantidad = 0
    p_unitario = 0
    i = 1
    
    for num in cant_precio_limpio:
        if isPar(i):
            p_unitario += int(num)
            i += 1
        else:
            cantidad += int(num)
            i += 1
    return cantidad, p_unitario

def salida_datos(cantidad, p_unitario): # Salida de datos
    f = open(DIR + "caso4.dat", "w")
    f.write("CASO " + NUM_CASO + "\n")
    f.write("CANTIDAD: " + str(cantidad) + "\n")
    f.write("UNITARIO: " + str(p_unitario) + "\n")

if __name__ == "__main__":
    datos = lectura_datos("SetDePruebas.txt")
    parrafo = extraer_parrafo(datos)
    cant_precio = limpar_parrafo(parrafo)
    cant_precio_limpio = limpiar_cant_precio(cant_precio)
    cantidad, p_unitario = calcular_total(cant_precio_limpio)
    salida_datos(cantidad, p_unitario)