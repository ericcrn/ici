def lectura_datos(archivo):
    datos = []
    f = open("unidad-2/other/" + archivo, "r")
    for linea in f:
        datos.append(linea.rstrip("\n"))
    f.close()
    
    return datos

def limpiar_datos(datos):
    datos_limpio = []
    checker = False
    i = 0
    for dato in datos:
        for letra in dato:
            if letra == '"':
                if checker:
                    checker = False
                elif checker == False:
                    checker = True
            if checker and letra == ",":
                dato = dato[:i] + "." + dato[i+1:]
            i += 1
        datos_limpio.append(dato.split(","))
        i = 0
        
    
    return datos_limpio

def grabar_usuarios(datos, archivo):
    f = open("unidad-2/temp/" + archivo, "w")
    for dato in datos:
        f.write(",".join(dato) + "\n")
    f.close()

if __name__ == '__main__':
    datos = lectura_datos("titanic3.txt")
    datos_limpios = limpiar_datos(datos)
    grabar_usuarios(datos_limpios, "titanic_limpio.txt")