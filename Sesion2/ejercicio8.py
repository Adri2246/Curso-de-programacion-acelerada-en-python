'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion2/ejercicio8.py
Autor: Adriana Romero
Action: detecta numero negativos
'''
numero = int(input("Escriba un número positivo: "))
if numero == 0:
  print("Neutro")
elif numero < 0:
    print("Negativo")
else:
    print("Positivo")