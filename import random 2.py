import random

# Algoritmo que genera un número aleatorio y lo disminuye en un 15%

# Generar número aleatorio entre 10 y 50
numero = random.randint(10, 50)

# Calcular el número disminuido en un 15%
disminuido = numero * 0.85  # 100% - 15% = 85% → 0.85

# Mostrar resultados
print("Número generado:", numero)
print("Número disminuido en un 15%:", disminuido)