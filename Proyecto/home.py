import tkinter as tk
from tkinter import ttk
from tkinter import *
import time as tm
import sys
import time
from datetime import date
from Login import Ingreso
from Registro import Registro

class Luxury:

    def FrontHome(self):
        #creacion de la ventana
        self.ventanaHome = tk.Tk()
        self.ventanaHome.title("LUXURY")
        self.ventanaHome.geometry("800x600")
        self.ventanaHome.resizable(0,0)
        self.ventanaHome.configure(bg= 'black')
        self.frameTitulo=ttk.Label(self.ventanaHome, text="Luxury")
        self.frameTitulo.config(background = "black", foreground="white",font=("Verdana",32))
        self.frameTitulo.pack(anchor=CENTER)

        #creacion de los botones(sin asignar una funcion aun)
        self.botonIngresar=tk.Button(self.ventanaHome, text="Ingresar", command= self.AbrirLogin, bg="black", fg="white", font=("Verdana",16), relief= RAISED)
        self.botonIngresar.place(x=550, y=150, width=210, height=105)
        
        self.botonRegistrarse=tk.Button(self.ventanaHome, text="Registrarse", command= self.AbrirRegistro, bg="black", fg="white", font=("Verdana",16), relief= RAISED)
        self.botonRegistrarse.place(x=550, y=300, width=210, height=105)

        #creacion de label
        #fecha
        
        self.fecha = date.today()
        self.fecha1=tk.Label(self.ventanaHome, text=self.fecha, font=("Verdana",16))
        self.fecha1.place(x=250, y=470, width=160, height=50)
        self.fecha1.configure(foreground="white", background="black",relief=RAISED, bd = 10)
        #hora
        self.hora1=tk.Label(self.ventanaHome, text="", font=("Verdana",16))
        self.hora1.place(x=250, y=530, width=160, height=50)
        self.hora1.configure(foreground="white", background="black", relief=RAISED, bd = 10)
        self.tiempo() 

        self.ventanaHome.mainloop()
    
    def tiempo(self):
        self.hora = tm.strftime('%H:%M:%S')
        self.hora1.config(text=self.hora, fg="white", bg="black")
        self.hora1.after(200,self.tiempo)

    def AbrirLogin(self):
        login=Ingreso(self.ventanaHome)
        
        
        

    def AbrirRegistro(self):
        registro=Registro(self.ventanaHome)
    

luxury = Luxury()
luxury.FrontHome()




     
