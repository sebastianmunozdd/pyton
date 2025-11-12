# primo

# Entrada
n = int(input("Ingrese un número entero mayor que 1: "))

es_primo = True  

for i in range(2, n):
    if n % i == 0:
        es_primo = False
        break  


if es_primo:
    print(f"{n} es un número primo.")
else:
    print(f"{n} NO es un número primo.")