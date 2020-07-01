import tkinter as tk
import sqlite3 
import bcrypt
from tkinter import messagebox as mb

class Registro:

    def __init__(self,ventanaPrincipal):
        # creacion de ventana
        self.ventanaRegistro = tk.Toplevel(ventanaPrincipal)
        self.ventanaRegistro.geometry("600x330")
        self.ventanaRegistro.resizable(0, 0)
        self.ventanaRegistro.title("Registro")
        self.center(self.ventanaRegistro)
        # Ingreso de nombre
        self.nombreLabel = tk.Label(self.ventanaRegistro, text="Nombre: ")
        self.nombreLabel.grid(column=0, row=0, padx=4, pady=6)
        self.nombreLabel.configure(foreground="black")
        # Entrada de datos
        self.datoNombre = tk.StringVar()
        self.inputNombre = tk.Entry(
        self.ventanaRegistro, width=20, textvariable=self.datoNombre)
        self.inputNombre.grid(column=1, row=0)

        # Ingreso de apellido
        self.apellidoLabel = tk.Label(self.ventanaRegistro, text="Apellido: ")
        self.apellidoLabel.grid(column=0, row=1, padx=4, pady=6)
        self.apellidoLabel.configure(foreground="black")
        # Entrada de datos(Apellido)
        self.datoApellido = tk.StringVar()
        self.inputApellido = tk.Entry(
        self.ventanaRegistro, width=20, textvariable=self.datoApellido)
        self.inputApellido.grid(column=1, row=1)

        # Ingreso DNI
        self.dniLabel = tk.Label(self.ventanaRegistro, text="DNI: ")
        self.dniLabel.grid(column=0, row=2, padx=4, pady=6)
        self.dniLabel.configure(foreground="black")
        # Entrada de datos(DNI)
        self.datoDNI = tk.StringVar()
        self.inputDNI = tk.Entry(self.ventanaRegistro,
        width=20, textvariable=self.datoDNI)
        self.inputDNI.grid(column=1, row=2)

        # Ingreso telefono
        self.telefonoLabel = tk.Label(self.ventanaRegistro, text="Tel/cel: ")
        self.telefonoLabel.grid(column=0, row=3, padx=4, pady=6)
        self.telefonoLabel.configure(foreground="black")
        # Entrada de datos(Telefono)
        self.datoTelefono = tk.StringVar()
        self.inputTelefono = tk.Entry(
        self.ventanaRegistro, width=20, textvariable=self.datoTelefono)
        self.inputTelefono.grid(column=1, row=3)

        # Ingreso de nombre de usuario
        self.usuarioLabel = tk.Label(
        self.ventanaRegistro, text="Nombre de usuario: ")
        self.usuarioLabel.grid(column=0, row=4, padx=4, pady=6)
        self.usuarioLabel.configure(foreground="black")
        # Entrada de datos(nombre usuario)
        self.datoUsuario = tk.StringVar()
        self.inputUsuario = tk.Entry(
        self.ventanaRegistro, width=20, textvariable=self.datoUsuario)
        self.inputUsuario.grid(column=1, row=4)

        # Ingreso de correo
        self.correoLabel = tk.Label(self.ventanaRegistro, text="Email: ")
        self.correoLabel.grid(column=0, row=5, padx=4, pady=6)
        self.correoLabel.configure(foreground="black")
        # Entrada de datos(Correo)
        self.datoCorreo = tk.StringVar()
        self.inputCorreo = tk.Entry(
        self.ventanaRegistro, width=20, textvariable=self.datoCorreo)
        self.inputCorreo.grid(column=1, row=5)

        # Ingreso contraseña
        self.passLabel = tk.Label(self.ventanaRegistro, text="Contraseña: ")
        self.passLabel.grid(column=0, row=6, padx=4, pady=6)
        self.passLabel.configure(foreground="black")
        # entrada de datos(contraseña)
        self.datoPass = tk.StringVar()
        self.inputPass = tk.Entry(
        self.ventanaRegistro, width=20, textvariable=self.datoPass, show="*")
        self.inputPass.grid(column=1, row=6)

        # Verificar contraseña
        self.pswLabel = tk.Label(self.ventanaRegistro,text="Reingresar contraseña: ")
        self.pswLabel.grid(column=0, row=7, padx=4, pady=6)
        self.pswLabel.configure(foreground="black")
        # entrada de datos(verificar contraseña)
        self.datoPsw = tk.StringVar()
        self.inputPsw = tk.Entry(self.ventanaRegistro,
        width=20, textvariable=self.datoPsw, show="*")
        self.inputPsw.grid(column=1, row=7)

        # Label Nombre
        self.errorLabelNombre = tk.Label(self.ventanaRegistro, text=" ")
        self.errorLabelNombre.grid(column=2, row=0)
        self.errorLabelNombre.configure(foreground="red")

        # Label Apellido
        self.errorLabelApellido = tk.Label(self.ventanaRegistro, text=" ")
        self.errorLabelApellido.grid(column=2, row=1)
        self.errorLabelApellido.configure(foreground="red")

        # Label DNI
        self.errorLabelDNI = tk.Label(self.ventanaRegistro, text=" ")
        self.errorLabelDNI.grid(column=2, row=2)
        self.errorLabelDNI.configure(foreground="red")

        # Label tel/cel
        self.errorLabelTel = tk.Label(self.ventanaRegistro, text=" ")
        self.errorLabelTel.grid(column=2, row=3)
        self.errorLabelTel.configure(foreground="red")

        # Label Usuario
        self.errorLabelUsuario = tk.Label(self.ventanaRegistro, text=" ")
        self.errorLabelUsuario.grid(column=2, row=4)
        self.errorLabelUsuario.configure(foreground="red")

        # Label Correo
        self.errorLabelCorreo = tk.Label(self.ventanaRegistro, text=" ")
        self.errorLabelCorreo.grid(column=2, row=5)
        self.errorLabelCorreo.configure(foreground="red")

        # Label Contraseña
        self.errorLabelContra = tk.Label(self.ventanaRegistro, text=" ")
        self.errorLabelContra.grid(column=2, row=6)
        self.errorLabelContra.configure(foreground="red")

        # Label verificar
        self.errorLabelVerificarPsw = tk.Label(self.ventanaRegistro, text=" ")
        self.errorLabelVerificarPsw.grid(column=2, row=7)
        self.errorLabelVerificarPsw.configure(foreground="red")

        # crear botón 
        self.botonRegistro = tk.Button(self.ventanaRegistro, text="Registrarse",command=self.Registrarse, background="#5FBD94", activebackground="#6BD8A9")
        self.botonRegistro.place(x=200, y=280, width=120, height=40)

        self.botonCerrar = tk.Button(self.ventanaRegistro, text="Salir", command=self.Close_VentanaRegistro, background="#D76458", activebackground="#FF7A6C")
        self.botonCerrar.place(x=450, y=280, width=120, height=40)

        self.ventanaRegistro.mainloop()

    def Registrarse(self):
        self.nombre = self.datoNombre.get()
        self.apellido = self.datoApellido.get()
        self.dni = self.datoDNI.get()
        self.largo = len(self.dni)
        self.telCel = self.datoTelefono.get()
        self.largoTel = len(self.telCel)
        self.nomUsuario1 = self.datoUsuario.get()
        self.email = self.datoCorreo.get()
        self.contra = self.datoPass.get()
        self.largoContra = len(self.contra)
        self.verificarPsw = self.datoPsw.get()
        self.condicion = 0
        sal = bcrypt.gensalt()
        self.pass_hasheada = ""
        self.pass_verif_hasheada = ""

        # verificar nombre['text']=
        if(self.nombre.isalpha() == False):
            self.condicion = self.condicion - 1
            self.errorLabelNombre['text'] = "Nombre ingresado no válido"

        else:
            self.condicion = self.condicion + 1
            self.errorLabelNombre['text'] = " "

        # Verificar Apellido
        if(self.apellido.isalpha() == False):
            self.condicion = self.condicion - 1
            self.errorLabelApellido['text'] = "Apellido ingresado no válido"

        else:
            self.condicion = self.condicion + 1
            self.errorLabelApellido['text'] = " "

        # Verificar DNI
        if(self.dni.isdigit() == False or (self.largo > 8 or self.largo < 7)):
            self.condicion = self.condicion - 1
            self.errorLabelDNI['text'] = "DNI ingresado no válido"

        else:
            self.condicion = self.condicion + 1
            self.errorLabelDNI['text'] = " "

        # VerificarTel/Cel
        if(self.telCel.isdigit == False or self.largoTel != 10):
            self.condicion = self.condicion - 1
            self.errorLabelTel['text'] = "Teléfono ingresado no válido"

        else:
            self.condicion = self.condicion + 1
            self.errorLabelTel['text'] = " "

        # Verificar Usuario
        if(self.nomUsuario1.isalpha() == False):
            self.condicion = self.condicion - 1
            self.errorLabelUsuario['text'] = "Nombre de usuario no válido"

        else:
            self.condicion = self.condicion + 1
            self.errorLabelUsuario['text'] = " "

        # Verificar Correo electrónico
        emailValido = True
        for i in self.email:
            if(i.isalpha() and i.islower()):
                emailValido = True
            elif(i.isdigit()):
                emailValido = True
            elif(i.isalpha() == False or i.isdigit() == False):
                if(i != "@" and i != "." and i != "-" and i != "_"):
                    emailValido = False
                    break
            pass
        
        if(emailValido == False):
            self.condicion = self.condicion - 1
            self.errorLabelCorreo['text'] = "Correo ingresado no válido"
        else:
            self.condicion = self.condicion + 1
            self.errorLabelCorreo['text'] = " "
       
        # Verificar contraseña1
        if(self.contra.isalnum() == False or self.largoContra < 8 or "@" in self.contra or "." in self.contra or "_" in self.contra or
           "," in self.contra or "*" in self.contra or "/" in self.contra or "}" in self.contra or "(" in self.contra or
           ")" in self.contra or "{" in self.contra or "|" in self.contra or "!" in self.contra or "[" in self.contra or
           "=" in self.contra or " " in self.contra or "]" in self.contra or "#" in self.contra or "$" in self.contra or
           "%" in self.contra or "&" in self.contra or "|" in self.contra or "¿" in self.contra or "?" in self.contra or
           "'" in self.contra or ";" in self.contra or "<" in self.contra or ">" in self.contra or "'" in self.contra or
           "+" in self.contra or "¡" in self.contra or ":" in self.contra):
            self.condicion = self.condicion - 1
            self.errorLabelContra['text'] = "Caracteres especiales no válidos (Debe tener 8 digitos)"

        else:
            self.condicion = self.condicion + 1
            self.errorLabelContra['text'] = " "
            self.contra = self.contra.encode()
            self.verificarPsw = self.verificarPsw.encode()
            self.pass_hasheada = bcrypt.hashpw(self.contra, sal)
            self.pass_verif_hasheada = bcrypt.hashpw(self.verificarPsw, sal)
        # Verificar verificar contraseña
        
         
        if(self.pass_hasheada != self.pass_verif_hasheada):
            self.condicion = self.condicion - 1
            self.errorLabelVerificarPsw['text'] = "La contraseña no coincide"

        else:
            self.condicion = self.condicion + 1
            self.errorLabelVerificarPsw['text'] = " "

        if(self.condicion == 8):
            self.CargarEmpleado(self.nombre,self.apellido,self.dni,self.telCel,self.nomUsuario1,self.email,self.pass_hasheada)

        
    def CargarEmpleado(self,nombre,apellido,dni,telefono,usuario,correo,contraseña):
        #Conexion a la base de datos!
        try:
            conexion = sqlite3.connect('empleadosDB.db')
            print("Conexion establecida con la base de datos!")
        
        except sqlite3.OperationalError:
            print("Error de conexion.")

        cursor = conexion.cursor()
        try:
            cursor.execute("INSERT INTO empleados(nombre,apellido,dni,telefono,usuario,email,contraseña) VALUES (?,?,?,?,?,?,?)", (nombre,apellido,dni,telefono,usuario,correo,contraseña))
        except sqlite3.OperationalError:
	        print("No se pudo insertar al empleado.")
        else:
            print("Se pudo insertar al empleado " + nombre + " " + apellido + " con exito en la base de datos.")
            mb.showinfo("Registro","Se pudo insertar al empleado " + nombre + " " + apellido + " con exito en la base de datos.")
            self.Close_VentanaRegistro()

        conexion.commit()
        conexion.close()
    

    def Close_VentanaRegistro(self):
        self.ventanaRegistro.destroy()

    def center(self,win):
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))   