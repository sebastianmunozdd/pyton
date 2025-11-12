# Menú sumar, restar o salir

while True:
    print("\n--- MENÚ DE OPERACIONES ---")
    print("1. Sumar")
    print("2. Restar")
    print("3. Salir")
    
    opcion = input("Seleccione una opción (1-3): ")
    
    if opcion == "1":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"Resultado de la suma: {num1 + num2}")
        
    elif opcion == "2":
        num1 = float(input("Ingrese el primer número: "))
        num2 = float(input("Ingrese el segundo número: "))
        print(f"Resultado de la resta: {num1 - num2}")
        
    elif opcion == "3":
        print("¡Programa finalizado! ")
        break  
        
    else:
        print("Opción no válida. Intente de nuevo.")