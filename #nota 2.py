#nota 2


nota = float(input("Ingrese la nota definitiva (0.0 a 5.0): "))

# Paso 2: rango 
if nota < 0 or nota > 5.0:
    print("Error: la nota debe estar entre 0.0 y 5.0.")
elif nota < 3.0:
    print("Insuficiente")
elif nota <= 3.5:
    print("Aceptable")
elif nota <= 4.0:
    print("Sobresaliente")
else:  # nota <= 5.0
    print("Excelente")