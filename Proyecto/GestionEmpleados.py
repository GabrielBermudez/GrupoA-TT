import tkinter as tk
from tkinter import ttk
from tkinter import *
import sqlite3
import bcrypt

class GestionEmpleados:
    
    def Inicio(self,ventanaMenuPrincipal):
################################################  creaciòn de la ventana principal  ##################################################################
        self.ventana = tk.Toplevel(ventanaMenuPrincipal)
        self.ventana.title("Gestion de Empleados")
        self.ventana.geometry("800x600")
        self.ventana.resizable(0,0)
        self.ventana.configure(bg= '#181818')
        self.center(self.ventana)
        self.frameTitulo=ttk.Label(self.ventana, text="Gestion Empleados")
        self.frameTitulo.config(background = "#181818", foreground="white",font='times 38 bold italic underline')
        self.frameTitulo.pack(anchor=CENTER)
        self.ventana.transient(ventanaMenuPrincipal)
        
        
#############################################################  Botones  ###############################################################################
        
        self.botonModificar = tk.Button(self.ventana, text="Modificar Contraseña", bg= "black", fg="white", font=('times 14 bold italic'), relief=RAISED, bd = 5, command=lambda:self.abrirModificar(self.ventana))
        self.botonModificar.place(x=260, y=150, width=270, height=90)
        
        self.botonModificar = tk.Button(self.ventana, text="Eliminar Empleado", bg= "black", fg="white", font=('times 14 bold italic'), relief=RAISED, bd = 5, command=lambda:self.abrirEliminar(self.ventana))
        self.botonModificar.place(x=260, y=300, width=270, height=90)
        
        self.botonVolver = tk.Button(self.ventana, text="Volver", bg="red", fg="white", font=('times 14 bold italic'), relief=RAISED, bd = 5, command=self.ventana.destroy)
        self.botonVolver.place(x=550, y=500, width=200, height=50)
 
        self.ventana.mainloop()  
############################################################ Creacion Ventana Modificar #########################################################################    
    def abrirModificar(self, ventana):
        self.ventanaModificar = tk.Toplevel(ventana)
        self.ventanaModificar.title("Modificar Empleado")
        self.ventanaModificar.geometry("700x500")
        self.ventanaModificar.resizable(0,0)
        self.ventanaModificar.configure(bg= '#181818')
        self.center(self.ventanaModificar)
        self.ventanaModificar.transient(ventana)
        
        self.labelTitulo=tk.Label(self.ventanaModificar,text="Modificar Contraseña",background="#181818", foreground="white",font=('times 22 bold italic underline'))
        self.labelTitulo.place(x=200, y=10)
        
        self.labelEmail=tk.Label(self.ventanaModificar,text="e-mail: ",background="#181818", foreground="white",font=('times 14 bold italic'))
        self.labelEmail.place(x=140, y=95)
        self.emailIngresado = tk.StringVar()
        self.inputEmail = tk.Entry(self.ventanaModificar, width = 41, textvariable = self.emailIngresado, bg="white", fg="black")
        self.inputEmail.place(x=220, y=100)
       
        self.labelUsuario=tk.Label(self.ventanaModificar,text="Usuario: ",background="#181818", foreground="white",font=('times 14 bold italic'))
        self.labelUsuario.place(x=130, y=150)
        self.labelDatoUsuario=tk.Label(self.ventanaModificar, text="", background="white",font=('times 14 bold italic'))
        self.labelDatoUsuario.place(x=220, y=150, width=250, height=20)
        
        self.labelContraseña=tk.Label(self.ventanaModificar,text="Contraseña: ",background="#181818", foreground="white",font=('times 14 bold italic'))
        self.labelContraseña.place(x=110, y=200)
        self.contraseñaIngresada = tk.StringVar()
        self.inputContraseña = tk.Entry(self.ventanaModificar, width = 41, textvariable = self.contraseñaIngresada, bg="white", fg="black",show="*")
        self.inputContraseña.place(x=220, y=202)
        
        self.labelConfirmacion=tk.Label(self.ventanaModificar,text="Confirmar Contraseña: ",background="#181818", foreground="white",font=('times 14 bold italic'))
        self.labelConfirmacion.place(x=20, y=250)
        self.confirmacionIngresada = tk.StringVar()
        self.inputConfirmacion = tk.Entry(self.ventanaModificar, width = 41, textvariable = self.confirmacionIngresada, bg="white", fg="black",show="*")
        self.inputConfirmacion.place(x=220, y=252)
        
        self.errorLabelPsw = tk.Label(self.ventanaModificar, text=" ", bg="#181818", fg="red", font=('times 14 italic'))
        self.errorLabelPsw.place(x=195, y=290)
        
        self.botonBuscar = tk.Button(self.ventanaModificar, text="Buscar", bg="black", fg="white", font=('times 14 bold italic'), relief=RAISED, bd = 5, command=lambda:self.buscarEmpleado())
        self.botonBuscar.place(x=520, y=85, width=100, height=50)
        
        self.botonVolver = tk.Button(self.ventanaModificar, text="Volver", bg="red", fg="white", font=('times 14 bold italic'), relief=RAISED, bd = 5, command=self.volver)
        self.botonVolver.place(x=480, y=430, width=200, height=50)
        
        self.botonConfirmar = tk.Button(self.ventanaModificar, text="Confirmar Cambio", bg="green", fg="white", font=('times 14 bold italic'), relief=RAISED, bd = 5, command=lambda:self.modificarContraseña())
        self.botonConfirmar.place(x=240, y=350, width=200, height=50)
        
    def buscarEmpleado(self):
        
        try:
            self.email = self.emailIngresado.get()
            if(self.validarCorreo()==True):
                self.conexion= sqlite3.connect('empleadosDB.db')
                self.cursor=self.conexion.cursor()
                self.cursor.execute("SELECT usuario FROM empleados WHERE email=?", (self.email,))
                self.datos=self.cursor.fetchone()
                self.usuario = self.datos[0]
                self.labelDatoUsuario["text"] = self.usuario
            else:
                self.errorLabelPsw['text'] = "El email ingresado no es válido"  
        except TypeError:
            self.errorLabelPsw['text'] = "Los campos deben contener datos validos"
    def validarCorreo(self):
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
                    if(i != "@" and i != "." and i != "-" and i != "_"):
                        emailValido = False
                        break
            pass        
        if(emailValido == False):
            return False
        else:
            return True
        
            
    def modificarContraseña(self):
        self.nuevaContraseña = self.contraseñaIngresada.get()
        self.confirmacion = self.confirmacionIngresada.get()
        self.usuario = self.labelDatoUsuario["text"]

        
        if(self.validarContraseña()):
            print("Es verdadero")
            #######################
            self.sal = bcrypt.gensalt()
            self.pass_hasheada = ""
            self.pass_verif_hasheada = ""

            self.nuevaContraseña = self.nuevaContraseña.encode()
            #self.confirmacion = self.confirmacion.encode()
            self.pass_hasheada = bcrypt.hashpw(self.nuevaContraseña, self.sal)
            #self.pass_verif_hasheada = bcrypt.hashpw(self.confirmacion, self.sal)
            #######################

            self.conexion= sqlite3.connect('empleadosDB.db')
            self.cursor=self.conexion.cursor()
            self.cursor.execute("UPDATE empleados SET contraseña=? WHERE usuario=?", (self.pass_hasheada,self.usuario,))
            self.conexion.commit()
            self.errorLabelPsw.configure(fg="green")
            self.errorLabelPsw['text']= "Se modificó la contraseña correctamente" 
  
        else:
            self.errorLabelPsw['text'] = "La contraseña ingresada no es valida"
            
    def validarContraseña(self):
        self.contraseñaValida = False
        if(len(self.nuevaContraseña)<8):
            self.contraseñaValida = False
        else:
            if(self.nuevaContraseña == self.confirmacion):
                for i in self.nuevaContraseña:
                    if(i.isalpha() and i.islower()):
                        self.contraseñaValida = True
                    elif(i.isdigit()):
                        self.contraseñaValida = True
                    elif(i.isalpha() == False or i.isdigit() == False):
                        self.contraseñaValida = False
                        break
                pass
            else:
               self.errorLabelPsw['text'] = "Las contraseñas ingresadas no coinciden"
        if(self.contraseñaValida == True):
            return True        
        else:
            return False           

        
    def volver(self):
        self.ventanaModificar.destroy()
            
    def abrirEliminar(self, ventana):
        self.ventanaEliminar = tk.Toplevel(ventana)
        self.ventanaEliminar.title("Eliminar Empleado")
        self.ventanaEliminar.geometry("700x500")
        self.ventanaEliminar.resizable(0,0)
        self.ventanaEliminar.configure(bg= '#181818')
        self.center(self.ventanaEliminar)
        self.ventanaEliminar.transient(ventana)
        
        self.labelTitulo=tk.Label(self.ventanaEliminar,text="Eliminar Empleado",background="#181818", foreground="white",font=('times 22 bold italic underline'))
        self.labelTitulo.place(x=200, y=10)
        
        self.labelUsuario=tk.Label(self.ventanaEliminar,text="Usuario: ",background="#181818", foreground="white",font=('times 14 bold italic'))
        self.labelUsuario.place(x=110, y=100)
        self.usuarioIngresado = tk.StringVar()
        self.inputUsuario = tk.Entry(self.ventanaEliminar, width = 41, textvariable = self.usuarioIngresado, bg="white", fg="black")
        self.inputUsuario.place(x=220, y=102)
        
        self.labelContraseña=tk.Label(self.ventanaEliminar,text="Contraseña: ",background="#181818", foreground="white",font=('times 14 bold italic'))
        self.labelContraseña.place(x=110, y=150)
        self.contraseñaIngresada1 = tk.StringVar()
        self.inputContraseña = tk.Entry(self.ventanaEliminar, width = 41, textvariable = self.contraseñaIngresada1, bg="white", fg="black",show="*")
        self.inputContraseña.place(x=220, y=152)
        
        self.errorLabelPsw = tk.Label(self.ventanaEliminar, text=" ", bg="#181818", fg="red", font=('times 14 italic'))
        self.errorLabelPsw.place(x=180, y=200)
        
        self.botonConfirmar = tk.Button(self.ventanaEliminar, text="Confirmar", bg="green", fg="white", font=('times 16 bold italic'), relief=RAISED, bd = 5, command=lambda:self.eliminarEmpleado())
        self.botonConfirmar.place(x=240, y=240, width=200, height=50)
        
        self.botonVolver = tk.Button(self.ventanaEliminar, text="Volver", bg="red", fg="white", font=('times 14 bold italic'), relief=RAISED, bd = 5, command=lambda:self.volverEliminar(self.ventanaEliminar))
        self.botonVolver.place(x=480, y=430, width=200, height=50)
    
    def eliminarEmpleado(self):


        #######################
     

       
        
        #######################



        try:
            self.usuario = self.usuarioIngresado.get()
            self.contraseña = self.contraseñaIngresada1.get()
            self.contraseña = self.contraseña.encode()

            self.conexion= sqlite3.connect('empleadosDB.db')
            self.cursor=self.conexion.cursor()
            self.cursor.execute("SELECT usuario, contraseña FROM empleados WHERE usuario=?",(self.usuario,))
            self.datos=self.cursor.fetchone()

            if((self.usuario == self.datos[0]) and (bcrypt.checkpw(self.contraseña, self.datos[1]))):
                self.cursor.execute("DELETE FROM empleados WHERE usuario=?", (self.usuario,))
                self.conexion.commit()
                self.errorLabelPsw.configure(fg="green")
                self.errorLabelPsw['text']="Se han removido los datos con éxito"

            else:
                self.errorLabelPsw['text'] = "El usuario o la contraseña son incorrectos"
        except TypeError:
                self.errorLabelPsw['text'] = "Los campos deben contener datos validos"
    def volverEliminar(self, ventanaEliminar):
        self.ventanaEliminar.destroy()
             
    def center(self,win):
        win.update_idletasks()
        width = win.winfo_width()
        height = win.winfo_height()
        x = (win.winfo_screenwidth() // 2) - (width // 2)
        y = (win.winfo_screenheight() // 2) - (height // 2)
        win.geometry('{}x{}+{}+{}'.format(width, height, x, y))  