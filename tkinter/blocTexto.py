from tkinter import Tk, Text

class Aplicacion:
    def __init__(self):
        self.root = Tk()
        self.root.resizable(False,False)
        self.root.title("Mi block de notas")
        #self.root.geometry("400x400")

        self.text = Text(self.root, height=8)
        self.text.pack()

        self.text.insert('1.0', 'Esto es un ejemplo de block de notas')




        self.root.mainloop()

aplicacion = Aplicacion()