def tomar_datos():
    d = float(input("Ingrese la distancia del objetivo (en millas): "))
    v = float(input("Ingrese la velocidad del torpedo (en nudos): "))

    return d, v

def millasnauticas_a_metros(millas):
    return millas * 1852

def nudos_a_metros_por_segundo(nudos):
    return nudos * 0.514444


def calcular_tiempo(d, v):
    return millasnauticas_a_metros(d) / nudos_a_metros_por_segundo(v)

if __name__ == "__main__":
    d, v = tomar_datos()
    t = calcular_tiempo(d, v)
    print(f"El tiempo que tarda el torpedo en llegar al objetivo es: {t} segundos")