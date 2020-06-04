import sqlite3

def conexion_sql():
    
    try:

        conexion = sqlite3.connect('empleadosDB.db')
        print("Conexion establecida con la base de datos!")
        return conexion

    except sqlite3.OperationalError:

        print("Error de conexion.")

def crear_bd(conexion):
    cursor = conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE empleados(
	            id INTEGER PRIMARY KEY  AUTOINCREMENT,
	            nombre VARCHAR (100) NOT NULL,
                apellido VARCHAR (100) NOT NULL,
                dni VARCHAR(8) NOT NULL,
                telefono VARCHAR(50) NOT NULL,
                usuario VARCHAR(100) NOT NULL,
                email VARCHAR(100) NOT NULL,
                contraseña VARCHAR (200) NOT NULL
                )''')

    except sqlite3.OperationalError:
	    print("La tabla de Empleados ya existe.")
    else:
	    print("La tabla de Empleados se ha creado correctamente.")

    conexion.close()

def InsertarUsuario(nombre, apellido, dni, telefono, usuario, email, password):
    conexion = sqlite3.connect("empleadosDB.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO empleados(nombre,apellido,dni,telefono,usuario,email,contraseña) VALUES (?,?,?,?,?,?,?)", (nombre,apellido,dni,telefono,usuario,email,password))
      
    except sqlite3.OperationalError:
	    print("No se pudo insertar al empleado.")
    else:
	    print("Se pudo insertar al empleado con exito en la base de datos.")

    conexion.commit()
    conexion.close()



def crearHabitaciones(conexion):
    cursor = conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE habitaciones(
                id INTEGER PRIMARY KEY  AUTOINCREMENT,
                id_Cliente INTEGER,
                piso VARCHAR (50) NOT NULL,
                capacidad VARCHAR (50) NOT NULL,
                disponibilidad VARCHAR(50) NOT NULL,
                precio DOUBLE NOT NULL,
                wifi VARCHAR(50) NOT NULL,
                aireAcondicionado VARCHAR(50) NOT NULL,
                smartTV VARCHAR(50) NOT NULL,
                tipoHabitacion VARCHAR (100) NOT NULL,
                FOREIGN KEY (id_cliente) REFERENCES clientes(id)
                )''')
        
    except sqlite3.OperationalError:
        print("La tabla de Habitaciones ya existe.")
    else:
        print("La tabla de Habitaciones se ha creado correctamente.")

    conexion.close()    

def crearClientes(conexion):
    cursor = conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE clientes(
                id INTEGER PRIMARY KEY  AUTOINCREMENT,
                nombre VARCHAR (50) NOT NULL,
                apellido VARCHAR (50) NOT NULL,
                dni VARCHAR(50) NOT NULL,
                telefono VARCHAR(50) NOT NULL,
                email VARCHAR(50) NOT NULL,
                domicilio VARCHAR(150) NOT NULL,
                fechaNacimiento DATE NOT NULL,
                nacionalidad VARCHAR(100) NOT NULL,
                formaDePago VARCHAR(50) NOT NULL,
                estadia INTEGER NOT NULL,
                patente VARCHAR(50) NOT NULL,
                checkIn DATETIME NOT NULL,
                checkOut DATETIME NOT NULL
                )''')
        
    except sqlite3.OperationalError:
        print("La tabla de Clientes ya existe.")
    else:
        print("La tabla de Clientes se ha creado correctamente.")

    conexion.close()  

#############################################¡¡¡¡¡¡HABITACIONES!!!!!!#######################################################
def InsertarHabitacion(id_Cliente,piso,capacidad,disponibilidad, precio,wifi,aireAcondicionado,smartTV, tipoHabitacion):
    conexion = sqlite3.connect("empleadosDB.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO habitaciones(id_Cliente,piso,capacidad,disponibilidad,precio,wifi,aireAcondicionado,smartTV, tipoHabitacion) VALUES (?,?,?,?,?,?,?,?,?)", (id_Cliente,piso,capacidad,disponibilidad,precio,wifi,aireAcondicionado,smartTV, tipoHabitacion))
        
    except sqlite3.OperationalError:
        print("No se pudo insertar la habitacion.")
    else:
        print("Se pudo insertar la habitacion con exito en la base de datos.")

    conexion.commit()
    conexion.close()
   
##########################################¡¡¡¡¡¡CLIENTES!!!!!!!##############################################################
def InsertarCliente(nombre,apellido,dni,telefono,email,domicilio,fechaNacimiento,nacionalidad,formaDePago,estadia,patente,checkIn,checkOut):
    conexion = sqlite3.connect("empleadosDB.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO clientes(nombre,apellido,dni,telefono,email,domicilio,fechaNacimiento,nacionalidad,formaDePago,estadia,patente,checkIn,checkOut) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?)", (nombre,apellido,dni,telefono,email,domicilio,fechaNacimiento,nacionalidad,formaDePago,estadia,patente,checkIn,checkOut))
        
    except sqlite3.OperationalError:
        print("No se pudo insertar el cliente.")
    else:
        print("Se pudo insertar el cliente con exito en la base de datos.")

    conexion.commit()
    conexion.close()
###############################################################################################################
#crear_bd(conexion_sql())
#InsertarUsuario("Leandro", "Mercado", "38236745","2616145345", "LeandroMercado", "leandro@gmail.com", "123123")
#InsertarUsuario("Gabriel", "Bermudez", "39237216","2616145079", "GabrielBermudez", "gabriel@gmail.com","12345")
#crearHabitaciones(conexion_sql())
#crearClientes(conexion_sql())

#piso,capacidad,disponibilidad, precio,wifi,aireAcondicionado,smartTV, tipoHabitacion


#InsertarHabitacion(1,1,"5","Si",25.50,"No","No","No", "Comun")
#InsertarHabitacion(2,2,"5","Si",25.50,"No","No","No", "Comun")
#InsertarHabitacion("null",1,"5","Si",25.50,"No","No","No", "Comun")
"""InsertarHabitacion(1,"5","Si",25.50,"No","No","No", "Comun")
InsertarHabitacion(1,"5","Si",25.50,"No","No","No", "Comun")
InsertarHabitacion(1,"5","Si",25.50,"No","No","No", "Comun")

InsertarHabitacion(2,"5","Si",25.50,"No","No","No", "Comun")
InsertarHabitacion(2,"5","Si",25.50,"No","No","No", "Comun")
InsertarHabitacion(2,"5","Si",25.50,"No","No","No", "Comun")
InsertarHabitacion(2,"5","Si",25.50,"No","No","No", "Comun")
InsertarHabitacion(2,"5","Si",25.50,"No","No","No", "Comun")
InsertarHabitacion(2,"5","Si",25.50,"No","No","No", "Comun")

InsertarHabitacion(3,"5","Si",25.50,"No","No","No", "Comun")
InsertarHabitacion(3,"5","Si",25.50,"No","No","No", "Comun")
InsertarHabitacion(3,"5","Si",25.50,"No","No","No", "Comun")
InsertarHabitacion(3,"5","Si",25.50,"No","No","No", "Comun")
InsertarHabitacion(3,"5","Si",25.50,"No","No","No", "Comun")
InsertarHabitacion(3,"5","Si",25.50,"No","No","No", "Comun")




#InsertarHabitacion(2,capacidad,disponibilidad, precio,wifi,aireAcondicionado,smartTV, tipoHabitacion)



#InsertarHabitacion(3,capacidad,disponibilidad, precio,wifi,aireAcondicionado,smartTV, tipoHabitacion)

"""


#InsertarCliente("Leandra","Malandra","50457890","261666999","leandra@malandra.com","Av Las Putas 666", "1945-06-15","Putona","Con el culo",10,"No tiene, es pobre","2020-06-01 21:07:30","2020-06-05 20:15:7")
InsertarCliente("Ramiro","Gonzales","38234765","2614578923","ramiro@malandra.com","Lujan de Cuyo", "1994-06-15","Argentina","Tarjeta Credito",7,"UHM365","2020-06-11 21:07:30","2020-06-18 20:15:7")
InsertarCliente("Gabriel","Bermudez","39237216","2614269628","gabriel@malandra.com","Niñas de Ayohuma 1395", "1995-10-06","Argentina","Efectivo",5,"ARK246","2020-06-10 21:07:30","2020-06-15 20:15:07")
#SELECT * FROM habitaciones, clientes WHERE clientes.id == habitaciones.id_Cliente;