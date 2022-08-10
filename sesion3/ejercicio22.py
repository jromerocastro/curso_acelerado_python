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


