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
            # cursor.close()
            # db.close()
            return {"respuesta": True,
                "mensaje": "\n 🔸 Paciente Registrado  Exitosamente 🔸 ✅"}
        else:
            # cursor.close()
            # db.close()
            return {"respuesta": True,
                "mensaje": "\n ❌❌ No se ha podido realizar la carga de datos. Aguarde e Intente Nuevamente... ❌❌"}
        
    except Exception as e:
        # if "UNIQUE" in  str (e) and "DNI" in str (e):                 # --> verifica que sólo haya un paciente por DNI
        #     mensaje = "Ya existe un Paciente registrada con ese DNI"
        # elif "UNIQUE" in  str (e) and "MAIL" in str (e):              # --> verifica que sólo haya un MAIL por paciente
        #     mensaje = "Ya existe un paciente que registró ese Mail, por favor indique otro..."
        # elif "UNIQUE" in  str (e) and "CELULAR" in str (e):           # --> verifica que sólo haya un CELULAR por paciente
        #     mensaje = "Ya existe un paciente que registró ese Celular de Contacto, por favor indique otro..."
        # else:
            mensaje = str(e) 
            # cursor.close()
            # db.close()
             
            return {"respuesta": False,
                "mensaje": mensaje}
    finally:
        db.close()
    
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
            return {"respuesta":False, "mensaje": "\n❌ No hay Paciente Registrado con ese DNI ❌"}
        
    except Exception as e:
        cursor.close()
        db.close()
        return {"respuesta": False, "mensaje": str (e)} 
    
#-----------------------------------------------------------------
# MENÚ OPCIÓN 3: MODIFICAR DATOS
#-----------------------------------------------------------------
def actualizar_datos(paciente):
    try:#
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
        return {"respuesta": True, "mensaje": "\n✅ Cambios guardados exitosamente."}
    except Exception as e:
        return {"respuesta": False, "mensaje": f"⚠{e}"}

#-----------------------------------------------------------------
# MENÚ OPCIÓN 4: MOSTRAR LISTADO TOTAL
#-----------------------------------------------------------------
def mostrar_pacientes ():
    try:
        db = c.conectar()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM pacientes")
        pacientes = cursor.fetchall()   #-- Obtiene TODOS los registros de la tabla

        print ("------------------------------------")
        print(f"--> Listado de Pacientes <--") 
        print ("------------------------------------")

        if pacientes:
           # Mostrar los registros en la consola

            print(f"{'ID':<6} {'Nombre':<10} {'Apellido':<17} {'Dni':<12} {'Género':<12} {'Fecha de Nacimiento':<14} {'Celular':<30} {'Mail':<13} {'Domicilio':<25}")  # Encabezados de la tabla
            print('-' * 155)  # Línea divisoria
            for paciente in pacientes:
                print(f"{paciente[0]:<6} {paciente[1]:<10} {paciente[2]:<13} {paciente[3]:<12} {paciente[4]:<14} {paciente[5]:<24} {paciente[6]:<11} {paciente[7]:<20} {paciente[8]:<12}")

        else:
            print("No se encontraron registros.")
                

        # Obtener los encabezados
        # columnas = [descripcion[0] for descripcion in cursor.description]
        # print(" | ".join(columnas))

        # # Mostrar los registros
        # for registro in cursor:
        #     print(" | ".join(str(campo) for campo in registro))

        # if pacientes:
        #     for paciente in pacientes:
        #         print (paciente)
        # else:
        #     print (" >> No hay Pacientes registrados aun... ❌")
    except Exception as e:
        return {"respuesta": False, "mensaje": str (e)}

    finally:
        cursor.close()
        db.close()

    
#-----------------------------------------------------------------
# MENÚ OPCIÓN 5: MOSTRAR LISTADO ORDENADO 
#-----------------------------------------------------------------
def listado_ordenado_apellido():
    try:
        db = c.conectar()
        cursor = db.cursor()

        cursor.execute ("SELECT * FROM pacientes ORDER BY apellido ASC")

        pacientes = cursor.fetchall()  # --Obtiene los registros

        print ("-----------------------------------------------------")
        print(f"--> Listado de Pacientes Ordenados por Apellido: <--") 
        print ("-----------------------------------------------------")

        for paciente in pacientes:
            print(f'🔹 {paciente[2]} {paciente[1]}, Id: {paciente[0]}, Dni: {paciente[3]}')
                    
    except Exception as e:
         return {"respuesta": False, "mensaje": str (e)}

    finally:
        cursor.close()
        db.close()

def listado_ordenado_id():
    try:
        db = c.conectar()
        cursor = db.cursor()

        cursor.execute ("SELECT * FROM pacientes ORDER BY id ASC")

        pacientes = cursor.fetchall()  # --Obtiene los registros

        print ("-----------------------------------------------------")
        print(f"--> Listado de Pacientes Ordenados por Id: <--") 
        print ("-----------------------------------------------------")

        for paciente in pacientes:
            print(f'🔹 Id: {paciente[0]}, {paciente[1]} {paciente[2]}, Dni: {paciente[3]}')
                    
    except Exception as e:
         return {"respuesta": False, "mensaje": str (e)}

    finally:
        cursor.close()
        db.close()

def listado_ordenado_dni():
    try:
        db = c.conectar()
        cursor = db.cursor()

        cursor.execute ("SELECT * FROM pacientes ORDER BY dni ASC")

        pacientes = cursor.fetchall()  # --Obtiene los registros

        print ("-----------------------------------------------------")
        print(f"--> Listado de Pacientes Ordenados por Dni: <--") 
        print ("-----------------------------------------------------")

        for paciente in pacientes:
            print(f'🔹 Dni: {paciente[3]}, {paciente[1]} {paciente[2]}, Id: {paciente[0]}')
                    
    except Exception as e:
         return {"respuesta": False, "mensaje": str (e)}

    finally:
        cursor.close()
        db.close()

#-----------------------------------------------------------------
# MENÚ OPCIÓN 6: ELIMINAR
#-----------------------------------------------------------------
def eliminar_paciente(id_paciente):
    try:
        db = c.conectar()
        cursor = db.cursor()
        
        cursor.execute("DELETE FROM pacientes WHERE ID = ?", (id_paciente,))
        
        if cursor.rowcount > 0:
            db.commit()
            return {"respuesta": True, "mensaje": "\n✅ Paciente eliminado"}
        else:
            return {"respuesta": False, "mensaje": "\nNo se encontró un paciente con ese ID ❌"}
    except Exception as e:
        return {"respuesta": False, "mensaje": str(e)}
    finally:
        cursor.close()
        db.close()

#-----------------------------------------------------------------
#  INGRESAR EN TABLA TRATAMIENTO
# ----------------------------------------------------------------
def carga_tabla (tratamiento):
    tratamiento = dict (tratamiento)

    try:
        db = c.conectar()
        cursor = db.cursor()
        columnas = tuple(tratamiento.keys())     # -> cargo en el campo seleccionado
        valores = tuple(tratamiento.values())    # -> cargo registros

        sql = """
              INSERT INTO tratamientos {campos} VALUES (?,?)
              """.format (campos = columnas)

        cursor.execute(sql, (valores))

        creado = cursor.rowcount > 0
        db.commit()

        if creado:
            return ("\n 🔸 Se Almacenó el Tratamiento! 🔸 ✅")  
        else:
            return ("\n ❌❌ No se ha podido realizar la carga ... ❌❌")
        
    except Exception as e:
        # if "UNIQUE" in  str (e) and "DNI" in str (e):                 # --> verifica que sólo haya un paciente por DNI
        #     mensaje = "Ya existe un Paciente registrada con ese DNI"
        # elif "UNIQUE" in  str (e) and "MAIL" in str (e):              # --> verifica que sólo haya un MAIL por paciente
        #     mensaje = "Ya existe un paciente que registró ese Mail, por favor indique otro..."
        # elif "UNIQUE" in  str (e) and "CELULAR" in str (e):           # --> verifica que sólo haya un CELULAR por paciente
        #     mensaje = "Ya existe un paciente que registró ese Celular de Contacto, por favor indique otro..."
        # else:
        mensaje = str(e) 
            # cursor.close()
            # db.close()
             
        return {"respuesta": False,
                "mensaje": mensaje}
    finally:
        cursor.close()
        db.close()
    