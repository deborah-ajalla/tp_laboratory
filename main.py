import conexion as c
import paciente_datos as p
#-----------------------------------------------------------------
"""
 -> PROYECTO: App que gestiona la actividad de COSMETÓLOGA.
 -> INTEGRANTES: 🔸 Ajalla, Deborah.
                 🔸 Colque, Mayde.
                 🔸 Galarza, Gimena.
 -> MATERIA: Laboratorio IV.
 -> DOCENTE: Alex Roberts.
 -> CARRERA: Tecnicatura Universitaria en Programación.
 -> UNIVERSIDAD: UTN.
 -> AÑO: 2024.
"""
#-----------------------------------------------------------------
print ("--------------------------------------------------------------")

# --> pruebo creacion de BBDD <--
c.conectar()

# --> pruebo carga datos <--
# persona = {
#     "dni": "26896334",
#     "nombre": "Luciano",
#     "apellido": "Pereyra",
#     "genero":  "masculino",
#     "fecha_nacimiento": "1980- 09- 21", 
#     "celular": "1562358972",
#     "mail": "lucianoo@gmail.com",
#     "domicilio": "un lugar 123"
# }
# prueba = p.carga_datos(persona)
# print("prueba de carga de paciente")
# print(prueba)


# ----> FUNCIONES <----
#-----------------------------------------------------------------
# >>> CARGA NUEVO PACIENTE <<<
#-----------------------------------------------------------------
# -- Ingresa datos
def nuevo_paciente ():
    print("Ingrese los datos del paciente: ")
    nombre = input ("Nombre: ")
    apellido = input ("Apellido: ")
    dni = int (input ("DNI: "))
    genero = input ("Género: ")
    fecha_nacimiento = input ("Fecha de Nacimiento: ")
    celular = input ("Celular: ")
    mail = input ("Email: ")
    domicilio = input ("Domicilio: ")

# -- Carga diccionario
    nuevo_p = {
       
        "nombre": nombre,
        "apellido": apellido,
        "dni": dni,
        "genero": genero,
        "fecha_nacimiento": fecha_nacimiento,
        "celular": celular,
        "mail": mail,
        "domicilio": domicilio
    }

    nuevo_paciente = p.carga_datos(nuevo_p)
    print (nuevo_paciente)


#-----------------------------------------------------------------
# >>> MUESTRA DATOS DE PACIENTE <<<
#-----------------------------------------------------------------
def mostrar_datos(paciente):
    print(f"\t ID: {paciente['id']}")
    print(f"\t Nombre: {paciente['nombre']}")
    print(f"\t Apellido: {paciente['apellido']}")
    print(f"\t DNI: {paciente['dni']}")
    print(f"\t Género: {paciente['genero']}")
    print(f"\t Fecha de Nacimiento: {paciente['fecha_nacimiento']}")
    print(f"\t Celular: {paciente['celular']}")
    print(f"\t Email: {paciente['mail']}")
    print(f"\t Domicilio: {paciente['domicilio']}")

#-----------------------------------------------------------------
# >>> MUESTRA RESULTADO DE BÚSQUEDA <<<
#-----------------------------------------------------------------
def resultado_busqueda():
    dni_buscado = input("Ingrese el DNI del paciente: ")
    resultado = p.buscar_paciente(dni_buscado)  

    if resultado["respuesta"]: 
        paciente = resultado["persona"]
        print("\n--- Resultado de la Búsqueda 👇")
        mostrar_datos(paciente)
        return paciente
    else: 
        print("\n--- Resultado de la Búsqueda 👇")
        print(resultado["mensaje"])
        return None  # Retorna None si no se encuentra el paciente
    
#-----------------------------------------------------------------
# >>>  MODIFICA DATOS <<<
#-----------------------------------------------------------------
def modificar():
    print("\n--- Modificación de Datos 📝 ---")
    paciente = resultado_busqueda()

    while not paciente:  # En caso de no encontrar coindidencias busca un paciente hasta que el usuario decida salir
        print("¿Qué desea hacer?")
        print("\t 1- Buscar otro paciente")
        print("\t 2- Regresar al Menú Principal")
        seleccionado = input("\nSeleccione una opción: ").strip()
            
        if seleccionado == "1":
            paciente = resultado_busqueda()
            continue  # Repite la búsqueda
        elif seleccionado == "2":
            print("Regresando al Menú Principal...")
            return  
        else:
            print("❌ Opción no válida. Inténtelo de nuevo.")
            continue

        # Sale del bucle si encontró un paciente para continuar con la operación de modificar datos

    
    #datos_originales = paciente.copy()
    
    dato_a_modificar = input("\n✍ Escriba el nombre del dato a modificar (ej: Email): ").strip().lower()
        
    # Modificar valores según el dato introducido 
    while True:
        if dato_a_modificar == "nombre":
            nuevo_valor = input("Ingrese el nuevo nombre: ").strip()
            paciente['nombre'] = nuevo_valor
            print(f"\n✅ Nombre actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "apellido":
            nuevo_valor = input("Ingrese el nuevo apellido: ").strip()
            paciente['apellido'] = nuevo_valor
            print(f"\n✅ Apellido actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "dni":
            nuevo_valor = input("Ingrese el nuevo DNI: ").strip()
            paciente['dni'] = nuevo_valor
            print(f"\n✅ DNI actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "género":
            nuevo_valor = input("Ingrese el nuevo género: ").strip()
            paciente['genero'] = nuevo_valor
            print(f"\n✅ Género actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "fecha_nacimiento":
            nuevo_valor = input("Ingrese la nueva fecha de nacimiento (formato: YYYY-MM-DD): ").strip()
            paciente['fecha_nacimiento'] = nuevo_valor
            print(f"\n✅ Fecha de nacimiento actualizada a: {nuevo_valor}")
        elif dato_a_modificar == "celular":
            nuevo_valor = input("Ingrese el nuevo celular: ").strip()
            paciente['celular'] = nuevo_valor
            print(f"\n✅ Celular actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "email":
            nuevo_valor = input("Ingrese el nuevo email: ").strip()
            paciente['mail'] = nuevo_valor
            print(f"\n✅ Email actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "domicilio":
            nuevo_valor = input("Ingrese el nuevo domicilio: ").strip()
            paciente['domicilio'] = nuevo_valor
            print(f"\n✅ Domicilio actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "salir":
            print("Volviendo al menú principal...")
            return
        else:
            print("❌ Opción no válida. Inténtelo de nuevo o si desea salir ingrese 'salir'.")
            dato_a_modificar = input("\n✍ Escriba el nombre del dato a modificar (ej: Email): ").strip().lower()
            continue


        print("\nVerifique que los datos actualizados sean correctos.")
        mostrar_datos(paciente)
        #Pregunta
        continuar = input("¿Desea continuar  con la modificación de datos? (s/n): ").strip().lower()
        
        if continuar == "s":
            dato_a_modificar = input("\n✍ Escriba el nombre del dato a modificar (ej: Email): ").strip().lower()
        else:
            break #Sale del bucle para confirmar los cambios

        #Confirmacion para guardar los datos modificados
    confirmar = input("¿Desea guardar los cambios? (s/n): ").strip().lower()
    if confirmar == "s":
        p.actualizar_datos(paciente)
        print("✅ Cambios guardados exitosamente en la base de datos.")
    else:
        print("❌ Cambios descartados.")

#-----------------------------------------------------------------
# ----> MENU: <----
#-----------------------------------------------------------------
while True:
        print("*\n \t --- Sistema de Gestion de Pacientes de Centro de Estética ---")
        print("\t 1- Ingresar Nuevo Paciente")
        print("\t 2- Buscar Paciente")
        print("\t 3- Modificar datos")
        print("\t 4- Mostrar Listado Total")  
        print("\t 5- Eliminar datos de Paciente")
        print("\t 6- Salir")

        opcion = input("Seleccione una opcion: ")
        if opcion =="1":
            nuevo_paciente()
        elif opcion =="2":
            print ("\n--- Buscador 🔎---")
            resultado_busqueda() 
        elif opcion =="3":
            modificar()
        elif opcion =="4":
            print (p.mostrar_pacientes()) 
        elif opcion =="5":
            print ("Eliminar datos de paciente")
        elif opcion =="6":
            print("Hasta la próxima!")
            break
        else :
            print("Opción Inválida")