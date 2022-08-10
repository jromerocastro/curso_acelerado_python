'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion2/ejercicio23.py
Autor: jromeroc
Action: diccionario
'''
a = (1, 2, 3)
b = (-1, 0, 2)
product = 0
for i in range(len(a)):
  product += a[i]*b[i]
print()
print()
print("El producto de los vectores" + str(a) + " y " + str(b) + " es " + str(product))

c = (2, -1, 8)
product2 = 0
for i in range(len(a)):
  product2 += a[i]*b[i]*c[i]

print("El producto de los vectores" + str(a) + ", " + str(b)+ " y " +  str(c) + " es " + str(product2))
