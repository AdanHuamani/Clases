# importamos Tkinter
# from tkinter import *
# # Instanciar la clase TK
# ventana=Tk()
# ventana.geometry("200x200")
# # Creo mis dos witget de orden inferior con la clase flame()
# Widget_uno=Frame()
# Widget_uno.grid(row=0,column=0)
# Widget_uno.config(width=200,height=200)
# # Creacion de Etiquetas
# etiqueta=Label(ventana,text="Hola ADAN")
# etiqueta.grid(row=1,column=0)
# # Crear cuadros de texto.
# cuadro_texto=Entry()
# cuadro_texto.grid(row=2,column=0)
# # Usar el metodo Loop para que la vantan sea imprimido
# ventana.mainloop()

## NUEVO EJEMPLO
from tkinter import *
ventana=Tk()
ventana.geometry("200x200")
Widget_uno=Frame()
Widget_uno.grid(row=0,column=0)
Widget_uno.config(width=100,height=100)
etiqueta=Label(ventana,text="Hola ADAN")
etiqueta.grid(row=1,column=0)
cuadro_texto=Entry()
cuadro_texto.grid(row=2,column=0)
Widget_dos=Frame()
Widget_dos.grid(row=3,column=0)
Widget_dos.config(width=200,height=200)
ventana.mainloop()
