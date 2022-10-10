'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion2/ejercicio13.py
Autor: Adriana Romero
Action: Persona Autorizada.
'''

personas_autorizadas = ["Alberto", "Carmen", "Adriana", "Lisa", "Marco"]
nombre = input("Dígame su nombre: ")
if nombre in personas_autorizadas:
  print("Está autorizado")
else:
  print("No está autorizado")