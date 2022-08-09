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