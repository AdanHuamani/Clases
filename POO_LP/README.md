# Programación Orientada a objetos(POO)
### En ingles es Object Orient Programing(OOP)
Es un paradigma de programacion
> **Paradigma**: es un modelo, patron o ejemplo que se debe seguir.
POO es un modelo de como programar
**Objeto** - El objetivo es organizar el codigo de manera que se asemeje a como pensamos en la vida real.

Se basa en objetos y en la POO un objeto es toda entidad que se puede describir atraves de **atributos** y **funciones** que puede realizar la entidad.
## EJEMPLO: 
### Celulares
```Python
class celular:
```
- atributos de tipo clase (Atributo general): quiere decir que son iguales para todos los objetos que se creen.
    ```python
    familia="smart phone"
    ```
- Atributos de instancia: Son atributos propios del objeto y creamos una funcion inicializadora.
    ```python
    def __init__(self,marca,modelo,imel,nroCelular)
    self.marca=marca
    self.Modelo=modelo
    self.imel=imel
    self.nroCelular=nroCelular
    ```
- funcionalidades
  ```python
    def llamar(self,destino):
        return f"llamando a {destino}"
    ```
- objeto celular Adan
    ```python
    llamandoAdan=celular("poco","X5","374532264834","910433710") 
    #Instanciando mi clase - creando mi objeto celular
    ```
- Por ultimo debemos ingresar con print para poder imprimir los atributos del celular:
  ```python
    print(llamandoAdan.marca)
    print(llamandoAdan.familia)
    print(llamandoAdan.llamar("David"))
    ```