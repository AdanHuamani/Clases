# Importamos tkinter
from tkinter import *
# Instanciar la clase TK()
ventana=Tk()
# Creo mis dos Widget de orden inferior con la clase frame()
# Instancio mi primer witget
Widget_uno=Frame()
# Usar metodo para mostrar el frame
Widget_uno.grid(row="0",column="0")
Widget_uno.config(width="200",height="300")
Widget_uno.config(bg="red")
# El metodo grid recibe 2 parametros el numero de la columna y el numero de la fila donde quiero colocar mi widget.

# Creacion del segundo widget.
Widget_dos=Frame()
Widget_dos.grid(row="2",column="0")
Widget_dos.config(width="300",height="300")
Widget_dos.config(bg="blue")
# Usar el metodo loop para que la ventana permanesca abierta
ventana.mainloop()
