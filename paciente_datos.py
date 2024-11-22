import conexion as c
#-----------------------------------------------------------------

def carga_datos (paciente):
    paciente = dict (paciente)

    try:
        db = c.conectar()
        cursor = db.cursor()
        columnas = tuple(paciente.keys())     # -> cargo en el campo seleccionado
        valores = tuple(paciente.values())  # -> cargo registros

        sql = """
              INSERT INTO pacientes {campos} VALUES (?,?,?,?,?,?,?)
              """.format (campos = columnas)
        
        cursor.execute(sql, (valores))

        creado = cursor.rowcount > 0
        db.commit()
        
        if creado:
            return {"respuesta": creado, "mensaje": "Paciente Registrado"}
        
        else:
            return {"respuesta": creado, "mensaje": "No se ha podido realizar la acción"}
        
    except Exception as e:
        return {"respuesta": False,
                "mensaje": str (e)}
    
    finally:
        cursor.close()
        db.close()

