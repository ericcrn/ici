def lectura_datos(archivo):
    full_names = []
    
    f = open("unidad-2/other/" + archivo, "r")
    for linea in f:
        full_names.append(linea.rstrip("\n").strip().split())
    f.close()
    
    return full_names

def generador_usuarios(full_names):
    users = []
    for name in full_names:
        user = (name[0][0] + name[1]).lower()
        if user in users:
            user = user + name[2].upper()
        users.append(user)
        
    return users

def grabacion_usuarios(users, archivo):
    f = open("unidad-2/temp/" + archivo, "w")
    for user in users:
        f.write(user + "\n")
    f.close()

if __name__ == "__main__":
    full_names = lectura_datos("nombres.txt")
    users = generador_usuarios(full_names)
    grabacion_usuarios(users, "usuarios.txt")