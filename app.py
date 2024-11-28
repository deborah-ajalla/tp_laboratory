# --> se realiza una app que..
# --> Funcionalidades:
"""
🔸 Login con usuario y password ❌
🔸 Almacenamiento en BBDD (se utiliza SQLite)
🔸 Se trabaja en una interfaz gráfica
🔸 Se ingresa campos: nombre, apellido, DNI, fecha de nacimiento, género, celular, mail
🔸 Permite realizar CRUD: carga nuevo cliente, muestra lista de usuarios, modifica campos de un registro, y borra un registro.
🔸 Permite la exportación dela info a un archivo txt
🔸 Cierra la ventana de la interfaz- previa confirmación del usuario-
"""
import tkinter as tk
from tkinter import *
from tkinter import ttk
#-------------------------------------------
# --> Se define paleta colores 
TITULOS = "#C93384"
SECONDARY = "#B794F4"
PRIMARY = "#ffc1ff"

#---------------------------------------------
# --> Se crea ventana gráfica

ventana = tk.Tk()
ventana.title("Centro de Estética")
ventana.geometry("1000x600+160+50")
ventana.resizable(0,0)
ventana.config(bg= PRIMARY)

etiqueta_titulo = tk.Label(ventana, text="Centro de Estética", font=("Nunito", 26), fg=TITULOS, bg=PRIMARY)
etiqueta_titulo.pack(pady=10)
#----------------------------------------------------------------------------------------
# -->Creacion de la tabla

tabla = ttk.Treeview (ventana, column = ('objetivo', ' cantidad comida', 'horario comida', 'comida preferida', 'comidas no', 'cocinar', 'cantidad agua', 'horas sueño', 'estres', 'estudio/trabajo', 'horas e/t', 'deporte', 'patologias', 'bañp'))
tabla.place(x =0, y = 400, width=1000, height=250)

scroll =ttk.Scrollbar( orient = 'horizontal') #command = self.tabla.xview)
scroll.place(x = 0, y = 630, width =1000)
tabla.configure(xscrollcommand = ventana)
tabla.heading('#0', text = 'Id')
tabla.heading('#1', text = 'nombre')
tabla.heading('#2', text = 'apellido')
tabla.heading('#3', text = 'dni')
tabla.heading('#4', text = 'genero')
tabla.heading('#5', text = 'fecha_nacimiento')
tabla.heading('#6', text = 'celular')
tabla.heading('#7', text = 'mail')

tabla.column ('#0', anchor = 'w', width = 60)
tabla.column ('#1', anchor = 'w', width = 130)
tabla.column ('#2', anchor = 'w', width = 130)
tabla.column ('#3', anchor = 'w', width = 130)
tabla.column ('#4', anchor = 'w', width = 130)
tabla.column ('#5', anchor = 'w', width = 130)
tabla.column ('#6', anchor = 'w', width = 130)
tabla.column ('#7', anchor = 'w', width = 130)


ventana.mainloop()