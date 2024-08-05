import os

PI = 3.14

msg_menu = [
"Introduce el número correspondiente para cada calculo que desees.",
"[1] Calculos de cilindros.",
"[2] Calculos de cubos.",
"[3] Calculos de conos.",
"[4] Calculos de esferas"]

msg_cilindros = [
"[1] Calcular area del cilindro.",
"[2] Calcular volumen del cilindro."
]

msg_cubos = [
"[1] Calcular area del cubo.",
"[2] Calcular volumen del cubo."
]

msg_conos = [
"[1] Calcular area del cono.",
"[2] Calcular volumen del cono."
]

msg_esferas = [
"[1] Calcular area de la esfera.",
"[2] Calcular volumen de la esfera."
]

def cls():
    if os.name=="nt":
        os.system("cls")
    else: 
        os.system("clear")

# CILINDRO
def area_cilindro(r, h):
    area_cilindro = 2 * PI * r * (r+h)
    return area_cilindro

def vol_cilindro(r, h):
    vol_cilindro = PI * (r**2) * h
    return vol_cilindro

# CUBO
def area_cubo(a):
    area_cubo = 6 * (a**2)
    return area_cubo

def vol_cubo(a):
    vol_cubo = a**3
    return vol_cubo

# CONO
def area_cono(r, g):
    area_cono = (PI * r * g) + (PI * (r**2))
    return area_cono

def vol_cono(r ,h):
    vol_cono = ((PI * (r**2) * h)/3)
    return vol_cono

# ESFERA
def area_esfera(r):
    area_esfera = 4 * PI * (r**2)
    return area_esfera

def vol_esfera(r):
    vol_esfera = (4/5) * (PI * (r**3))
    return vol_esfera


    
def menu_seleccion(num):
    cls()
    
    # CILINDRO
    if (num == 1):
        for msg in msg_cilindros:
            print(msg)
        
        seleccion = int(input())
        cls()
        
        if (seleccion == 1):
            r = float(input("Introduce el radio del cilindro en cm: "))
            h = float(input("Introduce la altura del cilindro en cm: "))
            area = area_cilindro(r, h)
            
            print("El area del cilindro es: ", area)
        
        if (seleccion == 2):
            r = float(input("Introduce el radio del cilindro en cm: "))
            h = float(input("Introduce la altura del cilindro en cm: "))
            vol = vol_cilindro(r, h)
            
            print("El volumen del cilindro es: ", vol)
            
    # CUBO
    if num == 2: 
        for msg in msg_cubos:
            print(msg)
        
        seleccion = int(input())
        cls()
        
        if (seleccion == 1):
            a = float(input("Introduce el lado del cubo en cm: "))
            area = area_cubo(a)
            
            print("El area del cubo es: ", area)
        
        if (seleccion == 2):
            a = float(input("Introduce el lado del cubo en cm: "))
            vol = vol_cubo(a)
            
            print("El volumen del cubo es: ", vol)
            
    # CONO
    if num == 3: 
        for msg in msg_conos:
            print(msg)
            
        seleccion = int(input())
        cls()
        
        if (seleccion == 1):
            r = float(input("Introduce el radio del cono en cm: "))
            g = float(input("Introduce la altura inclinada del cono en cm: "))
            area = area_cono(r, g)
            
            print("El area del cono es: ", area)
        
        if (seleccion == 2):
            r = float(input("Introduce el radio del cono en cm: "))
            h = float(input("Introduce la altura del cono en cm: "))
            vol = vol_cono(r, h)
            
            print("El volumen del cono es: ", vol)
            
    # ESFERA
    if num == 4: 
        for msg in msg_esferas:
            print(msg)

        seleccion = int(input())
        cls()
        
        if (seleccion == 1):
            r = float(input("Introduce el radio de la esfera en cm: "))
            area = area_esfera(r)
            
            print("El area de la esfera es: ", area)
        
        if (seleccion == 2):
            r = float(input("Introduce el radio de la esfera en cm: "))
            vol = vol_esfera(r)
            
            print("El volumen de la esfera es: ", vol)
            
    
def main():
    cls()
    
    for msg in msg_menu:
        print(msg)
        
    num = int(input())
    menu_seleccion(num)


if __name__ == "__main__":
    main()