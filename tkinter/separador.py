import tkinter as tk
from tkinter import ttk

class Aplicacion:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("300x200")
        self.root.resizable(False,False)
        self.root.title("Separador")

        ttk.Label(self.root, text = "Mi primer Label").pack()

        self.separador = ttk.Separator(self.root,orient="horizontal")
        self.separador.pack(fill="x")

        ttk.Label(self.root, text= "Mi segunda Label").pack()


        self.root.mainloop()



aplicacion = Aplicacion()
