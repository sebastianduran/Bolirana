import sys
from Tkinter import *

app = Tk();
app.title("Ventana con grillas")

vp = Frame(app)
vp.grid(column=0, row=0, padx=(50,50), pady=(10,10))
vp.columnconfigure(0,weight=1)
vp.rowconfigure(0,weight=1)

Jugador1Activo = Label(vp, text="JUGADOR 1", bg='#ffffff', bd='2m')
Jugador1Activo.grid(column=1, row=1)

Jugador2Activo = Label(vp, text="JUGADOR 2", bg='#ffff1f', bd='2m')
Jugador2Activo.grid(column=2, row=1)

Jugador3Activo = Label(vp, text="JUGADOR 3", bg='#ffff0f', bd='2m')
Jugador3Activo.grid(column=3, row=1)

app.mainloop()
