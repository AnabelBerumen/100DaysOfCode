from tkinter import *

root = Tk()
root.title("Ventana")
root.geometry("400x200")

#Utilizando grid
etiqueta = Label(root, text= "Etiqueta 0x0")
etiqueta.grid(row=0, column=0)

boton1 = Button(root, text ="boton 0 x 1")
boton1.grid(row=0, column=1)

#utilizando place
etiqueta2 = Label(root, text="labelPlace 50x50")
etiqueta2.place(x = 50, y = 50)


root.mainloop()