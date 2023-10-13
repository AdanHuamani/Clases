# 1. Import tkinter -> libreria para la creacion de interfaces graficas.
from tkinter import *
# 2. La libreria tkinter tiene 3 grandes clases para la creacion de interfaces.
# TK -> Es la mas usada
# TKK() -> Tiene mas herramientas y es poco mas complicado.
# TCL() -> Tiene mas herramientas y es poco mas complicado.

# 3. Instanciar TK() como generador de interfaz grafica.
nueva_ventana=Tk()
# 4. Frame es tambien es una clase, Frame() para crear un frame tengo que instanciar primero.
menu_principal=Frame()
# Montamos o Inicializamos el frame
menu_principal.pack()
# Haciendo uso del metodo config le damos un tamaño
menu_principal.config(width="200",height="200")
# Haciendo uso del config le asignamos un color
menu_principal.config(background="blue")
 
# Metodo de TK() que mantiene la ejecucion del programa en un bucle.
nueva_ventana.mainloop()