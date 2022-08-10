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

