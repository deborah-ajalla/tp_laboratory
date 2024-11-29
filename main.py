import conexion as c
import paciente_datos as p
import validar_datos as v

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
def nuevo_paciente():
    print("-------------------------------- ")
    print("💠 Ingrese los datos del paciente: ")
    print("-------------------------------- ")
   # Validación de datos
    nombre = input("\n🟢 Nombre: ").strip()
    nombre = v.validar_entrada(nombre, "^[a-zA-ZáéíóúÁÉÍÓÚ ]+$", "\n🟠 Ingrese un nombre válido (solo letras y espacios): ")

    apellido = input("\n🟢 Apellido: ").strip()
    apellido = v.validar_entrada(apellido, "^[a-zA-ZáéíóúÁÉÍÓÚ ]+$", "\n🟠 Ingrese un apellido válido (solo letras y espacios): ")

    dni = input("\n🟢 DNI: ").strip()
    dni = v.validar_entrada(dni, "^[0-9]{7,8}$", "\n🟠 Ingrese un DNI válido (solo números, 7 u 8 dígitos): ")

    genero = input("\n🟢 Género: ").strip()
    genero = v.validar_entrada(genero, "^[MF]$", "\n🟠 Ingrese un género válido (M/F): ").upper()

    mensaje = {
    "fecha_nacimiento": "\n🟢 Fecha de Nacimiento (DD/MM/YYYY): "
    }
    fecha_nacimiento = v.validar_fecha_nacimiento(mensaje)
    
    # fecha_nacimiento = input("\n🟢 Fecha de Nacimiento (YYYY-MM-DD): ").strip()
    # fecha_nacimiento = v.validar_entrada(fecha_nacimiento, "^\d{4}-\d{2}-\d{2}$", "\n🟠 Ingrese una fecha válida (YYYY-MM-DD): ")

    celular = input("\n🟢 Celular: ").strip()
    celular = v.validar_entrada(celular, "^[0-9]{10}$", "\n🟠 Ingrese un celular válido (solo números de 10 dígitos): ")

    mail = input("\n🟢 Email: ").strip()
    mail = v.validar_entrada(mail, "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", "\n🟠 Ingrese un correo electrónico válido: ")

    domicilio = input("\n🟢 Domicilio: ").strip()
    domicilio = v.validar_entrada(domicilio, "^[a-zA-Z0-9\s]+$", "\n🟠 Ingrese un domicilio válido (letras, números y espacios): ")


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

    repetido = p.buscar_paciente(nuevo_p['dni'])
    while True:
        if repetido['respuesta']:
            print("\n❌ DNI REPETIDO")
            dni = input("\n🟠 Ingrese otro DNI:").strip()
            nuevo_p['dni'] = dni
            repetido = p.buscar_paciente(nuevo_p['dni'])
        else:
            break

    nuevo_paciente = p.carga_datos(nuevo_p)
    if nuevo_paciente['respuesta']:
        print(nuevo_paciente['mensaje'])
    else:
        print(nuevo_paciente['mensaje'])

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
            nuevo_valor = v.validar_entrada(nuevo_valor, "^[a-zA-ZáéíóúÁÉÍÓÚ ]+$", "\n🟠 Ingrese un nombre válido (solo letras y espacios): ")
            paciente['nombre'] = nuevo_valor
            datos_modificados = True
            print(f"\n✅ Nombre actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "apellido":
            nuevo_valor = input("\n🟢 Ingrese el nuevo apellido: ").strip()
            nuevo_valor = v.validar_entrada(nuevo_valor, "^[a-zA-ZáéíóúÁÉÍÓÚ ]+$", "\n🟠 Ingrese un apellido válido (solo letras y espacios): ")
            paciente['apellido'] = nuevo_valor
            datos_modificados = True
            print(f"\n✅ Apellido actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "dni":
            nuevo_valor = input("\n🟢 Ingrese el nuevo DNI: ").strip()
            nuevo_valor = v.validar_entrada(nuevo_valor, "^[0-9]{7,8}$", "\n🟠 Ingrese un DNI válido (solo números, 7 u 8 dígitos): ")
            paciente['dni'] = nuevo_valor
            datos_modificados = True
            print(f"\n✅ DNI actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "genero" or dato_a_modificar == "género":
            nuevo_valor = input("\n🟢 Ingrese el nuevo género (M/F): ").strip()
            nuevo_valor = v.validar_entrada(nuevo_valor, "^[MF]$", "\n🟠 Ingrese un género válido (M/F): ")
            paciente['genero'] = nuevo_valor
            datos_modificados = True
            print(f"\n✅ Género actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "fecha de nacimiento":
            mensaje = {
                "fecha_nacimiento": "\n🟢 Fecha de Nacimiento (DD/MM/YYYY): "
            }
            nuevo_valor = v.validar_fecha_nacimiento(mensaje)
            paciente['fecha_nacimiento'] = nuevo_valor
            datos_modificados = True
            print(f"\n✅ Fecha de nacimiento actualizada a: {nuevo_valor}")
        elif dato_a_modificar == "celular":
            nuevo_valor = input("\n🟢 Ingrese el nuevo celular: ").strip()
            nuevo_valor = v.validar_entrada(nuevo_valor, "^[0-9]{10}$", "\n🟠 Ingrese un celular válido (solo números de 10 dígitos): ")
            paciente['celular'] = nuevo_valor
            datos_modificados = True
            print(f"\n✅ Celular actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "email":
            nuevo_valor = input("\n🟢 Ingrese el nuevo email: ").strip()
            nuevo_valor = v.validar_entrada(nuevo_valor, "^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$", "\n🟠 Ingrese un correo electrónico válido: ")
            paciente['mail'] = nuevo_valor
            datos_modificados = True
            print(f"\n✅ Email actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "domicilio":
            nuevo_valor = input("\n🟢 Ingrese el nuevo domicilio: ").strip()
            nuevo_valor = v.validar_entrada(nuevo_valor, "^[a-zA-Z0-9\s]+$", "\n🟠 Ingrese un domicilio válido (letras, números y espacios): ")
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
            print("\n\t💡 TIP: Si desea cancelar escriba: \n\t - 1 para CANCELAR y GUARDAR \n\t - 2 para CANCELAR y REGRESAR AL MENU PRINCIPAL 👇")
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
#--------------------------- FIN FUNCION MODIFICAR --------------------------------------

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
#------------------------ FIN FUNCION ELIMINAR-----------------------------------------

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
            respuesta = p.mostrar_pacientes()
            if respuesta['respuesta']:
            #Tabla para mostrar los datos de los pacientes
                # Encabezados
                headers = ["ID", "Nombre", "Apellido", "DNI", "Género", "Fecha Nac.", "Celular", "Email", "Domicilio"]
                # Define el ancho de las columnas: ':<' == ancho máximo y el número == cantidad de caractes de espacio
                formato = "{:<3} {:<10} {:<10} {:<10} {:<10} {:<12} {:<12} {:<25} {:<20}"
                print(formato.format(*headers))# Imprime encabezados
                print("-" * 110)#Inserta guiones al final de la tabla
                # Imprime los pacientes
                for paciente in respuesta['pacientes']:
                    print(formato.format(*paciente))
                print("-" * 110)
                print(respuesta['mensaje'])
            else:
                print(respuesta['mensaje'])
        elif opcion =="5":
            eliminar()
        elif opcion =="6":
            print("⏩ Hasta la próxima!!!⏪")
            break
        else :
            print("Opción Inválida")