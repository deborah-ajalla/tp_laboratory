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
persona = {

    "dni": "26896334",
    "nombre": "Luciano",
    "apellido": "Pereyra",
    "genero":  "masculino",
    "fecha_nacimiento": "1980- 09- 21", 
    "celular": "1562358972",
    "mail": "lucianoo@gmail.com",
    "domicilio": "un lugar 123"

}
prueba = p.carga_datos(persona)
print("prueba de carga de paciente")
print(prueba)

# --> pruebo listar <--
# listado = p.mostrar_pacientes()
# print("prueba de listado de paciente")
# print(listado)

# buscar = p.buscar_paciente("26896338")
# print("prueba de buscar un paciente")
# print(buscar)

# --> FUNCIONES <--
#Muestra los datos de paciente 
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
# --- Muestra el Resultado de la busqueda
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
            print("\n\t💡 TIP: Si desea cancelar escriba: \n\t - 1 para 'CANCELAR y GUARDAR' \n\t - 2 para 'CANCELAR y REGRESAR AL MENU PRINCIPAL' 👇")
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

# --- Eliminar Paciente
def eliminar():
    print("\n--- Eliminar Paciente 🗑 ---")
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

        # Sale del bucle si encontró un paciente para continuar con la operación de Eliminar

    while True:
        print(f"\n🛑 ¿Desea eliminar a {paciente['apellido']} {paciente['nombre']}? (s/n): ")
        print("\n⚠ IMPORTANTE: Una vez eliminado, no se podrá recuperar.")
        opcionSelec = input("\n🟡 Ingrese S para 'ELIMINAR' O N para 'CANCELAR': ").strip().lower()
        if opcionSelec == 's':
            respuesta = p.eliminar_paciente(paciente['id'])
            if respuesta['respuesta']:
                print(respuesta['mensaje'])
                print("\n🏠 Regresando al Menú Principal...")
            else:
                print(respuesta['mensaje'])
                print("\n🏠 Regresando al Menú Principal...")
            return
        elif opcionSelec == 'n':
            print("\n🚫 Operación cancelada.")
            print("\n🏠 Regresando al Menú Principal...")
            return
        else:
            print("\n❌ Opción no válida. Inténtelo de nuevo ❌")


#----> MENU: <----
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
            print ("nuevo paciente")
        elif opcion =="2":
            print ("\n--- Buscador 🔎---")
            resultado_busqueda() # --> hacer que se ingrese el dni por teclado!!
        elif opcion =="3":
            modificar()
        elif opcion =="4":
            print (p.mostrar_pacientes()) 
        elif opcion =="5":
            eliminar()
        elif opcion =="6":
            print("Hasta la próxima!")
            break
        else :
            print("Opción Inválida")