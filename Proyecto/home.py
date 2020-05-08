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
    login = Ingreso()
    
    def FrontHome(self):
        self.datoUsua=self.login.inputUsuario
        self.datoPass=self.login.inputPassword
        #creacion de la ventana
        self.ventanaHome = tk.Tk()
        self.ventanaHome.title("LUXURY")
        self.ventanaHome.geometry("800x600")
        self.ventanaHome.resizable(0,0)
        self.frameTitulo=ttk.Label(self.ventanaHome, text="Luxury")
        self.frameTitulo.config(foreground="black",font=("Verdana",24))
        self.frameTitulo.pack(anchor=CENTER)

        #creacion de los botones(sin asignar una funcion aun)
        self.botonIngresar=tk.Button(self.ventanaHome, text="Ingresar", command= lambda:self.login.FrontLogin(self.datoUsua,self.datoPass))
        self.botonIngresar.place(x=600, y=130, width=120, height=70)
        
        self.botonRegistrarse=tk.Button(self.ventanaHome, text="Registrarse", command= lambda:Registro())
        self.botonRegistrarse.place(x=600, y=230, width=120, height=70)

        #creacion de label
        #fecha
        
        self.fecha = date.today()
        self.fecha1=tk.Label(self.ventanaHome, text=self.fecha)
        self.fecha1.place(x=300, y=410, width=120, height=50)
        self.fecha1.configure(foreground="red")
        #hora
        self.hora1=tk.Label(self.ventanaHome, text="")
        self.hora1.place(x=300, y=460, width=120, height=50)
        self.hora1.configure(foreground="red")
        self.tiempo() 

        
        self.ventanaHome.mainloop()
    
    def tiempo(self):
        self.hora = tm.strftime('%H:%M:%S')
        self.hora1.config(text=self.hora, fg="red")
        self.hora1.after(200,self.tiempo)



     
luxury = Luxury()
luxury.FrontHome()

