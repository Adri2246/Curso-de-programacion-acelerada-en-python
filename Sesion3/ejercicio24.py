'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion2/ejercicio13.py
Autor: Adriana Romero
Action: Introducir Datos.
'''

persona = {}
continuar = True
while continuar:
  clave = input('¿Qué dato quieres introducir? ')
  valor = input(clave + ': ')
  persona[clave] = valor
  print(persona)
  continuar = input('¿Quieres añadir más información (Si/No)? ') == "Si"