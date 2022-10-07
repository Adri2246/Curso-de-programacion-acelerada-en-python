'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion2/ejercicio12.py
Autor: ..............
Action: estructura condicional anidada
'''
mes = int(input("Introduzca el mes de año: "))

P á g i n a 4 | 7

if 1 <= mes <= 12:
print("Se ha introducido un mes válido.")
else:
print("El mes es incorrecto. Por defecto se elige Enero.")
mes = 1

print("Se utilizará mes", mes)