# Ingresa tu nombre y apellido
nombre1 = input("Ingresa tu primer nombre: ")
nombre2 = input("Ingresa tu segundo nombre: ")
apellido1 = input("Ingresa tu primer apellido: ")
apellido2 = input("Ingresa tu segundo apellido: ")

# Eliminar espacios innecesarios
nombre1 = nombre1.strip().title()
nombre2 = nombre2.strip().title()
apellido1 = apellido1.strip().title()
apellido2 = apellido2.strip().title()

#Aquí se combina los nombres y apellidos
nombre_completo = " ".join(
    parte for parte in [nombre1, nombre2, apellido1, apellido2] if parte
)

# el reusltado
print("Nombre completo: ", nombre_completo)