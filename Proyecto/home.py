import tkinter as tk
from tkinter import ttk
from tkinter import *
import time as tm
import sys
import time
from datetime import date
from Login import *
from Registro import *
from tkinter import PhotoImage
from PIL import Image,ImageTk


class Luxury:

    def __init__(self):
        #creacion de la ventana
        self.ventanaHome = tk.Tk()
        self.ventanaHome.title("LUXURY")
        self.ventanaHome.geometry("800x600")
        self.ventanaHome.resizable(0,0)
        self.ventanaHome.configure(bg= 'black')
        self.frameTitulo=ttk.Label(self.ventanaHome, text="Luxury")
        self.frameTitulo.config(background = "black", foreground="white",font='times 38 bold italic underline')
        self.frameTitulo.place(x=330,y=10)
        self.center(self.ventanaHome)

        
        #creacion de los botones
        self.botonIngresar=tk.Button(self.ventanaHome, text="Ingresar", command= self.AbrirLogin, bg="black", fg="white", font='times 20 italic', relief= RAISED)
        self.botonIngresar.place(x=550, y=150, width=210, height=105)
        
        self.botonRegistrarse=tk.Button(self.ventanaHome, text="Registrarse", command= self.AbrirRegistro, bg="black", fg="white", font='times 20 italic', relief= RAISED)
        self.botonRegistrarse.place(x=550, y=300, width=210, height=105)

        #creacion de label
        #Imagen
        self.imagenLogo = Image.open('Image/Luxury.png')
        self.imagenLogo = self.imagenLogo.resize((350,350), Image.ANTIALIAS) # Redimension (Alto, Ancho)
        self.imagenLogo = ImageTk.PhotoImage(self.imagenLogo) 
        self.labelLogo = tk.Label(self.ventanaHome, text="", image=self.imagenLogo, bg="black")
        self.labelLogo.place(x=100,y=70)
        #fecha
        self.fecha = date.today()
        self.fecha1=tk.Label(self.ventanaHome, text=self.fecha, font='times 20 italic')
        self.fecha1.place(x=250, y=470, width=160, height=50)
        self.fecha1.configure(foreground="white", background="black",relief=RAISED, bd = 10)
        #hora
        self.hora1=tk.Label(self.ventanaHome, text="", font='times 20 italic')
        self.hora1.place(x=250, y=530, width=160, height=50)
        self.hora1.configure(foreground="white", background="black", relief=RAISED, bd = 10)
        self.tiempo() 

        self.ventanaHome.mainloop()
    
    def tiempo(self):
        self.hora = tm.strftime('%H:%M:%S')
        self.hora1.config(text=self.hora, fg="white", bg="black")
        self.hora1.after(200,self.tiempo)

    def AbrirLogin(self):
        login=Ingreso(self.ventanaHome)
        
        
        

    def AbrirRegistro(self):
        registro=Registro(self.ventanaHome)
        
  
    def center(self,win):
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))   

luxury = Luxury()





     
