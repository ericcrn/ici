def resolver_ec(a, b ,c):
    x_despejada = (c - b) / a

    return x_despejada


def main():
    print("Ingresa los valores correspondientes a la ecuación lineal con el siguiente formato: ax + b = c.\n")
    a = float(input("Ingresar valor de a: "))
    b = float(input("Ingresar valor de b: "))
    c = float(input("Ingresar valor de c: "))
    
    x = resolver_ec()
    print("El valor de 'x' es:", x)


if __name__ == "__main__":
    main()