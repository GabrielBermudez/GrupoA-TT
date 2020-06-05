import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.font import Font
from tkinter import PhotoImage
from PIL import Image,ImageTk
from tkinter import scrolledtext as st
class GestionHabitaciones:
     def FrontHome(self):
        #creacion de la ventana
        self.ventanaHome = tk.Tk()
        self.ventanaHome.title("LUXURY")
        self.ventanaHome.geometry("1280x720")
        self.ventanaHome.resizable(0,0)
        self.ventanaHome.configure(bg= 'black')
        #Frames
        self.frameDatos=tk.Frame(self.ventanaHome,highlightbackground="red", highlightcolor="red", highlightthickness=1, bd=0, padx=20, pady=20)
        self.frameDatos.config(width=650,height=300) 
        self.frameDatos.place(x=600,y=85)
        self.frameDatos.configure(bg="black")
        
        self.frameDatos1=tk.Frame(self.ventanaHome,highlightbackground="red", highlightcolor="red", highlightthickness=1, bd=0, padx=20, pady=20)
        self.frameDatos1.config(width=650,height=300) 
        self.frameDatos1.place(x=600,y=400)
        self.frameDatos1.configure(bg="black")
        #labels
        #Labels de frames
        #Frame 1
        self.labelTitulo=tk.Label(self.frameDatos,text="INFORMACION DE LA HABITACION",background="black", foreground="white", font=('times 16 bold italic underline'))
        self.labelTitulo.place(x=120, y=-20)
        
        self.labelPiso=tk.Label(self.frameDatos,text="Piso: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelPiso.place(x=0, y=20)
        self.labelDatoPiso=tk.Label(self.frameDatos, text="", background="white")
        self.labelDatoPiso.place(x=140, y=22, width=370, height=20)      

        self.labelNombre=tk.Label(self.frameDatos,text="Capacidad: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelNombre.place(x=0, y=60)
        self.labelDatoNombre=tk.Label(self.frameDatos, text="", background="white")
        self.labelDatoNombre.place(x=140, y=62, width=370, height=20)   

        self.labelNombre=tk.Label(self.frameDatos,text="Disponibilidad: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelNombre.place(x=0, y=100)
        self.labelDatoNombre=tk.Label(self.frameDatos, text="", background="white")
        self.labelDatoNombre.place(x=140, y=102, width=370, height=20) 

        self.labelNombre=tk.Label(self.frameDatos,text="WI-FI: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelNombre.place(x=0, y=140)
        self.labelDatoNombre=tk.Label(self.frameDatos, text="", background="white")
        self.labelDatoNombre.place(x=140, y=142, width=370, height=20)   


        self.ventanaHome.mainloop()
        
    
                
GestionHabitaciones = GestionHabitaciones()
GestionHabitaciones.FrontHome()
