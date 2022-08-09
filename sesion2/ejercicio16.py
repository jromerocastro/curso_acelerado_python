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