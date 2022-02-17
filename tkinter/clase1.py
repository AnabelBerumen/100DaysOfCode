from tkinter import *

root = Tk()
root.title("Ventana")
root.geometry("500x300")

#Textos
texto = Label(root, text = "Hola mundo")
texto.pack()

#Botones
boton1 = Button(root, text = "Minimizar", command=root.iconify, bg = "red")
boton1.pack(side = LEFT)

#Boton pasar una acción creada por nosotros
def imprimir():
    #print("Imprimiendo ....")
    label1 = Label(root, text="Imprimiendo...", bg = "green")
    label1.pack()

boton2 = Button(root, text = "Imprimir", command=imprimir, bg= "blue")
boton2.pack(side = RIGHT)




root.mainloop()