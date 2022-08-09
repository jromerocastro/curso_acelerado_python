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