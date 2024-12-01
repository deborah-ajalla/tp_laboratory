import sqlite3
import re
from datetime import datetime

# --> Función para validar el nombre
def validar_nombre_t(nombre):
    if nombre.strip() == "":
        raise ValueError("El nombre no puede estar vacío.")
    return nombre

# --> Función para validar descripción
def validar_descripcion (descripcion):
    if descripcion.strip() == "":
        raise ValueError("El nombre no puede estar vacío.")
    return descripcion

# --> Función para insertar los datos en la BBDD
def insertar_en_db(dni_paciente, nombre, descripcion):
    try:
        # -> Conectar a la base de datos
        conn = sqlite3.connect("tp.db")
        cursor = conn.cursor()

         # -> Insertar los datos validados
        cursor.execute('''
            INSERT INTO tratamientos (dni_pacientes, nombre, descripcion)
            VALUES (?, ?, ?)
        ''', (dni_paciente, nombre, descripcion))

        # -> Confirmar los cambios
        conn.commit()

    except sqlite3.Error as e:
        print(f"Error al interactuar con la base de datos: {e}")
    finally:
        conn.close()

#--------------------------------------------------------
# >>> MENÚ <<<
#--------------------------------------------------------
def carga_tabla():
    try:
        print("-------------------------------------- ")
        print("💠 Ingrese los datos del Tratamiento: ")
        print("-------------------------------------- ")
        # --> Solicitar nombre y fecha al usuario
        dni_paciente = input ("> Ingrese el Dni del Paciente: ")
        nombre = input("> Nombre: ")
        descripcion = input("> Descripción: ")

        # --> Validar los datos
        nombre = validar_nombre_t(nombre)
        descripcion = validar_descripcion(descripcion)

        # --> Insertar en la base de datos
        insertar_en_db(dni_paciente, nombre, descripcion)

        print("\n🔸Datos insertados correctamente ✅ ")
    
    except ValueError as e:
        print(f"Error de validación: {e}")
#------------------------------------------------------------------------------------------
def mostrar_listado_t ():
    try:
        # --> Conectar a la base de datos
        conn = sqlite3.connect("tp.db")
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM tratamientos")
        tratamientos = cursor.fetchall()   #--> Obtiene TODOS los registros de la tabla

        print ("-------------------------------------------------")
        print(f"--> Listado de Tratamientos <--") 
        print ("-------------------------------------------------")

        if tratamientos:
           # --> Mostrar los registros en la consola
            print(f" {'Nombre':<10} {'Descripción':<20}  {'id':<10} {'Dni Paciente':<10} " )  # --> Encabezados de la tabla
            print('-' * 70)  # --> Línea divisoria
            for tratamiento in tratamientos:
                print(f"{tratamiento[0]:<6} {tratamiento[1]:<20} {tratamiento[2]:<10} {tratamiento[4]:<10}")

        else:
            print("No se encontraron registros.")
    except Exception as e:
        return {"respuesta": False, "mensaje": str (e)}

    finally:
      conn.close()

def ver_info_compartida():
    try:
        # --> Conectar a la base de datos
        conn = sqlite3.connect("tp.db")
        cursor = conn.cursor()
        cursor.execute('''
                       SELECT pacientes.nombre, pacientes.apellido, pacientes.dni, tratamientos.nombre, tratamientos.descripcion
                        FROM pacientes
                        JOIN tratamientos ON pacientes.dni = tratamientos.dni_pacientes
                        ORDER BY pacientes.dni;
                       
                        ''')
        resultados  = cursor.fetchall()   #--> Obtiene TODOS los registros de la tabla

        print("\n 🔸 INFORMACIÓN 🔸 ")
        print ("----------------------\n")
        for fila in resultados:
            print(f'> Nombre: {fila[0]}, \n> Apellido de Paciente: {fila[1]}, \n> Dni: {fila[2]}, \n> Tratamiento: {fila[3]},\n> Descripción: {fila[4]}')
            print ("----------------------\n")


    except Exception as e:
        return {"respuesta": False, "mensaje": str (e)}

    finally:
      conn.close()

#-----------------------------------------------------------------
# >>>  CARGA TABLA TRATAMIENTOS  <<<
#-----------------------------------------------------------------
def tratamientos():
    while True:
         print("\n > Elija: ")
         print("\t 1- Cargar Tratamiento")
         print("\t 2- Ver Tratamientos")
         print("\t 3- Ver Información de Paciente")
         print("\t 4- Volver al Menú Principal")

         opcion = input("-> Seleccione una opcion: ")
         if opcion == "1":
            carga_tabla()
         elif opcion == "2":
            mostrar_listado_t()
         elif opcion =="3":
            ver_info_compartida()
         elif opcion =="4":
            break
         else :
            print("Opción Inválida")
