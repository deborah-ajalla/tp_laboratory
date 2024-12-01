import re
import datetime
import paciente_datos as p

def validar_entrada(entrada, patron, mensaje_error):
    while not re.match(patron, entrada):
        print(mensaje_error)
        entrada = input()
    return entrada

def cargar_datos():
    mensajes_error = {
        "nombre": "Ingrese un nombre válido (solo letras): ",
        "apellido": "Ingrese un apellido válido (solo letras): ",
        "dni": "Ingrese un DNI válido (solo números, 7 u 8 dígitos): ",
        "genero": "Ingrese un género válido (M/F): ",
        "fecha_nacimiento": "Ingrese una fecha de nacimiento válida (DD/MM/AAAA): ",
        "motivo_consulta": "Ingrese un motivo de consulta válido (solo letras y espacios): ",
        "tratamiento": "Ingrese un tratamiento válido (solo letras): ",
        "domicilio": "Ingrese un domicilio válido (letras, números): "
}
    
    dnis_registrados = []  # Lista para almacenar los DNIs ingresados


    nombre = validar_entrada(input("Ingrese el nombre del paciente: ").title(), "^[a-zA-ZáéíóúÁÉÍÓÚ ]{2,}$", mensajes_error["nombre"])
    apellido = validar_entrada(input("Ingrese el apellido del paciente: ").title(), "^[a-zA-ZáéíóúÁÉÍÓÚ ]{2,}$", mensajes_error["apellido"])
        
     # Validación de DNI y almacenamiento en la lista
    dni = validar_entrada(input("Ingrese el DNI del paciente: "), "^[0-9]{7,8}$", mensajes_error["dni"])
    while dni in dnis_registrados:
        print("El DNI ya está registrado. Ingrese otro DNI.")
        dni = validar_entrada(input("Ingrese el DNI del paciente: "), "^[0-9]{7,8}$", mensajes_error["dni"])
    dnis_registrados.append(dni)


    genero = validar_entrada(input("Ingrese el género del paciente (M/F): ").upper(), "^[MF]$", mensajes_error["genero"])
    domicilio = validar_entrada(input(mensajes_error["domicilio"]), "^[a-zA-Z0-9\s]+$", mensajes_error["domicilio"])

    # Validación fecha de nacimiento 
    while True:
        fecha_nacimiento = input(mensajes_error["fecha_nacimiento"])
        try:
            fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
            if fecha_nacimiento > datetime.date.today():
                print("La fecha de nacimiento no puede ser en el futuro.")
            else:
                break
        except ValueError:
            print("Fecha inválida. Intente nuevamente.")

    motivo_consulta = validar_entrada(input("Ingrese el motivo de consulta del paciente: "), "^[a-zA-ZáéíóúÁÉÍÓÚ ]+$", mensajes_error["motivo_consulta"])
    tratamiento = validar_entrada(input("Ingrese el tratamiento del paciente: "), "^[a-zA-ZáéíóúÁÉÍÓÚ ]+$", mensajes_error["tratamiento"])

def validar_fecha_nacimiento(mensajes_error):

  while True:
    fecha_nacimiento = input(mensajes_error["fecha_nacimiento"])
    try:
      fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d/%m/%Y").date()
      if fecha_nacimiento > datetime.date.today():
        print("\n❌ La fecha de nacimiento no puede ser en el futuro.")
      else:
        return fecha_nacimiento
    except ValueError:
      print("\n🟠 Fecha inválida. Intente nuevamente por favor.")

#---funcion validar dni repetido
# def dni_repetido(numero, modificar):
#     repetido = p.buscar_paciente(numero)
#     while repetido['respuesta']: 
#         if modificar: 
#             print("\n❌ El DNI ingresado ya está registrado en el sistema. Por favor, verifique si pertenece al actual paciente.")
#             respuesta = input("\n🛑 ¿Desea cancelar la modificación? (s/n): ").strip()
#             while respuesta not in ('s', 'n'): 
#                 print("\n❌ Opción no válida. Inténtelo de nuevo.")
#                 respuesta = input("\n🛑 ¿Desea cancelar la modificación? (s/n): ").strip()
#             if respuesta == 's':
#                 print("\n✅ Modificación de DNI CANCELADA.")
#                 return  numero
#         # Solo se ingresa n
#         dni = input("\n🟠 Ingrese otro DNI: ").strip()
#         dni = validar_entrada(dni, "^[0-9]{7,8}$", "\n🟠 Ingrese un DNI válido (solo números, 7 u 8 dígitos): ")
#         repetido = p.buscar_paciente(dni)
#     return dni
