from rich import print
from rich.markdown import Markdown
#Titulo
edad=20
respuesta="es mayor de edad]" if edad>17 else "es menor de edad]"
texto="""
    #parrafo
    '''bash
    git commit -m "titulo" -m "cuerpo del commit"
    #comentario
    '''
    *lista
    *lista
    >informacion valiosa
    {}
""".format(respuesta)
mostrar_mark=Markdown(texto)
print (mostrar_mark)