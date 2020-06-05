import tkinter as tk
import sqlite3
import bcrypt
from tkinter import messagebox as mb

class RegistroHuesped:
    def __init__(self, ventanaPrincipal):
        #Creaciòn de la ventana
        self.ventanaReg = tk.Toplevel(ventanaPrincipal)
        self.ventanaReg.geometry("600x330")
        self.ventanaReg.resizable(0, 0)
        self.ventanaReg.title("Registro de Huespedes")

        #Label de nombre
        self.labelNombre = tk.Label(self.ventanaReg, text="Nombre: ")
        self.labelNombre.grid(column = 0, row = 0, padx = 4, pady = 6)
        self.labelNombre.configure(foreground = "Black")

        #Label Apellido
        self.labelApellido = tk.Label(self.ventanaReg, text = "Apellido: ")
        self.labelApellido.grid(column = )

        self.botonRegistrar = tk.Button(self.ventanaReg, text="Registrar",command=self.Registrar, background="#5FBD94", activebackground="#6BD8A9")
        self.botonRegistrar.place(x=200, y=280, width=120, height=40)

    

    def Registrar(self):



    self.ventanaReg.mainloop()