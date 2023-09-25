# # 1. Crear un programa que me pida la edad de una persona, si la edad es mayor o igual a 18 que me muestre un mensaje "eres mayor de edad" caso contrario que me muestre un mensaje "eres menor de edad" 
# edad = int(input("Ingrese tu edad gil: "))
# if edad >= 18:
#     print("Eres mayor de edad.")
# else:
#     print("Eres menor de edad.")
# # 2. una tienda comercial desea hacer iun descuento del 20%, crear un programa
# # que me determine si el cliente se hace acreedor del descuento
# teniendo en cuenta lo siguiente, si el cliente realiza un acompra de igual o mayor a 
# 1000 soles mostrar un mensaje que diga que "ganaste el descuento del 20%, ahora pagaras <mostrar el total
# de la compra menos el descuento>"  en caso la compra no supere los 1000 soles, 
# entonces mostrar un mensaje que diga "no aplicas al descuento
# <mostrar el el monto de la compra>"
# monto_de_compra = float(input("Ingrese el monto de la compra en soles: "))
# if monto_de_compra >= 1000:
#     descuento = monto_de_compra * 0.2
#     total_con_descuento = monto_de_compra - descuento
#     print("¡Ganaste el descuento del 20%! Ahora pagarás", total_con_descuento, "soles.")
# else:
#     print("No aplicas al descuento. El monto de compra es de", monto_de_compra, "soles.")

# # 3. Crear un programa que me pida 5 veces un nombre y por cada ves 
# que lo pida muestre la cantidad de veces que ingreso el nombre.
# nombre_ = {}
# for a in range(5):
#     nombre = input("Ingresa un nombre: ")
#     if nombre in nombre_:
#         nombre_[nombre] += 1
#     else:
#         nombre_[nombre] = 1
# for nombre, cantidad in nombre_.items():
#     print(f"El nombre {nombre} fue ingresado {cantidad} veces.")
# # 4. Crear un programa que me pida un numero y lo evalue con el 
# numero premiado, si el numero ingresado es el premiado el programa finaliza,
# si el numero ingresado es incorrecto el programa seguirá pidiendo el numero premiado.
# numero_premiado = 17
# while True:
#     numero_ingresado = int(input("Ingresa un número: "))
#     if numero_ingresado == numero_premiado:
#         print("¡Felicidades! Has acertado el número premiado, SIUUUUUUUUUUUUUUUUU.")
#         break
#     else:
#         print("Número incorrecto. Sigue intentando.")

# # 5. Crear una funcion que por cada operador aritmetico que resiva dos parametros y retorne el resultado 
# de la operacion, ojo. crear una funcion que nos permita imprimir el resultado.
# def mi_print(texto):
#     print (texto)
# def suma(a,b):
#     return a+b
# def resta(a,b):
#     return a-b
# def multi(a,b):
#     return a*b
# def division(a,b):
#     return a/b

# mi_print(suma(4,5))
# mi_print(resta(10,7))
# mi_print(multi(12,3))
# mi_print(division(24/4))

## 6. Escribe una funcion que reciba un numero entero positivo y devuelva su factorial.
# def factorial(n):
#     if n < 0:
#         return "El factorial no está definido para números negativos."
#     elif n == 0:
#         return 1
#     else:
#         resultado = 1
#         for i in range(1, n + 1):
#             resultado *= i
#         return resultado
# numero = 17
# resultado = factorial(numero)
# print(f"El factorial de {numero} es: {resultado}")

## 7. Escribir una funcion que resiva como parametros una lista de numeros y retorne
# una nueva lista con el cuadro de cada numero de la lista ingresada.
def calcular_cuadrados(lista_numeros):
    lista_cuadrados = []
    for numero in lista_numeros:
        cuadrado = numero ** 2
        lista_cuadrados.append(cuadrado)
    return lista_cuadrados
numeros = [1, 2, 3, 4, 5, 6, 7]
cuadrados = calcular_cuadrados(numeros)
print(cuadrados)

## 8. Escribe un programa que reciba una cadena de caracteres y devuelva un objeto con cada palabra que contiene y su frecuencia.
 