'''
*********** Curso de programación acelerada en Python ************
Date xx-xx-xxxx
File: sesion/ejercicio6.py
Autor: Adriana Romero
Action: imprime capital obtenido de una inversión
'''
cantidad = float(input("¿Cantidad a invertir? "))
interes = float(input("¿Interés porcentual anual? "))
años = int(input("¿Años? "))
cantidadtotal = cantidad * interes * años

print("Capital final: " , cantidadtotal)