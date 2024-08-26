def es_triangulo(l1, l2, l3):
    if (l1 + l2) > l3 and (l1 + l3) > l2 and (l2 + l3) > l1:
        return True
    return False

def tipo_triangulo(l1, l2, l3):
    if es_triangulo(l1, l2, l3):
        if l1 == l2 and l2 == l3:
            return "Equilatero"
        elif l1 == l2 or l1 == l3 or l2 == l3:
            return "Isosceles"
        else:
            return "Escaleno"
    return "No es un triangulo"