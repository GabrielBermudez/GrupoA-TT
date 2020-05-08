import tkinter as tk
import time as tm
import sys
import time
from datetime import date
class luxury:
    def __init__(self):
        self.hora = tm.strftime('%H:%M:%S')
        self.fecha = date.today()
        #creacion de la ventana
        self.ventana1 = tk.Tk()
        self.ventana1.title("LUXURY")
        #creacion de los botones(sin asignar una funcion aun)
        self.boton1=tk.Button(self.ventana1, text="INGRESAR")
        self.boton1.grid(column = 5, row = 2)
        self.boton2=tk.Button(self.ventana1, text="REGISTRARSE")
        self.boton2.grid(column = 5, row = 4)
        #creacion de label
        #fecha
        self.fecha1=tk.Label(self.ventana1, text=self.fecha)
        self.fecha1.grid(column = 2, row = 7)
        self.fecha1.configure(foreground="red")
        #hora
        self.hora1=tk.Label(self.ventana1, text=self.hora)
        self.hora1.grid(column = 1, row = 6)
        self.hora1.configure(foreground="red") 
        self.ventana1.mainloop()
        
        
    
luxury1 = luxury()
