def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        raise ValueError("No se puede dividir por cero")
    return a / b

def calculator():
    while True:
        print("\nSeleccione una operación:")
        print("1. Sumar")
        print("2. Restar")
        print("3. Multiplicar")
        print("4. Dividir")
        print("5. Salir")
        
        try:
            option = int(input("Ingrese su opción (1/2/3/4/5): "))
        except ValueError:
            print("Entrada inválida. Por favor ingrese un número del 1 al 5.")
            continue

        if option == 5:
            print("Saliendo de la calculadora.")
            break

        if option in ["1", "2", "3", "4"]:
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Entrada inválida. Debe ingresar números.")
                continue

            if option == 1:
                print("La suma es:", add(num1, num2))
            elif option == 2:
                print("La resta es:", subtract(num1, num2))
            elif option == 3:
                print("La multiplicación es:", multiply(num1, num2))
            elif option == 4:
                try:
                    print("La división es:", divide(num1, num2))
                except ValueError as e:
                    print(e)
        else:
            print("Opción no válida. Intente de nuevo.")

# Llamar a la función para que se ejecute
calculator()
