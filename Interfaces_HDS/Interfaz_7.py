# from tkinter import *
# def calcular():
#     n1=num_1.get()
#     n2=num_2.get()
#     op=opcion.get()
#     if op==1:
#         total.set(n1+n2)
#     elif op==2:
#         total.set(n1-n2)
#     elif op==3:
#         total.set(n1*n2)
#     elif op==4:
#         total.set(n1/n2)
# def limpiar():
#     num_1.delete(0,END)
#     num_2.delete(0,END)
#     total.delete(0,END)
# # Ventana
# ventana=Tk()
# num_1=DoubleVar()
# num_2=DoubleVar()
# total=DoubleVar()
# limp=DoubleVar()
# opcion=IntVar()
# cuadro_texto=DoubleVar
# ventana.geometry("300x250")
# ventana.title("Calculadora")
# # Etiquetas:
# etiqueta1 = Label(ventana,text="Ingrese un numero: ")
# etiqueta1.place(x=20,y=20)
# etiqueta2 = Label(ventana,text="Ingrese un numero: ")
# etiqueta2.place(x=20,y=60)
# etiquetaT = Label(ventana,text="Total: ",)
# etiquetaT.place(x=20,y=100)

# # Cuadros de texto
# cuadro_1=Entry(ventana,textvariable=num_1)
# cuadro_1.place(x=20,y=40)
# cuadro_2=Entry(ventana,textvariable=num_2)
# cuadro_2.place(x=20,y=80)
# cuadro_T=Entry(ventana,textvariable=total,)
# cuadro_T.place(x=20,y=120)
# #Botones
# boton_calcular=Button(ventana,text="calcular",command=calcular)
# boton_calcular.place(x=60,y=180)
# boton_limpiar=Button(ventana,text="Limpiar",command=limpiar)
# boton_limpiar.place(x=140,y=180)
# # RADIO BOTONES
# radio1=Radiobutton(ventana,text="Suma",value=1,variable=opcion)
# radio1.place(y=40,x=190)

# radio2=Radiobutton(ventana,text="Resta",value=2,variable=opcion)
# radio2.place(y=60,x=190)

# radio3=Radiobutton(ventana,text="Multiplicacion",value=3,variable=opcion)
# radio3.place(y=80,x=190)

# radio4=Radiobutton(ventana,text="Division",value=4,variable=opcion)
# radio4.place(y=100,x=190)

# ventana.mainloop()

#################################################################
