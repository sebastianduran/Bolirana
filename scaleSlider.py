from Tkinter import *
ventana=Tk()
ventana.geometry("700x300+200+20")
ventana.title("Ejemplo de scale")
#creando el Scale
scaleBarra=Scale(ventana, label="Temperatura en C",orient=HORIZONTAL).place(x=100,y=100)

ventana.mainloop()
