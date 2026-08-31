numeros = [12, 7, 5, 18, 22, 9, 3, 14, 30, 11]
pares = []
impares = []

for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print(f"Lista completa: {numeros}")
print(f"Números pares: {pares}")
print(f"Números ímpares: {impares}")