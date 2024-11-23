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

#----> MENU: <----
while True:
        print("*\n \t --- Sistema de Gestion de Pacientes de Centro de Estética ---")
        print("\t 1- Ingresar Nuevo Paciente")
        print("\t 2- Buscar Paciente")
        print("\t 3- Modificar datos")
        print("\t 4- Mostrar Listado Total")  
        print("\t 5- Eliminar datos de Paciente")
        print("\t 6- Salir")

        opcion= input("Seleccione una opcion: ")
        if opcion =="1":
           print ("nuevo paciente")
        elif opcion =="2":

            print (p.buscar_paciente("26896332"))  # --> hacer que se ingrese el dni por teclado!!
        elif opcion =="3":
            print ("Modificar datos")
        elif opcion =="4":
            print (p.mostrar_pacientes()) 
        elif opcion =="5":
            print ("Eliminar datos de paciente")
        elif opcion =="6":
            print("Hasta la próxima!")
            break
        else :
            print("Opción Inválida")
          