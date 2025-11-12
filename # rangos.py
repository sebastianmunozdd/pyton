# rangos


x = float(input("Ingrese un número real: "))

# Paso 2: Verificar si el número pertenece a alguno de los rangos
if (3.5 < x <= 7.8) or (4.5 < x <= 9.3) or (23.4 <= x <= 45.3):
    print(f"El número {x} se encuentra dentro de uno de los rangos.")
else:
    print(f"El número {x} NO se encuentra dentro de ninguno de los rangos.")