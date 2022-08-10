'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion2/ejercicio20.py
Autor: jromeroc
Action: lista de precios
'''
prices = [50, 75, 46, 22, 80, 65, 8]
min = max = prices[0]
suma=0
for price in prices:
  suma += price
  if price < min:
    min = price
  elif price > max:
    max = price
  
print("El mínimo es " + str(min))
print("El máximo es " + str(max))
print("La suma es " + str(suma))