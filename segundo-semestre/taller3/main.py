# Autor: Eric Cerna
from tkinter import *
from tkinter import messagebox
from melamina import *

def mostrar_resultados():
    precio = float(entry_precio.get())
    perdida = float(entry_perdida.get())
    
    ancho_melamina = float(entry_ancho_melamina.get())
    alto_melamina = float(entry_alto_melamina.get())
    
    ancho = float(entry_ancho.get())
    alto = float(entry_alto.get())
    
    if (precio <= 0 or perdida <= 0 or ancho_melamina <= 0 or alto_melamina <= 0 or ancho <= 0 or alto <= 0):
        messagebox.showerror("Error", "Los datos ingresados no son validos")
    if (precio == "" or perdida == "" or ancho_melamina == "" or alto_melamina == "" or ancho == "" or alto == ""):
        messagebox.showerror("Error", "Los datos ingresados no son validos")
    else:
        planchas_totales, precio, perdida, sobrante = calcular_cantidad_melamina(ancho, alto, precio, perdida, [ancho_melamina, alto_melamina])
        messagebox.showinfo("Resultado", f"Plancahs utilizadas: {int(planchas_totales)}.\nPrecio: {int(precio)} clp.\nPerdida: {int(perdida)} cm2.\nSobrante: {int(sobrante)} cm2.")

if __name__ == "__main__":
    root = Tk()
    
    root.title("Calculadora Melamina")
    root.geometry("400x600")
    root.resizable(False, False)

    # GUI    
    label1 = Label(root, text="INGRESE LOS DATOS", font=("Arial", 20))
    label1.pack(pady=15)
    
    label2 = Label(root, text="Precio melamina:", font=("Arial", 15))
    label2.pack(pady=0)
    entry_precio = Entry(root)
    entry_precio.pack(pady=5)
    
    label3 = Label(root, text="Perdida corte:", font=("Arial", 15))
    label3.pack(pady=0)
    entry_perdida = Entry(root)
    entry_perdida.pack(pady=5)
    
    label4 = Label(root, text="Ancho Melamina", font=("Arial", 15))
    label4.pack(pady=0)
    entry_ancho_melamina = Entry(root)
    entry_ancho_melamina.pack(pady=5)
    
    label5 = Label(root, text="Alto Melamina", font=("Arial", 15))
    label5.pack(pady=0)
    entry_alto_melamina = Entry(root)
    entry_alto_melamina.pack(pady=5)
    
    
    label6 = Label(root, text="DIMENSIONES A CORTAR", font=("Arial", 20))
    label6.pack(pady=15)
    
    label7 = Label(root, text="Ancho:", font=("Arial", 15))
    label7.pack(pady=0)
    entry_ancho = Entry(root)
    entry_ancho.pack(pady=5)
    
    label8 = Label(root, text="Alto:", font=("Arial", 15))
    label8.pack(pady=0)
    entry_alto = Entry(root)
    entry_alto.pack(pady=5)
    
    boton = Button(root, text="Calcular", font=("Arial", 15), command=mostrar_resultados)
    boton.pack(pady=20)

    root.mainloop()