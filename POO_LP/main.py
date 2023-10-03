# 1. El nombre siempre debera ser en singular y con la primera letra mayusculas 
# class perro:
#     nombre="boby"
#     edad="2 meses"
#     color="cheqche"
#     raza="chusterrier"

#     def ladrar():
#         return "guau guau mascota"
#     def corre(self,pasos):
#         return "Corristes {pasos}, pasos"
    
# respuesta=perro()
# print(respuesta.nombre)
# print(respuesta.ladrar())
# print(respuesta.corre(10))

# 2. Haciendo uso de la POO crear un objeto para la entidad celular.
# class Celular:
#     def __init__(self, marca, modelo, color):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color

#     def llamar(self, numero):
#         print(f"Llamando al número {numero} desde un celular {self.marca} {self.modelo}")

#     def enviar_mensaje(self, numero, mensaje):
#         print(f"Enviando mensaje '{mensaje}' al número {numero} desde un celular {self.marca} {self.modelo}")
                     
# mi_celular = Celular("Redmi", "Miui 10", "Negro")
# print(f"Marca: {mi_celular.marca}")
# print(f"Modelo: {mi_celular.modelo}")
# print(f"Color: {mi_celular.color}")
# mi_celular.llamar("932429423")
# mi_celular.enviar_mensaje("910323323", "Hola mano ¿Cómo estás?")
# Haciendo uso de la POO crear un objeto para la entidad vehiculo.
# class Vehiculo:
#     def __init__(self, marca, modelo, color):
#         self.marca = marca
#         self.modelo = modelo
#         self.color = color

#     def acelerar(self):
#         print(f"El vehículo {self.marca} {self.modelo} está acelerando")

#     def frenar(self):
#         print(f"El vehículo {self.marca} {self.modelo} está frenando")
# mi_vehiculo = Vehiculo("Toyota", "Corolla", "Rojo")
# print(f"Marca: {mi_vehiculo.marca}")
# print(f"Modelo: {mi_vehiculo.modelo}")
# print(f"Color: {mi_vehiculo.color}")
# mi_vehiculo.acelerar()
# mi_vehiculo.frenar()
# 3. Haciendo uso de la POO crear un objeto para la entidad avion.
# class Avion:
#     def __init__(self, modelo, fabricante, capacidad):
#         self.modelo = modelo
#         self.fabricante = fabricante
#         self.capacidad = capacidad

#     def despegar(self):
#         print("El avión está despegando.")

#     def aterrizar(self):
#         print("El avión está aterrizando.")

# avion1 = Avion("Boeing 747", "Boeing", 416)

# print(avion1.modelo)
# print(avion1.fabricante) 
# print(avion1.capacidad)

# avion1.despegar()     
# avion1.aterrizar()         
# 4. Haciendo uso de la POO crear un objeto para un heroe de dota2.
# class HeroeDota2:
#     def __init__(self, nombre, atributo_principal, habilidades):
#         self.nombre = nombre
#         self.atributo_principal = atributo_principal
#         self.habilidades = habilidades

#     def usar_habilidad(self, habilidad):
#         print(f"El {self.nombre} está usando la habilidad {habilidad}.")

# heroe = HeroeDota2("Heroe Invoker", "Atributo: Inteligencia", "Habilidades: Sun Strike, Tornado,EMP")
# print(heroe.nombre)               
# print(heroe.atributo_principal)   
# print(heroe.habilidades)          
# heroe.usar_habilidad("Sun Strike")  
# 5. Haciendo uso de la POO crear un objeto para PC.
# class PC:
#     def __init__(self, marca, modelo, procesador, memoria_ram, capacidad_almacenamiento):
#         self.marca = marca
#         self.modelo = modelo
#         self.procesador = procesador
#         self.memoria_ram = memoria_ram
#         self.capacidad_almacenamiento = capacidad_almacenamiento

#     def Caracteristicas(self):
#         Carateristicas=f"""
#             "Marca" : {self.marca},
#             "Modelo" : {self.modelo}
#             "Procesador" : {self.procesador}
#             "Memoria RAM" : {self.memoria_ram}
#             "Almacenamiento" : {self.capacidad_almacenamiento}
#     """
#         return Carateristicas
    
# mi_pc = PC("HP", "Pavilion", "Intel Core i7", "8GB", "1TB")
# print(f"Marca: {mi_pc.marca}")                  
# print(f"Modelo: {mi_pc.modelo}")           
# print(f"Procesador: {mi_pc.procesador}")             
# print(f"Memoria Ram: {mi_pc.memoria_ram}")           
# print(f"Almacenamiento: {mi_pc.capacidad_almacenamiento}")
# 6. Haciendo uso de la POO crear un objeto para una impresora.
# class Impresora:
#     def __init__(self, marca, modelo):
#         self.marca = marca
#         self.modelo = modelo
#         self.encendida = False
#     def encender(self):
#         self.encendida = True
#         print("La impresora se ha encendido.")
#     def apagar(self):
#         self.encendida = False
#         print("La impresora se ha apagado.")
#     def imprimir(self, documento):
#         if self.encendida:
#             print("Imprimiendo:", documento)
#         else:
#             print("La impresora está apagada. Enciéndela antes de imprimir.")

# mi_impresora = Impresora("Epson", "L4150")

# print(mi_impresora.marca) 
# print(mi_impresora.modelo)  

# mi_impresora.encender()
# mi_impresora.imprimir("Mi documento")  
# mi_impresora.apagar()     
# mi_impresora.imprimir("Otro documento") 
# 7. Haciendo uso de la POO crear un objeto para imitir una factura.
# class Factura:
#     def __init__(self, numero, fecha, cliente, productos):
#         self.numero = numero
#         self.fecha = fecha
#         self.cliente = cliente
#         self.productos = productos

#     def calcular_total(self):
#         total = 0
#         for producto in self.productos:
#             total += producto.precio
#         return total

#     def imprimir_factura(self):
#         print("Factura Número:", self.numero)
#         print("Fecha:", self.fecha)
#         print("Cliente:", self.cliente)
#         print("Productos:")
#         for producto in self.productos:
#             print("- ", producto.nombre, ":", producto.precio)
#         print("Total:", self.calcular_total())

# class Producto:
#     def __init__(self, nombre, precio):
#         self.nombre = nombre
#         self.precio = precio
# producto1 = Producto("Camisa", 20)
# producto2 = Producto("Pantalón", 30)
# producto3 = Producto("Zapatos", 50)

# factura1 = Factura("F001", "01/01/2022", "Cliente1", [producto1, producto2, producto3])

# factura1.imprimir_factura()
## TKINTER - Libreria de python para la creacion de interfaces graficas.
