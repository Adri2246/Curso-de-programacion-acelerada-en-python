'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: Sesion2/ejercicio11.py
Autor: Adriana Romero
Action: estructura condicional anidada
'''

def isYearLeap(year):
    if year % 4 != 0:
        return False
    elif year % 100 != 0:
        return True
    elif year % 400 != 0:
        return False
    else:
        return True

def daysInMonth(year, month):
    monthDays = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if isYearLeap(year) and month == 2:
        return 29
    return monthDays[month - 1]

while True:
    mes = int(input("Ingrese mes:"))
    ano = int(input("Ingrese año:"))
    print(f"El mes {mes}/{ano} contiene {daysInMonth(ano, mes)}")