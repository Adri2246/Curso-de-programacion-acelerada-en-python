'''
*********** Curso de programación acelerada en Python ************
Date xx-xx-xxxx
File: sesion/ejercicio3.py
Autor: Adriana Romero
Action: pago de trabajador
'''
horas = float(input("Introduce tus horas de trabajo: "))
coste = float(input("Introduce lo que cobras por hora: "))
horasextra = float(input("Horas de trabajo extra: "))
totalhoras = horas + horasextra
paga = totalhoras * coste
print("Tu paga es", paga)