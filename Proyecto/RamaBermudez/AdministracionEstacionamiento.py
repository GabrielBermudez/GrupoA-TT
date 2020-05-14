import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter import PhotoImage
from PIL import Image,ImageTk
from tkinter import scrolledtext as st

class Estacionamiento:
    
    def __init__(self):

        self.ventanaHome = tk.Tk()
        self.ventanaHome.title("LUXURY")
        self.ventanaHome.geometry("1300x800")
        self.ventanaHome.resizable(0,0)
        self.ventanaHome.configure(bg="black")

        self.frameBotones=tk.Frame(self.ventanaHome,highlightbackground="red", highlightcolor="red", highlightthickness=1, bd=0, padx=20, pady=20)
        self.frameBotones.place(x=30,y=80)
        self.frameBotones.configure(bg="black")

        self.frameDatos=tk.Frame(self.ventanaHome,highlightbackground="red", highlightcolor="red", highlightthickness=1, bd=0, padx=20, pady=20)
        self.frameDatos.config(width=550,height=750) 
        self.frameDatos.place(x=700,y=80)
        self.frameDatos.configure(bg="black")

        self.LabelTituloFrameBotones=tk.Label(self.ventanaHome,text="Estacionamiento", font=("Verdana",26),fg="red", bg="black",borderwidth=2, relief="groove")
        self.LabelTituloFrameBotones.place(x=140,y=15)

        self.LabelTituloFrameDatos=tk.Label(self.ventanaHome,text="Administracion del Estacionamiento", font=("Verdana",26),fg="red", bg="black",borderwidth=2, relief="groove")
        self.LabelTituloFrameDatos.place(x=630,y=15)

        self.imagenIconVerde = Image.open('AutoVerdeIcon.png')
        self.imagenIconVerde = self.imagenIconVerde.resize((90, 80), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.imagenIconVerde = ImageTk.PhotoImage(self.imagenIconVerde)

        self.imagenIconRojo = Image.open('AutoRojoIcon.png')
        self.imagenIconRojo = self.imagenIconRojo.resize((90, 80), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.imagenIconRojo = ImageTk.PhotoImage(self.imagenIconRojo)
        


        self.columna=3
        self.fila=6
        self.contadorNombre=0
        self.habitacion=[]
       
        for i in range(1,self.columna+1): 
            for j in range(1,self.fila+1): 

                self.boton=tk.Button(self.frameBotones, image=self.imagenIconRojo, command= lambda contadorNombre=self.contadorNombre: self.MostrarDatos(self.habitacion,contadorNombre))
                #self.boton.place(relx=-0.09,rely=0.01,bordermode=OUTSIDE,x=i+(90*i), y=j+(80*j), width=90, height=80)
                self.boton.grid(column=i, row=j, padx=30, pady=8)
                self.habitacion.append(self.boton)
                self.contadorNombre+=1

                self.labelFila=tk.Label(self.frameBotones,text=self.contadorNombre,fg="black", bg="yellow")
                #self.labelFila.grid(column=i-1, row=j)
                self.labelFila.place(x=(160*(i-1)), y=3+(115*(j-1)))

##########################################BUSCAR CLIENTE###################################################
        self.labelBuscarCliente=tk.Label(self.frameDatos,text="Buscar Cliente", fg="red", bg="black",font=("Verdana",22))
        self.labelBuscarCliente.place(x=140, y=0)

        self.labelDni=tk.Label(self.frameDatos,text="DNI: ", fg="red",bg="black",font=("Verdana",18))
        self.labelDni.place(x=0, y=60)

        self.datoDni=tk.StringVar()
        self.inputDni=ttk.Entry(self.frameDatos, width=15, textvariable=self.datoDni)
        self.inputDni.place(x=70, y=60, width=200, height=40)   

        self.datosCliente=st.ScrolledText(self.frameDatos, width=55, height=12, state="disabled")
        self.datosCliente.place(x=20,y=120) 
        
        self.botonAsignar=tk.Button(self.frameDatos,text="Asignar", bg="green", font=("Verdana",18))
        self.botonAsignar.place(x=130,y=340, width=100,height=50)

        self.botonLimpiar=tk.Button(self.frameDatos,text="Limpiar", bg="red", font=("Verdana",18))
        self.botonLimpiar.place(x=260,y=340, width=100,height=50)


###########################################DATOS CLIENTE####################################################
        self.labelNombre=tk.Label(self.frameDatos,text="Nombre: ", fg="red",bg="black",font=("Verdana",14))
        self.labelNombre.place(x=0, y=400)
        self.labelDatoNombre=tk.Label(self.frameDatos, text="", bg="white")
        self.labelDatoNombre.place(x=100, y=400, width=300, height=30)      

        self.labelApellido=tk.Label(self.frameDatos,text="Apellido: ", fg="red",bg="black",font=("Verdana",14))
        self.labelApellido.place(x=0, y=440)
        self.labelDatoApellido=tk.Label(self.frameDatos, text="" ,bg="white")
        self.labelDatoApellido.place(x=100, y=440, width=300, height=30)  

        self.labelDni2=tk.Label(self.frameDatos,text="DNI: ", fg="red",bg="black",font=("Verdana",14))
        self.labelDni2.place(x=0, y=480)
        self.labelDatoDni2=tk.Label(self.frameDatos, textvariable="", bg="white")
        self.labelDatoDni2.place(x=100, y=480, width=300, height=30)

        self.labelPatente=tk.Label(self.frameDatos,text="Patente: ", fg="red",bg="black",font=("Verdana",14))
        self.labelPatente.place(x=0, y=520)
        self.labelDatoPatente=tk.Label(self.frameDatos, textvariable="", bg="white")
        self.labelDatoPatente.place(x=100, y=520, width=300, height=30)  

        self.labelTelefono=tk.Label(self.frameDatos,text="Telefono: ", fg="red",bg="black",font=("Verdana",14))
        self.labelTelefono.place(x=0, y=560)
        self.labelDatoTelefono=tk.Label(self.frameDatos,textvariable="",bg="white")
        self.labelDatoTelefono.place(x=100, y=560, width=300, height=30)

        self.labelNacionalidad=tk.Label(self.frameDatos,text="Nacionalidad: ", fg="red",bg="black",font=("Verdana",14))
        self.labelNacionalidad.place(x=0, y=600)
        self.labelDatoNacionalidad=tk.Label(self.frameDatos, textvariable="")
        self.labelDatoNacionalidad.place(x=100, y=600, width=300, height=30)

        self.labelCheckOut=tk.Label(self.frameDatos,text="CheckOut: ", fg="red",bg="black",font=("Verdana",14))
        self.labelCheckOut.place(x=0, y=640)
        self.labelDatoCheckOut=tk.Label(self.frameDatos, textvariable="", bg="white")
        self.labelDatoCheckOut.place(x=100, y=640, width=300, height=30)

                
        self.MainLoop()
    
    def MostrarDatos(self,habitacion,id):
        print(id+1)
        if(str(habitacion[id]['image']) == str(self.imagenIconRojo)):
            habitacion[id]['image'] = self.imagenIconVerde
            
        else:
            habitacion[id]['image'] = self.imagenIconRojo
        


    def MainLoop(self):
        self.ventanaHome.mainloop()
        
estacionamiento = Estacionamiento()

