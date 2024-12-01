import sqlite3
#--------------------------------------------------------------------
# ----> CONEXION <----
def conectar ():
    mi_conexion = sqlite3.connect ("tp.db")    # -> almaceno en variable la conexion que crea la BBDD
    cursor = mi_conexion.cursor()

# ----> CREA TABLA <----
    try:
        sql = """
              CREATE TABLE IF NOT EXISTS pacientes
             (
              ID INTEGER PRIMARY KEY AUTOINCREMENT,
              NOMBRE TEXT NOT NULL,
              APELLIDO TEXT NOT NULL,
              DNI INTEGER NOT NULL UNIQUE, 
              GENERO TEXT NOT NULL,
              FECHA_NACIMIENTO TEXT NOT NULL,
              CELULAR TEXT NOT NULL UNIQUE,
              MAIL TEXT NOT NULL UNIQUE, 
              DOMICILIO TEXT 
              );

               CREATE TABLE IF NOT EXISTS tratamientos
             (
              ID INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
              NOMBRE TEXT NOT NULL,
              DESCRIPCION TEXT NOT NULL,
              DNI_PACIENTES INTEGER,
              FOREIGN KEY (DNI_PACIENTES) REFERENCES pacientes (DNI)
              )
              """
        cursor.executescript(sql)       # para ejecutar multiples instrucciones... sino sería execute. ❌
        return mi_conexion
    
    except Exception as e:
        print (f"Error de Conexión ❌ {e} ❌")
        
    finally:
        cursor.close()