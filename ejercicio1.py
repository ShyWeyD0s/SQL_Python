
from sqlalchemy import create_engine
import pandas as pd

# Definir el el lenguaje+driver la url de la conexion local 
url_conexion = "mysql+pymysql://root:@127.0.0.1/ejercicio_bd_py"

# Crear el Engine, que es la conexión a la base de datos
engine = create_engine(url_conexion)


# Configurar las tablas para consultar todas de manera simplificada con un bucle for 
tablas = [
    'ventas', 
    'productos', 
    'clientes', 
    'empleados'
]


print("\n--- Tablas disponibles ---")

for i in tablas:
        query_bucle = f"SELECT * FROM {i} LIMIT 5;"
        df = pd.read_sql(query_bucle, engine)
        print(f"\n--- Tabla: {i} ---")
        print(df)
        



try:
    # 1. Total de ventas por producto 
    print("\n--- Total de ventas por producto ---")
    query_ventas = """
    SELECT p.producto, SUM(v.cantidad) AS total_ventas
    FROM ventas v
    JOIN productos p ON v.id = p.id
    GROUP BY p.producto
    ORDER BY total_ventas DESC;
    """
    df_ventas = pd.read_sql(query_ventas, engine)
    print(df_ventas)
    
    # 2. Ventas por ciudad 
    print("\n--- Ventas por ciudad ---")
    query_ciudad = """
    SELECT c.ciudad, SUM(v.cantidad) AS total_ventas
    FROM ventas v
    JOIN clientes c ON v.id = c.id
    GROUP BY c.ciudad
    ORDER BY total_ventas DESC;
    """
    df_ciudad = pd.read_sql(query_ciudad, engine)
    print(df_ciudad)
    
    # top productos vendidos
    print("\n--- Top productos vendidos ---")
    query_top_productos = """
    SELECT p.producto, 
    SUM(v.cantidad) AS total_ventas
    FROM ventas v JOIN productos p ON v.id = p.id
    GROUP BY p.producto
    ORDER BY total_ventas DESC
    LIMIT 5;
    """
    df_top_productos = pd.read_sql(query_top_productos, engine)
    print(df_top_productos)
    
 

except Exception as e:

    print(f"Error en las consultas: {e}")
    # realizar un debug con una consulta simple para verificar la conexión y las columnas disponibles
    df_debug = pd.read_sql("SELECT * FROM ventas LIMIT 1", engine)
    print("\n--- Debug ---")
    print(df_debug.columns.tolist())

finally:
    # cerrar la conexion, buena practica 
    engine.dispose()