import triangulos as t
from tkinter import * 
from tkinter import messagebox

def capturar_lados():
    lado1 = entry1.get()
    lado2 = entry2.get()
    lado3 = entry3.get()
    
    messagebox.showinfo("Resultado", t.tipo_triangulo(lado1, lado2, lado3)) 

if __name__ == "__main__":
    root = Tk()
    root.title("Triángulos")
    root.geometry("400x400")
    
    label = Label(root, text="Ingresa los lados del triángulo")
    label.pack()
    
    label1 = Label(root, text="Lado 1")
    label1.pack()
    entry1 = Entry(root)
    entry1.pack()
    
    label2 = Label(root, text="Lado 2")
    label2.pack()
    entry2 = Entry(root)
    entry2.pack()
    
    label3 = Label(root, text="Lado 3")
    label3.pack()
    entry3 = Entry(root)
    entry3.pack()
    
    button = Button(root, text="Calcular", command=capturar_lados)
    button.pack()
    
    root.mainloop()