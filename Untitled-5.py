# Ejemplo 2.7: Cálculo de aportes a salud y pensión en Colombia

# Entrada de datos
salario_base = float(input("Ingrese el salario base del empleado: "))

# Proceso
aporte_salud = salario_base * 0.04
aporte_pension = salario_base * 0.04
total_descuento = aporte_salud + aporte_pension
salario_neto = salario_base - total_descuento

# Salida de datos
print("\n--- Resultados ---")
print(f"Aporte a salud (4%): ${aporte_salud:.2f}")
print(f"Aporte a pensión (4%): ${aporte_pension:.2f}")
print(f"Total descuentos: ${total_descuento:.2f}")
print(f"Salario neto a recibir: ${salario_neto:.2f}")