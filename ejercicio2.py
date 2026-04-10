from sqlalchemy import create_engine
import pandas as pd

# Definir la URL de conexión
url_conexion = "mysql+pymysql://root:@127.0.0.1/ejercicio_bd_py"


engine = create_engine(url_conexion)

try:
    # ciudad con mas clientes
    
    print("\n--- Ciudad con más clientes ---")
    query_ciudad_clientes = """
    
    SELECT c.ciudad, COUNT(*) AS total_clientes
    FROM clientes c
    GROUP BY c.ciudad
    ORDER BY total_clientes DESC
    LIMIT 3;
    
    """
    
    df_ciudad_clientes = pd.read_sql(query_ciudad_clientes, engine)
    print(df_ciudad_clientes)
    
    # Calcular promedio de compras
    
    print("\n--- Promedio de compras por cliente ---")
    query_promedio_compras = """
    
    SELECT c.nombre, AVG(v.cantidad) AS promedio_compras
    FROM clientes c
    JOIN ventas v ON c.id = v.id
    GROUP BY c.nombre
    ORDER BY promedio_compras DESC;
    
    """
    df_promedio_compras = pd.read_sql(query_promedio_compras, engine)
    print(df_promedio_compras)
    
    # Identificar el cliente con más compras
    
    print("\n--- Cliente con más compras ---")
    query_cliente_mas_compras = """
    
    SELECT c.nombre, SUM(v.cantidad) AS total_compras
    FROM clientes c
    JOIN ventas v ON c.id = v.id
    GROUP BY c.nombre
    ORDER BY total_compras DESC
    LIMIT 3;
    
    """
    df_cliente_mas_compras = pd.read_sql(query_cliente_mas_compras, engine)
    print(df_cliente_mas_compras)
    
except Exception as e:
    print(f"Error: {e}")
    
finally:
    engine.dispose()