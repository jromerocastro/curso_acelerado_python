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
