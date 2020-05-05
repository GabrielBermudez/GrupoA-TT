import tkinter as tk

class Registro:
    existeLabelNombre = False
    existeLabelApellido = False
    existeLabelDNI = False
    existeLabelTel = False
    existeLabelUsuario = False
    existeLabelEmail = False
    existeLabelContra = False
    def __init__ (self):
        #creacion de ventana
        self.ventanaRegistro = tk.Tk()
        self.ventanaRegistro.title("Registro")

        #Ingreso de nombre
        self.nombreLabel = tk.Label(self.ventanaRegistro, text="Nombre: ")
        self.nombreLabel.grid(column = 0, row = 0)
        self.nombreLabel.configure(foreground="black")
        #Entrada de datos
        self.datoNombre = tk.StringVar()
        self.inputNombre = tk.Entry(self.ventanaRegistro, width= 20, textvariable=self.datoNombre)
        self.inputNombre.grid(column = 1, row = 0)

        #Ingreso de apellido
        self.apellidoLabel = tk.Label(self.ventanaRegistro, text="Apellido: ")
        self.apellidoLabel.grid(column = 0, row = 1)
        self.apellidoLabel.configure(foreground = "black")
        #Entrada de datos(Apellido)
        self.datoApellido = tk.StringVar()
        self.inputApellido = tk.Entry(self.ventanaRegistro, width=20, textvariable= self.datoApellido)
        self.inputApellido.grid(column= 1, row = 1)

        #Ingreso DNI
        self.dniLabel = tk.Label(self.ventanaRegistro, text="DNI: ")
        self.dniLabel.grid(column = 0, row = 2)
        self.dniLabel.configure(foreground = "black")
        #Entrada de datos(DNI)
        self.datoDNI = tk.StringVar()
        self.inputDNI = tk.Entry(self.ventanaRegistro, width = 20, textvariable = self.datoDNI)
        self.inputDNI.grid(column = 1, row = 2)

        #Ingreso telefono
        self.telefonoLabel = tk.Label(self.ventanaRegistro, text= "Tel/cel: ")
        self.telefonoLabel.grid(column = 0, row = 3)
        self.telefonoLabel.configure(foreground = "black")
        #Entrada de datos(Telefono)
        self.datoTelefono = tk.StringVar()
        self.inputTelefono = tk.Entry(self.ventanaRegistro, width = 20, textvariable = self.datoTelefono)
        self.inputTelefono.grid(column = 1, row = 3)

        #Ingreso de nombre de usuario
        self.usuarioLabel = tk.Label(self.ventanaRegistro, text = "Nombre de usuario: ")
        self.usuarioLabel.grid(column = 0, row = 4)
        self.usuarioLabel.configure(foreground = "black")
        #Entrada de datos(nombre usuario)
        self.datoUsuario = tk.StringVar()
        self.inputUsuario = tk.Entry(self.ventanaRegistro, width = 20, textvariable = self.datoUsuario)
        self.inputUsuario.grid(column = 1, row = 4)

        #Ingreso de correo
        self.correoLabel = tk.Label(self.ventanaRegistro, text = "Email: ")
        self.correoLabel.grid(column = 0, row = 5)
        self.correoLabel.configure(foreground = "black")
        #Entrada de datos(Correo)
        self.datoCorreo = tk.StringVar()
        self.inputCorreo = tk.Entry(self.ventanaRegistro, width = 20, textvariable = self.datoCorreo)
        self.inputCorreo.grid(column = 1, row = 5)

        #Ingreso contraseña
        self.passLabel = tk.Label(self.ventanaRegistro, text = "Contraseña: ")
        self.passLabel.grid(column = 0, row = 6)
        self.passLabel.configure(foreground = "black")
        #entrada de datos(contraseña)
        self.datoPass = tk.StringVar()
        self.inputPass = tk.Entry(self.ventanaRegistro, width = 20, textvariable = self.datoPass)
        self.inputPass.grid(column = 1, row = 6)

        #Verificar contraseña
        self.pswLabel = tk.Label(self.ventanaRegistro, text = "Reingresar contraseña: ")
        self.pswLabel.grid(column = 0, row = 7)
        self.pswLabel.configure(foreground = "black")
        #entrada de datos(verificar contraseña)
        self.datoPsw = tk.StringVar()
        self.inputPsw = tk.Entry(self.ventanaRegistro, width = 20, textvariable = self.datoPsw)
        self.inputPsw.grid(column = 1, row = 7)

        #crear botón
        self.botonRegistro = tk.Button(self.ventanaRegistro, text="Registrarse",command=self.Registrarse)
        self.botonRegistro.grid(column = 1, row = 8)


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
        self.condicion = 0

        

        #verificar nombre
        if(self.nombre.isalpha() == False and self.existeLabelNombre != True):
            self.errorLabelNombre = tk.Label(self.ventanaRegistro, text = "Nombre no válido")
            self.errorLabelNombre.grid(column = 2, row = 0)
            self.errorLabelNombre.configure(foreground = "red")
            self.condicion = self.condicion - 1
            self.existeLabelNombre=True

        if(self.nombre.isalpha()):
            self.condicion = self.condicion + 1
            if(self.existeLabelNombre):
                self.errorLabelNombre.grid_remove()
                self.existeLabelNombre=False
        
        #Verificar Apellido
        if(self.apellido.isalpha() == False and self.existeLabelApellido != True):
            self.errorLabelApellido = tk.Label(self.ventanaRegistro, text = "Apellido no válido")
            self.errorLabelApellido.grid(column = 2, row = 1)
            self.errorLabelApellido.configure(foreground = "red")
            self.condicion = self.condicion - 1
            self.existeLabelApellido = True
        
        if(self.apellido.isalpha()):
            self.condicion = self.condicion + 1
            if(self.existeLabelApellido):
                self.errorLabelApellido.grid_remove()
                self.existeLabelApellido = False

        
        #Verificar DNI
        if(self.dni.isdigit() == False or self.largo != 8 and self.existeLabelDNI != True ):
            self.errorLabelDNI = tk.Label(self.ventanaRegistro, text = "DNI no válido")
            self.errorLabelDNI.grid(column = 2, row = 2)
            self.errorLabelDNI.configure(foreground = "red")
            self.condicion = self.condicion - 1
            self.existeLabelDNI = True
            

        if(self.dni.isdigit() and (self.largo == 8 or self.largo == 7)):
            self.condicion = self.condicion + 1
            if(self.existeLabelDNI):
                self.errorLabelDNI.grid_remove()
                self.existeLabelDNI = False

        
        #VerificarTel/Cel
        if(self.telCel.isdigit == False or self.largoTel != 10 and self.existeLabelTel != True):
            self.errorLabelTel = tk.Label(self.ventanaRegistro, text = "Teléfono no válido")
            self.errorLabelTel.grid(column = 2, row = 3)
            self.errorLabelTel.configure(foreground = "red")
            self.condicion = self.condicion - 1
            self.existeLabelTel = True
        
        if(self.telCel.isdigit() and (self.largoTel == 10)):
            self.condicion = self.condicion + 1
            if(self.existeLabelTel):
                self.errorLabelTel.grid_remove()
                self.existeLabelTel = False
        
        
        #Verificar Usuario
        if(self.nomUsuario1.isalpha() == False and self.existeLabelUsuario != True):
            self.errorLabelUsuario = tk.Label(self.ventanaRegistro, text = "Nombre de suario no válido")
            self.errorLabelUsuario.grid(column = 2, row = 4)
            self.errorLabelUsuario.configure(foreground = "red")
            self.condicion = self.condicion - 1
            self.existeLabelUsuario = True
        
        if(self.nomUsuario1.isalpha()):
            self.condicion = self.condicion + 1
            if(self.existeLabelUsuario):
                self.errorLabelUsuario.grid_remove()
                self.existeLabelUsuario = False
        

        #Verificar Correo electrónico
        if(("@" in self.email) == False or (".com" in self.email) == False or self.email.islower() == False or 
        "," in self.email or "*" in self.email or "/" in self.email or "}" in self.email or "(" in self.email or ")" in self.email or
        "{" in self.email or "|" in self.email or "!" in self.email or "[" in self.email or "=" in self.email or " " in self.email or
        "]" in self.email or "#" in self.email or "$" in self.email or "%" in self.email or "&" in self.email or "|" in self.email or
        "¿" in self.email or "?" in self.email or "'" in self.email or ";" in self.email or "<" in self.email or ">" in self.email or
        "'" in self.email or "+" in self.email or "¡" in self.email or ":" in self.email and self.existeLabelEmail != True):
            self.errorLabelCorreo = tk.Label(self.ventanaRegistro, text = "Dirección de correo no válida")
            self.errorLabelCorreo.grid(column = 2, row = 5)
            self.errorLabelCorreo.configure(foreground = "red")
            self.condicion = self.condicion - 1
            self.existeLabelEmail = True

        if(("@" in self.email) == True and (".com" in self.email) == True and self.email.islower() == True):
            self.condicion = self.condicion + 1
            if(self.existeLabelEmail):
                self.errorLabelCorreo.grid_remove()
                self.existeLabelEmail = False


        print(self.condicion)


registro = Registro()