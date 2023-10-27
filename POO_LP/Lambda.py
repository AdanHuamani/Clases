# # Lambda es una funcion que se autoejecuta
# hola=lambda a,b:print (a+b)
# # funcion normal
# def suma (a,b):
#     print(a+b)
# suma(4,6)
# hola(10,20)
# ## if ternario
# "soy verdad ternario" if
# True else "soy falso ternario"
# print (ternario)
# # If normal
# if True:
#     print("soy verdad")
# else: 
#     print("soy mentira")

## Lambda
# lista_alumnos=[
#     {
#         "Nombre":"Adan",
#         "Edad":"19",
#         "Hobby":"Jugar futbol",
#         "Flaquita":"R",
#     },
#     {
#         "Nombre":"David",
#         "Edad":"19",
#         "Hobby":"cachar",
#         "Flaquita":"edith",
#     },
#     {
#         "Nombre":"Del mar",
#         "Edad":"50",
#         "Hobby":"tirar",
#         "Flaquita":"dsfdgf",
#     },
#     {
#         "Nombre":"Orlando",
#         "Edad":"19",
#         "Hobby":"Bailar",
#         "Flaquita":"susan",
#     }
    
# ]
# print(f"Todos mis alumnitos{lista_alumnos}")
# fans_melody=list(filter(lambda par:par["Flaquita"]=="melody",lista_alumnos))
# print(f"Los que quieren con melody{fans_melody}")

##################################################
## Crear una lista con 10 objetos que contengan los datos de las tiendas comerciales
# Observacion: las categorias sera: Abarrotes, farmacia, bodega, restaurantes.
# los gerentes solo serán los siguientes: Edwin, China, Cristian, Nadine.
# 1. crear un metodo que me filtre las tiendas que tiene cada gerente.
# 2. Crear un metodo que nos muestre los negocios que tienen mas de dos categorias.
# 3. Crear un metodo que me muestre solo el nombre y ruc de las tiendas.
## Agregar un codigo para crear un nuevo producto.
## Agregar un codigo para actualizar tienda.
## Agregar codigo para actualizar horario de atencion.
# class Tienda_Comercial:
# negocios = [
#     {"nombre": "Tienda 1", 
#      "categoria": "Abarrotes", 
#      "Horario": "8:00 AM - 5:00 PM",
#      "gerente": "Edwin", 
#      "ruc": "12345678901"},

#     {"nombre": "Tienda 2", 
#      "categoria": "Farmacia", 
#      "Horario": "8:00 AM - 5:00 PM",
#      "gerente": "China", 
#      "ruc": "23456789012"},

#     {"nombre": "Tienda 3", 
#      "categoria": "Bodega",
#      "Horario": "8:00 AM - 5:00 PM", 
#      "gerente": "Cristian", 
#      "ruc": "34567890123"},
     
#     {"nombre": "Tienda 4", 
#      "categoria": "Restaurantes", 
#      "Horario": "8:00 AM - 5:00 PM",
#      "gerente": "Nadine", 
#      "ruc": "45678901234"},

#     {"nombre": "Tienda 5", 
#      "categoria": "Farmacia", 
#      "Horario": "8:00 AM - 5:00 PM",
#      "gerente": "Edwin", 
#      "ruc": "56789012345"},

#     {"nombre": "Tienda 6", 
#      "categoria": "Bodega, Restaurantes", 
#      "Horario": "8:00 AM - 5:00 PM",
#      "gerente": "China", 
#      "ruc": "67890123456"},

#     {"nombre": "Tienda 7", 
#      "categoria": "Farmacia, Bodega", 
#      "Horario": "8:00 AM - 5:00 PM",
#      "gerente": "Cristian", 
#      "ruc": "78901234567"},

#     {"nombre": "Tienda 8", 
#      "categoria": "Abarrotes, Restaurantes", 
#      "Horario": "8:00 AM - 5:00 PM",
#      "gerente": "Nadine", 
#      "ruc": "89012345678"},

#     {"nombre": "Tienda 9", 
#      "categoria": "Farmacia, Restaurantes", 
#      "Horario": "8:00 AM - 5:00 PM",
#      "gerente": "Edwin", 
#      "ruc": "90123456789"},

#     {"nombre": "Tienda 10", 
#      "categoria": "Abarrotes, Bodega", 
#      "Horario": "8:00 AM - 5:00 PM",
#      "gerente": "China", 
#      "ruc": "01234567890"}
#     ]
# class Tiendas_comerciales:

#     def __init__(self,ruc,nombre, categoria,Horario,gerente,):
#         self.id=id
#         self.ruc=ruc
#         self.nombre=nombre
#         self.categoria=categoria
#         self.Horario=Horario
#         self.gerente=gerente


#     def tienda_gerente(self,bd_negocios,nombre_gerente):
#         respuesta=list(filter(lambda el:el["gerente"]==nombre_gerente,bd_negocios))
#         return respuesta

#     def tiendas_mas_categorias(self,bd_negocios):
#         respuesta1=list(filter(lambda xd:len(xd["categoria"])>2,bd_negocios))
#         return respuesta1
    
#     def ruc_nombre(self,bd_negocios):
#         respuesta2=list(map(lambda par:{"ruc":par["ruc"],"nombre" :par["nombre"]},bd_negocios))
#         return respuesta2
    
#     def eliminar_negocio(self,bd_negocios,ruc):
#         respuesta=list(filter(lambda el:el["ruc"]!=ruc,bd_negocios))
#         return respuesta
#     ## tarea
#     def actualizar_negocio(self,id,clave,valor):
#         ol=valor
#         actualizar_negocio=list(filter(lambda obj:obj[clave]==id,negocios))[0].update({clave:valor}) 
#         return 'se actualizo la tienda'
#     ## otro metodo para crear un nuevo producto
#     def registrar_negocio(self):
#         nuevo_id=len(negocios)+1
#         negocio_nuevo={
#         'id':nuevo_id,
#         'ruc':self.ruc,
#         'nombre':self.nombre,
#         'categoria':self.categoria,
#         'Horario':self.Horario,
#         'gerente':self.gerente
#     }
#         registro_negocio=negocios.append(negocio_nuevo)
#         return 'producto registrado exitosamente'
    
#     def mostrar_negocio(self, ide):
#         g=list(filter(lambda par:par['id']==ide,negocios))
#         return f'''Aqui tienes informacion de la tienda que buscaste:
#         .................................................................................................................................................................................................................... 
#         {g}'''

#     ## otro metodo para actualizar el horario de atencion
#     def actualizar_horario(self, id, clave, valor):
#         negocios[id-1][clave]=valor
#         #actu_hora=list(filter(lambda obj:obj[clave]==dato,negocios))[0].update({clave:valor}) 
#         return 'se actualizo el horario'

# actu=Tiendas_comerciales(56789012345,'Areola','bodega',{"dia":"7am-12m","tarde":"2pm-8pm"},'edwin')
# print(actu.actualizar_negocio('xd','nombre','jijijja'))

# print(actu.registrar_negocio())
# print(actu.mostrar_negocio(11))

# print(actu.actualizar_horario(1,'horario_atencion',{'dia':'7am-12pm','tarde':'3pm-9pm'}))
# print(actu.mostrar_negocio(2))

negocios = [
    {"nombre": "Tienda 1", 
     "categoria": "Abarrotes", 
     "Horario": "8:00 AM - 5:00 PM",
     "gerente": "Edwin", 
     "ruc": "12345678901"},
    {"nombre": "Tienda 2", 
     "categoria": "Farmacia", 
     "Horario": "8:00 AM - 5:00 PM",
     "gerente": "China", 
     "ruc": "23456789012"},
    {"nombre": "Tienda 3", 
     "categoria": "Bodega",
     "Horario": "8:00 AM - 5:00 PM", 
     "gerente": "Cristian", 
     "ruc": "34567890123"},
    {"nombre": "Tienda 4", 
     "categoria": "Restaurantes", 
     "Horario": "8:00 AM - 5:00 PM",
     "gerente": "Nadine", 
     "ruc": "45678901234"},
    {"nombre": "Tienda 5", 
     "categoria": "Farmacia", 
     "Horario": "8:00 AM - 5:00 PM",
     "gerente": "Edwin", 
     "ruc": "56789012345"},
    {"nombre": "Tienda 6", 
     "categoria": "Bodega, Restaurantes", 
     "Horario": "8:00 AM - 5:00 PM",
     "gerente": "China", 
     "ruc": "67890123456"},
    {"nombre": "Tienda 7", 
     "categoria": "Farmacia, Bodega", 
     "Horario": "8:00 AM - 5:00 PM",
     "gerente": "Cristian", 
     "ruc": "78901234567"},
    {"nombre": "Tienda 8", 
     "categoria": "Abarrotes, Restaurantes", 
     "Horario": "8:00 AM - 5:00 PM",
     "gerente": "Nadine", 
     "ruc": "89012345678"},
    {"nombre": "Tienda 9", 
     "categoria": "Farmacia, Restaurantes", 
     "Horario": "8:00 AM - 5:00 PM",
     "gerente": "Edwin", 
     "ruc": "90123456789"},
    {"nombre": "Tienda 10", 
     "categoria": "Abarrotes, Bodega", 
     "Horario": "8:00 AM - 5:00 PM",
     "gerente": "China", 
     "ruc": "01234567890"}
]

class Tiendas_comerciales:
    def __init__(self, ruc, nombre, categoria, horario, gerente):
        self.ruc = ruc
        self.nombre = nombre
        self.categoria = categoria
        self.horario = horario
        self.gerente = gerente

    def tienda_gerente(self, bd_negocios, nombre_gerente):
        respuesta = list(filter(lambda el: el["gerente"] == nombre_gerente, bd_negocios))
        return respuesta

    def tiendas_mas_categorias(self, bd_negocios):
        respuesta1 = list(filter(lambda xd: len(xd["categoria"]) > 2, bd_negocios))
        return respuesta1

    def ruc_nombre(self, bd_negocios):
        respuesta2 = list(map(lambda par: {"ruc": par["ruc"], "nombre": par["nombre"]}, bd_negocios))
        return respuesta2

    def eliminar_negocio(self, bd_negocios, ruc):
        respuesta = list(filter(lambda el: el["ruc"] != ruc, bd_negocios))
        return respuesta

    def actualizar_negocio(self, id, clave, valor):
        negocios[id - 1][clave] = valor
        return 'Se actualizó la tienda'

    def registrar_negocio(self):
        nuevo_id = len(negocios) + 1
        negocio_nuevo = {
            'id': nuevo_id,
            'ruc': self.ruc,
            'nombre': self.nombre,
            'categoria': self.categoria,
            'Horario': self.horario,
            'gerente': self.gerente
        }
        negocios.append(negocio_nuevo)
        return 'Producto registrado exitosamente'

    def mostrar_negocio(self, ide):
        g = list(filter(lambda par: par['id'] == ide, negocios))
        return f'''Aquí tienes información de la tienda que buscaste:
        .................................................................................................................................................................................................................... 
        {g}'''

    def actualizar_horario(self, id, clave, valor):
        negocios[id - 1][clave] = valor
        return 'Se actualizó el horario'


actu = Tiendas_comerciales(56789012345, 'Areola', 'bodega', {"dia": "7am-12m", "tarde": "2pm-8pm"}, 'edwin')
print(actu.actualizar_negocio('Ropa', 'Adan', 'David'))
print(actu.registrar_negocio())
print(actu.mostrar_negocio(11))
print(actu.actualizar_horario(1, 'Horario', {'dia': '7am-12pm', 'tarde': '3pm-9pm'}))
print(actu.mostrar_negocio(2))