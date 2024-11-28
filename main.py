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

# ----> FUNCIONES <----
#-----------------------------------------------------------------
# >>> CARGA NUEVO PACIENTE <<<
#-----------------------------------------------------------------
# -- Ingresa datos
def nuevo_paciente ():
    print("-------------------------------- ")
    print("Ingrese los datos del paciente: ")
    print("-------------------------------- ")
    nombre = input ("\n> Nombre: ")
    apellido = input ("> Apellido: ")
    dni = int (input ("> DNI: "))
    genero = input ("> Género: ")
    fecha_nacimiento = input ("> Fecha de Nacimiento: ")
    celular = input ("> Celular: ")
    mail = input ("> Email: ")
    domicilio = input ("> Domicilio: ")

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

    dni_buscado = input("\n🟢 Ingrese el DNI del paciente: ")

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
# --- Modifica los datos
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
            print("\n🏠 Regresando al Menú Principal...")
            return  
        else:
            print("\n❌ Opción no válida. Inténtelo de nuevo.")
            continue

        # Sale del bucle si encontró un paciente para continuar con la operación de modificar datos
    
    dato_a_modificar = input("\n✍  Escriba el nombre del dato a modificar (ej: Email): ").strip().lower()
    datos_modificados = False
    # Modificar valores según el dato introducido 
    while True:
        if dato_a_modificar == "nombre":
            nuevo_valor = input("\n🟢 Ingrese el nuevo nombre: ").strip()
            paciente['nombre'] = nuevo_valor
            datos_modificados = True
            print(f"\n✅ Nombre actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "apellido":
            nuevo_valor = input("\n🟢 Ingrese el nuevo apellido: ").strip()
            paciente['apellido'] = nuevo_valor
            datos_modificados = True
            print(f"\n✅ Apellido actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "dni":
            nuevo_valor = input("\n🟢 Ingrese el nuevo DNI: ").strip()
            paciente['dni'] = nuevo_valor
            datos_modificados = True
            print(f"\n✅ DNI actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "género" or dato_a_modificar == "genero":
            nuevo_valor = input("\n🟢 Ingrese el nuevo género: ").strip()
            paciente['genero'] = nuevo_valor
            datos_modificados = True
            print(f"\n✅ Género actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "fecha_nacimiento":
            nuevo_valor = input("\n🟢 Ingrese la nueva fecha de nacimiento (formato: YYYY-MM-DD): ").strip()
            paciente['fecha_nacimiento'] = nuevo_valor
            datos_modificados = True
            print(f"\n✅ Fecha de nacimiento actualizada a: {nuevo_valor}")
        elif dato_a_modificar == "celular":
            nuevo_valor = input("\n🟢 Ingrese el nuevo celular: ").strip()
            paciente['celular'] = nuevo_valor
            datos_modificados = True
            print(f"\n✅ Celular actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "email":
            nuevo_valor = input("\n🟢 Ingrese el nuevo email: ").strip()
            paciente['mail'] = nuevo_valor
            datos_modificados = True
            print(f"\n✅ Email actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "domicilio":
            nuevo_valor = input("\n🟢 Ingrese el nuevo domicilio: ").strip()
            paciente['domicilio'] = nuevo_valor
            datos_modificados = True
            print(f"\n✅ Domicilio actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "1" or dato_a_modificar == "2":
            if dato_a_modificar == "2":
                print("\n❌ Operación cancelada.")
                print("\n🏠 Regresando al menú principal...")
                return
            elif not datos_modificados:
                print("\n❌ No has realizado ninguna modificación.")
                print("\n🏠 Regresando al menú principal...")
                return
        else:
            print("\n❌ Opción no válida. Inténtelo de nuevo.")
            print("\n\t💡 TIP: Si desea cancelar escriba: \n\t - 1 para 'CANCELAR y GUARDAR' \n\t - 2 para CANCELAR y REGRESAR AL MENU PRINCIPAL 👇")
            dato_a_modificar = input("\n✍  Escriba el nombre del dato a modificar (ej: Email): ").strip().lower()
            continue

        print("\nVerifique que los datos actualizados sean correctos 👇")
        mostrar_datos(paciente)
        continuar_modificando = True

        #Pregunta
        while True:
            continuar = input("\n🛑 ¿Desea continuar con la modificación de datos? (s/n): ").strip().lower()
            if continuar == "s":
                dato_a_modificar = input("\n✍  Escriba el nombre del dato a modificar (ej: Email): ").strip().lower()
                break
            elif continuar == "n":
                continuar_modificando = False
                break
            else:
                print("\n❌ Opción no válida. Inténtelo de nuevo.")

        #Confirmacion para guardar los datos modificados
        if not continuar_modificando:

            while True: #Únicamente acepta s o n como opciones válidas
                confirmar = input("\n🛑 ¿Desea guardar los cambios? (s/n): ").strip().lower()
                if confirmar == "s":
                    resultado = p.actualizar_datos(paciente)
                    if resultado["respuesta"]:
                        print(resultado['mensaje'])
                        print("\n🏠 Regresando al menú principal...")
                        return
                    else:
                        print(f"\n❌ No se pudo guardar los cambios: {resultado['mensaje']}")
                    break 
                elif confirmar == "n":
                    print("\n❌ Cambios descartados.")
                    print("\n🏠 Regresando al menú principal...")
                    return
                else:
                    print("\n❌ Opción no válida. Ingrese S para GUARDAR o N para DESCARTAR.")

#-----------------------------------------------------------------
# >>> MENU: <<<
#-----------------------------------------------------------------
while True:
        print("\n  >>>>>  Sistema de Gestion de Pacientes de Centro de Estética  <<<<<\n")
        print("\t\t 1- Ingresar Nuevo Paciente")
        print("\t\t 2- Buscar Paciente")
        print("\t\t 3- Modificar datos")
        print("\t\t 4- Mostrar Listado Total")  
        print("\t\t 5- Eliminar datos de Paciente")
        print("\t\t 6- Salir")

        opcion = input("--> Seleccione una opcion: ")
        if opcion =="1":
            nuevo_paciente()
        elif opcion =="2":
            print ("\n--- Buscador 🔎 ---")
            resultado_busqueda() 
        elif opcion =="3":
            modificar()
        elif opcion =="4":
            print (p.mostrar_pacientes()) 
        elif opcion =="5":
            p.eliminar_paciente()
        elif opcion =="6":
            print("⏩ Hasta la próxima!!!⏪")
            break
        else :
            print("Opción Inválida")