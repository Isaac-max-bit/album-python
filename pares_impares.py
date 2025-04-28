# Crear los generadores pares e impares 

#Generador de números pares

def generador_pares(n):
    a=0
    while a < n:
        yield a
        a += 2
for num in generador_pares(10):
    print(num)
    
print("-------------FIN DE LOS PARES-----------------")

def generador_impares(n):
    a=1
    while a < n:
        yield a
        a += 2

for num in generador_impares(10):
    print(num)
    
    print("-------------FIN DE LOS IMPARES-----------------")
    