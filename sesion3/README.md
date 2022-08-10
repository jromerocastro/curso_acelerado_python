# Sesion 3
<img src="https://www.redeszone.net/app/uploads-redeszone.net/2018/07/C%C3%B3digo-Python.jpg">

---
Listado de ejercicios

* ejercicio18.py

Descripcion: listas
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion2/ejercicio18.py
Autor: jromeroc
Action: listas
'''
personas_autorizadas = ["Alberto", "Carmen", "Luis", "Javier", "Diana"]
nombre = input("Dígame su nombre: ")
if nombre in personas_autorizadas:
  print("Está autorizado")
else:
  print("No está autorizado")
``` 
* ejercicio19.py

Descripcion: palindromo
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion2/ejercicio19.py
Autor: jromeroc
Action: palindromo
'''
word = input("Introduce una palabra: ")
reversed_word = word
word = list(word)
reversed_word = list(reversed_word)
reversed_word.reverse()
if word == reversed_word:
  print("Es un palíndromo")
else:
  print("No es un palíndromo")

``` 
* ejercicio20.py

Descripcion: lista de precios
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion2/ejercicio20.py
Autor: jromeroc
Action: lista de precios
'''
prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
suma=0
for price in prices:
  suma += price
  if price < min:
    min = price
  elif price > max:
    max = price
  
print("El mínimo es " + str(min))
print("El máximo es " + str(max))
print("La suma es " + str(suma))
``` 
* ejercicio21.py

Descripcion: listas de materias
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion2/ejercicio21.py
Autor: jromeroc
Action: listas de materias
'''
materias = ["Matemáticas", "Física", "Química",
"Historia", "Lengua"]
for materia in materias:
  print(materia)

``` 
* ejercicio22.py

Descripcion: listas de numeros de loteria
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion2/ejercicio22.py
Autor: jromeroc
Action: listas de numeros de loteria
'''
loteria = list()
cantidad = 5
print("Numeros de la loteria")
for n in range(cantidad):
  numero=input("Ingrese un numero ganador:")
  loteria.append(numero)

print("Numeros ordenados:")
loteria.sort()
for numero in loteria:
  print(numero)

``` 
* ejercicio23.py

Descripcion: diccionario
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion2/ejercicio23.py
Autor: jromeroc
Action: diccionario
'''
a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
  product += a[i]*b[i]
print()
print()
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product))

c = (2, -1, 8)
product2 = 0
for i in range(len(a)):
  product2 += a[i]*b[i]*c[i]

print("El producto de los vectores" + str(a) + ", " + str(b)+ " y " +  str(c) + " es " + str(product2))


``` 
* ejercicio24.py

Descripcion: diccionario
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion2/ejercicio24.py
Autor: jromeroc
Action: diccionario
'''
persona = {}
continuar = True
while continuar:
  clave = input('¿Qué dato quieres introducir? ')
  valor = input(clave + ': ')
  persona[clave] = valor
  print(persona)
  continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"

``` 
* ejercicio25.py

Descripcion: diccionario español- ingles
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion2/ejercicio25.py
Autor: jromeroc
Action: diccionario español- ingles
'''

diccionario = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
  clave, valor = i.split(':')
  diccionario[clave] = valor

frase = input('Introduce una frase en español: ')
for i in frase.split():
  if i in diccionario:
    print(diccionario[i], end=' ')
  else:
    print(i, end=' ')

``` 
* ejercicio26.py

Descripcion: diccionario de divisas
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion2/ejercicio26.py
Autor: jromeroc
Action: diccionario de divisas
'''
divisas = {'Euro':'€', 'Dollar':'$', 'Peso':'$'}
consulta = input("Ingrese una divisa: ")
if consulta in divisas:
  print ("El simbolo del", consulta, "es", divisas[consulta])
else:
  print ("Esa divisa no está registrada")

``` 
* ejercicio27.py

Descripcion: diccionario de datos de un usuario
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion2/ejercicio27.py
Autor: jromeroc
Action: diccionario de datos de un usuario 
'''

usuario = {}
usuario["nombre"]    = input("Ingrese su nombre: ")
usuario["edad"]      = input("Ingrese su edad: ")
usuario["direccion"] = input("Ingrese su dirección: ")
usuario["telefono"]  = input("Ingrese su teléfono: ")

print ("El usuario", usuario["nombre"], "tiene",usuario["edad"],"años, vive en", usuario["direccion"], "y su numero de telefono es", usuario["telefono"])

``` 
* ejercicio28.py

Descripcion:  diccionario de facturas
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion2/ejercicio28.py
Autor: jromeroc
Action: diccionario de facturas
'''
pendiente= 0
cobrado  = 0
opcion = 0
facturas = {}
while opcion != 3:
  print("===================")
  print("Facturas por cobrar")
  print("===================")
  for factura in facturas:
    print(factura,"Importe",facturas[factura])
    
  print("Importe pendiente:", pendiente)
  print("Importe cobrado:", cobrado)
  
  print("===================")
  print("Menu del sistema")
  print("===================")
  print("1. Agregar factura")
  print("2. Pagar una factura")
  print("3. Terminar")
  print()
  opcion=int(input("Seleccione una opcion (1-3):"))
  print()
  if opcion==1:
    print("Agregar una nueva factura")
    num = str(input("Numero de factura:"))
    imp = float(input("Importe de la factura:"))
    pendiente += imp
    facturas[num] = imp
  if opcion==2:
    print("Pagar una factura existente")
    num = str(input("Numero de factura:"))
    if num in facturas:
      pendiente -= facturas[num]
      cobrado   += facturas[num]
      facturas.pop(num)
    else:
      print("No existe la factura",num)

``` 
