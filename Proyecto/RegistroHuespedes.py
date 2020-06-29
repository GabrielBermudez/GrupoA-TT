import tkinter as tk
from tkinter import ttk
from tkinter import *
import bcrypt
from datetime import date
from GestionHabitaciones import *


class RegistroHuesped:
    
    valorEntry = ""

    def Inicio(self,ventanaMenuPrincipal):
        
################################################  creaciòn de la ventana principal  ###############################################################
        self.ventana = tk.Toplevel(ventanaMenuPrincipal)
        self.ventana.title("Registro")
        self.ventana.geometry("800x600")
        self.ventana.resizable(0,0)
        self.center(self.ventana)
        self.ventana.transient(ventanaMenuPrincipal)
################################################  Creación de los botones  ###############################################################
        self.botonRegistro = tk.Button(self.ventana, text = "Registro de Huespedes", command=lambda: self.RegistroFront(self.ventana), background="#5FBD94", activebackground="#6BD8A9")
        self.botonRegistro.place(x=300, y=50, width=200, height=100)

        self.botonRegistro = tk.Button(self.ventana, text = "Lista de Huespedes", background="#5FBD94", activebackground="#6BD8A9")
        self.botonRegistro.place(x=300, y=175, width=200, height=100)

        self.botonRegistro = tk.Button(self.ventana, text = "Check-Out", background="#5FBD94", activebackground="#6BD8A9")
        self.botonRegistro.place(x=300, y=300, width=200, height=100)

        self.botonRegistro = tk.Button(self.ventana, text = "Salir", command=lambda: self.Salir(ventanaMenuPrincipal), background="#D76458", activebackground="#FF7A6C")
        self.botonRegistro.place(x=300, y=425, width=200, height=100)


        self.ventana.mainloop()

    def Salir(self, ventanaMenuPrincipal):
        #ventanaMenuPrincipal.deiconify()
        self.ventana.destroy()
        
#################################################  creaciòn de la ventana de registro  ###############################################################

    def RegistroFront(self, ventana):
        self.ventana2 = tk.Toplevel(ventana)
        self.ventana2.title("Check-In")
        self.ventana2.geometry("600x530")
        self.ventana2.resizable(0,0)
        self.center(self.ventana2)
        self.ventana2.transient(ventana)

##################################################  Nombre  ##############################################################################################
        self.labelNombre = tk.Label(self.ventana2, text = "Nombre: ")
        self.labelNombre.grid(column = 0, row = 0, padx = 4, pady = 6)
        self.labelNombre.configure(foreground = "Black")
        #Ingreso de datos (Nombre)
        self.nombreIngresado = tk.StringVar()
        self.inputNombre = tk.Entry(self.ventana2, width = 20, textvariable = self.nombreIngresado)
        self.inputNombre.grid(column = 1, row = 0)

##################################################  Apellido  #######################################################################################
        self.labelApellido = tk.Label(self.ventana2, text = "Apelldio: ")
        self.labelApellido.grid(column = 0, row = 1, padx = 4, pady = 6)
        self.labelApellido.configure(foreground = "Black")
        #Ingreso de datos(Apellido)
        self.apellidoIngresado = tk.StringVar()
        self.inputApellido = tk.Entry(self.ventana2, width = 20, textvariable = self.apellidoIngresado)
        self.inputApellido.grid(column = 1, row = 1)

###################################################  DNI  ##############################################################################################
        self.labelDni = tk.Label(self.ventana2, text = "DNI: ")
        self.labelDni.grid(column = 0, row = 2, padx = 4, pady = 6)
        self.labelDni.configure(foreground = "Black")
        #Ingreso de datos (DNI)
        self.dniIngresado = tk.StringVar()
        self.inputDNI = tk.Entry(self.ventana2, width = 20, textvariable = self.dniIngresado)
        self.inputDNI.grid(column = 1, row = 2)

################################################### Telefono  ##############################################################################################
        self.labelTel = tk.Label(self.ventana2, text = "Tel/Cel: ")
        self.labelTel.grid(column = 0, row = 3, padx = 4, pady = 6)
        self.labelTel.configure(foreground = "Black")
        #Ingreso de datos(Telefono)
        self.telIngresado = tk.StringVar()
        self.inputTel = tk.Entry(self.ventana2, width = 20, textvariable = self.telIngresado)
        self.inputTel.grid(column = 1, row = 3)

#####################################################  Email  #####################################################################################
        self.labelCorreo = tk.Label(self.ventana2, text = "Email: ")
        self.labelCorreo.grid(column = 0, row = 4, padx = 4, pady = 6)
        self.labelCorreo.configure(foreground = "Black")
        #Ingreso de datos (Email)
        self.correoIngresado = tk.StringVar()
        self.inputCorreo = tk.Entry(self.ventana2, width = 20, textvariable = self.correoIngresado)
        self.inputCorreo.grid(column = 1, row = 4)

#####################################################  Domicilio  #####################################################################################
        self.labelDir = tk.Label(self.ventana2, text = "Dirección: ")
        self.labelDir.grid(column = 0, row = 5, padx = 4, pady = 6)
        self.labelDir.configure(foreground = "Black")
        #Ingreso de datos (dirección)
        self.dirIngresada = tk.StringVar()
        self.inputDir = tk.Entry(self.ventana2, width = 20, textvariable = self.dirIngresada)
        self.inputDir.grid(column = 1, row = 5)

######################################################  Fecha de Nacimiento  ########################################################################
        self.labelFecha = tk.Label(self.ventana2, text = "Fecha de Nacimiento: ")
        self.labelFecha.grid(column = 0, row = 6, padx = 4, pady = 6)
        self.labelFecha.configure(foreground = "Black")
        #Ingreso de datos (fecha de nacimiento)
        self.fechaIngresada = tk.StringVar()
        self.inputFecha = tk.Entry(self.ventana2, width = 20, textvariable = self.fechaIngresada)
        #self.inputFecha.insert(0, "dd/mm/aaaa")
        #self.inputFecha.delete(0, tk.END)
        self.inputFecha.grid(column = 1, row = 6)

######################################################  Nacionalidad  ###############################################################################
        self.labelNacion = tk.Label(self.ventana2, text = "Nacionalidad: ")
        self.labelNacion.grid(column = 0, row = 7, padx = 4, pady = 6)
        self.labelNacion.configure(foreground = "Black")
        #Ingreso de datos (Nacionalidad)
        self.inputNacion = ttk.Combobox(self.ventana2, width = 19, text = "Nacionalidad", state="readonly")
        self.inputNacion["values"] = ["Afganistán", "Albania", "Alemania", "Andorra", "Angola", "Antigua y Barbuda", "Arabia Saudita", "Argelia", "Argentina",
        "Armenia", "Australia", "Austria", "Azerbaiyán", "Bahamas", "Bangladés", "Barbados", "Baréin", "Bélgica", "Belice", "Benín",
        "Bielorrusia", "Birmania", "Bolivia", "Bosnia y Herzegovina", "Botsuana", "Brasil", "Brunéi", "Bulgaria", "Burkina Faso", "Burundi", 
        "Bután", "Cabo Verde", "Camboya", "Camerún", "Canadá", "Catar", "Chad", "Chile", "China", "Chipre", "Ciudad del Vaticano", "Colombia",
        "Comoras", "Corea del Norte", "Corea del Sur", "Costa de Marfil", "Costa Rica", "Croacia", "Cuba", "Dinamarca", "Dominica", "Ecuador", 
        "Egipto", "El Salvador", "Emiratos Árabes Unidos", "Eritrea", "Eslovaquia", "Eslovenia", "España", "Estados Unidos", "Estonia", "Etiopía", 
        "Filipinas", "Finlandia", "Fiyi", "Francia", "Gabón", "Gambia", "Georgia", "Ghana", "Granada", "Grecia", "Guatemala", "Guyana", "Guinea", 
        "Guinea ecuatorial", "Guinea-Bisáu", "Haití", "Honduras", "Hungría", "India", "Indonesia", "Irak", "Irán", "Irlanda", "Islandia", "Islas Marshall", 
        "Islas Salomón", "Israel", "Italia", "Jamaica", "Japón", "Jordania", "Kazajistán", "Kenia", "Kirguistán", "Kiribati", "Kuwait", "Laos", "Lesoto"
        "Letonia", "Líbano", "Liberia", "Libia", "Liechtenstein", "Lituania", "Luxemburgo", "Macedonia del Norte", "Madagascar", "Malasia", "Malaui", 
        "Maldivas", "Malí", "Malta", "Marruecos", "Mauricio", "Mauritania", "México", "Micronesia", "Moldavia", "Mónaco", "Mongolia", "Montenegro", "Mozambique", 
        "Namibia", "Nauru", "Nepal", "Nicaragua", "Níger", "Nigeria", "Noruega", "Nueva Zelanda", "Omán", "Países Bajos", "Pakistán", "Palaos", "Panamá"
        "Papúa Nueva Guinea", "Paraguay", "Perú", "Polonia", "Portugal", "Reino Unido", "República Centroafricana", "República Checa", "República del Congo"
        "República Democrática del Congo", "República Dominicana", "Ruanda", "Rumanía", "Rusia", "Samoa", "San Cristóbal y Nieves", "San Marino", "San Vicente y las Granadinas", 
        "Santa Lucía", "Santo Tomé y Príncipe", "Senegal", "Serbia", "Seychelles", "Sierra Leona", "Singapur", "Siria", "Somalia", "Sri Lanka", "Suazilandia"
        "Sudáfrica", "Sudán", "Sudán del Sur", "Suecia", "Suiza", "Surinam", "Tailandia", "Tanzania", "Tayikistán", "Timor Oriental", "Togo", "Tonga", "Trinidad y Tobago", 
        "Túnez", "Turkmenistán", "Turquía", "Tuvalu", "Ucrania", "Uganda", "Uruguay", "Uzbekistán", "Vanuatu", "Venezuela", "Vietnam", "Yemen", "Yibuti"
        "Zambia", "Zimbabue", ]
        self.inputNacion.grid(column = 1, row = 7)
        self.inputNacion.set("Nacionalidad")
        
        #print(str(self.nacionIngresada))

#######################################################  Forma de Pago  ########################################################################################
        self.labelPago = tk.Label(self.ventana2, text = "Forma de Pago: ")
        self.labelPago.grid(column = 0, row = 8, padx = 4, pady = 6)
        self.labelPago.configure(foreground = "Black")

        #Ingreso de datos (Forma de pago)
        self.inputFDP = ttk.Combobox(self.ventana2, width = 19, text  = "Forma De Pago", state = "readonly")
        self.inputFDP["values"] = ["Efectivo","Débito","Crédito","Depósito","Transferencia","Pago Online"]
        #Si se elige otro, se tiene que cambiar el state del combobox para poder escribir la forma de pago
        #o se tiene que habilitar un textfield para poder ingresar la forma de pago manualmente
        self.inputFDP.grid(column = 1, row = 8)
        self.inputFDP.set("Forma de Pago")
           
#######################################################  Estadía  ##############################################################################################
        self.labelEstadia = tk.Label(self.ventana2, text = "Estadía: ")
        self.labelEstadia.grid(column = 0, row = 9, padx = 4, pady = 6)
        self.labelEstadia.configure(foreground = "Black")
        #Ingreso de datos (Estadía)
        self.estadiaIngresada = tk.StringVar()
        self.inputEstadia = tk.Entry(self.ventana2, width = 20, textvariable = self.estadiaIngresada)
        self.inputEstadia.grid(column = 1, row = 9)

#####################################################  Patente  ##############################################################################################
        self.labelPatente = tk.Label(self.ventana2, text = "Patente: ")
        self.labelPatente.grid(column = 0, row = 10, padx = 4, pady = 6)
        self.labelPatente.configure(foreground = "Black")
        #Ingreso de datos (Patente)
        self.patenteIngresada = tk.StringVar()
        self.inputPatente = tk.Entry(self.ventana2, width = 20, textvariable = self.patenteIngresada)
        self.inputPatente.grid(column = 1, row = 10)

######################################################  Check-In  ##############################################################################################
        self.labelChkIn = tk.Label(self.ventana2, text = "Check-In")
        self.labelChkIn.grid(column = 0, row = 11, padx = 4, pady = 6)
        self.labelChkIn.configure(foreground = "Black")
        #Ingreso de datos (Check-in)
        self.fechaDeIngreso = tk.StringVar()
        self.inputFIngreso = tk.Entry(self.ventana2, width = 20, textvariable = self.fechaDeIngreso)
        self.inputFIngreso.grid(column = 1, row = 11)

######################################################  Check-Out  ##############################################################################################
        self.labelChkOut = tk.Label(self.ventana2, text = "Check-Out")
        self.labelChkOut.grid(column = 0, row = 12, padx = 4, pady = 6)
        self.labelChkOut.configure(foreground = "Black")
        #Ingreso de datos (Check-Out)
        self.fechaDeSalida = tk.StringVar()
        self.inputFDeSalida = tk.Entry(self.ventana2, width = 20, textvariable = self.fechaDeSalida)
        self.inputFDeSalida.grid(column = 1, row = 12)

###################################################### HABITACIÓN  ##############################################################################################
        self.labelHab = tk.Label(self.ventana2, text = "Habitación asignada")
        self.labelHab.grid(column = 0, row = 13, padx = 4, pady = 6)
        self.labelHab.configure(foreground = "Black")
        #Ingreso de datos
        self.habEntry = tk.StringVar()
        self.inputHab = tk.Entry(self.ventana2, width = 20, textvariable = self.habEntry, state = "readonly")
        self.inputHab.grid(column = 1, row = 13)
        
######################################################  BOTONES VENTANA 2  ######################################################################################
        #Botones
        self.botonValidar = tk.Button(self.ventana2, text = "Check-In", command=lambda:self.logicaRegistro(), background="#5FBD94", activebackground="#6BD8A9")
        self.botonValidar.place(x = 475, y = 480, width = 80, height = 45)

        self.botonCerrar = tk.Button(self.ventana2, text = "Volver", command=lambda:self.Volver(self.ventana2), background="#D76458", activebackground="#FF7A6C")
        self.botonCerrar.place(x = 370, y = 480, width = 80, height = 45)

        self.botonVerificar = tk.Button(self.ventana2, text = "Verificar Hab.",  command=lambda:self.VerifHabitacion(), background="#C1C1C1", activebackground="#DADADA")
        self.botonVerificar.place(x = 175, y = 460, width = 120, height = 45)

##################################################  ETIQUETAS DE LOS ERRORES  ####################################################################

        #ERROR EN EL NOMBRE
        self.errorLabelNombre = tk.Label(self.ventana2, text=" ")
        self.errorLabelNombre.grid(column=2, row=0)
        self.errorLabelNombre.configure(foreground="red")

        #ERROR EN EL APELLIDO
        self.errorLabelApellido = tk.Label(self.ventana2, text = " ")
        self.errorLabelApellido.grid(column = 2, row = 1)
        self.errorLabelApellido.configure(foreground = "red")

        #ERROR EN EL DNI
        self.errorLabelDNI = tk.Label(self.ventana2, text = " ")
        self.errorLabelDNI.grid(column = 2, row = 2)
        self.errorLabelDNI.configure(foreground = "red")

        #ERROR EN EL TELÉFONO
        self.errorLabelTel = tk.Label(self.ventana2, text = " ")
        self.errorLabelTel.grid(column = 2, row = 3)
        self.errorLabelTel.configure(foreground = "red")

        #ERROR EN EL EMAIL
        self.errorLabelEmail = tk.Label(self.ventana2, text = " ")
        self.errorLabelEmail.grid(column = 2, row = 4)
        self.errorLabelEmail.configure(foreground = "red")

        #ERROR EN EL DOMICILIO
        self.errorLabelDomicilio = tk.Label(self.ventana2, text = " ")
        self.errorLabelDomicilio.grid(column = 2, row = 5)
        self.errorLabelDomicilio.configure(foreground = "red")

        #ERROR EN LA FECHA DE NACIMIENTO
        self.errorLabelFechaNac = tk.Label(self.ventana2, text = " ")
        self.errorLabelFechaNac.grid(column = 2, row = 6)
        self.errorLabelFechaNac.configure(foreground = "red")

        #ERROR EN LA NACIONALIDAD
        self.errorLabelNacionalidad = tk.Label(self.ventana2, text = " ")
        self.errorLabelNacionalidad.grid(column = 2, row = 7)
        self.errorLabelNacionalidad.configure(foreground = "red")

        #ERROR EN LA FORMA DE PAGO
        self.errorLabelFDP = tk.Label(self.ventana2, text = " ")
        self.errorLabelFDP.grid(column = 2, row = 8)
        self.errorLabelFDP.configure(foreground = "red")

        #ERROR EN LA ESTADIA
        self.errorLabelEstadia = tk.Label(self.ventana2, text = " ")
        self.errorLabelEstadia.grid(column = 2, row = 9)
        self.errorLabelEstadia.configure(foreground = "red")

        #ERROR EN LA PATENTE
        self.errorLabelPatente = tk.Label(self.ventana2, text = " ")
        self.errorLabelPatente.grid(column = 2, row = 10)
        self.errorLabelPatente.configure(foreground = "red")

        #ERROR EN LA FECHA DEL CHECK-IN
        self.errorLabelIngreso = tk.Label(self.ventana2, text = " ")
        self.errorLabelIngreso.grid(column = 2, row = 11)
        self.errorLabelIngreso.configure(foreground = "red")

        #ERROR EN LA FECHA DEL CHECK-OUT
        self.errorLabelSalida = tk.Label(self.ventana2, text = " ")
        self.errorLabelSalida.grid(column = 2, row = 12)
        self.errorLabelSalida.configure(foreground = "red")

###################################################  LÓGICA DE LA VENTANA REGISTRO  ###############################################################################
    def logicaRegistro(self):
        #Variables para realizar las validaciones
        self.condicion = 0
        self.nombre = self.nombreIngresado.get()
        self.apellido = self.apellidoIngresado.get()
        self.dni = self.dniIngresado.get()
        self.largo = len(self.dni)
        self.tel = self.telIngresado.get()
        self.cantDigitos = len(self.tel)
        self.email = self.correoIngresado.get()
        self.direccion = self.dirIngresada.get()
        self.fecha = self.fechaIngresada.get()
        self.nacionIngresada = self.inputNacion.get()
        self.fdpIngresada = self.inputFDP.get()
        self.estadia = self.estadiaIngresada.get()
        self.patente = self.patenteIngresada.get()
        self.ingreso = self.fechaDeIngreso.get()
        self.salida = self.fechaDeSalida.get()
        #['text']=

####################################################   verificar nombre  ##########################################################################
        if(self.nombre.isalpha() == False):
            self.condicion = self.condicion - 1
            self.errorLabelNombre['text'] = "Nombre ingresado no válido"
        else:
            self.condicion = self.condicion + 1
            self.errorLabelNombre['text'] = " "

####################################################  Verificar Apellido  ##########################################################################
        if(self.apellido.isalpha() == False):
            self.condicion = self.condicion - 1
            self.errorLabelApellido['text'] = "Apellido ingresado no válido"
        else:
            self.condicion = self.condicion + 1
            self.errorLabelApellido['text'] = " "

####################################################  Verificar DNI  ##########################################################################
        if(self.dni.isdigit() == False or (self.largo > 8 or self.largo < 7)):
            self.condicion = self.condicion - 1
            self.errorLabelDNI['text'] = "DNI ingresado no válido"
        else:
            self.condicion = self.condicion + 1
            self.errorLabelDNI['text'] = " "

####################################################  Verificar teléfono  ##########################################################################
        if(self.tel.isdigit() == False or (self.cantDigitos != 10)):
            self.condicion = self.condicion - 1
            self.errorLabelTel['text'] = "Teléfono ingresado no válido"
        else:
            self.condicion = self.condicion + 1
            self.errorLabelTel['text'] = " "

#####################################################  Verificar Correo  ##########################################################################
        emailValido = True
        largoEmail = len(self.email)
        if(largoEmail == 0):
            emailValido = False
        else:
            for i in self.email:
                if(i.isalpha() and i.islower()):
                    emailValido = True
                elif(i.isdigit()):
                    emailValido = True
                elif(i.isalpha() == False or i.isdigit() == False):
                    if(i != "@" and i != "." and i != "_" and i != "_"):
                        emailValido = False
                        break                
            pass
        
        if(emailValido == False):
            self.condicion = self.condicion - 1
            self.errorLabelEmail['text'] = "Correo ingresado no válido"
        else:
            self.condicion = self.condicion + 1
            self.errorLabelEmail['text'] = " "

######################################################  Verificar Domicilio  ##########################################################################
        esValido = False
        for i in self.direccion:
            if(i.isalpha()):
                esValido = True
            elif(i.isdigit):
                esValido = True
            elif(i.isalpha()== False or i.isdigit() == False):
                esValido = False
                break
            else:
                esValido = False
                break
            pass

        if(esValido == False):
            self.condicion = self.condicion - 1
            self.errorLabelDomicilio['text'] = "Domicilio ingresado no válido"
        else:
            self.condicion = self.condicion + 1
            self.errorLabelDomicilio['text'] = " "

#####################################################  Verificar Fecha Nacimiento  #####################################################################
        self.dia = 0
        self.mes = 0
        self.anio = 0
        fechaValida = True
        for i in self.fecha:
            if(i.isdigit() == False):
                if(i != "/"):
                    fechaValida = False
                    break
                else:                    
                    self.dia = self.fecha[0:2]
                    self.mes = self.fecha[3:5]
                    self.anio = self.fecha[6:10]
        
        self.enteroDia = int(self.dia)
        self.enteroMes = int(self.mes)
        self.enteroAnio = int(self.anio)
        self.fechaActual = date.today()
        self.fechaActualTupla = self.fechaActual.timetuple()
        self.anioActual = self.fechaActualTupla.tm_year
        #print(self.fechaActualTupla.tm_year)

        if(self.enteroAnio < (self.anioActual - 100) or self.enteroAnio > self.anioActual):
            fechaValida = False
        elif(self.enteroMes < 0 or self.enteroMes > 12):
            fechaValida = False
        elif(self.enteroDia <= 0 or self.enteroDia > 31):
            fechaValida = False

        if(self.enteroMes == 1 and self.enteroMes == 3 and self.enteroMes == 5 and self.enteroMes == 7 and self.enteroMes == 8
            and self.enteroMes == 10 and self.enteroMes == 12 or (self.enteroDia > 31)):
            #print("El mes ingresado no contiene esa cantidad de días 31+")
            fechaValida = False
        elif(self.enteroMes == 4 or self.enteroMes == 6 or self.enteroMes == 9 or self.enteroMes == 11 and (self.enteroDia > 30)):
            #print("El mes ingresado no contiene esa cantidad de días 30+")
            fechaValida = False
        #si el mes ingresado es febrero
        elif(self.enteroMes == 2):
            #me fijo si el año es bisiesto
            if((self.enteroAnio % 4 == 0) or ((self.enteroAnio % 100 != 0) and (self.enteroAnio % 400 == 0))):
                #si es bisiesto febrero no puede tener más de 29 días
                if(self.enteroDia > 29):
                    #print("Febrero tiene 29 dìas bisiesto")
                    fechaValida = False
            #Si el año no es bisiesto
            else:
                #febrero no puede tener más de 28 dias
                if(self.enteroDia > 28):
                    #print("Febrero tiene 28 dìas No bisiesto")
                    fechaValida = False

        if(fechaValida == False):
            self.condicion = self.condicion - 1
            self.errorLabelFechaNac['text'] = "Fecha ingresado no válida"
        else:
            self.condicion = self.condicion + 1
            self.errorLabelFechaNac['text'] = " "

######################################################  Verificar Nacionalidad  ##########################################################################
        if(self.nacionIngresada == "Nacionalidad"):
            self.condicion = self.condicion - 1
            self.errorLabelNacionalidad['text'] = "Seleccione una opción"
        else:
            self.condicion = self.condicion + 1
            self.errorLabelNacionalidad['text'] = " "

######################################################  Verificar Forma de Pago  ##########################################################################
        if(self.fdpIngresada == "Forma de Pago"):
            self.condicion = self.condicion - 1
            self.errorLabelFDP['text'] = "Seleccione una opción"
        else:
            self.condicion = self.condicion + 1
            self.errorLabelFDP['text'] = " "

#####################################################  Verificar Estadía(cant noches)  ##########################################################################
        estadiaValida = False
        for i in self.estadia:
            if(i.isalpha() == True):
                estadiaValida = True
            elif(i.isdigit()== True):
                estadiaValida = True
            else:
                estadiaValida = False
            pass

        if(estadiaValida == False):
            self.condicion = self.condicion - 1
            self.errorLabelEstadia['text'] = "Estadía ingresada no válido"
        else:
            self.condicion = self.condicion + 1
            self.errorLabelEstadia['text'] = " "

#######################################################  Verificar Patente  ##########################################################################
        patenteValida = False
        for i in self.patente:
            if(i.isalpha() == True):
                patenteValida = True
            elif(i.isdigit() == True):
                patenteValida = True
            else:
                patenteValida = False
            pass
        if(patenteValida == False):
            self.condicion = self.condicion - 1
            self.errorLabelPatente['text'] = "Patente ingresada no válida"
        else:
            self.condicion = self.condicion + 1
            self.errorLabelPatente['text'] = " "

########################################################  Verificar Fecha Ingreso  ##########################################################################
        self.diaIngreso = 0
        self.mesIngreso = 0
        self.anioIngreso = 0
        fechaIngresoValida = True
        for i in self.ingreso:
            if(i.isdigit() == False):
                if(i != "/" and i.isalpha() == True):
                    fechaIngresoValida = False
                    break
                else:
                    self.diaIngreso = self.ingreso[0:2]
                    self.mesIngreso = self.ingreso[3:5]
                    self.anioIngreso = self.ingreso[6:10]

        self.numeroDia = int(self.diaIngreso)
        self.numeroMes = int(self.mesIngreso)
        self.numeroAnio = int(self.anioIngreso)

        if(self.numeroAnio < (self.anioActual - 100) or self.numeroAnio > self.anioActual):
            fechaIngresoValida = False
        elif(self.numeroMes < 0 or self.numeroMes > 12):
            fechaIngresoValida = False
        elif(self.numeroDia <= 0 or self.numeroDia > 31):
            fechaIngresoValida = False
        
        if(self.numeroMes == 1 and self.numeroMes == 3 and self.numeroMes == 5 and self.numeroMes == 7 and self.numeroMes == 8
            and self.numeroMes == 10 and self.numeroMes == 12 or (self.numeroDia > 31)):
            fechaIngresoValida = False
        elif(self.numeroMes == 4 and self.numeroMes == 6 and self.numeroMes == 9 and self.numeroMes == 11 or (self.numeroDia > 30)):
            fechaIngresoValida = False
        elif(self.numeroMes == 2):
            if((self.numeroAnio % 4 == 0) or ((self.numeroAnio % 100 != 0) and (self.numeroAnio % 400 == 0))):
                if(self.numeroDia > 29):
                    fechaIngresoValida = False
            else:
                if(self.numeroDia > 28):
                    fechaIngresoValida = False
        
        if(fechaIngresoValida == False):
            self.condicion = self.condicion - 1
            self.errorLabelIngreso['text'] = "Fecha de ingreso no válida"
        else:
            self.condicion = self.condicion + 1
            self.errorLabelIngreso['text'] = " "

########################################################  Verificar Fecha Salida  ##########################################################################

        self.diaSalida = 0
        self.mesSalida = 0
        self.anioSalida = 0
        fechaSalidaValida = True
        print(self.salida)

        for i in self.salida:
            if(i.isdigit() == False):
                if(i != "/" and i.isalpha() == True):
                    fechaSalidaValida = False
                    break
                else:
                    self.diaSalida = self.salida[0:2]
                    self.mesSalida = self.salida[3:5]
                    self.anioSalida = self.salida[6:10]
            pass
        
        self.numDiaSalida = int(self.diaSalida)
        self.numMesSalida = int(self.mesSalida)
        self.numAnioSalida = int(self.anioSalida)
        
        if(self.numAnioSalida < (self.anioActual - 100) or self.numAnioSalida > self.anioActual):
            fechaSalidaValida = False
        elif(self.numMesSalida < 0 or self.numMesSalida > 12):
            fechaSalidaValida = False
        elif(self.numDiaSalida <= 0 or self.numDiaSalida > 31):
            fechaSalidaValida = False
        
        if(self.numMesSalida == 1 and self.numMesSalida == 3 and self.numMesSalida == 5 and self.numMesSalida == 7 and self.numMesSalida == 8
            and self.numMesSalida == 10 and self.numMesSalida == 12 or (self.numDiaSalida > 31)):
            fechaSalidaValida = False
        elif(self.numMesSalida == 4 and self.numMesSalida == 6 and self.numMesSalida == 9 and self.numMesSalida == 11 or (self.numDiaSalida > 30)):
            #Mostrar error de los operadores or y and al gabi
            fechaSalidaValida = False
        elif(self.numMesSalida == 2):
            if((self.numAnioSalida % 4 == 0) or ((self.numAnioSalida % 100 != 0) and (self.numAnioSalida % 400 == 0))):
                if(self.numDiaSalida > 29):
                    fechaSalidaValida = False
            else:
                if(self.numDiaSalida > 28):
                    fechaSalidaValida = False
        #Si el numero del mes de ingreso es mayor al numero del mes de salida no es válido
        if(self.numeroMes > self.numMesSalida):
            fechaSalidaValida = False
        #Si el año de salida es diferente al año de entrada no es válido (excepto entre diciembre y enero(CONSULTAR DUDA))
        if(self.numAnioSalida != self.numeroAnio):
            fechaSalidaValida = False
        #Si el mes es el mismo pero el dìa de ingreso es mayor al de salida tampoco es válido
        if(self.numeroMes == self.numMesSalida):
            if(self.numeroDia > self.numDiaSalida):
                fechaSalidaValida = False

        if(fechaSalidaValida == False):
            self.condicion = self.condicion - 1
            self.errorLabelSalida['text'] = "Fecha de salida no válida"
        else:
            self.condicion = self.condicion + 1
            self.errorLabelSalida['text'] = " "
##################################################  MÉTODOS  ##########################################################################################
    def VerifHabitacion(self):
        gestion2 = GestionHabitaciones()
        gestion2.FrontHome(self.ventana2, self.habEntry)


    def Volver(self, ventana2):
        self.ventana2.destroy()

#################################################  CREACION DE LA VENTANA LISTA DE HUESPEDES  ###############################################################
    def ListaHuespedes(self, ventana):
        self.ventana3 = tk.Toplevel(ventana)
        self.ventana3.title("Huéspedes")
        self.ventana3.geometry("500x450")
        self.center(self.ventana3)
        self.ventana3.resizable(0,0)

        """ NECESITO ESTABLECER UN CRITERIO DE BÚSQUEDA PARA ENTRAR A LA BASE DE DATOS Y TRAER LOS DATOS DEL CLIENTE
            TENGO PENSADO PONER UN CUADRO DE BÚSQUEDA QUE CONSULTE EL DNI A LA BASE DE DATOS Y TRAIGA TODOS LOS DATOS
            DE ESE CLIENTE, AUNQUE CREO QUE SE PODRÍA ASIGNAR UN ID AL CLIENTE CUANDO SE LE ASIGNA LA HABITACIÓN TAMBIÉN"""

        self.labelBusqueda = tk.Label(self.ventana3, text = "Búsqueda: ")
        self.labelBusqueda.grid(column = 0, row = 0, padx = 4, pady = 6)
        self.labelBusqueda.configure(foreground = "Black")
        #Ingreso del criterio de búsqueda, con el que se va a hacer la consulta a la base de datos
        self.criterioBusqueda = tk.StringVar()
        self.inputBusqueda = tk.Entry(self.ventana3, width = 30, textvariable = self.criterioBusqueda)
        self.inputBusqueda.grid(column = 1, row = 0)

        self.labelTituloMuestra = tk.Label(self.ventana3, text = "Resultados de la búsqueda")
        self.labelTituloMuestra.grid(column = 1, row = 3, padx = 4, pady = 6)
        #self.labelTituloMuestra.place(x = 175, y = 50)
        self.labelTituloMuestra.config(fg = "Black", font = ("Chilanka",16))

##################################################  Nombre  ##############################################################################################
        self.labelNombreMuestra = tk.Label(self.ventana3, text = "Nombre: ")
        self.labelNombreMuestra.grid(column = 0, row = 4, padx = 50, pady = 6)
        self.labelNombreMuestra.configure(foreground = "Black")
        #Obtención de datos, acá tiene que hacer la consulta a la base de datos, traer la info y llenar los campos
        self.nombreObtenido = tk.StringVar()
        self.muestraNombre = tk.Entry(self.ventana3, width = 30, textvariable = self.nombreObtenido, state = "readonly")
        self.muestraNombre.grid(column = 1, row = 4)

##################################################  Apellido  ##############################################################################################
        self.labelApellidoMuestra = tk.Label(self.ventana3, text = "Apellidos: ")
        self.labelApellidoMuestra.grid(column = 0, row = 5, padx = 50, pady = 6)
        self.labelApellidoMuestra.configure(foreground = "Black")
        #
        self.apellidoObtenido = tk.StringVar()
        self.muestraApellido = tk.Entry(self.ventana3, width = 30, textvariable = self.apellidoObtenido, state = "readonly")
        self.muestraApellido.grid(column = 1, row = 5)

##################################################  DNI  ##############################################################################################
        self.labelDNIMuestra = tk.Label(self.ventana3, text = "DNI: ")
        self.labelDNIMuestra.grid(column = 0, row = 6, padx = 50, pady = 6)
        self.labelDNIMuestra.configure(foreground = "Black")
        #
        self.dniObtenido = tk.StringVar()
        self.muestraDNI = tk.Entry(self.ventana3, width = 30, textvariable = self.dniObtenido, state = "readonly")
        self.muestraDNI.grid(column = 1, row = 6)

##################################################  Telefono  ##############################################################################################
        self.labelTelMuestra = tk.Label(self.ventana3, text = "Teléfono: ")
        self.labelTelMuestra.grid(column = 0, row = 7, padx = 50, pady = 6)
        self.labelTelMuestra.configure(foreground = "Black")
        #
        self.telObtenido = tk.StringVar()
        self.muestraTel = tk.Entry(self.ventana3, width = 30, textvariable = self.telObtenido, state = "readonly")
        self.muestraTel.grid(column = 1, row = 7)

##################################################  Nacionalidad  ##############################################################################################
        self.labelNacMuestra = tk.Label(self.ventana3, text = "Nacionalidad: ")
        self.labelNacMuestra.grid(column = 0, row = 8, padx = 50, pady = 6)
        self.labelNacMuestra.configure(foreground = "Black")
        #
        self.nacionalidadObtenida = tk.StringVar()
        self.muestraNacion = tk.Entry(self.ventana3, width = 30, textvariable = self.nacionalidadObtenida, state = "readonly")
        self.muestraNacion.grid(column = 1, row = 8)

##################################################  Estadia  ##############################################################################################
        self.labelMuestraEstadia = tk.Label(self.ventana3, text = "Estadía: ")
        self.labelMuestraEstadia.grid(column = 0, row = 9, padx = 50, pady = 6)
        self.labelMuestraEstadia.configure(foreground = "Black")
        #
        self.estadiaObtenida = tk.StringVar()
        self.muestraEstadia = tk.Entry(self.ventana3, width = 30, textvariable = self.estadiaObtenida, state = "readonly")
        self.muestraEstadia.grid(column = 1, row = 9)

##################################################  Check-in  ##############################################################################################
        self.labelMuestraIngreso = tk.Label(self.ventana3, text = "Check-in: ")
        self.labelMuestraIngreso.grid(column = 0, row = 10, padx = 50, pady = 6)
        self.labelMuestraIngreso.configure(foreground = "Black")
        #
        self.ingresoObtenido = tk.StringVar()
        self.muestraIngreso = tk.Entry(self.ventana3, width = 30, textvariable = self.ingresoObtenido, state = "readonly")
        self.muestraIngreso.grid(column = 1, row = 10)

##################################################  Check-out  ##############################################################################################
        self.labelMuestraSalida = tk.Label(self.ventana3, text = "Check-out: ")
        self.labelMuestraSalida.grid(column = 0, row = 11, padx = 50, pady = 6)
        self.labelMuestraSalida.configure(foreground = "Black")
        #
        self.salidaObtenida = tk.StringVar()
        self.muestraSalida = tk.Entry(self.ventana3, width = 30, textvariable = self.salidaObtenida, state = "readonly")
        self.muestraSalida.grid(column = 1, row = 11)

######################################################  BOTONES VENTANA 3  ######################################################################################

        self.botonValidar = tk.Button(self.ventana3, text = "Consultar", command=lambda: self.LogicaLista(), background="#5FBD94", activebackground="#6BD8A9")
        self.botonValidar.place(x = 275, y = 390, width = 80, height = 45)

        self.botonCerrar = tk.Button(self.ventana3, text = "Cerrar", command=lambda:self.CerrarLista(self.ventana3), background="#D76458", activebackground="#FF7A6C")
        self.botonCerrar.place(x = 175, y = 390, width = 80, height = 45)

        self.botonBuscar = tk.Button(self.ventana3, text = "Buscar", command=lambda:self.Busqueda(self.ventana3), background="#D8D8D8", activebackground="#EAEDEC")
        self.botonBuscar.grid(column = 1, row = 2, padx = 4, pady = 6)

###################################################  LÓGICA DE LA VENTANA LISTA HUESPEDES  ###############################################################################
    def LogicaLista(self):
        print("Holiiiiiii")
        print("Esto creo que no va a hacer falta")
        
    
    def Busqueda(self, ventana3):
        print("Acá es donde se hacen las consultas a la base de datos")


    def CerrarLista(self, ventana3):
        self.ventana3.destroy()




######################################################  CREACIÓN DE LA VENTANA DE CHECK OUT  ######################################################################################

    def CheckOut(self, ventana):
        self.ventana4 = tk.Toplevel(ventana)
        self.ventana4.title("Check-Out")
        self.ventana4.geometry("500x590")
        self.center(self.ventana4)
        self.ventana4.resizable(0,0)

        self.lblBusquedaOut = tk.Label(self.ventana4, text = "Búsqueda: ")
        self.lblBusquedaOut.grid(column = 0, row = 0, padx = 4, pady = 6)
        self.lblBusquedaOut.configure(foreground = "Black")
        #Ingreso del criterio de búsqueda, con el que se va a hacer la consulta a la base de datos
        self.entradaBusqueda = tk.StringVar()
        self.inputBusquedaEntrada = tk.Entry(self.ventana4, width = 30, textvariable = self.entradaBusqueda)
        self.inputBusquedaEntrada.grid(column = 1, row = 0)

        self.labelTituloMuestra = tk.Label(self.ventana4, text = "Resultados de la búsqueda")
        self.labelTituloMuestra.grid(column = 1, row = 3)
        #self.labelTituloMuestra.place(x = 175, y = 50)
        self.labelTituloMuestra.config(fg = "Black", font = ("Chilanka",16))

##################################################  Nombre  ##############################################################################################
        self.lblNombreSalida = tk.Label(self.ventana4, text = "Nombre: ")
        self.lblNombreSalida.grid(column = 0, row = 4, padx = 25, pady = 6)
        self.lblNombreSalida.configure(foreground = "Black")
        #
        self.nombreSalida = tk.StringVar()
        self.muestraNombreSalida = tk.Entry(self.ventana4, width = 30, textvariable = self.nombreSalida, state = "readonly")
        self.muestraNombreSalida.grid(column = 1, row = 4)

##################################################  Apellido  ##############################################################################################
        self.lblApellidoSalida = tk.Label(self.ventana4, text = "Apellido")
        self.lblApellidoSalida.grid(column = 0, row = 5, padx = 25, pady = 6)
        self.lblApellidoSalida.configure(foreground = "Black")
        #
        self.apellidoSalida = tk.StringVar()
        self.muestraApellidoSalida = tk.Entry(self.ventana4, width = 30, textvariable = self.apellidoSalida, state = "readonly")
        self.muestraApellidoSalida.grid(column = 1, row = 5)

##################################################  DNI  ##############################################################################################
        self.lblDniSalida = tk.Label(self.ventana4, text = "DNI: ")
        self.lblDniSalida.grid(column = 0, row = 6, padx = 25, pady = 6)
        self.lblDniSalida.configure(foreground = "Black")
        #
        self.dniSalida = tk.StringVar()
        self.muestraDNISalida = tk.Entry(self.ventana4, width = 30, textvariable = self.dniSalida, state = "readonly")
        self.muestraDNISalida.grid(column = 1, row = 6)

##################################################  Telefono  ##############################################################################################
        self.lblTelSalida = tk.Label(self.ventana4, text = "Teléfono: ")
        self.lblTelSalida.grid(column = 0, row = 7, padx = 25, pady = 6)
        self.lblTelSalida.configure(foreground = "Black")
        #
        self.telSalida = tk.StringVar()
        self.muestraTelSalida = tk.Entry(self.ventana4, width = 30, textvariable = self.telSalida, state = "readonly")
        self.muestraTelSalida.grid(column = 1, row = 7)

##################################################  Email  ##############################################################################################
        self.lblEmailSalida = tk.Label(self.ventana4, text = "Email: ")
        self.lblEmailSalida.grid(column = 0, row = 8, padx = 25, pady = 6)
        self.lblEmailSalida.configure(foreground = "Black")
        #
        self.emailSalida = tk.StringVar()
        self.muestraEmailSalida = tk.Entry(self.ventana4, width = 30, textvariable = self.emailSalida, state = "readonly")
        self.muestraEmailSalida.grid(column = 1, row = 8)

##################################################  Domicilio  ##############################################################################################
        self.lblDomicilioSalida = tk.Label(self.ventana4, text = "Domicilio: ")
        self.lblDomicilioSalida.grid(column = 0, row = 9, padx = 25, pady = 6)
        self.lblDomicilioSalida.configure(foreground = "Black")
        #
        self.dirSalida = tk.StringVar()
        self.muestraDirSalida = tk.Entry(self.ventana4, width = 30, textvariable = self.dirSalida, state = "readonly")
        self.muestraDirSalida.grid(column = 1, row = 9)

##################################################  Fecha Nacimiento  ##############################################################################################
        self.lblFechaNacSalida = tk.Label(self.ventana4, text = "Fecha de Nacimiento: ")
        self.lblFechaNacSalida.grid(column = 0, row = 10, padx = 25, pady = 6)
        self.lblFechaNacSalida.configure(foreground = "Black")
        #
        self.fechaNacSalida = tk.StringVar()
        self.muestraFechaNacSalida = tk.Entry(self.ventana4, width = 30, textvariable = self.fechaNacSalida, state = "readonly")
        self.muestraFechaNacSalida.grid(column = 1, row = 10)

##################################################  Nacionalidad  ##############################################################################################
        self.lblNacionalidadSalida = tk.Label(self.ventana4, text = "Nacionalidad: ")
        self.lblNacionalidadSalida.grid(column = 0, row = 11, padx = 25, pady = 6)
        self.lblNacionalidadSalida.configure(foreground = "Black")
        #
        self.nacionSalida = tk.StringVar()
        self.muestraNacionSalida = tk.Entry(self.ventana4, width = 30, textvariable = self.nacionSalida, state = "readonly")
        self.muestraNacionSalida.grid(column = 1, row = 11)

##################################################  Forma de Pago  ##############################################################################################
        self.lblFDPSalida = tk.Label(self.ventana4, text = "Forma de Pago: ")
        self.lblFDPSalida.grid(column = 0, row = 12, padx = 25, pady = 6)
        self.lblFDPSalida.configure(foreground = "Black")
        #
        self.formaSalida = tk.StringVar()
        self.muestraFormaSalida = tk.Entry(self.ventana4, width = 30, textvariable = self.formaSalida, state = "readonly")
        self.muestraFormaSalida.grid(column = 1, row = 12)

##################################################  Estadia  ##############################################################################################
        self.lblEstadiaSalida = tk.Label(self.ventana4, text = "Estadía: ")
        self.lblEstadiaSalida.grid(column = 0, row = 13, padx = 25, pady = 6)
        self.lblEstadiaSalida.configure(foreground = "Black")
        #
        self.estSalida = tk.StringVar()
        self.muestraEstSalida = tk.Entry(self.ventana4, width = 30, textvariable = self.estSalida, state = "readonly")
        self.muestraEstSalida.grid(column = 1, row = 13)

##################################################  Patente  ##############################################################################################
        self.lblPatenteSalida = tk.Label(self.ventana4, text = "Patente: ")
        self.lblPatenteSalida.grid(column = 0, row = 14, padx = 25, pady = 6)
        self.lblPatenteSalida.configure(foreground = "Black")
        #
        self.patSalida = tk.StringVar()
        self.muestraPatSalida = tk.Entry(self.ventana4, width = 30, textvariable = self.patSalida, state = "readonly")
        self.muestraPatSalida.grid(column = 1, row = 14)

##################################################  Chechk-in  ##############################################################################################        
        self.lblChinSalida = tk.Label(self.ventana4, text = "Check-in: ")
        self.lblChinSalida.grid(column = 0, row = 15, padx = 25, pady = 6)
        self.lblChinSalida.configure(foreground = "Black")
        #
        self.chinSalida = tk.StringVar()
        self.muestraChinSalida = tk.Entry(self.ventana4, width = 30, textvariable = self.chinSalida, state = "readonly")
        self.muestraChinSalida.grid(column = 1, row = 15)

##################################################  Check-out  ##############################################################################################
        self.lblCoutSalida = tk.Label(self.ventana4, text = "Check-out: ")
        self.lblCoutSalida.grid(column = 0, row = 16, padx = 25, pady = 6)
        self.lblCoutSalida.configure(foreground = "Black")
        #
        self.coutSalida = tk.StringVar()
        self.muestraCoutSalida = tk.Entry(self.ventana4, width = 30, textvariable = self.coutSalida, state = "readonly")
        self.muestraCoutSalida.grid(column = 1, row = 16)

##################################################  BOTONES VENTANA 4 CHK-OUT  ##############################################################################################
        self.botonValidar = tk.Button(self.ventana4, text = "Confirmar", command=lambda: self.LogicaCheckout(), background="#5FBD94", activebackground="#6BD8A9")
        self.botonValidar.place(x = 275, y = 540, width = 80, height = 45)

        self.botonCerrar = tk.Button(self.ventana4, text = "Cerrar", command=lambda:self.CerrarCheckOut(self.ventana4), background="#D76458", activebackground="#FF7A6C")
        self.botonCerrar.place(x = 175, y = 540, width = 80, height = 45)

        self.botonBusqueda = tk.Button(self.ventana4, text = "Buscar", command=lambda:self.Busqueda(self.ventana4), background="#D8D8D8", activebackground="#EAEDEC")
        self.botonBusqueda.grid(column = 1, row = 2, padx = 4, pady = 6)

###################################################  LÓGICA DE LA VENTANA CHECK-OUT  ###############################################################################
    def LogicaCheckout(self):
        print("Esto creo que no va a hacer falta x2")

    def Busqueda(self, ventana4):
        print("Acá va la conexión para dar de baja en la base de datos x2")

    def CerrarCheckOut(self, ventana4):
        self.ventana4.destroy()

    def center(self,win):
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))   