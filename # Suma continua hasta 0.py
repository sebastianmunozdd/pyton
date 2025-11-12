# Suma continua hasta 0

suma = 0

while True:
    num = int(input("Ingrese un número (0 para terminar): "))
    
    if num == 0:
        break  
    
    if num < 0:
        continue  
    
    suma += num  
    
print("La suma total de los números positivos es:", suma)