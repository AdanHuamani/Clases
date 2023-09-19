# REPASO PYTHON
## 1. TIPOS DE DATOS
### TEXTO:
En Python, el tipo de datos de texto se conoce como secuencia de caracteres (string). Las secuencias de caracteres pueden contener números y/o caracteres. Por ejemplo, una secuencia de caracteres puede ser una palabra, una oración, o varias oraciones.

Un string puede estar entre comillas simples o dobles. Todo lo que esté entre comillas es un  string,
```python
Ejm.
"a"
"hola"
"hola como estas"
```
### NUMERICO:
Existen dos tipos de datos numéricos: números enteros y de punto flotante o flotantes. A veces, trabajará en el código de otra persona y necesitará convertir un entero en un flotante o viceversa, o puede darse cuenta de que está usando un entero cuando lo que realmente necesita es un flotante.
+ Entero: 100
+ Flotante: 10.1
## BOOLEANO:
Una variable booleana es una variable que sólo puede tomar dos posibles valores: True (verdadero) o False (falso). En Python cualquier variable (en general, cualquier objeto) puede considerarse como una variable booleana. En general los elementos nulos o vacíos se consideran False y el resto se consideran True.
- x = Verdadero
- Y = Falso
## 2. VARIABLES
Es un lugar donde se almacena un tipo de dato, los datos guadados pueden mutar o variar constantemente.
El nombre de la variable tiene que tener un relación con el daro que estas guardando.

Todo lo que se puede describir es un ente:
+ Atributo codificado: Es exacto  
+ Atributo: Varia

### Como creeamos una variable para almacenar datos.
1. Darle un nombre significativo o relacionado al dato que estamos almacenando.
```python
Nombre de estudiante = Adan Huamani Colorado
```
2. Indicarle a que dato esta relacionado (asignación).
```python
Adan = Estudiante
```
3. Indicar el tipo de dato que se va a almacenar (darle el dato a guardar)
```python
Edad_Adan = 19
```
## 3. OPERADORES
### Operadores aritmeticos:
Los operadores aritméticos en Python se utilizan para realizar operaciones matemáticas en valores numéricos.
- Suma -> +
- Resta -> - 
- Multiplicación -> *
- Division -> /
#### EJEMPLOS:
Suma es la variable y el dato es el resultado de la operación.
```python
> Suma: 2+2
> Resta: 4-3
> Multiplicación: 5*8
> Division: 35/5
```
Hay operadores de uso especial 
```python
- Suma=45+30 (El operador suma resultado es 75).
- Suma="45"+12 (Operador concatena y el resultado es 4512).
- Saludo="hola"+"mundo" (Al concatenar queda holamundo).
- Saludo2="hola"+" "+"mundo" (Al concatenar queda hola mundo).
- Saludos="hola"*2 (Se multiplica la palabra por la cantidad de veces que desees "holahola").
```
## 4. DATOS ESTRUCTURADOS
Son tipos de datos ya estructurados 
### listas:
Puede almacenar distintos tipos de datos en una sola lista separados por comas.
```python
+ Lista= ["nombre",10,false]
```
### Objetos:
Tambien al igual que las listas almacenan distintos tipos de datos pero con un orden para almacenar daros en un objeto necesitamos especificar un indice y un valor clave -> valor 

```Python
Alumno={
"Nombre":"Adan"
"Edad":19
}
```
Tambien se puede combinar ambas estructuras de datos.
```python
Alumnos={
    Nombre:"Adan"
    Edad:19
    Amigos:["Pepito","Pepita"]
    Dirección:{
        "Departamento":"Ayacucho"
        "Provincia":"Lucanas"
        "Distrito":"Puquio"
        "Jiron":"Salados Bendezu"
    }
}
```

## 5. CONTROLES DE FLUJO: 
### DECISIONES: 
Solo se ejecuta el codigo si la condicion es verdadera. Podemos hacer que si la condicion sea falsa se ejecute otro codigo.
#### Sintaxis:
Primerpoc especificar el codigo que se ejecutara si cumple una condicion.
```python
if <condicion>
```
El cidigo que deseamos ejecutar si la condicion es verdad.
```python
   print("Ejecuta esto")
   ```
Aquí estamos fuera del if o del si este codigo siempre se ejecutara no depende del if.
```python
print("esto siempre se ejecutara")
```
Si queremos que se ejecute otro codigo en caso sea falso.
```python
if <condicion falsa>:
    print("solo emprime si es verdad")
else
    print("solo imprime si es falso")
```
Ejemplitos:
```Python
if 15>18
    print("solo imprime si es verdad")
else:
    print("solo imprime si es falso")
```
```python
if 15*2==30:
    print("imprime esto si es verdad")
else:
    print("imprime esto si es falso")
```
```python
if condicion=true
    print("imprime esto si es verdad")
else: 
    print("imprime esto si es falso")
```
### CICLOS: 
#### Existen dos tipos de ciclos:
- Cuando sabes la cantidad de veces que vamos a repetir.
  - para este caso existe el for.
  - sentaxis despues de la palabra reservada for debemos crear una variable que almacene el numero que iremos iterando.
  - Luego tendremos que indicar el rango a iterar a los elementos.
```python
  vocales=[a,e,i,o,u]
  for i in vocales:
    print(i)
  ```
- Cuando no sabemos la cantidad de veces a repetir. para eso usamos while.
  - **while:** todas las condiciones que son verdaderas van a permitir que el codigo se ejecute, evalua si la condicion es verdadera (es un ciclo infinito).
  ```python
  condicion = true
  while condicion 
    print ("hola")
    texto=input("ingresa tu nombre o salir para terminar el programa:")
    if texto=="salir"
        condicion=false    
  ```
  - for: Sabe la cantidad de veces que se va ejecutar el ciclo en el programa.
## FUNCIONES:
Existen 2 tipos de funciones.
1. Funciones propias del lenguaje: Que ya vienen creadas e insertadas en python y estan listas para ser usadas.
   
   Estructura de uso de una funcion:
   Tiene nombre seguido de parentesis ( ), dentro de las parentisis podremos pasarle que nesecita la funcion para ejecutarse.
   Esta es una funcion que nos sirve para mostrar datos por consola.

     #### **Print:**
    Esta es una funbcion que nos sirve para mostrar el dato por consola.
    ```python
    print("Hola Chamo")
    ```
    #### **Len:** 
    Esta funcion nos permite saber la longitud de una lista o un string.
    ```python
    print(len([7,1,10,17]))
    ```
    #### **Input:** 
    Es una funcion que se detiene a esperar que el usuario. entre parentisis podremos escribir un mensaje que indique que accion realizara el usuario.
    ```python
    input("Ingresa tu nombre")
    ```
    #### **Max**: 
    Esta funcion nos muestra el numero mayor de una lista.
    ```python
    Lista=[12,43,6,77,9,17,10]
    numero_mayor=max(lista)
    print(numero_mayor)
    ```
    #### **Min**: 
    Esta funcion nos muestra el numero menor de una lista.
    ```python
    Lista=[43,54,65,87,10,7]
    numero_menor=min(lista)
    print(numero_menor)
    ```
    #### **int**: 
    Funcion para convertir de un string a un numero entero
    ```python
    int("100") -> 100 -> entero
    ```
    #### **str**: 
    Funcion para convertir un entero a un string.
    ```python
    str(100) -> "100" -> string
    ```
    #### **append**:
    Funcion de python que nos permite agregar elementos al finmal de una lista.
    ```python
    lista=[15,32,10,7]
    elemento=100
    lista.append(elemento)
    print(lista)
    ```
    #### **pop**: 
    Funcion de python que nos permite eliminar los elementos que se encuentran al final de una lista.
    ```python
    lista=[10,7,17,47]
    lista.pop()
    print(lista)
    ```
    #### **insert**:
    Funcion de python que nos permite agregar elementos en cualquier posicion de mi lista para eso se le tiene que pasar dos parametros, primero indicarle el indice y segundo el dato que se va agregar.
    ```python
    lista_nombres=["jory","nadine","bicho"]
    lista_numbres.insert(1,"adan")
    print(lista_nombres)
    ```
    #### **remove**: 
    Funcion de python que nos permite eliminar elementos de cualquier posicion de una lista, esta funcion solo recibe elementos que deseamos eliminar.
    ```python
    lista=[4,5,6,7,8,9]
    lista.remove(6)
    print(lista)
    ```
    #### split: 
    Funcion que nos permite dividir en una lista una cadena.
    ```python
    cadena="hola como estas"
    lista=cadena.split()
    print(lista)
    url="www.golle.com/id=70133573"
    id=url.split("=").pop()
    print(id)
    ```
### 2. FUNCIONES CREADAS.
Una funcion son miniprogramas tambien se le conoce como modulos o fragmentos de cidgo de uso exclusivo.
### Funciones propias: 
Pasos para crear una funcion propia.
1. Hacer uso de la palabra resevada def.
2. Definir un nombre de funcion que describa que tarea va a realizar.
3. Establecer los paramtros que resivira la funcion entre parentisis ().
4. Establecer que valor o dato va retornar mi funcion con la palabra reservada return.
5. **Observación**: Tambien podemos hacer uso de la funcion print () para retornar un mensaje en nuestra funcion.
Existen dos tipos de funciones los que no reciben ningun parametro y los que reciben parametros.
```python
def saludo():
    print("hola este es un saludo")
```
- Como hacemos uso de la funcion?
- Nombre de la funcion y perentisis.
- Funcion con parametros.
```python
def mi_print(texto)
print(texto)
print("hola este es print de python")
mi_print("hola este es mi print creado")
```
```python
def suma(a+b)
    total=a+b
    return total
mi_print(suma(10+7))
```
+ Ejemplo: Para que se usa esta funcion. Para mostrar el valor maximo de una lista.
  ```python
  lista=[12,4,10,17,7]
  mi_print(max(lista))
  
  def mi_max(lista):
    numero_mayor=lista[0]
    for numero in lista:
        if numero > numero_mayor:
            numero_mayor=numero
    return numero_mayor
mi_print(mi_max(lista))
```


