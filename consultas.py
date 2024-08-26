import mysql.connector as db

# Conexión a la base de datos MySQL
mydb = db.connect(
    host="localhost",
    user="root",
    password="sqlroot",
    database="mp2"  # Asegúrate de especificar la base de datos
)

miCursor = mydb.cursor()

 #! Primera consulta
# sqlsentence = """
# SELECT c.nombre, c.email, COUNT(DISTINCT p.id) AS numero_de_pedidos
# FROM pedidos p
# JOIN clientes c ON p.id_cliente = c.id
# JOIN productos_pedidos pp ON p.id = pp.id_pedido
# WHERE c.email = 'jessicaflores@example.com'
# GROUP BY c.nombre, c.email;
# """

#! Segunda consulta
# sqlsentence = """
# SELECT 
#     pp.id_pedido AS Pedido_ID, 
#     p.id AS Producto_ID, 
#     p.nombre AS Producto_Nombre, 
#     p.precio AS Producto_Precio, 
#     pp.cantidad AS Cantidad_Pedida
# FROM productos p
# JOIN productos_pedidos pp ON p.id = pp.id_producto
# WHERE pp.id_pedido = 2;
# """

#! Tercera consulta
sqlsentence = """
    SELECT 
    p.id AS Producto_ID, 
    p.nombre AS Producto_Nombre, 
    SUM(pp.cantidad) AS Total_Unidades_Vendidas
FROM productos p
JOIN productos_pedidos pp ON p.id = pp.id_producto
GROUP BY p.id, p.nombre
ORDER BY Total_Unidades_Vendidas DESC
LIMIT 3;
"""


miCursor.execute(sqlsentence)
rows = miCursor.fetchall()  # usar fetchone si solo necesitamos una fila o fetchmany(2) si queremos dos filas, etc.
for row in rows:
    print(row)  # usar row[1] y devolverá la fila en esa posición contando desde 0 como el primero
