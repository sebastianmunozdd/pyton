n = int(input("Ingrese un número entero: "))
invertido = 0
original = n

while n != 0:
    digito = n % 10
    invertido = invertido * 10 + digito
    n = n // 10

print(f"El número invertido de {original} es: {invertido}")