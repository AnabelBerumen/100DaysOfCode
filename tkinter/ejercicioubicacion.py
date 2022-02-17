from tkinter import *

root = Tk()
root.title("Posicionar")
root.geometry("400x200")

#funciones
def saludo():
    print("Hola que tal")

def minimizar():
    root.iconify()


#Interfaz

etiqueta1 = Label(root, text = "Saluda desde aquí")
etiqueta1.place(x=30, y=50)

etiqueta2 = Label(root, text="Minimiza desde aquí")
etiqueta2.place(x =30, y=100)

boton1 = Button(root, text="Haz click aqui para saludar",command=saludo)
boton1.place(x=200, y=50)

boton2 = Button(root, text="Haz click aqui para minimizar",command=minimizar)
boton2.place(x=200, y=100)



root.mainloop()