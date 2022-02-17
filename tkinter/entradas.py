from tkinter import *
from tokenize import String

root = Tk()
root.title("Entradas")
root.geometry("330x300")
root.resizable(0,0)

nombre = StringVar()
apellido = StringVar()
saludo = StringVar()

nombre.set("Ingresa tu nombre")
apellido.set("Ingresa tu apellido")

def saludar():
    saludo.set("Hola "+nombre.get()+" "+apellido.get())




etiqueta1 = Label(root, text="Escribe tu nombre: ", bd=4, bg="red",font=("Curier 10"))
etiqueta1.place(x=10,y=10)
entrada1 = Entry(root, textvariable=nombre, bd=5)
entrada1.place(x=170,y=10)

etiqueta2 = Label(root,text="Escribe tu apellido: ", bd=4,bg="red",font=("Curier 10"))
etiqueta2.place(x=10, y=40)
entrada2 = Entry(root, textvariable=apellido, bd=5)
entrada2.place(x=170, y=40)


boton = Button(root, text="Saludar ahora", command=saludar,bd=5,bg="red")
boton.place(x=112, y=123)

entrada3 = Entry(root, bd=20, font=("Curier 10"),textvariable=saludo, state="disable")
entrada3.place(x=70, y=221)


root.mainloop()