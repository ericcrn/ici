#Autor(es): Mauricio Castro - Eric Cerna
#Fecha: 1/12/24
#Objetivo: Gato/Tres en Raya

import os
import random

def limpiar():
    # Limpiar pantalla
    if os.name == 'nt':  
        os.system('cls')
    else: 
        os.system('clear')

def turnos():
    # Seleccionar aleatoriamente el jugador que inicia
    jugador = random.randint(1, 6)
    computador = random.randint(1, 6)
    print(f'Lanza dado Humano -> {jugador}\n')
    print(f'Lanza dado Computador -> {computador}\n')

    # Condicionales que comprueban quien empieza el juego
    if jugador == computador:
        print('Empate, se vuelven a lanzar los dados\n')
        return turnos()
    elif jugador > computador:
        return 'Humano'
    else:
        return 'Computador'


def movimientos_validos(tablero, movimiento):
    # Verificar si el movimiento es válido
    for lista in tablero:
        if movimiento in lista:
            return movimiento
    return False


def elegir_movimiento_aleatorio(tablero):
    # Movimientos aleatorios para el computador
    movimiento_valido_encontrado = False
    while not movimiento_valido_encontrado:
        movimiento = random.randint(1, 9)
        if movimientos_validos(tablero, movimiento):
            movimiento_valido_encontrado = True
            return movimiento


def obtener_movimiento_humano(tablero):
    # Obtener movimiento del jugador humano
    lista_movimientos = [1, 2, 3, 4, 5, 6, 7, 8, 9]

    movimiento_valido = False 
    while not movimiento_valido:
        entrada = input('Humano: \nJuega en ')
        if entrada.isdigit():
            movimiento = int(entrada)
            if movimiento in lista_movimientos and movimientos_validos(tablero, movimiento):
                movimiento_valido = True  
                return movimiento
            else:
                print(f'\nEl valor seleccionado puede estar ocupado o es inválido. Intente de nuevo.\n')
        else:
            print(f'\nEntrada inválida. Por favor ingrese un número entre 1 y 9.\n')


def obtener_movimiento_computador(tablero):
    # Obtener movimiento del computador
    for fila in range(3):
        for columna in range(3):
            # Similación de movimiento para verificar si es ganador
            if isinstance(tablero[fila][columna], int):
                # Si la celda es un número, entonces está disponible
                movimiento_temporal = tablero[fila][columna]
                tablero[fila][columna] = 'C'  
                
                if verificar_ganador(tablero) == 'C':
                    tablero[fila][columna] = movimiento_temporal 
                    return movimiento_temporal
                tablero[fila][columna] = movimiento_temporal  
    
    # Si no hay movimientos ganadores, elegimos un movimiento aleatorio
    return elegir_movimiento_aleatorio(tablero)


def actualizar_tablero(tablero, movimiento, marca):
    # Actualizar tablero con el movimiento
    for fila in range(3):
        for columna in range(3):
            if tablero[fila][columna] == movimiento:
                tablero[fila][columna] = marca


def mostrar_tablero(tablero):
    # Mostrar tablero como cuadrícula sin números iniciales
    for indice, fila in enumerate(tablero):
        # Recorremos cada fila y mostramos cada celda, usando espacios si aún no está ocupada
        celdas = []
        for celda in fila:
            if isinstance(celda, int):
                celdas.append(" ")
            else:
                celdas.append(celda)
        print(" | ".join(celdas))
        # Imprimir la línea divisoria solo entre filas, no al final
        if indice < 2:
            print("—" * 9)
    print("\n")



def cambiar_string_ganador(ganador):
    # Cambiar el valor de la marca (H o C) por un string más amigable
    if ganador == 'H':
        return 'Humano'
    else:
        return 'Computador'

def verificar_ganador(tablero):
    #Ganador por filas
    for fila in tablero:
        if fila[0] == fila[1] == fila[2]:
            return fila[0]
    #Ganador por columnas
    for columna in range(3):
        if tablero[0][columna] == tablero[1][columna] == tablero[2][columna]:
            return tablero[0][columna]
    #Ganador por diagonales 
    if tablero[0][0] == tablero[1][1] == tablero[2][2]:
        return tablero[0][0]
    #Ganador por diagonale inversa
    if tablero[0][2] == tablero[1][1] == tablero[2][0]:
        return tablero[0][2]
    
    return False

def quedan_movimientos(tablero):
    # Verificar si quedan movimientos disponibles
    for fila in tablero:
        for celda in fila:
            if celda in range(1, 10):
                return True
    return False


def juego(turno):
    # Función principal del juego
    tablero = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]]
    
    print(f'Inicia el juego: {turno}\n')
    mostrar_tablero(tablero)

    en_juego = True
    while en_juego:
        # Bucle principal del juego
        if turno == 'Humano':
            # Turno del jugador humano
            movimiento = obtener_movimiento_humano(tablero)
            actualizar_tablero(tablero, movimiento, 'H')
        else:
            # Turno del computador
            movimiento = obtener_movimiento_computador(tablero)
            print(f'Computador: \njuega en {movimiento}.')
            actualizar_tablero(tablero, movimiento, 'C')

        mostrar_tablero(tablero)
        ganador = verificar_ganador(tablero)
        if ganador:
            # Verificar si hay un ganador
            print(f'El Ganador es: {cambiar_string_ganador(ganador)}.')
            en_juego = False
        if not quedan_movimientos(tablero):
            # Verificar si hay un empate
            print(f'Se ha producido un empate.')
            en_juego = False

        # Cambiar de turno
        if turno == 'Humano':
            turno = 'Computador'
        else:
            turno = 'Humano'

    reiniciar = int(input('¿Desea jugar nuevamente? (0 = Sí / 1 = No): '))
    if reiniciar == 0:
        # Reiniciar el juego
        limpiar()
        juego(turnos())
    elif reiniciar == 1:
        print(f'¡Gracias por jugar!')
    else:
        print(f'Opción no valida')


if __name__ == '__main__':
    limpiar()
    turno = turnos()
    juego(turno)
