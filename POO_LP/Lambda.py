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
lista_alumnos=[
    {
        "Nombre":"Adan",
        "Edad":"19",
        "Hobby":"Jugar futbol",
        "Flaquita":"R",
    },
    {
        "Nombre":"David",
        "Edad":"19",
        "Hobby":"cachar",
        "Flaquita":"edith",
    },
    {
        "Nombre":"Del mar",
        "Edad":"50",
        "Hobby":"tirar",
        "Flaquita":"dsfdgf",
    },
    {
        "Nombre":"Orlando",
        "Edad":"19",
        "Hobby":"Bailar",
        "Flaquita":"susan",
    }
    
]
print(f"Todos mis alumnitos{lista_alumnos}")
fans_melody=list(filter(lambda par:par["Flaquita"]=="melody",lista_alumnos))
print(f"Los que quieren con melody{fans_melody}")

##################################################
nuevo_objet=list(map(lambda par:{"nombre_alumno":par["Nombre"],"germita":par["Flaquita"]},lista_alumnos))
print(nuevo_objet)
