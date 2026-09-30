# Taller #3: Condiciones Simples (AA3-EV01)
# Autor: Isaac Alejandro García Amaya
# Ficha: 3621358
# Fecha: 29/09/2026

from datetime import date 

# Obtener y mostrar la fecha actual 
hoy = date.today()
print("Hoy es el dia: ",hoy)
print("_" * 30)

#Ejercicio 1: Comparación de 2 valores numéricos

a = int(input("Digite el primer valor de A: "))
b = int(input("Digite el segundo valor de B: "))

if a >= b:
    print("Resultado: A es mayor o igual que B")
else:
    print("Resultado: A es menor que B")
    
print("_" * 30)

# Ejercicio 2: Validación con operadores lógicos (and)

curso1 = "Requerimientos"
curso2 = "Algoritmos"

print("El curso 1 es: ",curso1)
print("El curso 2 es: ",curso2)

if curso1 == "Requerimientos" and curso2 == "Algoritmos":
    print("Resultado: Los cursos son Requerimientos y Algoritmos")
else:
    print("Resultado: No cumple con los cursos requeridos")