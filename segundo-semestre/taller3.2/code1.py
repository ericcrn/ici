def factorial(n):
    if (n == 0): 
        return 1
    else: 
        if n < 0:
            return n * factorial(n + 1)
        else:
            return n * factorial(n - 1) 


def suma_lista(lista):
    suma = ""
    for i in lista: 
        suma += i
    return suma


# Código que solo se ejecuta cuando se ejecuta el script directamente 
if __name__ == "__main__": 
    resultado_factorial = factorial(-10) 
    resultado_suma = suma_lista("resultado") 
    
    print("El factorial de -10 es:", resultado_factorial) 
    print("La suma de la lista es:", resultado_suma)