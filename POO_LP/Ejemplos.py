# Crear un sistema para gestion, conjtrol de stock de productos.
# La base de datos en el que voy a trabajar.
productos=[
    {
        "1D":1,
        "nombre":"arroz",
        "descripcion":"costeño costal x 100 k",
        "stock":5,
        "unidad":"costales",
        "precio":125,
        "moneda":"soles",
    }
]
# Casos de Uso 
class producto:
    # Atributos de instancia.
   def __init__(self,nombre,descripcion,stock,unidad,precio,moneda="soles"):
        self.nombre=nombre
        self.descripcion=descripcion
        self.stock=stock
        self.unidad=unidad
        self.precio=precio
        self.moneda=moneda
    # creacion de metodos
   def mostrar_productos(self):
       mensaje=f"""
      tienes{len(productos)}productos
      los productos son:
      {productos}
      """
       return mensaje
   def registrar_producto(self):
      nuevo_id=len(productos)+1
      producto_nuevo={
         "id":nuevo_id,
         "nombre":self.nombre,
         "descripcion":self.descripcion,
         "stock":self.stock,
         "unidad":self.unidad,
         "precio":self.precio,
         "moneda":self.moneda
      }
      registro_producto=productos.append(producto_nuevo)
      return f"el siguiente producto se reigistro exitosamente {producto_nuevo}"

   def mostrar_producto(self,id):
      producto_buscar=productos[id-1]
      return producto_buscar

   def eliminar_producto(self,id):
       producto_eliminar=productos.pop(id-1)
       return f"el siguiente producto fue eliminado {producto_eliminar}"

   def actualizar_producto(self,id,clave,valor):
       ol=valor
       producto_actualizar=list(filter(lambda obje:obje[clave]==id,productos))[0].update ({clave:valor})
       return "se actualizó"
   # list funcion para crear funcion lista
   
prod=producto("aceite","Extra virgen",2,"botella x litro",12.50)
print(prod.registrar_producto())
print(prod.mostrar_productos())
print(prod.mostrar_producto(1))
print(prod.eliminar_producto(2))
print(prod.mostrar_productos())
print(prod.actualizar_producto(125,"precio",130))
# Historias de usuario
# Producto Ower 
# baclog
# MVP
# Prototipos de mierda