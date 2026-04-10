
from sqlalchemy import create_engine
import pandas as pd

# Definir la URL de conexión
# Formato: mysql+pymysql://usuario:password@host/nombre_bd
url_conexion = "mysql+pymysql://root:@127.0.0.1/ejercicio_bd_py"

# Crear el Engine
engine = create_engine(url_conexion)


# realizar la consulta 
tablas = ['ventas', 'productos', 'clientes', 'empleados']



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
    SELECT p.producto, SUM(v.cantidad) AS total_ventas
    FROM ventas v
    JOIN productos p ON v.id = p.id
    GROUP BY p.producto
    ORDER BY total_ventas DESC
    LIMIT 5;
    """
    df_top_productos = pd.read_sql(query_top_productos, engine)
    print(df_top_productos)
    
 

except Exception as e:

    print(f"Error: {e}")
    df_debug = pd.read_sql("SELECT * FROM ventas LIMIT 1", engine)
    print(df_debug.columns.tolist())

finally:
    engine.dispose()