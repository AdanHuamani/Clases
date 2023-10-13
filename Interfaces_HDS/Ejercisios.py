from tkinter import *
ventana=Tk()

Widget_uno=Frame()

Widget_uno.grid(row="100",column="100")
Widget_uno.config(width="100",height="100")
Widget_uno.config(bg="red")

Widget_dos=Frame()

Widget_dos.grid(row="100",column="100")
Widget_dos.config(width="100",height="100")
Widget_dos.config(bg="yellow")

Widget_tres=Frame()

Widget_tres.grid(row="200",column="200")
Widget_tres.config(width="200",height="200")
Widget_tres.config(bg="blue")

Widget_cuatro=Frame()

Widget_cuatro.grid(row="50",column="50")
Widget_cuatro.config(width="50",height="50")
Widget_cuatro.config(bg="orange")

Widget_cinco=Frame()

Widget_cinco.grid(row="50",column="50")
Widget_cinco.config(width="50",height="50")
Widget_cinco.config(bg="black")

Widget_seis=Frame()

Widget_seis.grid(row="0",column="4")
Widget_seis.config(width="50",height="50")
Widget_seis.config(bg="red")

ventana.mainloop()