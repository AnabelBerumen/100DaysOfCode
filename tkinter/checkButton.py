from tkinter import *


class Aplicacion:
    def __init__(self):
        self.root = Tk()
        self.root.title("Casas de comidas")
        self.root.config(bd=20, bg="lavender")

        self.queso = IntVar()
        self.lechuga = IntVar()

        self.imagen = PhotoImage(file = "C:/Users/Equipo/Desktop/python/100DaysOfCode/100DaysOfCode/tkinter/bob.gif")
        Label(self.root, image=self.imagen).pack(side=LEFT)

        self.frame = Frame()
        self.frame.pack(side=RIGHT)
        self.frame.config(bg="DeepSkyBlue2")

        Label(self.frame, text = "¿Como quieres tu hamburguesa?",bg="DeepSkyBlue2", font="Curier 15").pack(anchor="w")
        Checkbutton(self.frame, text= "Con queso", variable=self.queso, onvalue=1,offvalue=0,bg="DeepSkyBlue2",font="Curier 10",command=self.orden).pack(anchor="w")

        Checkbutton(self.frame, text="Con lechuga",variable=self.lechuga, onvalue=1,offvalue=0,bg="DeepSkyBlue2",font="Curier 10",command=self.orden).pack(anchor="w")

        self.imprimir = Label(self.frame,bg="DeepSkyBlue2")
        self.imprimir.pack()

        self.root.mainloop()

    def orden(self):
        self.lista=""
        if (self.queso.get()):
            self.lista += " Con queso"
        else:
            self.lista += " Sin queso"

        if (self.lechuga.get()):
            self.lista += " y con lechuga"
        else:
            self.lista += " y sin lechuga"
        
        self.imprimir.config(text=self.lista)
        



aplicacion = Aplicacion()




