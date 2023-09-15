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
- Cuando no sabemos la cantidad de veces a repetir.
