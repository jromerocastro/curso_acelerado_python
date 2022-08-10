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