'''
*********** Curso de programación acelerada en Python ************
Date 08-08-2022
File: sesion/ejercicio3.py
Autor: jromeroc
Action: pago de trabajador
'''
horas = float(input("Introduce tus horas de trabajo: "))
extra = float(input("Introduce tus horas extra: "))
coste = float(input("Introduce lo que cobras por hora: "))

paga = horas * coste + extra * coste * 2
print("Tu paga es", paga)