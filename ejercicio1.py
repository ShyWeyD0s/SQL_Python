
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
    for tabla in tablas:
        print(f"\n--- Datos de la tabla: {tabla} ---")
        query = f"SELECT * FROM {tabla}"
        df = pd.read_sql(query, engine)
        print(df.head())
except Exception as e:
    print(f"Ocurrió un error al consultar las tablas: {e}")
    
finally:
    engine.dispose()
    
    
# calcular el total de ventas por producto  

try:    
    print("\n--- Total de ventas por producto ---")
    query = """
    SELECT p.nombre_producto, SUM(v.cantidad) AS total_ventas
    FROM ventas v
    JOIN productos p ON v.producto_id = p.id
    GROUP BY p.nombre_producto
    ORDER BY total_ventas DESC;
    """
    df_ventas = pd.read_sql(query, engine)
    print(df_ventas)
    
except Exception as e:
    print(f"Ocurrió un error al calcular el total de ventas por producto: {e}")
    
finally:
    engine.dispose()