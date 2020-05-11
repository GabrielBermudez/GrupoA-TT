import tkinter as tk
from tkinter import ttk
from tkinter import *
class Botones:
    global auxiliar
    def __init__(self):

        self.ventanaHome = tk.Tk()
        self.ventanaHome.title("LUXURY")
        self.ventanaHome.geometry("800x600")
        self.ventanaHome.resizable(0,0)


        self.fila=3
        self.columna=6
        self.contadorNombre=1
        self.habitacion=[]
        for i in range(self.columna): 
            for j in range(self.fila): 

                auxiliar=self.contadorNombre
                self.boton=tk.Button(self.ventanaHome,text="Habitacion "+str(self.contadorNombre), command= lambda contadorNombre=self.contadorNombre: self.MostrarDatos(self.habitacion,contadorNombre))
                self.boton.place(x=j+(95*j), y=i+(70*i), width=85, height=40)
                self.habitacion.append(self.boton)
                self.contadorNombre+=1

        self.ventanaHome.mainloop()
    
    def MostrarDatos(self,habitacion,id):
         print(id) 
boton = Botones()



