# Sesion 1

---
Listado de ejercicios

* ejercicio1.py

Descripcion: asignación de variables
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 08-08-2022
File: sesion/ejercicio1.py
Autor: jromeroc
Action: asignación de variables
'''
nombre_estado = 'Tabasco'
superficie = 25267
poblacion_total = 2403000000
promedio_temperatura = 31.3
estados_cercanos = ['Chiapas','Campeche','Veracruz']
productos = ['cacao','coco','caña']
print(nombre_estado, "es un estado que", )
print("colinda al sur","con",estados_cercanos[0],  "y")
print("tiene una superficie de", superficie)
print("tiene una poblacion de", poblacion_total, "habitantes")
print("tiene un promedio de temperatura de", promedio_temperatura, "° C")

print("Sus principales productos son:", productos)

``` 
* ejercicio2.py

Descripcion: superficie de un cuadrado
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 08-08-2022
File: sesion/ejercicio2.py
Autor: jromeroc
Action: superficie de un cuadrado
'''
lado=input("Ingrese la medida del lado del cuadrado:")
lado=float(lado)
superficie=lado*lado
print("La superficie del cuadrado es")
print(superficie)
``` 
* ejercicio3.py

Descripcion: pago de un trabajador
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 08-08-2022
File: sesion/ejercicio3.py
Autor: jromeroc
Action: pago de trabajador
'''
horas = float(input("Introduce tus horas de trabajo: "))
extra = float(input("Introduce tus horas extra: "))
coste = float(input("Introduce lo que cobras por hora: "))

paga = horas * coste + extra * coste * 2
print("Tu paga es", paga)
``` 
* ejercicio4.py

Descripcion: indice de masa corporal peso en kg/ estatura mtrs cuadrados
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 08-08-2022
File: sesion/ejercicio4.py
Autor: jromeroc
Action: indice de masa corporal peso en kg/ estatura mtrs cuadrados
'''
peso = input("¿Cuál es tu peso en kg? ")
estatura = input("¿Cuál es tu estatura en metros?")
imc = round(float(peso)/float(estatura)**2,2)
print("Tu índice de masa corporal es " + str(imc))
``` 
* ejercicio5.py

Descripcion: convertir temperatura
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 08-08-2022
File: sesion/ejercicio5.py
Autor: jromeroc
Action: convertir temperatura
'''
celsius=input("Ingrese la temperatura en grados celsius:")
celsius=float(celsius)
farenheit= celsius*1.8 + 32
print(celsius,"° C =>", farenheit,"° F")
``` 
* ejercicio6.py

Descripcion: imprime capital obtenido de una inversión
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 08-08-2022
File: sesion/ejercicio6.py
Autor: jromeroc
Action: imprime capital obtenido de una inversión
'''
cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = float(input("¿Años?"))
print("Capital final: " + 
      str(round(cantidad * (interes / 100 + 1) ** años, 2)))
``` 
* ejercicio7.py

Descripcion: Suma de los primeros números enteros
``` python
'''
*********** Curso de programación acelerada en Python ************
Date 08-08-2022
File: sesion/ejercicio7.py
Autor: jromeroc
Action: Suma de los primeros números enteros
'''
n = int(input("Introduce un número entero: "))
suma = int(n * (n + 1) / 2)
print("La suma de los primeros enteros desde 1 hasta " + str(n) + " es " + str(suma))

