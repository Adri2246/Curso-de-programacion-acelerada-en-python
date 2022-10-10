'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion2/ejercicio13.py
Autor: Adriana Romero
Action: Permita ingresar un valor del 1 al
10 y nos muestre la tabla de multiplicar del mismo.
'''

numero = int(input("Introduce un valor: "))
for i in range(0, 11):
  resultado = i*numero
  print(("%d x %d = %d") % (numero, i, resultado))