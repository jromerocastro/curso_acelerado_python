'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion2/ejercicio25.py
Autor: jromeroc
Action: diccionario español- ingles
'''

diccionario = {}
palabras = input("Introduce la lista de palabras y traducciones en formato palabra:traducción separadas por comas: ")
for i in palabras.split(','):
  clave, valor = i.split(':')
  diccionario[clave] = valor

frase = input('Introduce una frase en español: ')
for i in frase.split():
  if i in diccionario:
    print(diccionario[i], end=' ')
  else:
    print(i, end=' ')