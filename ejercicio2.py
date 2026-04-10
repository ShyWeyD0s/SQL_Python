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
    LIMIT 1;
    
    """
    
    df_ciudad_clientes = pd.read_sql(query_ciudad_clientes, engine)
    print(df_ciudad_clientes)