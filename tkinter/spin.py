from tkinter import *
from tkinter import messagebox

class Aplicacion:
    def __init__(self):
        self.root = Tk()
        self.root.geometry("200x100")

        self.w = Spinbox(self.root, values=("Python","Java","Javascript","C++"))
        self.w.pack()

        self.q = Spinbox(self.root, values=("SQLite","MySQL","Django","PostgreSQL"))
        self.q.pack()

        self.root.mainloop()





aplicacion = Aplicacion()