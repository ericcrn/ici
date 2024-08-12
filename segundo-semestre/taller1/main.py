import os

estudiantes = {
    "Ana": [8, 9, 7, 10],
    "Julia": [8, 9, 7, 10],
    "Adriana": [8, 9, 7, 10],
    "Benjamín": [8, 9, 7, 10],
    "Diego": [8, 9, 7, 10],
    "Juan": [8, 9, 7, 10],
    "María": [9, 10, 9, 8],
    "Pedro": [7, 8, 6, 9]
}

def promedio_notas(lista):
    return sum(lista) / len(lista)

def nota_maxima(lista):
    return max(lista)

def nota_minima(lista):
    return min(lista)

def crear_dict(estudiantes):
    for estudiante in estudiantes:
        promedio = promedio_notas(estudiantes[estudiante])
        maxima = nota_maxima(estudiantes[estudiante])
        minima = nota_minima(estudiantes[estudiante])
        estudiantes[estudiante] = [promedio, maxima, minima]
    return estudiantes

def salida(estudiantes):
    columns = os.get_terminal_size().columns
    linea = '-' * columns
    print(f"{"Nombre":<12} {"Promedio":<10} {"Máxima":<8} {"Mínima":<8}")
    print(linea)
    for estudiante in estudiantes:
        print(f"{estudiante:<12} {estudiantes[estudiante][0]:<10} {estudiantes[estudiante][1]:<8} {estudiantes[estudiante][2]:<8}")

if __name__ == "__main__":
    dict = crear_dict(estudiantes)
    salida(dict)