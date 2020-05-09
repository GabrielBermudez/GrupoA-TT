import tkinter as tk
from tkinter import ttk
from tkinter import *
import bcrypt
import sqlite3
from tkinter import messagebox as mb

class Ingreso:
       

    def __init__(self, ventanaPrincipal):
        self.auxiliar=False
          #Creacion de la ventana
        self.ventanaLogin = tk.Toplevel(ventanaPrincipal)
        self.ventanaLogin.title("Login")
        self.ventanaLogin.geometry("400x300")
        self.frameTitulo=ttk.Label(self.ventanaLogin, text="Luxury")
        #self.frameTitulo.place(x=150, y=15, width=250, height=40)
        self.frameTitulo.pack(anchor=CENTER)
        self.frameTitulo.config(foreground="black",font=("Verdana",24))
        #self.ventanaLogin.configure(bg='black')
        self.ventanaLogin.resizable(0,0)
        self.labelFrameLogin=ttk.LabelFrame(self.ventanaLogin, text="Login:")        
        self.labelFrameLogin.place(x=55, y=60, width=300, height=150)

         #Label Usuario
        self.labelUsuario = ttk.Label(self.labelFrameLogin, text="Usuario o Email: ")
        self.labelUsuario.grid(column=1, row=1, padx=4, pady=4)
        self.labelUsuario.configure(foreground="black")

        
        self.datoUsuario=tk.StringVar()
        self.inputUsuario=ttk.Entry(self.labelFrameLogin, width=15, textvariable=self.datoUsuario)
        self.inputUsuario.grid(column=2, row=1, padx=4, pady=4)
        
        
        #Label Pass
        self.labelPass = ttk.Label(self.labelFrameLogin, text="Password: ")
        self.labelPass.grid(column=1, row=2, padx=4, pady=4)
        self.labelPass.configure(foreground="black")

        self.datoPassword=tk.StringVar()     
        self.inputPassword=ttk.Entry(self.labelFrameLogin, width=15, textvariable=self.datoPassword, show="*")
        self.inputPassword.grid(column=2, row=2, padx=4, pady=4)

        #Boton Ingresar
        self.botonIngresar=tk.Button(self.labelFrameLogin, text="Ingresar", command=lambda: self.LogicaLogin(ventanaPrincipal), background="#1BFF00", activebackground="#29DC13")
        self.botonIngresar.place(x=40, y=80, width=70, height=40)

        #Boton Salir
        self.botonSalir=tk.Button(self.labelFrameLogin, text="Salir", command=self.Close_VentanaLogin, background="#FF0000", activebackground="#E91212")
        self.botonSalir.place(x=120, y=80, width=70, height=40)

        self.ventanaLogin.grab_set()
        
        self.ventanaLogin.mainloop()

    def LogicaLogin(self,ventanaPrincipal):
       
        self.correoInput = self.datoUsuario.get()
        self.contraseñaInput = self.datoPassword.get()
        self.contraseñaInput = self.contraseñaInput.encode()

        self.conexion= sqlite3.connect('empleadosDB.db')
        self.cursor=self.conexion.cursor()
        self.cursor.execute("SELECT usuario, email, contraseña FROM empleados WHERE usuario=? OR email=?",(self.correoInput, self.correoInput))
        self.datos=self.cursor.fetchone()

        if(self.datos and ((self.correoInput == self.datos[0] or self.correoInput == self.datos[1]) and bcrypt.checkpw(self.contraseñaInput, self.datos[2]))):
            mb.showinfo("Bienvenido", "Bienvenido al sistema de Administracion Hotelera Luxury")
            self.ventanaLogin.destroy()
            ventanaPrincipal.destroy()
        else:
            print("Datos Incorrectos")
    def Close_VentanaLogin(self):
        self.ventanaLogin.destroy()

#login = Ingreso()
#login.FrontLogin(" ","")