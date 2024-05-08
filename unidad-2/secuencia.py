lista_numeros = []
numero = 2
sumando = 3

while numero <= 1800:
    print(numero)
    lista_numeros.append(numero)
    numero += sumando 
    
    if sumando == 3:
        sumando = 2
    else:
        sumando = 3

print(lista_numeros)