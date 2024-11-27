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
    "dni": "26896332",
    "nombre": "Pablo",
    "edad": "abcd",
    "apellido": "Torrez",
    "genero":  "masculino",
    "celular": "1562358970",
    "mail": "algo6@gmail.com"
}
prueba = p.carga_datos(persona)
print("prueba de carga de paciente")
print(prueba)

# --> pruebo listar <--
# listado = p.mostrar_pacientes()
# print("prueba de listado de paciente")
# print(listado)

buscar = p.buscar_paciente("26896338")
print("prueba de buscar un paciente")
print(buscar)

# --> FUNCIONES <--
#Muestra los datos de paciente 
def mostrarDatos(paciente):
    print(f"\t ID: {paciente['id']}")
    print(f"\t Nombre: {paciente['nombre']}")
    print(f"\t Apellido: {paciente['apellido']}")
    print(f"\t DNI: {paciente['dni']}")
    print(f"\t Género: {paciente['género']}")
    print(f"\t Edad: {paciente['edad']}")
    #print(f"\t Fecha de Nacimiento: {paciente['fecha_nacimiento']}")
    print(f"\t Celular: {paciente['celular']}")
    print(f"\t Email: {paciente['mail']}")

# --- Muestra el Resultado de la busqueda
def resultadoBusqueda():
    dni_buscado = input("Ingrese el DNI del paciente: ")
    resultado = p.buscar_paciente(dni_buscado)  

    if resultado["respuesta"]: 
        paciente = resultado["persona"]
        print("\n--- Resultado de la Búsqueda 👇")
        mostrarDatos(paciente)
        return paciente
    else: 
        print("\n--- Resultado de la Búsqueda 👇")
        print(resultado["mensaje"])
        return None  # Retorna None si no se encuentra el paciente
# --- Modifica los datos
def modificar():
    print("\n--- Modificación de Datos 📝 ---")
    paciente = resultadoBusqueda()

    while not paciente:  # En caso de no encontrar coindidencias busca un paciente hasta que el usuario decida salir
        print("¿Qué desea hacer?")
        print("\t 1- Buscar otro paciente")
        print("\t 2- Regresar al Menú Principal")
        seleccionado = input("\nSeleccione una opción: ").strip()
            
        if seleccionado == "1":
            paciente = resultadoBusqueda()
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
            paciente['género'] = nuevo_valor
            print(f"\n✅ Género actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "edad":
            nuevo_valor = input("Ingrese la nueva edad: ").strip()
            paciente['edad'] = int(nuevo_valor)
            print(f"\n✅ Edad actualizada a: {nuevo_valor}")
        elif dato_a_modificar == "celular":
            nuevo_valor = input("Ingrese el nuevo celular: ").strip()
            paciente['celular'] = nuevo_valor
            print(f"\n✅ Celular actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "email":
            nuevo_valor = input("Ingrese el nuevo email: ").strip()
            paciente['mail'] = nuevo_valor
            print(f"\n✅ Email actualizado a: {nuevo_valor}")
        elif dato_a_modificar == "salir":
            print("Volviendo al menú principal...")
            return
        else:
            print("❌ Opción no válida. Inténtelo de nuevo o si desea salir ingrese 'salir'.")
            dato_a_modificar = input("\n✍ Escriba el nombre del dato a modificar (ej: Email): ").strip().lower()
            continue


        print("\nVerifique que los datos actualizados sean correctos.")
        mostrarDatos(paciente)
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
            resultadoBusqueda() # --> hacer que se ingrese el dni por teclado!!
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