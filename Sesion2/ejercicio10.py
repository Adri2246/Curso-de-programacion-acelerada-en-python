'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion2/ejercicio10.py
Autor: Adriana Romero
Action: numero par o impar
'''
num = input("Introduce un número: ")
num = int(num)
if num == 0:
    print ("Este número es par.")
elif num%2 == 0:
    print ("Este numero es par")
else:
    print ("Este numero es impar")