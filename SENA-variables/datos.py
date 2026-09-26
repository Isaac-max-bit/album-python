# Taller 1: ENTRADA Y SALIDA DE DATOS
# Autor: Isaac Alejandro García Amaya
# Fecha: 25/09/2026

from datetime import date

hoy = date.today()
print("Hoy es el dia: ",hoy)

n1 = int(input("Digite  el primer numero: "))
n2 = int(input("Digite  el segundo numero: "))

suma = n1 + n2
resta = n1 - n2
producto = n1 * n2
division = n1 / n2

print("El resultado de la suma es: ",suma)
print("El resultado de la resta es: ",resta)
print("El resultado del producto es: ",producto)
print("El resultado de la division es: ",division)

print("FIN")