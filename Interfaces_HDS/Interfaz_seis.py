# primero importar la libreria
from tkinter import*
# instanciamos nuestra clase tk()
ventana=Tk() #clase para crear una ventana
ventana.title("clase radiobutton") # Haciendo uso del metodo title para el titulo de mi ventana
ventana.geometry("400x400") #Haciendo uso del metodo geometry para asignarle un tamaño de ventana.

## Instanciar mi clase label
etiqueta=Label(ventana,text="Radio Buttons") #Clase para crear una etiqueta
#Indicar la parte de la venta que deseo que se muestre.
# Puedo usar los metodos grid o pack
etiqueta.config(fg="#EB6828",font=50)
etiqueta.pack()

info=IntVar()
def mostrar_radio():
    if info.get()==1:
        etiquetaRespuesta=Label(ventana,text="Eres Masculino")
        etiquetaRespuesta.pack()
    else:
        etiquetaRespuesta=Label(ventana,text="Eres Femenino")
        etiquetaRespuesta.pack()
    print(info.get())
#Instanciar la clase radiobutton 
radiomasculino=Radiobutton(ventana,text="Masculino",value=1,variable=info)
radiomasculino.pack()
radiofemenino=Radiobutton(ventana,text="Femenino",value=0,variable=info)
radiofemenino.pack()

# Instanciar la clase Button
boton=Button(ventana,text="Enviar",command=mostrar_radio)
boton.pack()
#Llamar el metodo de TK que me permite tener persistencia para mostrar la ventana.
ventana.mainloop()