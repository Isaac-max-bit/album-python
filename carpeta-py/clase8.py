to_do = ["Dirigirnos al hotel", 
         "Ir a almorzar", 
         "Visitar un museo",
         "Volver al hotel"]

print(to_do)
numbers = [1,2,3,4, "Cinco"]
print(type(numbers))
mix = ["uno", 2, 3.14, True, [1,2,3]]

print(mix)
print(len(mix))
print("Primer elemento", mix[0])
print("Segundo elemento", mix[1])
print("Ultimo elemento:", mix[-1])
string = "Hola Mundo"
print("Primer elemento", string[0])
print("Segundo elemento", string[1])
print("Ultimo elemento:", string[-3])
# print(mix[0:2])
# print(mix[:2])
# print(mix[2:])

print(mix[2:-2])
print(mix)
mix.append(False)
print(mix)
mix.append(["a","b"])
print(mix)
mix.insert(1,["a","b"])
print(mix)
print(mix.index(["a","b"]))


numbers = [1, 2, 100, 90.45, 3, 4, 5]
print(numbers)

# Obtener el valor máximo y mínimo
print("Mayor: ", max(numbers))  # 100
print("Menor: ", min(numbers))  # 1

# Eliminar el último elemento de la lista
del numbers[-1]
print(numbers)  # [1, 2, 100, 90.45, 3, 4]

# Eliminar los dos primeros elementos
del numbers[:2]
print(numbers)  # [100, 90.45, 3, 4]

# Eliminar la lista completamente
numbers = []  # En lugar de usar del para eliminar la lista, se puede vaciarla de esta manera.
print("Lista vacía:", numbers)  # Lista vacía: []
