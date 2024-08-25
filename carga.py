import mysql.connector as db
import csv



# Conexión a la base de datos MySQL
mydb = db.connect(
    host="localhost",
    user="root",
    password="sqlroot",
    database="mp2"  # Asegúrate de especificar la base de datos
)

miCursor = mydb.cursor()

# Parte comentada para evitar la recreación de las tablas
# # Sentencia SQL para crear tabla productos
# sqlsentence = """CREATE TABLE productos (
#                     id INT AUTO_INCREMENT PRIMARY KEY,
#                     nombre VARCHAR(45),
#                     descripcion VARCHAR(150),
#                     precio INT
#                  )"""
# miCursor.execute(sqlsentence)

# # Sentencia SQL para crear tabla clientes
# sqlsentence = """CREATE TABLE clientes (
#                     id INT AUTO_INCREMENT PRIMARY KEY,
#                     nombre VARCHAR(45),
#                     email VARCHAR(45)
#                  )"""
# miCursor.execute(sqlsentence)

# # Sentencia SQL para crear tabla pedidos
# sqlsentence = """CREATE TABLE pedidos (
#                     id INT AUTO_INCREMENT PRIMARY KEY,
#                     fecha DATE,
#                     direccion VARCHAR(100),
#                     id_cliente INT,
#                     detalle VARCHAR(150),
#                     FOREIGN KEY (id_cliente) REFERENCES clientes(id)
#                  )"""
# miCursor.execute(sqlsentence)

# # Sentencia SQL para crear tabla productos_pedidos
# sqlsentence = """CREATE TABLE productos_pedidos (
#                     id_producto INT,
#                     id_pedido INT,
#                     cantidad INT,
#                     PRIMARY KEY (id_producto, id_pedido),
#                     FOREIGN KEY (id_producto) REFERENCES productos(id),
#                     FOREIGN KEY (id_pedido) REFERENCES pedidos(id)
#                  )"""
# miCursor.execute(sqlsentence)

# Insertar datos desde CSV en la tabla clientes
with open('clientes.csv', mode='r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    next(reader)  # Saltar la cabecera
    for row in reader:
        sql = "INSERT INTO clientes (id, nombre, email) VALUES (%s, %s, %s)"
        try:
            miCursor.execute(sql, tuple(row))
        except db.errors.ProgrammingError as e:
            print(f"Error en 'clientes': {e}")
            print(f"Fila: {tuple(row)}")

# Insertar datos desde CSV en la tabla productos
with open('productos.csv', mode='r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    next(reader)  # Saltar la cabecera
    for row in reader:
        sql = "INSERT INTO productos (id, nombre, descripcion, precio) VALUES (%s, %s, %s, %s)"
        try:
            miCursor.execute(sql, tuple(row))
        except db.errors.ProgrammingError as e:
            print(f"Error en 'productos': {e}")
            print(f"Fila: {tuple(row)}")

# Insertar datos desde CSV en la tabla pedidos
with open('pedidos.csv', mode='r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    next(reader)  # Saltar la cabecera
    for row in reader:
        sql = "INSERT INTO pedidos (id, fecha, direccion, id_cliente, detalle) VALUES (%s, %s, %s, %s, %s)"
        try:
            miCursor.execute(sql, tuple(row))
        except db.errors.ProgrammingError as e:
            print(f"Error en 'pedidos': {e}")
            print(f"Fila: {tuple(row)}")

# Insertar datos desde CSV en la tabla productos_pedidos
with open('productos_pedidos.csv', mode='r', encoding='utf-8-sig') as file:
    reader = csv.reader(file)
    next(reader)  # Saltar la cabecera
    for row in reader:
        sql = "INSERT INTO productos_pedidos (id_producto, id_pedido, cantidad) VALUES (%s, %s, %s)"
        try:
            miCursor.execute(sql, tuple(row))
        except db.errors.ProgrammingError as e:
            print(f"Error en 'productos_pedidos': {e}")
            print(f"Fila: {tuple(row)}")

# Confirmar los cambios
mydb.commit()

# Cerrar el cursor y la conexión
miCursor.close()
mydb.close()