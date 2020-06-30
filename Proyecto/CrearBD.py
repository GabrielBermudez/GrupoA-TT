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
                piso VARCHAR (50) NOT NULL,
                capacidad VARCHAR (50) NOT NULL,
                disponibilidad VARCHAR(50) NOT NULL,
                precio DOUBLE NOT NULL,
                wifi VARCHAR(50) NOT NULL,
                aireAcondicionado VARCHAR(50) NOT NULL,
                smartTV VARCHAR(50) NOT NULL,
                tipoHabitacion VARCHAR (100) NOT NULL
                )''')
        
    except sqlite3.OperationalError:
        print("La tabla de Habitaciones ya existe.")
    else:
        print("La tabla de Habitaciones se ha creado correctamente.")

    conexion.close()    
#############################CREAR CLIENTES ############################################
def crearClientes(conexion):
    cursor = conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE clientes(
                id INTEGER PRIMARY KEY  AUTOINCREMENT,
                id_habitacion Integer,
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
                checkOut DATETIME NOT NULL,
                FOREIGN KEY (id_habitacion) REFERENCES habitacion(id)
                )''')
        
    except sqlite3.OperationalError:
        print("La tabla de Clientes ya existe.")
    else:
        print("La tabla de Clientes se ha creado correctamente.")

    conexion.close()  

#############################################  HABITACIONES  #############################################################
def InsertarHabitacion(piso,capacidad,disponibilidad, precio,wifi,aireAcondicionado,smartTV, tipoHabitacion):
    conexion = sqlite3.connect("empleadosDB.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO habitaciones(piso,capacidad,disponibilidad,precio,wifi,aireAcondicionado,smartTV, tipoHabitacion) VALUES (?,?,?,?,?,?,?,?)", (piso,capacidad,disponibilidad,precio,wifi,aireAcondicionado,smartTV, tipoHabitacion))
        
    except sqlite3.OperationalError:
        print("No se pudo insertar la habitacion.")
    else:
        print("Se pudo insertar la habitacion con exito en la base de datos.")

    conexion.commit()
    conexion.close()
   
##########################################¡¡¡¡¡¡CLIENTES!!!!!!!##############################################################
def InsertarCliente(id_habitacion,nombre,apellido,dni,telefono,email,domicilio,fechaNacimiento,nacionalidad,formaDePago,estadia,patente,checkIn,checkOut):
    conexion = sqlite3.connect("empleadosDB.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO clientes(id_habitacion,nombre,apellido,dni,telefono,email,domicilio,fechaNacimiento,nacionalidad,formaDePago,estadia,patente,checkIn,checkOut) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?)", (id_habitacion,nombre,apellido,dni,telefono,email,domicilio,fechaNacimiento,nacionalidad,formaDePago,estadia,patente,checkIn,checkOut))
        
    except sqlite3.OperationalError:
        print("No se pudo insertar el cliente.")
    else:
        print("Se pudo insertar el cliente con exito en la base de datos.")

    conexion.commit()
    conexion.close()
###########################CREAR TABLA ESTACIONAMIENTO##################################################
def CrearEstacionamiento(conexion):
    cursor = conexion.cursor()

    try:
        cursor.execute('''CREATE TABLE estacionamientos(
                id INTEGER PRIMARY KEY  AUTOINCREMENT,
                id_Cliente INTEGER,
                ocupado BOOLEAN NOT NULL,
                FOREIGN KEY (id_Cliente) REFERENCES clientes(id)
                )''')
        
    except sqlite3.OperationalError:
        print("La tabla de Estacionamientos ya existe.")
    else:
        print("La tabla de Estacionamientos se ha creado correctamente.")

    conexion.close()  

def InsertarEspacioEstacionamiento(id_cliente,ocupado):
    conexion = sqlite3.connect("empleadosDB.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("INSERT INTO estacionamientos(id_cliente,ocupado) VALUES (?,?)", (id_cliente,ocupado))
    except sqlite3.OperationalError:
        print("No se pudo insertar el espacio de estacionamiento.")
    else:
        print("Se pudo insertar el espacio de estacionamiento con exito en la base de datos.")    
    

    conexion.commit()
    conexion.close()


def UpdateEspacioEstacionamiento(espacio,id_cliente,ocupado):
    conexion = sqlite3.connect("empleadosDB.db")
    cursor = conexion.cursor()
    try:
        cursor.execute("UPDATE estacionamientos SET id_cliente = ?, ocupado=? WHERE id = ?", (id_cliente,ocupado,espacio))
    except sqlite3.OperationalError:
        print("No se pudo actualizar el espacio de estacionamiento.")
    else:
        print("Se pudo actualizar el espacio de estacionamiento con exito en la base de datos.") 
    conexion.commit()
    conexion.close()

############################################################################################################

#crear_bd(conexion_sql())
#InsertarUsuario("Leandro", "Mercado", "38236745","2616145345", "LeandroMercado", "leandro@gmail.com", "123123")
#InsertarUsuario("Gabriel", "Bermudez", "39237216","2616145079", "GabrielBermudez", "gabriel@gmail.com","12345")
#crearHabitaciones(conexion_sql())
#crearClientes(conexion_sql())

#piso,capacidad,disponibilidad, precio,wifi,aireAcondicionado,smartTV, tipoHabitacion

#dni_Cliente,piso,capacidad,disponibilidad, precio,wifi,aireAcondicionado,smartTV, tipoHabitacion
#InsertarHabitacion(39237216,1,"5","Si",25.50,"No","No","No", "Comun")

"""InsertarHabitacion(1,"2","0",18.99,"No","No","No", "Comun")
InsertarHabitacion(1,"2","0",18.99,"No","No","No", "Comun")
InsertarHabitacion(1,"2","0",20.00,"si","No","No", "Comun")
InsertarHabitacion(1,"4","0",22.50,"No","No","No", "Comun")
InsertarHabitacion(1,"4","0",25.50,"si","No","No", "Comun")
InsertarHabitacion(1,"6","0",33.99,"si","No","No", "Comun")

InsertarHabitacion(2,"2","0",34.99,"Si","Si","No", "Comodo")
InsertarHabitacion(2,"2","0",34.99,"Si","Si","No", "Comodo")
InsertarHabitacion(2,"2","0",34.99,"Si","Si","No", "Comodo")
InsertarHabitacion(2,"4","0",39.99,"Si","Si","No", "Comodo")
InsertarHabitacion(2,"4","0",39.99,"Si","Si","No", "Comodo")
InsertarHabitacion(2,"6","0",44.99,"Si","Si","No", "Comodo")

InsertarHabitacion(3,"2","0",44.99,"Si","Si","Si", "Premium")
InsertarHabitacion(3,"2","0",44.99,"Si","Si","Si", "Premium")
InsertarHabitacion(3,"2","0",44.99,"Si","Si","Si", "Premium")
InsertarHabitacion(3,"4","0",44.99,"Si","Si","Si", "Premium")
InsertarHabitacion(3,"4","0",44.99,"Si","Si","Si", "Premium")
InsertarHabitacion(3,"6","0",49.99,"Si","Si","Si", "Premium")"""





#InsertarHabitacion(2,capacidad,disponibilidad, precio,wifi,aireAcondicionado,smartTV, tipoHabitacion)



#InsertarHabitacion(3,capacidad,disponibilidad, precio,wifi,aireAcondicionado,smartTV, tipoHabitacion)





#InsertarCliente("Ramiro","Gonzales","38234765","2614578923","ramiro@malandra.com","Lujan de Cuyo", "1994-06-15","Argentina","Tarjeta Credito",7,"UHM365","2020-06-11 21:07:30","2020-06-18 20:15:7")
#InsertarCliente("Gabriel","Bermudez","39237216","2614269628","gabriel@malandra.com","Niñas de Ayohuma 1395", "1995-10-06","Argentina","Efectivo",5,"ARK246","2020-06-10 21:07:30","2020-06-15 20:15:07")
#SELECT * FROM habitaciones, clientes WHERE clientes.id == habitaciones.id_Cliente;

#CrearEstacionamiento(conexion_sql())

contador=0
"""while(contador<18):
    InsertarEspacioEstacionamiento(False)
    contador+=1"""

contador2=1
"""while(contador2<19):
    UpdateEspacioEstacionamiento(contador2,0)
    contador2+=1"""

#InsertarCliente(4,"Leandro","Mercado","39842421","2616767667","leandro@gmail.com","Rodeo de la Cruz", "1996-08-17","Argentina","Efectivo",5,"ADB493","2020-06-10 21:07:30","2020-06-15 20:15:07")
"""crearHabitaciones(conexion_sql())
crearClientes(conexion_sql())

InsertarHabitacion(1,"2","1",18.99,"No","No","No", "Comun")
InsertarHabitacion(1,"2","1",18.99,"No","No","No", "Comun")
InsertarHabitacion(1,"2","1",20.00,"si","No","No", "Comun")
InsertarHabitacion(1,"4","0",22.50,"No","No","No", "Comun")
InsertarHabitacion(1,"4","0",25.50,"si","No","No", "Comun")
InsertarHabitacion(1,"6","0",33.99,"si","No","No", "Comun")

InsertarHabitacion(2,"2","0",34.99,"Si","Si","No", "Comodo")
InsertarHabitacion(2,"2","0",34.99,"Si","Si","No", "Comodo")
InsertarHabitacion(2,"2","0",34.99,"Si","Si","No", "Comodo")
InsertarHabitacion(2,"4","0",39.99,"Si","Si","No", "Comodo")
InsertarHabitacion(2,"4","0",39.99,"Si","Si","No", "Comodo")
InsertarHabitacion(2,"6","0",44.99,"Si","Si","No", "Comodo")

InsertarHabitacion(3,"2","0",44.99,"Si","Si","Si", "Premium")
InsertarHabitacion(3,"2","0",44.99,"Si","Si","Si", "Premium")
InsertarHabitacion(3,"2","0",44.99,"Si","Si","Si", "Premium")
InsertarHabitacion(3,"4","0",44.99,"Si","Si","Si", "Premium")
InsertarHabitacion(3,"4","0",44.99,"Si","Si","Si", "Premium")
InsertarHabitacion(3,"6","0",49.99,"Si","Si","Si", "Premium")

InsertarCliente(1,"Ramiro","Gonzales","38234765","2614578923","ramiro@gmail.com","Lujan de Cuyo", "1994-06-15","Argentina","Tarjeta Credito",7,"UHM365","2020-06-11 21:07:30","2020-06-18 20:15:7")
InsertarCliente(2,"Gabriel","Bermudez","39237216","2614269628","gabriel@gmail.com","Niñas de Ayohuma 1395", "1995-10-06","Argentina","Efectivo",5,"ARK246","2020-06-10 21:07:30","2020-06-15 20:15:07")
InsertarCliente(3,"Leandro","Mercado","39842421","2616767667","leandro@gmail.com","Rodeo de la Cruz", "1996-08-17","Argentina","Efectivo",5,"ADB493","2020-06-10 21:07:30","2020-06-15 20:15:07")"""

