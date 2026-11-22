# Conversor de divisas

# 1. Solicitar una cantidad al usuario
cantidad = float(input("Ingrese la cantidad en moneda local: "))

# 2. Consultar las conversiones
usd = cantidad * 0.050
eur = cantidad * 0.047
gbp = cantidad * 0.039
jpy = cantidad * 7.71

# 3. Mostrar los resultados
print(" === CONVERSIÓN DE DIVISAS === ")
print("USD: ", format(usd, ".2f"))
print("EUR: ", format(eur, ".2f"))
print("GBP: ", format(gbp, ".2f"))
print("JPY: ", format(jpy, ".2f"))