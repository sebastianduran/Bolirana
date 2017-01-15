from Tkinter import *
ventana = Tk()
ventana.geometry("600x600+0+0")
ventana.title("Menu")
## RECETA PARA CREAR MENUS ##
#1. Crear barra de menu
barraMenu = Menu(ventana)
#2. Crear los menues
menuArchivo = Menu(barraMenu)
#3. Crear los comandos de lo menues
menuArchivo.add_command(label="Abrir")
menuArchivo.add_command(label="Nuevo")
menuArchivo.add_command(label="Guardar")
menuArchivo.add_command(label="Cerrar")
menuArchivo.add_command(label="Salir")
#4. Agregar los menues a la barra de munes
barraMenu.add_cascade(label="Archivo",menu=menuArchivo)
#5. Indicar que la barra de menues estar en la ventana y en que ventana
ventana.config(menu=barraMenu)
ventana.mainloop()
