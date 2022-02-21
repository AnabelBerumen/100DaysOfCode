from tkinter import *

class Aplicacion:
    def __init__(self):
        self.root = Tk()
        
        self.menuBar = Menu(self.root)
        self.root.config(menu=self.menuBar)

        self.archivoMenu = Menu(self.menuBar, tearoff=0)
        
        self.archivoMenu.add_command(label="Nuevo")
        self.archivoMenu.add_command(label="Abrir")
        self.archivoMenu.add_command(label="Guardar")
        self.archivoMenu.add_command(label="Cerrar")
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label="Salir", command=self.root.quit)

        self.editMenu = Menu(self.menuBar, tearoff=0)

        self.editMenu.add_command(label="Cortar")
        self.editMenu.add_command(label="Copiar")
        self.editMenu.add_command(label="Pegar")

        self.ayudaMenu = Menu(self.menuBar,tearoff=0)
        self.ayudaMenu.add_command(label="Ayuda")
        self.ayudaMenu.add_separator()

        self.menuBar.add_cascade(label="Archivo", menu=self.archivoMenu)
        self.menuBar.add_cascade(label="Editar", menu=self.editMenu)
        self.menuBar.add_cascade(label="Ayuda", menu=self.ayudaMenu)
        



        self.root.mainloop()




aplicacion = Aplicacion()