import sqlite3
#--------------------------------------------------------------------

# ----> CONEXION <----
def conectar ():
    mi_conexion = sqlite3.connect ("tp.bd")    # -> almaceno en variable la conexion que crea la BBDD
    cursor = mi_conexion.cursor()

# ----> CREA TABLA <----
    try:
        sql = """
              CREATE TABLE IF NOT EXISTS pacientes
             (
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              NOMBRE TEXT NOT NULL,
              APELLIDO TEXT NOT NULL,
              DNI TEXT NOT NULL UNIQUE,
              GENERO TEXT NOT NULL,
              EDAD INTEGER NOT NULL,
              CELULAR TEXT NOT NULL UNIQUE,
              MAIL TEXT NOT NULL UNIQUE
              )
              """
        cursor.execute(sql)
        cursor.close()
        return mi_conexion
    
    except Exception as e:
        print (f"Error de Conexión {e}")
        
    finally:
        cursor.close()
