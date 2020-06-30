import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.font import Font
from tkinter import PhotoImage
from PIL import Image,ImageTk
from tkinter import scrolledtext as st

import sqlite3
#import CrearBD
class GestionHabitaciones:
    def FrontHome(self,ventana2, habEntry): 

####################################################################  creacion de la ventana  #######################################################################################
        self.ventanaHome = tk.Toplevel(ventana2) 
        self.ventanaHome.title("LUXURY")
        self.ventanaHome.geometry("1280x700")
        self.ventanaHome.resizable(0,0)
        self.ventanaHome.configure(bg= 'black')
        
###################################################################### Creacion de Frames #######################################################################################
        self.frameDatos=tk.Frame(self.ventanaHome,highlightbackground="red", highlightcolor="red", highlightthickness=1, bd=0, padx=20, pady=20)
        self.frameDatos.config(width=650,height=275) 
        self.frameDatos.place(x=600,y=85)
        self.frameDatos.configure(bg="black")
        
        self.frameDatos1=tk.Frame(self.ventanaHome,highlightbackground="red", highlightcolor="red", highlightthickness=1, bd=0, padx=20, pady=20)
        self.frameDatos1.config(width=650,height=315)#335 
        self.frameDatos1.place(x=600,y=375)
        self.frameDatos1.configure(bg="black")
        #labels

#########################################################################  Frame 1  #################################################################################################


        self.labelTitulo=tk.Label(self.frameDatos,text="INFORMACION DE LA HABITACION",background="black", foreground="white", font=('times 16 bold italic underline'))
        self.labelTitulo.place(x=120, y=-20)   

        self.labelCapacidad=tk.Label(self.frameDatos,text="Capacidad: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelCapacidad.place(x=0, y=20)
        self.labelDatoCapacidad=tk.Label(self.frameDatos, text="", background="white",font=('times 14 bold italic'))
        self.labelDatoCapacidad.place(x=140, y=22, width=370, height=20)   

        self.labelSmart=tk.Label(self.frameDatos,text="Smart TV: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelSmart.place(x=0, y=60)
        self.labelDatoSmart=tk.Label(self.frameDatos, text="", background="white",font=('times 14 bold italic'))
        self.labelDatoSmart.place(x=140, y=62, width=370, height=20) 

        self.labelWifi=tk.Label(self.frameDatos,text="WI-FI: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelWifi.place(x=0, y=100)
        self.labelDatoWifi=tk.Label(self.frameDatos, text="", background="white",font=('times 14 bold italic'))
        self.labelDatoWifi.place(x=140, y=102, width=370, height=20)   

        self.labelAC=tk.Label(self.frameDatos,text="A/C: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelAC.place(x=0, y=140)
        self.labelDatoAC=tk.Label(self.frameDatos, text="", background="white",font=('times 14 bold italic'))
        self.labelDatoAC.place(x=140, y=142, width=370, height=20)
        
        self.labelCalidad=tk.Label(self.frameDatos,text="Calidad: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelCalidad.place(x=0, y=180)
        self.labelDatoCalidad=tk.Label(self.frameDatos, text="", background="white",font=('times 14 bold italic'))
        self.labelDatoCalidad.place(x=140, y=182, width=370, height=20)
        
        self.labelPrecio=tk.Label(self.frameDatos,text="Precio: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelPrecio.place(x=0, y=220)
        self.labelDatoPrecio=tk.Label(self.frameDatos, text="", background="white", foreground="black",font=('times 14 bold italic'))
        self.labelDatoPrecio.place(x=140, y=225, width=100, height=20)         
        
#########################################################################  Frame 2  ####################################################################################################
        self.labelTitulo=tk.Label(self.frameDatos1,text="INFORMACION DEL CLIENTE",background="black", foreground="white", font=('times 16 bold italic underline'))
        self.labelTitulo.place(x=160, y=-20)
        
        self.labelNombre=tk.Label(self.frameDatos1,text="Nombre: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelNombre.place(x=0, y=20)
        self.labelDatoNombre=tk.Label(self.frameDatos1, text="", background="white",font=('times 14 bold italic'))
        self.labelDatoNombre.place(x=140, y=22, width=370, height=20)      

        self.labelApellido=tk.Label(self.frameDatos1,text="Apellido: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelApellido.place(x=0, y=60)
        self.labelDatoApellido=tk.Label(self.frameDatos1, text="", background="white",font=('times 14 bold italic'))
        self.labelDatoApellido.place(x=140, y=62, width=370, height=20)   

        self.labelDNI=tk.Label(self.frameDatos1,text="DNI: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelDNI.place(x=0, y=100)
        self.labelDatoDNI=tk.Label(self.frameDatos1, text="", background="white",font=('times 14 bold italic'))
        self.labelDatoDNI.place(x=140, y=102, width=370, height=20)
        
        self.labelTelefono=tk.Label(self.frameDatos1,text="Telefono: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelTelefono.place(x=0, y=140)
        self.labelDatoTelefono=tk.Label(self.frameDatos1, text="", background="white",font=('times 14 bold italic'))
        self.labelDatoTelefono.place(x=140, y=142, width=370, height=20)
        
        """self.labelFDP=tk.Label(self.frameDatos1,text="Forma de Pago: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelFDP.place(x=0, y=140)
        self.labelDatoFDP=tk.Label(self.frameDatos1, text="", background="white",font=('times 14 bold italic'))
        self.labelDatoFDP.place(x=140, y=142, width=370, height=20)"""
        
        self.labelEstadia=tk.Label(self.frameDatos1,text="Estadia: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelEstadia.place(x=0, y=180)
        self.labelDatoEstadia=tk.Label(self.frameDatos1, text="", background="white",font=('times 14 bold italic'))
        self.labelDatoEstadia.place(x=140, y=182, width=370, height=20)
        
        self.labelCheckin = tk.Label(self.frameDatos1,text="Check in: ",bg="black", fg= "white", font=('times 14 bold italic'))
        self.labelCheckin.place(x=0, y=222)
        self.labelDatosCheckin =tk.Label(self.frameDatos1,text=" ", bg="white",font=('times 14 bold italic'))
        self.labelDatosCheckin.place(x=140,y=222, width=370, height=20)
        
        self.labelCheckout = tk.Label(self.frameDatos1, text="Check out: ", bg="black", fg="white", font=('times 14 bold italic'))
        self.labelCheckout.place(x=0, y=262)
        self.labelDatosCheckout = tk.Label(self.frameDatos1, text=" ", bg="white",font=('times 14 bold italic'))
        self.labelDatosCheckout.place(x=140, y=262, width=370, height=20)
        

############################################################################# Labels  ##############################################################################################
        self.frameTitulo=ttk.Label(self.ventanaHome, text="Gestion de Habitaciones")
        self.frameTitulo.config(background = "black", foreground="white",font='times 28 bold italic underline')#34
        self.frameTitulo.pack(anchor=CENTER)
        self.piso1=ttk.Label(self.ventanaHome, text="Piso 1")
        self.piso1.config(background = "black", foreground="white",font='times 16 bold italic underline')
        self.piso1.place(x=95, y=75)
        self.piso2=ttk.Label(self.ventanaHome, text="Piso 2")
        self.piso2.config(background = "black", foreground="white",font='times 16 bold italic underline')
        self.piso2.place(x=275, y=75)
        self.piso3=ttk.Label(self.ventanaHome, text="Piso 3")
        self.piso3.config(background = "black", foreground="white",font='times 16 bold italic underline')
        self.piso3.place(x=455, y=75)
        
#############################################################################  Iconos  ##########################################################################################
        self.imagenIconVerde = Image.open('Image/habitacionVerde.png')
        self.imagenIconVerde = self.imagenIconVerde.resize((110, 85), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.imagenIconVerde = ImageTk.PhotoImage(self.imagenIconVerde)

        self.imagenIconRojo = Image.open('Image/habitacionRojo.png')
        self.imagenIconRojo = self.imagenIconRojo.resize((110, 85), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.imagenIconRojo = ImageTk.PhotoImage(self.imagenIconRojo)
                
#############################################################################  botones ############################################################################################
        self.botonConfirmar = tk.Button(self.frameDatos, text="Confirmar Habitacion", bg="green", font=('times 14 bold italic'),  command= lambda: self.ConfirmarDato(habEntry))
        self.botonConfirmar.place(x=300, y=225, width=200, height=20) 
        
        self.fila=6
        self.columna=3
        self.contadorNombre=0
        self.habitacion=[]
        self.ConsultarDisponibilidad()
        self.color = ""
        for j in range(self.columna): 
            for i in range(self.fila):
                
                if(str(self.datosDisponibilidad[self.contadorNombre]) == "('0',)"):
                    self.color=self.imagenIconVerde
                else:
                    self.color=self.imagenIconRojo 
                
                auxiliar=self.contadorNombre
                #self.boton=tk.Button(self.ventanaHoma, image=self.imagenIconVerde, command= lambda contadorNombre=self.contadorNombre: self.EnviarDatosBoton(self.habitacion,contadorNombre))
                self.boton=tk.Button(self.ventanaHome, image=self.color, command= lambda contadorNombre=self.contadorNombre: self.MostrarDatos(self.habitacion,contadorNombre),  bg="black", fg="white", relief=RAISED, bd = 5)
                self.boton.place(x=j+(180*j+60), y=i+(95*i+115), width=120, height=90)
                self.habitacion.append(self.boton)
                self.contadorNombre+=1
                
                self.labelFila=tk.Label(self.ventanaHome,text=self.contadorNombre,fg="white", bg="black")
                self.labelFila.place(y=(95*(i-1)+240), x=3+(185*(j-1)+210))
        self.ventanaHome.mainloop()
        
#############################################################################  metodos ##############################################################################################        
        
    def datosHabitacion(self,id):
        print("Dentro de datos habitacion")
        self.conexion= sqlite3.connect('empleadosDB.db')
        self.c=self.conexion.cursor()
        self.c.execute("SELECT * FROM habitaciones WHERE id=?",(self.valorId,))
        self.datos=self.c.fetchone()
        
        self.valorId=(id)
        #Creacion de variables
        print(self.valorId)
        self.capacidad=self.datos[2]
        self.disponibilidad = self.datos[3]
        self.precio = self.datos[4]
        self.wifi = self.datos[5]
        self.AC = self.datos[6]
        self.smart = self.datos[7]
        self.tipoHab = self.datos[8]
        #Asignacion
        self.labelDatoCapacidad["text"] = self.capacidad
        self.labelDatoSmart["text"] = self.smart
        self.labelDatoWifi["text"] = self.wifi
        self.labelDatoAC["text"] = self.AC
        self.labelDatoPrecio["text"] = self.precio
        self.labelDatoCalidad["text"] = self.tipoHab
        
    def DatosCliente(self,dni):
        print("Dentro de Datos Cliente")
        self.dni = dni
        print(dni)
        self.conexion= sqlite3.connect('empleadosDB.db')
        self.c=self.conexion.cursor()
        self.c.execute("SELECT * FROM clientes WHERE dni=?",(self.dni,))
        self.datos=self.c.fetchone()
        print(self.datos)
        #Creacion de variables
        print(self.valorId)
        self.nombre=self.datos[2]
        self.apellido = self.datos[3]
        self.DNI = self.datos[4]
        self.telefono = self.datos[5]
        self.estadia = self.datos[11]
        self.CheckIn = self.datos[13]
        self.CheckOut = self.datos[14]
        #Asignacion
        self.labelDatoNombre["text"] = self.nombre
        self.labelDatoApellido["text"] = self.apellido
        self.labelDatoDNI["text"] = self.DNI
        self.labelDatoTelefono["text"] = self.telefono
        self.labelDatoEstadia["text"] = self.estadia
        self.labelDatosCheckin["text"] = self.CheckIn
        self.labelDatosCheckout["text"] = self.CheckOut
        
  
    def ConsultarDisponibilidad(self):
        self.conexion= sqlite3.connect('empleadosDB.db')
        self.cursor=self.conexion.cursor()
        self.cursor.execute("SELECT disponibilidad FROM habitaciones",)
        self.datosDisponibilidad=self.cursor.fetchall()
        
    def MostrarDatos(self,habitacion,id):
        self.LimpiarDatos()
        self.habitacion = habitacion
        self.valorId = id+1
        #Conexion
        
        self.conexion= sqlite3.connect('empleadosDB.db')
        self.cursor=self.conexion.cursor()

        
        print(self.valorId)
        if(str(habitacion[id]['image']) == str(self.imagenIconVerde)):
             #Query 2
            self.cursor.execute("SELECT disponibilidad FROM habitaciones WHERE id=?",(self.valorId,))
            self.datosDisponibilidad=self.cursor.fetchone()
            self.disp = self.datosDisponibilidad[0] 
            self.datosHabitacion(self.valorId)
                  
            
        else:
            #Query 1
               
            self.cursor.execute("SELECT dni FROM clientes, habitaciones WHERE habitaciones.id == clientes.id_habitacion AND habitaciones.id=?",(self.valorId,))
            self.datos =self.cursor.fetchone()
            self.dni = self.datos[0]
            self.DatosCliente(self.dni) 
           

    def LimpiarDatos(self):
        self.labelDatoNombre["text"] = ""
        self.labelDatoApellido["text"] = ""
        self.labelDatoDNI["text"] = ""
        self.labelDatoTelefono["text"] = ""
        self.labelDatoEstadia["text"] = ""
        self.labelDatosCheckin["text"] = ""
        self.labelDatosCheckout["text"] = ""
        
        self.labelDatoCapacidad["text"] = ""
        self.labelDatoSmart["text"] = ""
        self.labelDatoWifi["text"] = ""
        self.labelDatoAC["text"] = ""
        self.labelDatoPrecio["text"] = ""
        self.labelDatoCalidad["text"] = ""
    
    def ConfirmarDato(self,habEntry):
        self.valor=self.valorId
        habEntry.set(self.valor)
        self.ventanaHome.destroy()
