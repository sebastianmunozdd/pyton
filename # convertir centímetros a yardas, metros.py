# convertir centímetros a yardas, metros, pies y pulgadas

# Entrada de datos
cm = float(input("Introduce una longitud en centímetros: "))

# Proceso de conversión
metros = cm / 100
pulgadas = cm / 2.54
pies = pulgadas / 12
yardas = pies / 3

# Salida de datos
print("Longitud en centímetros:", cm)
print("Equivale a:")
print("=", metros, "metros")
print("=", yardas, "yardas")
print("=", pies, "pies")
print("=", pulgadas, "pulgadas")