import conexion as c
#-----------------------------------------------------------------
# MENÚ OPCIÓN 1: INGRESAR NUEVO PACIENTE
#-----------------------------------------------------------------
def carga_datos (paciente):
    paciente = dict (paciente)

    try:
        db = c.conectar()
        cursor = db.cursor()
        columnas = tuple(paciente.keys())     # -> cargo en el campo seleccionado
        valores = tuple(paciente.values())    # -> cargo registros

        sql = """
              INSERT INTO pacientes {campos} VALUES (?,?,?,?,?,?,?,?)
              """.format (campos = columnas)
        
        cursor.execute(sql, (valores))

        creado = cursor.rowcount > 0
        db.commit()
        
        if creado:
            cursor.close()
            db.close()
            return {"respuesta": creado, "mensaje": "Paciente Registrado"} 
        else:
            cursor.close()
            db.close()
            return {"respuesta": creado, "mensaje": "No se ha podido realizar la acción"}
        
    except Exception as e:
        if "UNIQUE" in  str (e) and "DNI" in str (e):                 # --> verifica que sólo haya un paciente por DNI
            mensaje = "Ya existe un Paciente registrada con ese DNI"
        elif "UNIQUE" in  str (e) and "MAIL" in str (e):              # --> verifica que sólo haya un MAIL por paciente
            mensaje = "Ya existe un paciente que registró ese Mail, por favor indique otro..."
        elif "UNIQUE" in  str (e) and "CELULAR" in str (e):           # --> verifica que sólo haya un CELULAR por paciente
            mensaje = "Ya existe un paciente que registró ese Celular de Contacto, por favor indique otro..."
        else:
            mensaje = str(e) 
            cursor.close()
            db.close()
             
        return {"respuesta": False,
                "mensaje": mensaje}
    
#-----------------------------------------------------------------
# MENÚ OPCIÓN 2: BUSCAR PACIENTE (POR DNI)
#-----------------------------------------------------------------
def buscar_paciente (dni_buscado):
    try:
        db = c.conectar()
        cursor = db.cursor()
        cursor.execute ("SELECT * FROM pacientes WHERE DNI = '{dni}'".format(dni = dni_buscado))
        resultado = cursor.fetchall()
        if resultado:
            info = resultado [0]
            persona = {"id": info[0], 
                       "nombre": info[1],
                       "apellido": info[2], 
                       "dni": info[3],
                       "genero": info [4],
                       "fecha_nacimiento": info [5],
                       "celular": info [6],
                       "mail": info [7],
                       "domicilio": info[8],
                       }
            cursor.close()
            db.close()
            return {"respuesta": True, "persona": persona, "mensaje": "Paciente Encontrado!! ✔"}
        else:
            cursor.close()
            db.close()
            return {"respuesta":False, "mensaje": "❌ No hay Paciente Registrado con ese DNI ❌"}
        
    except Exception as e:
        cursor.close()
        db.close()
        return {"respuesta": False, "mensaje": str (e)} 
#-----------------------------------------------------------------
# MENÚ OPCIÓN 3: MODIFICAR DATOS
#-----------------------------------------------------------------

def actualizar_datos(paciente):
    try:
        # Asegurarse de que el diccionario contiene todos los campos necesarios
        
        id = paciente['id']
        nombre = paciente['nombre']
        apellido = paciente['apellido']
        dni = paciente['dni']
        genero = paciente['genero']
        fecha_nacimiento = paciente['fecha_nacimiento']
        celular = paciente['celular']
        mail = paciente['mail']
        domicilio = paciente['domicilio']

        db = c.conectar()
        cursor = db.cursor()

        # Ejecutar la consulta de actualización, usando los valores recibidos
        cursor.execute("""
            UPDATE pacientes
            SET nombre = ?, apellido = ?, dni = ?, genero = ?,
                fecha_nacimiento = ?, celular = ?, mail = ?, domicilio = ?
            WHERE id = ?
        """, (nombre, apellido, dni, genero, fecha_nacimiento, celular, mail, domicilio, id))

        # Su función es confirmar los cambios
        db.commit()

        # Cierra conexión
        cursor.close()
        db.close()
    except Exception as e:
        print(f"⚠ Error al actualizar el paciente: {e}")


#-----------------------------------------------------------------
# MENÚ OPCIÓN 4: MOSTRAR LISTADO TOTAL
#-----------------------------------------------------------------
def mostrar_pacientes ():
    try:
        db = c.conectar()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM pacientes")
        pacientes = cursor.fetchall()

        if pacientes:
            cursor.close()
            db.close()
            return {"respuesta": True, "pacientes": pacientes, "mensaje": "Listado todo OK ✔"}
        else:
            cursor.close()
            db.close()
            return {"respuesta": False ,"pacientes": pacientes,  "mensaje": "No hay Pacientes registrados aun... ❌"}
    except Exception as e:
        cursor.close()
        db.close()
        return {"respuesta": False, "mensaje": str (e)}
