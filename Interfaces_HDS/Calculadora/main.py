from tkinter import*
from funciones import*
# root=Tk()
# root.geometry("300x300")

# frameL=LabelFrame(root,text="cuadro",padx=20,pady=20)
# frameL.config(width=200,height=200)
# frameL.pack(pady=15)

# Variable=1
# texto=Entry(frameL,width=20)
# texto.insert(0,str(Variable)+"Mundo")
# texto.pack()

# root.mainloop()
#######################################################################
# Configuracion de 
root=Tk()
root.title("Calculadora")
root.geometry("330x300")
root.resizable(0,0)
####
fuente_general=("arial",8,"bold")
# pantalla que muestra los numeoros ingresados y el resultado
pantalla=Entry(root,
               width=22,
               bg="black", # Asigna el color de fondo
               fg="white", # Asigna el color de letra
               borderwidth=2, # Asigna el tamaño de borde de mi cuadro de texto
               font=("arial",18,"bold")) # con este formato asignamos el tamaño de fuente
pantalla.grid(row=0,columnspan=5,padx=4,pady=4)
########################################################
#Añadir los botones de mi calculadora
boton_1=Button(root,text="1",
               width=9, #Ancho
               height=3, #Altura
               bg="white", #Para color de fondo
               fg="red", #Para color de texto
               borderwidth=0,
               cursor="hand1",
               font=fuente_general,
               command=lambda:enviar_boton(1,pantalla)).grid(row=1,column=1,padx=1,pady=1) #Sirve para cambiar el estilo del mouse.

boton_2=Button(root,text="2",
               width=9, #Ancho
               height=3, #Altura
               bg="white", #Para color de fondo
               fg="red", #Para color de texto
               borderwidth=0,
               cursor="hand1",
               font=fuente_general).grid(row=2,column=1,padx=1,pady=1) #Sirve para cambiar el estilo del mouse.

boton_3=Button(root,text="3",
               width=9, #Ancho
               height=3, #Altura
               bg="white", #Para color de fondo
               fg="red", #Para color de texto
               borderwidth=0,
               cursor="hand1",
               font=fuente_general).grid(row=3,column=1,padx=1,pady=1) #Sirve para cambiar el estilo del mouse.

boton_4=Button(root,text="4",
               width=9, #Ancho
               height=3, #Altura
               bg="white", #Para color de fondo
               fg="red", #Para color de texto
               borderwidth=0,
               cursor="hand1",
               font=fuente_general).grid(row=1,column=2,padx=1,pady=1) #Sirve para cambiar el estilo del mouse.

boton_5=Button(root,text="5",
               width=9, #Ancho
               height=3, #Altura
               bg="white", #Para color de fondo
               fg="red", #Para color de texto
               borderwidth=0,
               cursor="hand1",
               font=fuente_general).grid(row=2,column=2,padx=1,pady=1) #Sirve para cambiar el estilo del mouse.

boton_6=Button(root,text="6",
               width=9, #Ancho
               height=3, #Altura
               bg="white", #Para color de fondo
               fg="red", #Para color de texto
               borderwidth=0,
               cursor="hand1",
               font=fuente_general).grid(row=3,column=2,padx=1,pady=1) #Sirve para cambiar el estilo del mouse.

boton_7=Button(root,text="7",
               width=9, #Ancho
               height=3, #Altura
               bg="white", #Para color de fondo
               fg="red", #Para color de texto
               borderwidth=0,
               cursor="hand1",
               font=fuente_general).grid(row=1,column=3,padx=1,pady=1) #Sirve para cambiar el estilo del mouse.

boton_8=Button(root,text="8",
               width=9, #Ancho
               height=3, #Altura
               bg="white", #Para color de fondo
               fg="red", #Para color de texto
               borderwidth=0,
               cursor="hand1",
               font=fuente_general).grid(row=2,column=3,padx=1,pady=1) #Sirve para cambiar el estilo del mouse.

boton_9=Button(root,text="9",
               width=9, #Ancho
               height=3, #Altura
               bg="white", #Para color de fondo
               fg="red", #Para color de texto
               borderwidth=0,
               cursor="hand1",
               font=fuente_general).grid(row=3,column=3,padx=1,pady=1) #Sirve para cambiar el estilo del mouse.

boton_0=Button(root,text="0",
               width=9, #Ancho
               height=3, #Altura
               bg="white", #Para color de fondo
               fg="red", #Para color de texto
               borderwidth=0,
               cursor="hand1",
               font=fuente_general).grid(row=4,column=2,padx=1,pady=1) #Sirve para cambiar el estilo del mouse.
#Boton Igual
boton_igual=Button(root,text="=",
               width=9, #Ancho
               height=3, #Altura
               bg="blue", #Para color de fondo
               fg="red", #Para color de texto
               borderwidth=0,
               cursor="hand1",
               font=fuente_general).grid(row=4,column=1,padx=1,pady=1) #Sirve para cambiar el estilo del mouse.
#Boton del punto
boton_punto=Button(root,text=".",
               width=9, #Ancho
               height=3, #Altura
               bg="orange", #Para color de fondo
               fg="red", #Para color de texto
               borderwidth=0,
               cursor="hand1",
               font=fuente_general).grid(row=4,column=3,padx=1,pady=1) #Sirve para cambiar el estilo del mouse.
#Bontones de operaciones:
boton_Mas=Button(root,text="+",
               width=9, #Ancho
               height=3, #Altura
               bg="white", #Para color de fondo
               fg="red", #Para color de texto
               borderwidth=0,
               cursor="hand1",
               font=fuente_general).grid(row=1,column=4,padx=1,pady=1) #Sirve para cambiar el estilo del mouse.
boton_menos=Button(root,text="-",
               width=9, #Ancho
               height=3, #Altura
               bg="white", #Para color de fondo
               fg="red", #Para color de texto
               borderwidth=0,
               cursor="hand1",
               font=fuente_general).grid(row=2,column=4,padx=1,pady=1) #Sirve para cambiar el estilo del mouse.
boton_Mutiplicacion=Button(root,text="*",
               width=9, #Ancho
               height=3, #Altura
               bg="white", #Para color de fondo
               fg="red", #Para color de texto
               borderwidth=0,
               cursor="hand1",
               font=fuente_general).grid(row=3,column=4,padx=1,pady=1) #Sirve para cambiar el estilo del mouse.
boton_division=Button(root,text="/",
               width=9, #Ancho
               height=3, #Altura
               bg="white", #Para color de fondo
               fg="red", #Para color de texto
               borderwidth=0,
               cursor="hand1",
               font=fuente_general).grid(row=4,column=4,padx=1,pady=1) #Sirve para cambiar el estilo del mouse.

root.mainloop()
