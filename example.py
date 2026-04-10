from sqlalchemy import create_engine
import pandas as pd

# Definir la URL de conexión
# Formato: mysql+pymysql://usuario:password@host/nombre_bd
url_conexion = "mysql+pymysql://root:@127.0.0.1/db_python"

# Crear el Engine
engine = create_engine(url_conexion)


# realizar la consulta
tablas = ['usuarios']

# imprimimos cada tabla con un encabezado indicando el nombre de la tabla

try:
    
    for tabla in tablas:
        print(f"\n--- Datos de la tabla: {tabla} ---")
        query = f"SELECT * FROM {tabla}"
        df = pd.read_sql(query, engine)
        print(df.head())
        
except Exception as e:
    print(f"Ocurrió un error al consultar las tablas: {e}")
finally:
    engine.dispose()  # Cerrar la conexión al finalizar