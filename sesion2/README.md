# Sesion 2
<img src="https://www.redeszone.net/app/uploads-redeszone.net/2018/07/C%C3%B3digo-Python.jpg">

---
Listado de ejercicios

* ejercicio9.py

Descripcion: preguntar contraseña
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 09-08-2022
File: sesion2/ejercicio9.py
Autor: jromeroc
Action: preguntar contraseña
'''
PASSWORD = "98765"
contraseña = str(input("Escriba su contraseña: "))
if contraseña == PASSWORD:
  print("¡contraseña correcta!")
else:
  print("¡contraseña incorrecta!")
``` 

* ejercicio10.py

Descripcion: numero par o impar
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 05-08-2022
File: sesion2/ejercicio10.py
Autor: jromeroc
Action: numero par o impar
'''
n = int(input("Introduce un número entero: "))
if n % 2 == 0:
  print("El número " + str(n) + " es par")
else:
  print("El número " + str(n) + " es impar")
``` 

* ejercicio11.py

Descripcion: estructura condicional anidada
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 05-08-2022
File: sesion2/ejercicio11.py
Autor: jromeroc
Action: estructura condicional anidada
'''
mes = int(input("Introduzca el mes del año: "))
if mes == 1 or mes == 3 or mes == 5 or mes == 7 or mes == 8 or mes == 10 or mes == 12:
  print("El mes tiene 31 días.")
elif mes == 2:
  print("El mes tiene 28 o 29 días.")
elif mes == 4 or mes == 6 or mes == 9 or mes == 11:
  print("El mes tiene 30 días.")
else:
  print("Mes no válido.")
``` 

* ejercicio12.py

Descripcion: estructura condicional anidada
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 09-08-2022
File: sesion2/ejercicio12.py
Autor: jromeroc
Action: estructura condicional anidada
'''
mes = int(input("Introduzca el mes de año: "))
if 1 <= mes <= 12:
  print("Se ha introducido un mes válido.")
else:
  print("El mes es incorrecto. Por defecto se elige Enero.")
  mes = 1
  
print("Se utilizará mes", mes)
``` 

* ejercicio13.py

Descripcion: suma de 10 primeros numeros
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 09-08-2022
File: sesion2/ejercicio13.py
Autor: jromeroc
Action: suma de 10 primeros numeros
'''
num = 1
suma = 0
while num <= 10:
  suma += num
  print(suma)
  num += 1
``` 

* ejercicio14.py

Descripcion: repetir una palabra
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 09-08-2022
File: sesion2/ejercicio9.py
Autor: jromeroc
Action: repetir una palabra
'''
palabra = str(input("Escriba una palabra: "))
num = 1
while num <= 10:
  print(num,palabra)
  num += 1
``` 

* ejercicio15.py

Descripcion: 
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 09-08-2022
File: sesion2/ejercicio13.py
Autor: jromeroc
Action: suma valores ingresados por teclado
'''
suma = 0
for f in range(10):
  valor = int(input("Ingrese valor:"))
  suma = suma + valor
  
print("La suma es")
print(suma)
promedio = suma / 10
print("El promedio es:")
print(promedio)

``` 

* ejercicio16.py

Descripcion: imprime un triangulo
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 09-08-2022
File: sesion2/ejercicio16.py
Autor: jromeroc
Action: imprime un triangulo
'''
n = int(input("Introduce la altura del triángulo (entero positivo): "))
for i in range(n):
  for j in range(i + 1):
    print("*", end="")
  print("")
``` 

* ejercicio17.py

Descripcion: imprime una tabla de multiplicar
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 09-08-2022
File: sesion2/ejercicio17.py
Autor: jromeroc
Action: imprime una tabla de multiplicar
'''
n = int(input("Introduce un numero (entero positivo): "))
for i in range(1,11):
  print(n,"x",i,"=",n*i)
``` 
