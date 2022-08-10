'''
*********** Curso de programación acelerada en Python ************
Date 10-08-2022
File: sesion2/ejercicio28.py
Autor: jromeroc
Action: diccionario de facturas
'''
pendiente= 0
cobrado  = 0
opcion = 0
facturas = {}
while opcion != 3:
  print("===================")
  print("Facturas por cobrar")
  print("===================")
  for factura in facturas:
    print(factura,"Importe",facturas[factura])
    
  print("Importe pendiente:", pendiente)
  print("Importe cobrado:", cobrado)
  
  print("===================")
  print("Menu del sistema")
  print("===================")
  print("1. Agregar factura")
  print("2. Pagar una factura")
  print("3. Terminar")
  print()
  opcion=int(input("Seleccione una opcion (1-3):"))
  print()
  if opcion==1:
    print("Agregar una nueva factura")
    num = str(input("Numero de factura:"))
    imp = float(input("Importe de la factura:"))
    pendiente += imp
    facturas[num] = imp
  if opcion==2:
    print("Pagar una factura existente")
    num = str(input("Numero de factura:"))
    if num in facturas:
      pendiente -= facturas[num]
      cobrado   += facturas[num]
      facturas.pop(num)
    else:
      print("No existe la factura",num)
    
    
    