def resolver_ec(a, b ,c):
    discriminante = (b ** 2) - (4 * a * c) 

    return discriminante


def main():
    print("Ingresa los valores correspondientes a la ecuación cuadrática con el siguiente formato: ax^2 + bx + c = 0.\n")
    a = float(input("Ingresar valor de a: "))
    b = float(input("Ingresar valor de b: "))
    c = float(input("Ingresar valor de c: "))
    
    discriminante = resolver_ec(a, b, c)

    if discriminante > 0: 
        print("La ecuación tiene dos soluciones. Valor de discriminante: ", discriminante)
    
    if discriminante == 0:
        print("La ecuación tiene una soluciones. Valor del discriminante: ", discriminante)
        
    if discriminante < 0:
        print("La ecuaciín no tiene soluciones. Valor del discriminantre: ", discriminante)


if __name__ == "__main__":
    main()