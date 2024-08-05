cords = []
punto_temp = 1

while punto_temp < 5:
    print("Intrduce la posición x del punto ", punto_temp)
    cord_x_temp = input()

    print("Intrduce la posición y del punto ", punto_temp)
    cord_y_temp = input()
    
    punto_temp += 1

    cords.append([cord_x_temp, cord_y_temp])

print(cords)

ok = True

# Verificamos y
if (cords[0][1] != cords[1][1]) or (cords[2][1] != cords[3][1]):
    ok = False

# Verificamos x
if (cords[0][0] != cords[2][0]) or (cords[1][0] != cords[3][0]):
    ok = False

if ok == True:
    print("es rectangulo")
else:
    print("no es rectangulo")