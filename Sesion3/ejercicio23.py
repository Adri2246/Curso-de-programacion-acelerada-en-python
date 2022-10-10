'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion2/ejercicio13.py
Autor: Adriana Romero
Action: Números ganadores de la lotería,
'''

a = (1, 2, 3)
b = (-1, 0, 2)
c = (-2, 1, 3)
product = 0
for i in range(len(a)):
  product += a[i]*b[i]
  product1 =  product*c[i]
  print("El producto de los vectores" + str(a) + " y " + str(b) + " es "   + str
  (product))
  print("El producto de los vectores" + str(a) + " y " + str(b) + " y " + str(c) + "es "   + str  (product1))