from tkinter import *

class Aplicacion:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("400x400")

        self.productos = Label(self.root, text="Productos")
        self.productos.pack()


        self.listaProductos = Listbox(self.root, width=50,)
        self.listaProductos.insert(0,"Carne")
        self.listaProductos.insert(1, "Pollo")
        self.listaProductos.insert(2,"Salmon")
        self.listaProductos.insert(3,"Verdura")
        self.listaProductos.pack()

        #Eliminar productos
        #self.listaProductos.delete(0)

        self.entrada = Entry(self.root, bd=10)
        self.entrada.pack()

        self.boton = Button(self.root, text="Agregar producto",command=self.agregar)
        self.boton.pack()

        self.boton2 = Button(self.root, text="Eliminar Producto",command=self.eliminar)
        self.boton2.pack()

        self.root.mainloop()

    def agregar(self):
        self.listaProductos.insert(END, self.entrada.get())

    def eliminar(self):
        num = self.entrada.index(self.entrada.get())
        self.listaProductos.delete(num)


aplicacion = Aplicacion()