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

## Celulares
# class celular:
#     #atributos de tipo clase (Atributo general): quiere decir que son iguales para todos los objetos que se creen
#     familia="smart phone"
# #Atributos de instancia: Son atributos propios del objeto y creamos una funcion inicializadora.
#     def __init__(self,marca,modelo,imel,nroCelular)
#         self.marca=marca
#         self.Modelo=modelo
#         self.imel=imel
#         self.nroCelular=nroCelular
#     #funcionalidades
#     def llamar(self,destino):
#         return f"llamando a {destino}"
# #objeto celular jory
# llamandoAdan=celular("poco","X5","374532264834","910433710") #Instanciando mi clase - 
# #creando mi objeto celular
# print(llamandoAdan.marca)
# print(llamandoAdan.familia)
# print(llamandoAdan.llamar("David"))

## 1. crear un objeto Clase laptop con dos atributos de clase y 5 atributos de instancias devera tener hasta 3
# funcionalidades como minimo
# Crear tres objetos instancias de clase distintos
# class Laptop:
#     # Atributos de clase
#     marca = ""
#     modelo = ""

#     def __init__(self, procesador, ram, almacenamiento, pantalla, bateria):
#         # Atributos de instancia
#         self.procesador = procesador
#         self.ram = ram
#         self.almacenamiento = almacenamiento
#         self.pantalla = pantalla
#         self.bateria = bateria

#     def encender(self):
#         print("La laptop se ha encendido.")

#     def apagar(self):
#         print("La laptop se ha apagado.")

#     def mostrar_informacion(self):
#         print("Marca:", self.marca)
#         print("Modelo:", self.modelo)
#         print("Procesador:", self.procesador)
#         print("RAM:", self.ram)
#         print("Almacenamiento:", self.almacenamiento)
#         print("Pantalla:", self.pantalla)
#         print("Batería:", self.bateria)

# # Crear tres instancias de la clase Laptop
# laptop1 = Laptop("Intel i5", "8GB", "500GB", "15.6 pulgadas", "4000mAh")
# laptop2 = Laptop("AMD Ryzen 7", "16GB", "1TB", "14 pulgadas", "5000mAh")
# laptop3 = Laptop("Intel i7", "12GB", "256GB", "13.3 pulgadas", "3500mAh")

# # Modificar atributos de clase
# laptop1.marca = "Dell"
# laptop1.modelo = "Inspiron"

# laptop2.marca = "HP"
# laptop2.modelo = "Envy"

# laptop3.marca = "Lenovo"
# laptop3.modelo = "ThinkPad"

# # Llamar a las funcionalidades
# laptop1.encender()
# laptop1.mostrar_informacion()
# laptop1.apagar()

# laptop2.encender()
# laptop2.mostrar_informacion()
# laptop2.apagar()

# laptop3.encender()
# laptop3.mostrar_informacion()
# laptop3.apagar()

## Crear una clase de puesto de mercado que tenga un atributo de clase, 
# 5 atributos de instancia y 5 funcionalidades.
## debera crear 4 instancia de la clase mercado
# Ejemplo: puesto mechita, puesto gringa, Puesto ojo de uva.
class PuestoDeMercado:
    mercado = "Mercado Central"

    def __init__(self, nombre, ubicacion, productos, empleados, horario):
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.productos = productos
        self.empleados = empleados
        self.horario = horario

    def mostrar_informacion(self):
        print("Nombre del puesto:", self.nombre)
        print("Ubicación:", self.ubicacion)
        print("Productos:", self.productos)
        print("Número de empleados:", self.empleados)
        print("Horario de atención:", self.horario)
    def cambiar_ubicacion(self, nueva_ubicacion):
        self.ubicacion = nueva_ubicacion
        print("La ubicación del puesto ha sido cambiada a:", self.ubicacion)
    def agregar_producto(self, nuevo_producto):
        self.productos.append(nuevo_producto)
        print("Se ha agregado un nuevo producto:", nuevo_producto)
    def contratar_empleado(self, nuevo_empleado):
        self.empleados += 1
        print("Se ha contratado a un nuevo empleado:", nuevo_empleado)
    def cambiar_horario(self, nuevo_horario):
        self.horario = nuevo_horario
        print("El horario de atención ha sido cambiado a:", self.horario)
# Crear instancias de la clase Puesto de Mercado
puesto_mechita = PuestoDeMercado("Puesto Mechita", "Plaza Central", ["Frutas", "Verduras"], 2, "8am - 6pm")
puesto_gringa = PuestoDeMercado("Puesto Gringa", "Plaza Norte", ["Carnes", "Embutidos"], 3, "9am - 7pm")
puesto_ojo_de_uva = PuestoDeMercado("Puesto Ojo de Uva", "Plaza Sur", ["Vinos", "Licores"], 1, "10am - 8pm")
# Modificar el atributo de clase
PuestoDeMercado.mercado = "Mercado Central"
# Llamar a las funcionalidades de las instancias
puesto_mechita.mostrar_informacion()
puesto_mechita.cambiar_ubicacion("Plaza Este")
puesto_mechita.agregar_producto("Hortalizas")
puesto_mechita.contratar_empleado("Ana")
puesto_mechita.cambiar_horario("7am - 5pm")

puesto_gringa.mostrar_informacion()
puesto_gringa.cambiar_ubicacion("Plaza Oeste")
puesto_gringa.agregar_producto("Quesos")
puesto_gringa.contratar_empleado("Pedro")
puesto_gringa.cambiar_horario("8am - 6pm")

puesto_ojo_de_uva.mostrar_informacion()
puesto_ojo_de_uva.cambiar_ubicacion("Plaza Central")
puesto_ojo_de_uva.agregar_producto("Espumantes")
puesto_ojo_de_uva.contratar_empleado("María")
puesto_ojo_de_uva.cambiar_horario("9am - 7pm")