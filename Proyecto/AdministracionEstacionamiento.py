import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import PhotoImage
from PIL import Image,ImageTk
from tkinter import scrolledtext as st
import sqlite3
import CrearBD
class Estacionamiento:
    
    def Inicio(self,ventanaMenuPrincipal):

        self.ventanaHome = tk.Toplevel(ventanaMenuPrincipal)
        self.ventanaHome.title("LUXURY")
        self.ventanaHome.geometry("1300x800")
        self.ventanaHome.resizable(0,0)
        self.ventanaHome.configure(bg="black")
        self.center(self.ventanaHome)
        self.frameBotones=tk.Frame(self.ventanaHome,highlightbackground="red", highlightcolor="red", highlightthickness=1, bd=0, padx=20, pady=20)
        self.frameBotones.place(x=45,y=55)
        self.frameBotones.configure(bg="black")

        self.frameDatos=tk.Frame(self.ventanaHome,highlightbackground="red", highlightcolor="red", highlightthickness=1, bd=0, padx=20, pady=20)
        self.frameDatos.config(width=550,height=655) 
        self.frameDatos.place(x=685,y=55)
        self.frameDatos.configure(bg="black")

        self.LabelTituloFrameBotones=tk.Label(self.ventanaHome,text="Estacionamiento", font=("Verdana",20),fg="red", bg="black",borderwidth=2, relief="groove")
        self.LabelTituloFrameBotones.place(x=170,y=10)

        self.LabelTituloFrameDatos=tk.Label(self.ventanaHome,text="Administracion del Estacionamiento", font=("Verdana",20),fg="red", bg="black",borderwidth=2, relief="groove")
        self.LabelTituloFrameDatos.place(x=720,y=10)

        self.imagenIconVerde = Image.open('Image/AutoVerdeIcon.png')
        self.imagenIconVerde = self.imagenIconVerde.resize((90, 80), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.imagenIconVerde = ImageTk.PhotoImage(self.imagenIconVerde)

        self.imagenIconRojo = Image.open('Image/AutoRojoIcon.png')
        self.imagenIconRojo = self.imagenIconRojo.resize((90, 80), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.imagenIconRojo = ImageTk.PhotoImage(self.imagenIconRojo)
        

        self.CrearBotones()
        
##########################################BUSCAR CLIENTE###################################################
        self.labelBuscarCliente=tk.Label(self.frameDatos,text="Buscar Cliente", fg="red", bg="black",font=("Verdana",18))
        self.labelBuscarCliente.place(x=140, y=-15)

        self.labelDni=tk.Label(self.frameDatos,text="DNI: ", fg="red",bg="black",font=("Verdana",14))
        self.labelDni.place(x=0, y=45)

        self.datoDni=tk.StringVar()
        self.inputDni=ttk.Entry(self.frameDatos, width=15, textvariable=self.datoDni)
        self.inputDni.place(x=70, y=45, width=200, height=30)   

        self.datosCliente=st.ScrolledText(self.frameDatos, width=55, height=8.5, state="disabled")
        self.datosCliente.place(x=20,y=95) 
        
        self.datoAparcamiento=tk.Label(self.frameDatos,text="", fg="black",bg="grey",font=("Verdana",14))
        self.datoAparcamiento.place(x=70, y=270, width=40, height=30)   
       

        self.botonBuscar=tk.Button(self.frameDatos,text="Buscar", bg="green", font=("Verdana",15), command=self.BuscarCliente)
        self.botonBuscar.place(x=300,y=40, width=90,height=35)

        self.botonAsignar=tk.Button(self.frameDatos,text="Asignar", bg="green", font=("Verdana",18), command=self.AsignarEspacio)
        self.botonAsignar.place(x=130,y=270, width=100,height=35)

        self.botonLimpiar=tk.Button(self.frameDatos,text="Limpiar", bg="red", font=("Verdana",18), command=self.LimpiarDatosCliente)
        self.botonLimpiar.place(x=260,y=270, width=100,height=35)

        self.botonLimpiar=tk.Button(self.frameDatos,text="Volver", bg="red", font=("Verdana",18), command=self.CerrarVentana)
        self.botonLimpiar.place(x=400,y=595, width=100,height=35)


###########################################DATOS CLIENTE####################################################
        self.labelNombre=tk.Label(self.frameDatos,text="Nombre: ", fg="red",bg="black",font=("Verdana",14))
        self.labelNombre.place(x=0, y=320)
        self.labelDatoNombre=tk.Label(self.frameDatos, text="", bg="white")
        self.labelDatoNombre.place(x=150, y=320, width=300, height=30)      

        self.labelApellido=tk.Label(self.frameDatos,text="Apellido: ", fg="red",bg="black",font=("Verdana",14))
        self.labelApellido.place(x=0, y=360)
        self.labelDatoApellido=tk.Label(self.frameDatos, text="" ,bg="white")
        self.labelDatoApellido.place(x=150, y=360, width=300, height=30)  

        self.labelDni2=tk.Label(self.frameDatos,text="DNI: ", fg="red",bg="black",font=("Verdana",14))
        self.labelDni2.place(x=0, y=400)
        self.labelDatoDni2=tk.Label(self.frameDatos, textvariable="", bg="white")
        self.labelDatoDni2.place(x=150, y=400, width=300, height=30)

        self.labelPatente=tk.Label(self.frameDatos,text="Patente: ", fg="red",bg="black",font=("Verdana",14))
        self.labelPatente.place(x=0, y=440)
        self.labelDatoPatente=tk.Label(self.frameDatos, textvariable="", bg="white")
        self.labelDatoPatente.place(x=150, y=440, width=300, height=30)  

        self.labelTelefono=tk.Label(self.frameDatos,text="Telefono: ", fg="red",bg="black",font=("Verdana",14))
        self.labelTelefono.place(x=0, y=480)
        self.labelDatoTelefono=tk.Label(self.frameDatos,textvariable="",bg="white")
        self.labelDatoTelefono.place(x=150, y=480, width=300, height=30)

        self.labelNacionalidad=tk.Label(self.frameDatos,text="Nacionalidad: ", fg="red",bg="black",font=("Verdana",14))
        self.labelNacionalidad.place(x=0, y=520)
        self.labelDatoNacionalidad=tk.Label(self.frameDatos, textvariable="")
        self.labelDatoNacionalidad.place(x=150, y=520, width=300, height=30)

        self.labelCheckOut=tk.Label(self.frameDatos,text="CheckOut: ", fg="red",bg="black",font=("Verdana",14))
        self.labelCheckOut.place(x=0, y=560)
        self.labelDatoCheckOut=tk.Label(self.frameDatos, textvariable="", bg="white")
        self.labelDatoCheckOut.place(x=150, y=560, width=300, height=30)

        
        
                
        self.MainLoop()
    
    def EnviarDatosBoton(self,habitacion,id):
        self.id=str(id+1)
        if(str(habitacion[id]['image']) == str(self.imagenIconVerde)):
            self.datoAparcamiento["text"]=""
            self.datoAparcamiento["text"]=str(id+1)
            self.datosCliente.delete(1.0,END)
            self.EscribirMensajeScrollText("")
            
        else:
            self.datosCliente.delete(1.0,END)
            self.EscribirMensajeScrollText("El espacio clickeado ya se encuentra ocupado.")
            self.DatosHabitacionOcupada()



    def MainLoop(self):
        self.ventanaHome.mainloop()

    def BuscarCliente(self):
        self.dni=self.datoDni.get()
        self.conexion= sqlite3.connect('empleadosDB.db')
        self.cursor=self.conexion.cursor()
        self.cursor.execute("SELECT * FROM clientes WHERE dni=?", (self.dni,))
        self.datos=self.cursor.fetchone()
        print(self.datos)

        if(self.datos):
            self.mensaje=("Nombre: " + self.datos[2] + "\nApellido: " + self.datos[3] + "\nDNI: " + self.datos[4]
                        + "\nTelefono: " + self.datos[5] + "\nCorreo: " + self.datos[6] + "\nDireccion: " 
                        + self.datos[7] + "\nFecha de Nacimiento: " + self.datos[8] + "\nNacionalidad: " 
                        + self.datos[9] + "\nMetodo de Pago: " + self.datos[10] + "\nEstadia: " 
                        + str(self.datos[11]) + "\nPatente: " + self.datos[12] + "\nCheckIn: " 
                        + self.datos[13] + "\nCheckOut: " + self.datos[14])
                        
           
            self.datosCliente["state"]="normal"
            self.datosCliente.delete(1.0,END)
            self.datosCliente.insert(tk.INSERT,self.mensaje)
            self.datosCliente["state"]="disabled"
        else:
            self.datosCliente["state"]="normal"
            self.datosCliente.insert(tk.INSERT,"No se encontro al cliente solicitado!")
            self.datosCliente["state"]="disabled"

    def AsignarEspacio(self):
        if(len(self.datoAparcamiento["text"])>0 ):
            self.id=int(self.datoAparcamiento["text"])
        #print(self.id)
        #print(self.habitacion[int(self.id)]['image'])
            if(str(self.habitacion[int(self.id)-1]['image']) == str(self.imagenIconVerde)):
                print("Entre")
                CrearBD.UpdateEspacioEstacionamiento(int(self.id),self.datos[0],True)
                self.habitacion[int(self.id)-1]['image'] = self.imagenIconRojo

                self.datoAparcamiento["text"]=""
                self.EscribirMensajeScrollText("Se asigno correctamente el cliente al espacio de estacionamiento.")
            else:
                print("Fallo")
            
    def LimpiarDatosCliente(self):
        self.datosCliente["state"]="normal"
        self.datosCliente.delete(1.0,END)
        self.datosCliente["state"]="disabled"
        self.datoAparcamiento["text"]=""

        self.labelDatoNombre["text"]=""
        self.labelDatoApellido["text"]=""
        self.labelDatoDni2["text"]=""
        self.labelDatoTelefono["text"]=""
        self.labelDatoNacionalidad["text"]=""
        self.labelDatoPatente["text"]=""
        self.labelDatoCheckOut["text"]=""

    def EscribirMensajeScrollText(self,mensaje):
        self.datosCliente["state"]="normal"
        self.datosCliente.delete(1.0,END)
        self.datosCliente.insert(tk.INSERT,mensaje)
        self.datosCliente["state"]="disabled"

    def CrearBotones(self):
        self.columna=3
        self.fila=6
        self.contadorNombre=0
        self.habitacion=[]
        self.ConsultarEspacios()
        self.color=""
       
        for i in range(1,self.columna+1): 
            for j in range(1,self.fila+1): 
                
                if(str(self.datosEspacios[self.contadorNombre]) == "(0,)"):
                    self.color=self.imagenIconVerde
                else:
                    self.color=self.imagenIconRojo

                self.boton=tk.Button(self.frameBotones, image=self.color, command= lambda contadorNombre=self.contadorNombre: self.EnviarDatosBoton(self.habitacion,contadorNombre))
                #self.boton.place(relx=-0.09,rely=0.01,bordermode=OUTSIDE,x=i+(90*i), y=j+(80*j), width=90, height=80)
                self.boton.grid(column=i, row=j, padx=30, pady=8)
                self.habitacion.append(self.boton)
                self.contadorNombre+=1

                self.labelFila=tk.Label(self.frameBotones,text=self.contadorNombre,fg="black", bg="yellow")
                #self.labelFila.grid(column=i-1, row=j)
                self.labelFila.place(x=(160*(i-1)), y=3+(115*(j-1)))

    def ConsultarEspacios(self):
        self.conexion= sqlite3.connect('empleadosDB.db')
        self.cursor=self.conexion.cursor()
        self.cursor.execute("SELECT ocupado FROM estacionamientos",)
        self.datosEspacios=self.cursor.fetchall()
    
    def center(self,win):
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))   

    def DatosHabitacionOcupada(self):

        self.conexion= sqlite3.connect('empleadosDB.db')
        self.cursor=self.conexion.cursor()
        self.cursor.execute("SELECT * FROM clientes, estacionamientos WHERE estacionamientos.id_Cliente == clientes.id AND estacionamientos.id=?", (self.id,))
        self.datos=self.cursor.fetchone()
        print(self.datos)
        if(self.datos):
            self.labelDatoNombre["text"]=self.datos[2]
            self.labelDatoApellido["text"]=self.datos[3]
            self.labelDatoDni2["text"]=self.datos[4]
            self.labelDatoTelefono["text"]=self.datos[5]
            self.labelDatoNacionalidad["text"]=self.datos[9]
            self.labelDatoPatente["text"]=self.datos[12]
            self.labelDatoCheckOut["text"]=self.datos[14]
    
    def CerrarVentana(self):
        self.ventanaHome.destroy()

