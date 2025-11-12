# mayor o menor de edad

# Paso 1: Solicitar el nombre y la edad
nombre = input("Ingrese su nombre: ")
edad = int(input("Ingrese su edad: "))


print(f"Nombre: {nombre}")
print(f"Edad: {edad}")

if edad >= 18:
    print(f"{nombre} es Mayor de edad.")
else:
    print(f"{nombre} es Menor de edad.")