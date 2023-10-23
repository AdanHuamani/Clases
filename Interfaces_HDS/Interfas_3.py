# from tkinter import *

# def suma():
#     num1 = int(numero_uno.get())
#     num2 = int(numero_dos.get())
#     resultado = num1 + num2
#     result.insert(0, resultado)

# def limpiar():
#     numero_uno.delete(0, END)
#     numero_dos.delete(0, END)
#     result.delete(0, END)
#     numero_uno.focus()

# ventana = Tk()
# ventana.title('Bienvenid@')

# etiqueta = Label(ventana, text='primer numero: ')
# etiqueta.grid(row=0, column=0)

# etiqueta = Label(ventana, text='segundo numero: ')
# etiqueta.grid(row=1, column=0)

# etiqueta = Label(ventana, text='resultado: ')
# etiqueta.grid(row=2, column=0)

# numero_uno = Entry()
# numero_uno.grid(row=0, column=1)

# numero_dos = Entry()
# numero_dos.grid(row=1, column=1)

# result = Entry()
# result.grid(row=2, column=1)

# ventana.mainloop()

## 2 
# from tkinter import*

# def suma():
# 	num1=int(numero_uno.get())
# 	num2=int(numero_dos.get())
# 	resultado=num1+num2
# 	result.insert(0,resultado)
	

	
# def limpiar():
# 	numero_uno.delete(0,END)
# 	numero_dos.delete(0,END)
# 	result.delete(0,END)
# 	numero_uno.focus()


# ventana= Tk() 
# ventana.title('Bienvenid@') 
# # primero instanciar la variable 
# etiqueta=Label(ventana, text='primer numero: ') 
# etiqueta.grid(row=0, column=0) 
  
# etiqueta=Label(ventana, text='segundo numero: ') 
# etiqueta.grid(row=1, column=0) 
  
# etiqueta=Label(ventana, text='resultado: ') 
# etiqueta.grid(row=2, column=0) 
  
  
#  ## cuadro de texto -- entry 
# numero_uno=Entry() 
# numero_uno.grid(row=0,column=1)  
  
# numero_dos=Entry() 
# numero_dos.grid(row=1,column=1)  
  
# result=Entry() 
# result.grid(row=2,column=1)

# boton_limpiar=Button(ventana,text="Limpiar",comand=limpiar())
# boton_limpiar.grid(row=7,column=1)

# boton_suma=Button(ventana,text="sumar",command=suma)
# boton_suma.grid(row=3,column=0)

# ventana.mainloop()

# 3
from tkinter import *

def calcular_promedio():
    notas = [float(nota.get()) for nota in notas_entry]
    promedio = sum(notas) / len(notas)
    resultado_label.config(text="El promedio es: {:.2f}".format(promedio))

def limpiar():
    for nota in notas_entry:
        nota.delete(0, END)
    resultado_label.config(text="")

ventana = Tk()
ventana.title("Calculadora de Promedio")

notas_entry = []
for i in range(3):
    nota_label = Label(ventana, text="Nota {}: ".format(i+1))
    nota_label.grid(row=i, column=0, padx=10, pady=5)
    nota_entry = Entry(ventana)
    nota_entry.grid(row=i, column=1, padx=10, pady=5)
    notas_entry.append(nota_entry)

calcular_button = Button(ventana, text="Calcular", command=calcular_promedio)
calcular_button.grid(row=5, column=0, pady=10)

limpiar_button = Button(ventana, text="Limpiar", command=limpiar)
limpiar_button.grid(row=5, column=1, pady=10)

resultado_label = Label(ventana, text="")
resultado_label.grid(row=6, columnspan=2)

ventana.mainloop()