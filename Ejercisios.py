## Crear un programa que me pida la edad de una persona, si la edad es mayor o igual a 18 que me muestre un mensaje "eres mayor de edad" caso contrario que me muestre un mensaje "eres menor de edad" 
edad = int(input("Ingrese tu edad gil: "))
if edad >= 18:
    print("Eres mayor de edad.")
else:
    print("Eres menor de edad.")
## una tienda comercial desea hacer iun descuento del 20%, crear un programa
## que me determine si el cliente se hace acreedor del descuento
# teniendo en cuenta lo siguiente, si el cliente realiza un acompra de igual o mayor a 
# 1000 soles mostrar un mensaje que diga que "ganaste el descuento del 20%, ahora pagaras <mostrar el total
# de la compra menos el descuento>"  en caso la compra no supere los 1000 soles, 
# entonces mostrar un mensaje que diga "no aplicas al descuento
# <mostrar el el monto de la compra>"
monto_de_compra = float(input("Ingrese el monto de la compra en soles: "))
if monto_de_compra >= 1000:
    descuento = monto_de_compra * 0.2
    total_con_descuento = monto_de_compra - descuento
    print("¡Ganaste el descuento del 20%! Ahora pagarás", total_con_descuento, "soles.")
else:
    print("No aplicas al descuento. El monto de compra es de", monto_de_compra, "soles.")