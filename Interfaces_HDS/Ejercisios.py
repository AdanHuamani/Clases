from tkinter import *
ventana=Tk()

Widget_uno=Frame()

Widget_uno.grid(row="0",rowspan="2",column="0") 
Widget_uno.config(width="50",height="100")
Widget_uno.config(bg="purple")

Widget_dos=Frame()

Widget_dos.grid(row="0",column="1")
Widget_dos.config(width="50",height="50")
Widget_dos.config(bg="yellow")

Widget_tres=Frame()

Widget_tres.grid(row="2",column="0")
Widget_tres.config(width="50",height="50")
Widget_tres.config(bg="blue")

Widget_cuatro=Frame()

Widget_cuatro.grid(row="2",column="1")
Widget_cuatro.config(width="50",height="50")
Widget_cuatro.config(bg="orange")

Widget_cinco=Frame()

Widget_cinco.grid(row="1",column="1")
Widget_cinco.config(width="50",height="50")
Widget_cinco.config(bg="black")

Widget_seis=Frame()

Widget_seis.grid(row="4",column="0",columnspan="4")
Widget_seis.config(width="100",height="50")
Widget_seis.config(bg="red")

ventana.mainloop()

