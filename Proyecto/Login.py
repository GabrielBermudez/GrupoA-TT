import tkinter as tk
from tkinter import ttk

class Login:
    def __init__ (self):
        #Creacion de la ventana
        self.ventanaLogin = tk.Tk()
        self.ventanaLogin.title("Login")
        self.ventanaLogin.geometry("400x300")
        #self.ventanaLogin.configure(bg='white')
        self.ventanaLogin.resizable(0,0)
        self.labelFrameLogin=ttk.LabelFrame(self.ventanaLogin, text="Login:")        
        self.labelFrameLogin.place(x=70, y=60, width=250, height=150)
       
        
        self.FrontLogin()
        self.ventanaLogin.mainloop()

    def FrontLogin(self):
         #Label Usuario
        self.labelUsuario = ttk.Label(self.labelFrameLogin, text="Usuario o Email: ")
        self.labelUsuario.grid(column=1, row=1, padx=4, pady=4)
        self.labelUsuario.configure(foreground="red")

        self.datoUsuario=tk.StringVar()
        self.inputUsuario=ttk.Entry(self.labelFrameLogin, width=15, textvariable=self.datoUsuario)
        self.inputUsuario.grid(column=2, row=1, padx=4, pady=4)
        
        #Label Pass
        self.labelPass = ttk.Label(self.labelFrameLogin, text="Password: ")
        self.labelPass.grid(column=1, row=2, padx=4, pady=4)
        self.labelPass.configure(foreground="red")

        self.datoPassword=tk.StringVar()
        self.inputPassword=ttk.Entry(self.labelFrameLogin, width=15, textvariable=self.datoPassword, show="*")
        self.inputPassword.grid(column=2, row=2, padx=4, pady=4)

        #Boton Ingresar
        self.boton1=ttk.Button(self.labelFrameLogin, text="Ingresar", command=self.LogicaLogin)
        self.boton1.grid(column=2, row=3, padx=4, pady=4)

    def LogicaLogin(self):

        self.correoInput = self.datoUsuario.get()
        self.contraseñaInput = self.datoPassword.get()

        self.conexion1=mysql.connector.connect(host="localhost", 
                                  user="root", 
                                  passwd="", 
                                  database="luxury")
        self.cursor1=self.conexion1.cursor()
        self.cursor1.execute("SELECT usuario, email, contraseña FROM empleados WHERE usuario=%s OR email=%s",(self.correoInput, self.correoInput))
        self.datos=self.cursor1.fetchone()
        
        if(self.datos and ((self.correoInput == self.datos[0] or self.correoInput == self.datos[1]) and self.contraseñaInput == self.datos[2])):
            print("Bienvenido")
        else:
            print("Datos Incorrectos")

login = Login()