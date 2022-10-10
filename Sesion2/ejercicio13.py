'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion2/ejercicio13.py
Autor: Adriana Romero
Action: suma de 10 primeros numeros
'''
import os

suma = 0
for i in range (1, 11):
    print ('Numero ' + repr (i))
    suma=suma+i
    print ()
print ('Valor de suma: ' + repr (suma))
