import tkinter as tk
from tkinter import ttk
from tkinter import *
from tkinter.font import Font
from tkinter import PhotoImage
from PIL import Image,ImageTk
from tkinter import scrolledtext as st

class GestionHabitaciones:
    def FrontHome(self):
        #creacion de la ventana
        self.ventanaHome = tk.Tk()
        self.ventanaHome.title("LUXURY")
        self.ventanaHome.geometry("1280x720")
        self.ventanaHome.resizable(0,0)
        self.ventanaHome.configure(bg= 'black')
        #Frames
        self.frameDatos=tk.Frame(self.ventanaHome,highlightbackground="red", highlightcolor="red", highlightthickness=1, bd=0, padx=20, pady=20)
        self.frameDatos.config(width=650,height=275) 
        self.frameDatos.place(x=600,y=85)
        self.frameDatos.configure(bg="black")
        
        self.frameDatos1=tk.Frame(self.ventanaHome,highlightbackground="red", highlightcolor="red", highlightthickness=1, bd=0, padx=20, pady=20)
        self.frameDatos1.config(width=650,height=335) 
        self.frameDatos1.place(x=600,y=375)
        self.frameDatos1.configure(bg="black")
        #labels
        #Labels de frames
        #Frame 1
        self.labelTitulo=tk.Label(self.frameDatos,text="INFORMACION DE LA HABITACION",background="black", foreground="white", font=('times 16 bold italic underline'))
        self.labelTitulo.place(x=120, y=-20)
        
        """self.labelPiso=tk.Label(self.frameDatos,text="Piso: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelPiso.place(x=0, y=20)
        self.labelDatoPiso=tk.Label(self.frameDatos, text="", background="white")
        self.labelDatoPiso.place(x=140, y=22, width=370, height=20)"""      

        self.labelCapacidad=tk.Label(self.frameDatos,text="Capacidad: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelCapacidad.place(x=0, y=20)
        self.labelDatoCapacidad=tk.Label(self.frameDatos, text="", background="white")
        self.labelDatoCapacidad.place(x=140, y=22, width=370, height=20)   

        self.labelDisponibilidad=tk.Label(self.frameDatos,text="Disponibilidad: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelDisponibilidad.place(x=0, y=60)
        self.labelDatoDisponibilidad=tk.Label(self.frameDatos, text="", background="white")
        self.labelDatoDisponibilidad.place(x=140, y=62, width=370, height=20) 

        self.labelWifi=tk.Label(self.frameDatos,text="WI-FI: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelWifi.place(x=0, y=100)
        self.labelDatoWifi=tk.Label(self.frameDatos, text="", background="white")
        self.labelDatoWifi.place(x=140, y=102, width=370, height=20)   

        self.labelAC=tk.Label(self.frameDatos,text="A/C: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelAC.place(x=0, y=140)
        self.labelDatoAC=tk.Label(self.frameDatos, text="", background="white")
        self.labelDatoAC.place(x=140, y=142, width=370, height=20)
        
        self.labelCalidad=tk.Label(self.frameDatos,text="Calidad: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelCalidad.place(x=0, y=180)
        self.labelDatoCalidad=tk.Label(self.frameDatos, text="", background="white")
        self.labelDatoCalidad.place(x=140, y=182, width=370, height=20)
        
        self.labelPrecio=tk.Label(self.frameDatos,text="Precio: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelPrecio.place(x=0, y=220)
        self.labelDatoPrecio=tk.Label(self.frameDatos, text="", background="white")
        self.labelDatoPrecio.place(x=140, y=225, width=100, height=20)         

        
        

        #Frame 2
        self.labelTitulo=tk.Label(self.frameDatos1,text="INFORMACION DEL CLIENTE",background="black", foreground="white", font=('times 16 bold italic underline'))
        self.labelTitulo.place(x=160, y=-20)
        
        self.labelNombre=tk.Label(self.frameDatos1,text="Nombre: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelNombre.place(x=0, y=20)
        self.labelDatoNombre=tk.Label(self.frameDatos1, text="", background="white")
        self.labelDatoNombre.place(x=140, y=22, width=370, height=20)      

        self.labelApellido=tk.Label(self.frameDatos1,text="Apellido: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelApellido.place(x=0, y=60)
        self.labelDatoApellido=tk.Label(self.frameDatos1, text="", background="white")
        self.labelDatoApellido.place(x=140, y=62, width=370, height=20)   

        self.labelDNI=tk.Label(self.frameDatos1,text="DNI: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelDNI.place(x=0, y=100)
        self.labelDatoDNI=tk.Label(self.frameDatos1, text="", background="white")
        self.labelDatoDNI.place(x=140, y=102, width=370, height=20)
        
        self.labelTelefono=tk.Label(self.frameDatos1,text="Telefono: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelTelefono.place(x=0, y=140)
        self.labelDatoTelefono=tk.Label(self.frameDatos1, text="", background="white")
        self.labelDatoTelefono.place(x=140, y=142, width=370, height=20)
        
        self.labelFDP=tk.Label(self.frameDatos1,text="Forma de Pago: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelFDP.place(x=0, y=140)
        self.labelDatoFDP=tk.Label(self.frameDatos1, text="", background="white")
        self.labelDatoFDP.place(x=140, y=142, width=370, height=20)
        
        self.labelEstadia=tk.Label(self.frameDatos1,text="Estadia: ",background="black", foreground="white",font=('times 14 bold italic'))
        self.labelEstadia.place(x=0, y=180)
        self.labelDatoEstadia=tk.Label(self.frameDatos1, text="", background="white")
        self.labelDatoEstadia.place(x=140, y=182, width=370, height=20)
        
        self.labelCheckin = tk.Label(self.frameDatos1,text="Check in: ",bg="black", fg= "white", font=('times 14 bold italic'))
        self.labelCheckin.place(x=0, y=222)
        self.labelDatosCheckin =tk.Label(self.frameDatos1,text=" ", bg="white")
        self.labelDatosCheckin.place(x=140,y=222, width=370, height=20)
        
        self.labelCheckout = tk.Label(self.frameDatos1, text="Check out: ", bg="black", fg="white", font=('times 14 bold italic'))
        self.labelCheckout.place(x=0, y=262)
        self.labelDatosCheckout = tk.Label(self.frameDatos1, text=" ", bg="white")
        self.labelDatosCheckout.place(x=140, y=262, width=370, height=20)
        #Labels
        self.frameTitulo=ttk.Label(self.ventanaHome, text="Gestion de Habitaciones")
        self.frameTitulo.config(background = "black", foreground="white",font='times 34 bold italic underline')
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
        #Iconos
        self.imagenIconVerde = Image.open('habitacionVerde.png')
        self.imagenIconVerde = self.imagenIconVerde.resize((110, 85), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.imagenIconVerde = ImageTk.PhotoImage(self.imagenIconVerde)

        self.imagenIconRojo = Image.open('habitacionRojo.png')
        self.imagenIconRojo = self.imagenIconRojo.resize((110, 85), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.imagenIconRojo = ImageTk.PhotoImage(self.imagenIconRojo)
        
        
        #botones
        self.botonRegistro = tk.Button(self.frameDatos, text="Registrar huesped", bg="white")
        self.botonRegistro.place(x=300, y=225, width=200, height=20) 
        
        self.fila=6
        self.columna=3
        self.contadorNombre=0
        self.habitacion=[]
        for j in range(self.columna): 
            for i in range(self.fila): 
                
                auxiliar=self.contadorNombre
                self.boton=tk.Button(self.ventanaHome, image=self.imagenIconVerde, command= lambda contadorNombre=self.contadorNombre: self.MostrarDatos(self.habitacion,contadorNombre),  bg="black", fg="white", relief=RAISED, bd = 5)
                self.boton.place(x=j+(180*j+60), y=i+(95*i+115), width=120, height=90)
                self.habitacion.append(self.boton)
                self.contadorNombre+=1
                
                self.labelFila=tk.Label(self.ventanaHome,text=self.contadorNombre,fg="white", bg="black")
                self.labelFila.place(y=(95*(i-1)+240), x=3+(185*(j-1)+210))
        self.ventanaHome.mainloop()
    def MostrarDatos(self,habitacion,id):
        print(id+1)
        if(str(habitacion[id]['image']) == str(self.imagenIconRojo)):
            habitacion[id]['image'] = self.imagenIconVerde
            
        else:
            habitacion[id]['image'] = self.imagenIconRojo   
    
                  
GestionHabitaciones = GestionHabitaciones()
GestionHabitaciones.FrontHome()
