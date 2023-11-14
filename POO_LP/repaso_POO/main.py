# from rich import print
# from rich.markdown import Markdown
# #Titulo
# edad=20
# respuesta="es mayor de edad]" if edad>17 else "es menor de edad]"
# texto="""
#     #parrafo
#     '''bash
#     git commit -m "titulo" -m "cuerpo del commit"
#     #comentario
#     '''
#     *lista
#     *lista
#     >informacion valiosa
#     {}
# """.format(respuesta)
# mostrar_mark=Markdown(texto)
# print (mostrar_mark)

##################################################################
#REPASO POO
from rich import print
# class mascota:
#     #Atributo de clase
#     espacie="animal"
#     #Atributos de instancia
#     def __init__(self):
#         self.nombre=None
#         self.edad=None
#         self.tipo_animal=None
#     def hablar(self,sonido):
#         return sonido
#     def datos_mascota(self,nombre,edad,tipo_animal):
#         self.nombre=nombre
#         self.edad=edad
#         self.tipo_animal=tipo_animal
# class Perro(mascota):
#     def atacar(self):
#         return "ladra y muerde"
# class Gato(mascota):
#     def atacar(self):
#         return "Razguños y Arañazos"

# Perro_boby=Perro()
# Perro_boby.datos_mascota("boby",14,"perro")
# print(f'[bold blue]'+Perro_boby.hablar("guauuu guauuu"))
# print('[bold blue]'+Perro_boby.atacar())
# print('[bold blue]'+Perro_boby.nombre+""+Perro_boby.tipo_animal)

# Gata_persa=Gato()
# Gata_persa.datos_mascota("persa",13,"gato")
# print(f'[bold red]'+Gata_persa.hablar("miauuu miauuu"))
# print('[bold red]'+Gata_persa.atacar())
# print('[bold red]'+Gata_persa.nombre+""+Gata_persa.tipo_animal)

################################################################################
class Persona:
    #Atributo de clase
    #Atributos de instancia
    def __init__(self,nombre:str,edad:int,sexo:str):
        self.nombre=nombre
        self.edad=edad
        self.sexo=sexo
    def comen(self,plato_favorito:str):
        return f"yo {self.nombre} estoy comiendo mi {plato_favorito}"
    def cagar(self):
        return "pipi popo"
class estudiente(Persona):
    def __init__(self, nombre: str, edad: int, sexo: str, carrera_profesional:str):
        super().__init__(nombre, edad, sexo)
        self.carrera_profesional=carrera_profesional
    def estudiar(self):
        return "Estoy estudiando POO"
class trabajador(Persona):
    def __init__(self, nombre: str, edad: int, sexo: str, profesion:str):
        super().__init__(nombre, edad, sexo)
        self.profesion=profesion
    def trabajar(self):
        return "Estoy trabajando en ISTPJMA"
jhona=Persona("jhonatan henry","masculino",18,71458988,"Arquitectura")
print(f"[bold blue]"+jhona.habla('hola causa'))
print("[bold blue]"+jhona.come("cebiche"))
print("[bold blue]"+jhona.estudiar())
print("[bold blue]"+jhona.nombre)