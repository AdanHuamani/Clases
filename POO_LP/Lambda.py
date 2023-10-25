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
#     def tienda_gerente(self, bd_negocios, nombre_gerente):
#         respuesta = list(filter(lambda el: el["gerente"] == nombre_gerente, bd_negocios))
#         return respuesta
    
#     def tienda_mas_categorias(self, bd_negocios):
#         negocios_mas_categorias = list(filter(lambda el: len(el["categoria"].split(", ")) > 2, bd_negocios))
#         return negocios_mas_categorias
    
#     def ruc_nombre(self, bd_negocios):
#         nombre_ruc = [(el["nombre"], el["ruc"]) for el in bd_negocios]
#         return nombre_ruc
    
#     def mostrar_todo(self, bd_negocios):
#         for el in bd_negocios:
#             print("Nombre:", el["nombre"])
#             print("Categoría:", el["categoria"])
#             print("Gerente:", el["gerente"])
#             print("RUC:", el["ruc"])
#             print("----------------------")
    
#     def eliminar_tienda(self, bd_negocios, nombre_tienda):
#         bd_negocios = list(filter(lambda el: el["nombre"] != nombre_tienda, bd_negocios))
#         return bd_negocios
    
#     def actualizar_tienda(self, bd_negocios, nombre_tienda, nueva_categoria, nuevo_gerente, nuevo_ruc):
#         for el in bd_negocios:
#             if el["nombre"] == nombre_tienda:
#                 el["categoria"] = nueva_categoria
#                 el["gerente"] = nuevo_gerente
#                 el["ruc"] = nuevo_ruc
#         return bd_negocios

# # Crear una lista con 10 objetos de tiendas comerciales
# negocios = [
#     {"nombre": "Tienda 1", "categoria": "Abarrotes", "gerente": "Edwin", "ruc": "12345678901"},
#     {"nombre": "Tienda 2", "categoria": "Farmacia", "gerente": "China", "ruc": "23456789012"},
#     {"nombre": "Tienda 3", "categoria": "Bodega", "gerente": "Cristian", "ruc": "34567890123"},
#     {"nombre": "Tienda 4", "categoria": "Restaurantes", "gerente": "Nadine", "ruc": "45678901234"},
#     {"nombre": "Tienda 5", "categoria": "Abarrotes, Farmacia", "gerente": "Edwin", "ruc": "56789012345"},
#     {"nombre": "Tienda 6", "categoria": "Bodega, Restaurantes", "gerente": "China", "ruc": "67890123456"},
#     {"nombre": "Tienda 7", "categoria": "Farmacia, Bodega", "gerente": "Cristian", "ruc": "78901234567"},
#     {"nombre": "Tienda 8", "categoria": "Abarrotes, Restaurantes", "gerente": "Nadine", "ruc": "89012345678"},
#     {"nombre": "Tienda 9", "categoria": "Farmacia, Restaurantes", "gerente": "Edwin", "ruc": "90123456789"},
#     {"nombre": "Tienda 10", "categoria": "Abarrotes, Bodega", "gerente": "China", "ruc": "01234567890"}
# ]

# gerente = Tienda_Comercial()

# # Ejemplo de uso de los métodos de la clase
# print("Tiendas del gerente China:")
# tiendas_china = gerente.tienda_gerente(negocios, "China")
# for tienda in tiendas_china:
#     print(tienda["nombre"])

# print("\nNegocios con más de dos categorías:")
# negocios_mas_categorias = gerente.tienda_mas_categorias(negocios)
# for negocio in negocios_mas_categorias:
#     print(negocio["nombre"])

# print("\nNombre y RUC de las tiendas:")
# nombre_ruc = gerente.ruc_nombre(negocios)
# for tienda in nombre_ruc:
#     print(f"Nombre: {tienda[0]}, RUC: {tienda[1]}")

# print("\nMostrar todos los datos de las tiendas:")
# gerente.mostrar_todo(negocios)

# print("\nEliminar una tienda:")
# negocios = gerente.eliminar_tienda(negocios, "Tienda 3")
# gerente.mostrar_todo(negocios)

# print("\nActualizar una tienda:")
# negocios = gerente.actualizar_tienda(negocios, "Tienda 1", "Supermercado", "Pedro", "09876543210")
# gerente.mostrar_todo(negocios)

###########
class Tienda_Comercial:
    def tienda_gerente(self, bd_negocios, nombre_gerente):
        respuesta = list(filter(lambda el: el["gerente"] == nombre_gerente, bd_negocios))
        return respuesta
    
    def tienda_mas_categorias(self, bd_negocios):
        negocios_mas_categorias = list(filter(lambda el: len(el["categoria"].split(", ")) > 2, bd_negocios))
        return negocios_mas_categorias
    
    def ruc_nombre(self, bd_negocios):
        nombre_ruc = [(el["nombre"], el["ruc"]) for el in bd_negocios]
        return nombre_ruc
    
    def mostrar_todo(self, bd_negocios):
        for el in bd_negocios:
            print("Nombre:", el["nombre"])
            print("Categoría:", el["categoria"])
            print("Gerente:", el["gerente"])
            print("RUC:", el["ruc"])
            print("----------------------")
    
    def eliminar_tienda(self, bd_negocios, nombre_tienda):
        bd_negocios = list(filter(lambda el: el["nombre"] != nombre_tienda, bd_negocios))
        return bd_negocios
    
    def actualizar_tienda(self, bd_negocios, nombre_tienda, nueva_categoria, nuevo_gerente, nuevo_ruc):
        for el in bd_negocios:
            if el["nombre"] == nombre_tienda:
                el["categoria"] = nueva_categoria
                el["gerente"] = nuevo_gerente
                el["ruc"] = nuevo_ruc
        return bd_negocios
    
    def crear_producto(self, bd_negocios, nombre_tienda, nuevo_producto):
        for el in bd_negocios:
            if el["nombre"] == nombre_tienda:
                if "productos" not in el:
                    el["productos"] = []
                el["productos"].append(nuevo_producto)
        return bd_negocios
    
    def actualizar_horario(self, bd_negocios, nombre_tienda, nuevo_horario):
        for el in bd_negocios:
            if el["nombre"] == nombre_tienda:
                el["horario"] = nuevo_horario
        return bd_negocios


# Crear una lista con 10 objetos de tiendas comerciales
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

gerente = Tienda_Comercial()

# Crear un nuevo producto en una tienda específica
negocios = gerente.crear_producto(negocios, "Tienda 1", "Nuevo producto 1")
negocios = gerente.crear_producto(negocios, "Tienda 1", "Nuevo producto 2")

# Actualizar una tienda
negocios = gerente.actualizar_tienda(negocios, "Tienda 2", "Nueva categoría", "Nuevo gerente", "09876543210")

# Actualizar el horario de atención de una tienda
negocios = gerente.actualizar_horario(negocios, "Tienda 3", "8:00 AM - 6:00 PM")

# Mostrar todos los datos actualizados de las tiendas
gerente.mostrar_todo(negocios)