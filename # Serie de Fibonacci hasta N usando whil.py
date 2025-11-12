# Serie de Fibonacci hasta N usando while


N = int(input("Ingrese un número N: "))


a, b = 0, 1

print("Serie de Fibonacci hasta", N, ":")

# Proceso con ciclo while


while a <= N:
    print(a, end=" ")
    a, b = b, a + b  # Avanzar en la serie

print()  # Salto de línea final