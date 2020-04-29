import tkinter as tk

class Login:
    def __init__ (self):
        #Creacion de la ventana
        self.ventanaLogin = tk.Tk()
        self.ventanaLogin.title("Login")
        
        #Label Usuario
        self.labelUsuario = tk.Label(self.ventanaLogin, text="Usuario o Email: ")
        self.labelUsuario.grid(column=0, row=0)
        self.labelUsuario.configure(foreground="red")

        self.datoUsuario=tk.StringVar()
        self.inputUsuario=tk.Entry(self.ventanaLogin, width=15, textvariable=self.datoUsuario)
        self.inputUsuario.grid(column=4, row=0)
        
        #Label Pass
        self.labelPass = tk.Label(self.ventanaLogin, text="Password: ")
        self.labelPass.grid(column=0, row=10)
        self.labelPass.configure(foreground="red")

        self.datoPassword=tk.StringVar()
        self.inputPassword=tk.Entry(self.ventanaLogin, width=15, textvariable=self.datoPassword)
        self.inputPassword.grid(column=4, row=10)

        #Boton Ingresar
        self.boton1=tk.Button(self.ventanaLogin, text="Ingresar", command=self.Logeo)
        self.boton1.grid(column=0, row=20)

        self.ventanaLogin.mainloop()



    def Logeo(self):
        self.correo="gabriel@gmail.com"
        self.usuario="Gabriel"
        self.contraseña="12345"

        self.correoInput = self.datoUsuario.get()
        self.contraseñaInput = self.datoPassword.get()

        #print(self.correoInput)
        #print(self.contraseñaInput)

        if((self.correoInput == self.correo or self.correoInput == self.usuario) and self.contraseñaInput == self.contraseña):
            print("Logeo con exito!")
        else:
            print("Datos ingresados incorrectos")

login = Login()