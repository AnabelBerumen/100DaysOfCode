from tkinter import *
from tkinter import ttk
"""
def calcular(*args):
    try:
        valor = float(pies.get())
        metros.set(int(0.3048 * valor * 10000.0 + 0.5)/10000.0)
        except ValueError:
            pass
"""

ventana = Tk()
ventana.title("Pies a metros")

mainframe = ttk.Frame(ventana, padding="3 3 12 12")
mainframe.grid(column=0, row= 0, sticky=(N,W,E,S))
ventana.columnconfigure(0, weight=1)
ventana.rowconfigure(0, weight=1)

pies = StringVar()
pies_entry = ttk.Entry(mainframe, width=7, textvariable=pies)
pies_entry.grid(column=2,  row=1,sticky=(W,E))




ventana.mainloop()