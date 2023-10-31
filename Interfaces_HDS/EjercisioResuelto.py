from tkinter import*
ventana=Tk
ventana.geometry("300x300")
## clase operadores
class Operadores:
    def suma(self,num1,num2):
        return num1+num2
    def resta(self,num1,num2):
        return num1-num2
    def multiplicación(self,num1,num2):
        return num1*num2
    def Division(self,num1,num2):
        return num1/num2

## Manejador de operadores:
operacion=StringVar()
classOperadores=Operadores()
def manejadorOperadores():
    num1=int(textoUno.get())
    num2=int(textoDos.get())
    ope=operacion.get()
    if ope=="suma":
        resultado=classOperadores.sumar(num1,num2)
        Label(ventana,text=f'el resultado de la suma es: {resultado}').Pack()
    if ope=="resta":
        resultado=classOperadores.sumar(num1,num2)
        Label(ventana,text=f'el resultado de la suma es: {resultado}').Pack()
    if ope=="multiplicación":
        resultado=classOperadores.sumar(num1,num2)
        Label(ventana,text=f'el resultado de la suma es: {resultado}').Pack()
    if ope=="division":
        resultado=classOperadores.sumar(num1,num2)
        Label(ventana,text=f'el resultado de la suma es: {resultado}').Pack()

