temperatures = {}
bars = {}

def check_is_number(value):
    try:
        value = int(value)
        return True
    except ValueError:
        return False

def ingresar_temperatura():
    num = input("Ingrese la cantidad de temperaturas que desea convertir: ")
    if not check_is_number(num):
        print("Por favor ingrese un número")
        num = input("Ingrese la cantidad de temperaturas que desea convertir")
        num = int(num)
    i = 0
    while int(num) > i:
        input_temp = input("Ingrese la temperatura en grados celcius: ")
        try:
            temp = float(input_temp)
        except ValueError:
            print("Por favor ingrese un número")
            i -= 1
        temp_num = "temp{}".format(i)
        temperatures[temp_num] = temp
        i += 1

def ingresar_bar():
    num = input("Ingrese la cantidad de bar que desea convertir: ")
    if not check_is_number(num):
        print("Por favor ingrese un número")
        num = input("Ingrese la cantidad de bar que desea convertir")
        num = int(num)
    i = 0
    while int(num) > i:
        input_bar = input("Ingrese la presión en bar: ")
        try:
            bar = float(input_bar)
        except ValueError:
            print("Por favor ingrese un número")
            i -= 1
        bar_num = "bar{}".format(i)
        bars[bar_num] = bar
        i += 1

def celcius_to_fahrenheit(celcius):
    return celcius * 9/5 + 32

def celcius_to_kelvin(celcius):
    return celcius + 273.15

def bar_to_pascales(bar):
    return bar * 100000

def bar_to_kilo_pascals(bar):
    return bar * 100

if __name__ == "__main__":
    ingresar_temperatura()
    ingresar_bar()
    for key, value in temperatures.items():
        print(f"{key}: {value}°C = {celcius_to_fahrenheit(value)}°F = {celcius_to_kelvin(value)}K") 
    print("\n")
    for key, value in bars.items():
        print(f"{key}: {value}bar = {bar_to_pascales(value)}Pa = {bar_to_kilo_pascals(value)}kPa")