from tkinter import *
from tkinter import messagebox

class Aplicacion:
    def __init__(self):
        self.root = Tk()
        
        self.menuBar = Menu(self.root)
        self.root.config(menu=self.menuBar)

        self.archivoMenu = Menu(self.menuBar, tearoff=0)
        
        self.archivoMenu.add_command(label="Nuevo")
        self.archivoMenu.add_command(label="Abrir", command=self.atencion)
        self.archivoMenu.add_command(label="Guardar", command=self.error)
        self.archivoMenu.add_command(label="Cerrar", command=self.cerrar)
        self.archivoMenu.add_separator()
        self.archivoMenu.add_command(label="Salir", command=self.root.quit)

        self.editMenu = Menu(self.menuBar, tearoff=0)

        self.editMenu.add_command(label="Cortar")
        self.editMenu.add_command(label="Copiar")
        self.editMenu.add_command(label="Pegar")

        self.ayudaMenu = Menu(self.menuBar,tearoff=0)
        self.ayudaMenu.add_command(label="Licencia", command=self.licencia)
        self.ayudaMenu.add_separator()

        self.menuBar.add_cascade(label="Archivo", menu=self.archivoMenu)
        self.menuBar.add_cascade(label="Editar", menu=self.editMenu)
        self.menuBar.add_cascade(label="Ayuda", menu=self.ayudaMenu)
        



        self.root.mainloop()


    def cerrar(self):
        messagebox.askquestion("Cerrar",message="¿Esta seguro?")
    

    def licencia(self):
        messagebox.showinfo("Versión", message="Versión 1.0")


    def error(self):
        messagebox.showerror("!ERROR CRITICO!", message="SE ENCONTRO UN ERROR FATAL")

    
    def atencion(self):
        messagebox.showwarning("ATENCIÓN", message= "Se borrara el actual")





aplicacion = Aplicacion()