# Crear un iterador para los numeros impares

#Limite
limit = 10

odd_itter = iter(range(0, limit+ 1,2))

#Usar el iterador 

for num in odd_itter:
    print(num)