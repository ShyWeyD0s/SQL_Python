from sqlalchemy import create_engine
import pandas as pd


url_conexion = "mysql+pymysql://root:@127.0.0.1/ejercicio_bd_py"

engine = create_engine(url_conexion)