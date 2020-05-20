import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.font import Font
class GestionHabitaciones:
     def FrontHome(self):
        #creacion de la ventana
        self.ventanaHome = tk.Tk()
        self.ventanaHome.title("Gestion de Habitaciones")
        self.ventanaHome.geometry("800x600")
        self.ventanaHome.resizable(0,0)
        self.ventanaHome.configure(bg= 'black')
        #labels
        self.frameTitulo=ttk.Label(self.ventanaHome, text="Gestion de Habitaciones")
        self.frameTitulo.config(background = "black", foreground="white",font='times 34 bold italic underline')
        self.frameTitulo.pack(anchor=CENTER)
        self.piso1=ttk.Label(self.ventanaHome, text="Piso 1")
        self.piso1.config(background = "black", foreground="white",font='times 16 bold italic underline')
        self.piso1.place(x=45, y=75)
        self.piso2=ttk.Label(self.ventanaHome, text="Piso 2")
        self.piso2.config(background = "black", foreground="white",font='times 16 bold italic underline')
        self.piso2.place(x=140, y=75)
        self.piso3=ttk.Label(self.ventanaHome, text="Piso 3")
        self.piso3.config(background = "black", foreground="white",font='times 16 bold italic underline')
        self.piso3.place(x=235, y=75)
        
        #botones
        self.fila=3
        self.columna=6
        self.contadorNombre=1
        self.habitacion=[]
        for i in range(self.columna): 
            for j in range(self.fila): 
                
                auxiliar=self.contadorNombre
                self.boton=tk.Button(self.ventanaHome,text="Habitacion "+str(self.contadorNombre), command= lambda contadorNombre=self.contadorNombre: self.MostrarDatos(self.habitacion,contadorNombre),  bg="red", fg="white", relief=RAISED, bd = 5)
                self.boton.place(x=j+(95*j+30), y=i+(70*i+120), width=85, height=70)
                self.habitacion.append(self.boton)
                self.contadorNombre+=1
        self.ventanaHome.mainloop()
GestionHabitaciones = GestionHabitaciones()
GestionHabitaciones.FrontHome()
