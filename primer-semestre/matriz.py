def fabrir():
    try:
        # Abre el archivo en modo lectura ('r' significa lectura)
        f = open('unidad-2/matriz.txt', 'r', encoding='UTF-8')
        # Realiza operaciones de lectura en el archivo
        contenido = f.read()
        f.close()
        return contenido

    except FileNotFoundError:
        print("El archivo no existe")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

def extraer_matriz(texto):
    filas = texto.split('\n')
    letras = ["A", "B"]
    
    for letra in letras:
        if letra in filas:
            filas.remove(letra)
    
    matrizA = filas[:2]
    matrizB = filas[2:]
    
    return matrizA, matrizB


def sumar_matriz(A,B):
    c = [
    int(A[0][0]) + int(B[0][0]),
    int(A[0][1]) + int(B[0][1]),
    int(A[1][0]) + int(B[1][0]),
    int(A[1][1]) + int(B[1][1])]
    
    return c


def main():
    matrizA, matrizB = extraer_matriz(fabrir())
    print(matrizA, matrizB)
    c = sumar_matriz(matrizA, matrizB)
    print(c)


if __name__ == '__main__':
    main()