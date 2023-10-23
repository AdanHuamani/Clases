# from tkinter import*
# ventana=Tk()
# ventana.geometry("300x350")
# ventana.title("Ventana Edad")

# def capturar_dato():
#     Text=int(Text_edad.get())
#     nombre=Text_nombre
#     if Text>=18:
#         mensaje=Label(ventana,text=f"!Hola¡ Eres Mayor de edad,{nombre}")
#         mensaje.pack()
    
#     else:   
#         mensaje=Label(ventana,text=f"!Hola¡ Eres Menor de edad,{nombre}")
#         mensaje.pack()

# etiqueta=Label(ventana,text="Ingresa tu Nombre: ")
# etiqueta.pack()
# Text_nombre=Entry(ventana)
# Text_nombre.config(bg="blue",fg="white")
# Text_nombre.pack()

# etiqueta=Label(ventana,text="Ingresa tu Edad: ")
# etiqueta.pack()
# Text_edad=Entry(ventana)
# Text_edad.config(bg="blue",fg="white")
# Text_edad.pack()

# boton_capturar=Button(ventana,text="Enviar",command=capturar_dato)
# boton_capturar.pack()
# ventana.mainloop()

## 4
from tkinter import *

ventana = Tk()
ventana.geometry("300x300")
ventana.title("Formulario")

def verificar_usuario_contraseña():
    usuario = text_usuario.get()
    contraseña = text_contraseña.get()
    
    if usuario == contraseña:
        resultado = "Su Usuario y Contraseña son correctos."
    else:
        resultado = "Su Usuario y Contraseña no son correctos, vuelve a intentarlo."
    
    mensaje.config(text=resultado)

etiqueta_usuario = Label(ventana, text="Introduce tu usuario:")
etiqueta_usuario.pack()

text_usuario = Entry(ventana)
text_usuario.pack()

etiqueta_contraseña = Label(ventana, text="Introduce tu contraseña:")
etiqueta_contraseña.pack()

text_contraseña = Entry(ventana, show="*") 
text_contraseña.pack()

boton_verificar = Button(ventana, text="Verificar Usuario y Contraseña", command=verificar_usuario_contraseña)
boton_verificar.pack()

mensaje = Label(ventana, text="")
mensaje.pack()

ventana.mainloop()

