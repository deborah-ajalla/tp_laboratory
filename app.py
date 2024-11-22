# --> se realiza una app que..
# --> Funcionalidades:
"""
🔸 Login con usuario y password
🔸 Almacenamiento en BBDD (se utiliza SQLite)
🔸 Se trabaja en una interfaz gráfica
🔸 Se ingresa campos: nombre, apellido, DNI, fecha de nacimiento, género
🔸 Permite realizar CRUD: carga nuevo cliente, muestra lista de usuarios, modifica campos de un registro, y borra un registro.
🔸 Permite la exportación dela info a un archivo txt
🔸 Cierra la ventana de la interfaz- previa confirmación del usuario-
"""
import tkinter as tk
from tkinter import *


# se crea ventana gráfica

ventana = tk.Tk()
ventana.title("Centro de Estética")
ventana.geometry("1000x600+160+50")
ventana.resizable(0,0)

ventana.mainloop()