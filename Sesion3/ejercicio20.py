'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion2/ejercicio13.py
Autor: Adriana Romero
Action: Almacene Lista
'''

prices = [50, 75, 46, 22, 80, 65, 8]
suma_de_prices = sum(prices)
min = max = prices[0]
print("La suma de precios es: " + str(suma_de_prices))
for price in prices:
  if price < min:
    min = price
  elif price > max:
    max = price
    print("El mínimo es " + str(min))
    print("El máximo es " + str(max))