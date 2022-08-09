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