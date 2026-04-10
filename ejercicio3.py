from sqlalchemy import create_engine
import pandas as pd

# Definir la URL de conexión
url_conexion = "mysql+pymysql://root:@127.0.0.1/ejercicio_bd_py"


engine = create_engine(url_conexion)

try:
    # Departamento con mayor salario promedio
    
    query_departamento_salario = """
    
    SELECT e.departamento, AVG(e.salario) AS salario_promedio
    FROM empleado e GROUP BY e.departamento ORDER BY salario_promedio DESC
    LIMIT 3;
    
    """
    print("\n--- Departamento con mayor salario promedio ---")
    df_departamento_salario = pd.read_sql(query_departamento_salario, engine)
    print(df_departamento_salario)
          

    # empleado con mayor salario
    
    query_empleado_salario = """
    
    SELECT e.nombre, AVG(e.salario) AS salario_empleado_promedio
    FROM empleado e GRUP BY e.nombre ORDER BY salario_empleado_promedio DESC
    LIMIT 3;
    
    """
    
    print("\n--- Empleado con mayor salario ---")
    df_empleado_salario = pd.read_sql(query_empleado_salario, engine)
    print(df_empleado_salario)
    
    #antiguedad promedio 
    
    query_antiguedad = """
    SELECT e.departamento, AVG(YEAR(CURDATE()) - YEAR(e.fecha_contratacion)) AS antiguedad_promedio
    FROM empleado e GROUP BY e.departamento ORDER BY antiguedad_promedio DESC;
    
    """
    
    print("\n--- Antiguedad promedio por departamento ---")
    df_antiguedad = pd.read_sql(query_antiguedad, engine)
    print(df_antiguedad)
    

    
    
    
    
except Exception as e:
    print(f"Error: {e}")
    
    

