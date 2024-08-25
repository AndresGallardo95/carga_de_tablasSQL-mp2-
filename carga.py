import mysql.connector as db

# Conexión a la base de datos MySQL
mydb = db.connect(
    host="localhost",
    user="root",
    password="sqlroot",
    database="mp2"  # Asegúrate de especificar la base de datos
)

miCursor = mydb.cursor()

# Sentencia SQL para crear tabla productos
sqlsentence = """CREATE TABLE productos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(45),
                    descripcion VARCHAR(150),
                    precio INT
                     )"""
# Sentencia SQL para crear tabla clientes
sqlsentence = """CREATE TABLE clientes (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    nombre VARCHAR(45),
                    email VARCHAR(45)
                      )"""

#Sentecia SQL para crear tabla pedidos
sqlsentence = """CREATE TABLE pedidos (
                    id INT AUTO_INCREMENT PRIMARY KEY,
                    fecha DATE,
                    direccion VARCHAR(100),
                    id_cliente INT,
                    detalle VARCHAR (150),
                    FOREIGN KEY (id_cliente) REFERENCES clientes(id)
                      )"""

#Sentecia SQL para crear tabla productos pedidos
sqlsentence = """CREATE TABLE productos pedidos (
                    id_producto INT,
                    id_pedido INT,
                    cantidad INT
                    PRIMARY KEY (id_producto, id_pedido),
                    FOREIGN KEY (id_producto) REFERENCES productos(id),
                    FOREIGN KEY (id_pedido) REFERENCES pedidos(id)
                      )"""
#Sentencia sql para cargar nuevas tablas en base de datos mp2



# Ejecutar la sentencia SQL
miCursor.execute(sqlsentence)

# Cerrar el cursor y la conexión
miCursor.close()
mydb.close()
