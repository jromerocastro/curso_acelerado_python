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