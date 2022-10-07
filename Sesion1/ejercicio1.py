'''
*********** Curso de programación acelerada en Python ************
Date 04-08-2022
File: sesion/ejercicio1.py
Autor: Adriana Romero
Action: asignación de variables
'''
nombre_estado = 'Tabasco'
superficie = 25267
poblacion_total = 2403000000
promedio_temperatura = 31.3
estados_cercanos = 'chiapas','campeche','veracruz'
productos_locales = 'Cacao','Coco','Caña'

print(nombre_estado, " es un estado que ", )
print("con ", estados_cercanos, "colinda al sur", "y")
print("Tiene una superficie de ", superficie)
print("además se consume mucho el ", productos_locales)

#Ejecute Operaciones matemáticas
c1 = 10
c2 = 8
c3 = 8
promedio = (c1+c2+c3)/3
print()
print("El promedio es: ", promedio)

#Funciones precargadas y anote la acción
ciudad = "villahermosa"
len(ciudad)
estado = "tabasco"
tiempo = 40
precio = 34.78
type(estado)
type(tiempo)
type(precio)
numbers = [3,5,6,2]
sum(numbers)
numbers = [3,5,6,2]
min(numbers)
chr(65)
str.capitalize("villa")
str.lower("VILLAHERMOSA")