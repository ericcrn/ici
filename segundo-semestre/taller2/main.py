import os

def leer_archivo(archivo):
    DIR = os.path.dirname(os.path.realpath(__file__)) + "/"
    datos = []
    f = open(DIR + archivo, "r")
    for linea in f:
        datos.append(linea.rstrip("\n"))
    f.close()
    del datos[0]
    return datos


def extraer_datos(*args):
    dict = {}
    i = -1
    lista_txts = ["nombre", "precio", "ajuste"]
    
    for arg in args:
        i += 1
        for linea in arg:
            if linea != " ":
                producto = linea.split("\t")
                codigo = producto[0]
                desc = producto[1]
                if codigo in dict:
                    dict[codigo][lista_txts[i]] = desc
                else:
                    dict[codigo] = {}
                    dict[codigo][lista_txts[i]] = desc
    return dict

def pventa(precio, ajuste):
    if ajuste[0] == "(":
        ajuste = ajuste[1:-1]
        ajuste = "-" + ajuste
    precio = float(precio)
    ajuste = float(ajuste)
    
    return precio + (precio * ajuste / 100)

def clear_record(record):
    list = []
    in_pais = False
    
    for char in record[0]:
        if char 

def mostrar_datos(dict):
    columns = os.get_terminal_size().columns
    linea = '-' * columns
    sumPventa = 0
    print(f"{"Código":<12} {"Producto":<32} {"Precio":<12} {"Ajuste":<12} {"PVenta":<12}")
    print(linea)
    
    for i in dict:
        Pventa = pventa(dict[i]['precio'], dict[i]['ajuste'])
        sumPventa += Pventa
        print(f"{i:<12} {dict[i]['nombre'][:32]:<32} {dict[i]['precio']:<12} {dict[i]['ajuste']:<12} {Pventa:<12}")
    print(linea)
    print(f"\t\tTotal: {sumPventa}")


if __name__ == "__main__":
    productos = leer_archivo("productos.txt")
    precios = leer_archivo("precios.txt")
    ajuste = leer_archivo("ajuste.txt")
    
    dict = extraer_datos(productos, precios, ajuste)
    mostrar_datos(dict)