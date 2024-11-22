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

#----> MENU: <----
while True:
        print("*\n \t --- Sistema de Gestion de Pacientes de Centro de Estética ---")
        print("\t 1- Ingresar Nuevo Paciente")
        print("\t 2- Modificar datos de Paciente ")
        print("\t 3- Mostrar datos de Paciente")
        print("\t 4- Eliminar datos de Paciente")
        print("\t 5- Salir")

        opcion= input("Seleccione una opcion: ")
        if opcion =="1":
           print ("nuevo paciente")
        elif opcion =="2":
            print ("modificar datos de paciente")
        elif opcion =="3":
            print ("Mostrar datos de paciente")
        elif opcion =="4":
            print ("eliminar datos de paciente")
        elif opcion =="5":
            print("Hasta la próxima!")
            break
        else :
            print("Opción Inválida")
          