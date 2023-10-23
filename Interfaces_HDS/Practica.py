from tkinter import*
ventana=Tk()
ventana.geometry("300x350")
ventana.title("Ventana suma")

def capturar_dato():
    Text=Text_nombre.get()
    mensaje=Label(ventana,text=f"Hola,{Text}")
    mensaje.pack()

etiqueta=Label(ventana,text="Introduce tu nombre")
etiqueta.pack()
Text_nombre=Entry(ventana)
Text_nombre.config(bg="blue",fg="white")
Text_nombre.pack()

boton_capturar=Button(ventana,text="Enviar",command=capturar_dato)
boton_capturar.pack()
ventana.mainloop()