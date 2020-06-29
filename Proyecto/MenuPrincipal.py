import tkinter as tk
from tkinter import ttk
from tkinter import *
from RegistroHuespedes import RegistroHuesped
from GestionHabitaciones import *
from AdministracionEstacionamiento import *

class Menu:
    def Inicio(self):
        self.ventanaHome = tk.Tk()
        self.ventanaHome.title("LUXURY")
        self.ventanaHome.geometry("800x600")
        self.ventanaHome.resizable(0,0)
        self.ventanaHome.configure(bg= 'black')
        self.frameTitulo=ttk.Label(self.ventanaHome, text="Luxury")
        self.frameTitulo.config(background = "black", foreground="white",font='times 38 bold italic underline')
        self.frameTitulo.pack(anchor=CENTER)
        self.center(self.ventanaHome)
        #creacion de los botones
        self.botonIngresar=tk.Button(self.ventanaHome, text="Registro Huespedes", bg="black", fg="white", font='times 20 italic', relief= RAISED, command=self.AbrirRegistroHuesped)
        self.botonIngresar.place(x=230, y=150, width=350, height=105)
        
        self.botonRegistrarse=tk.Button(self.ventanaHome, text="Disponibilidad Habitaciones", bg="black", fg="white", font='times 20 italic', relief= RAISED, command=self.AbrirGestionHabitaciones)
        self.botonRegistrarse.place(x=230, y=300, width=350, height=105)

        self.botonRegistrarse=tk.Button(self.ventanaHome, text="Estacionamiento", bg="black", fg="white", font='times 20 italic', relief= RAISED, command=self.AbrirGestionEstacionamiento)
        self.botonRegistrarse.place(x=230, y=450, width=350, height=105)

        self.ventanaHome.mainloop()

    def AbrirRegistroHuesped(self):
       
        self.registroHuesped = RegistroHuesped()
        #self.ventanaHome.iconify()
        
        self.registroHuesped.Inicio(self.ventanaHome)
        
        
        
    def AbrirGestionHabitaciones(self):
        gestion = GestionHabitaciones()
        gestion.FrontHome()

    def AbrirGestionEstacionamiento(self):
        estacionamiento = Estacionamiento()
        estacionamiento.Inicio()

    def center(self,win):
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))    
"""menu = Menu()
menu.Inicio()"""