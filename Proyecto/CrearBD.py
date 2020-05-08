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
        self
    except sqlite3.OperationalError:
	    print("No se pudo insertar al empleado.")
    else:
	    print("Se pudo insertar al empleado con exito en la base de datos.")

    conexion.commit()
    conexion.close()



#crear_bd(conexion_sql())
#InsertarUsuario("Leandro", "Mercado", "38236745","2616145345", "LeandroMercado", "leandro@gmail.com", "123123")
#InsertarUsuario("Gabriel", "Bermudez", "39237216","2616145079", "GabrielBermudez", "gabriel@gmail.com","12345")