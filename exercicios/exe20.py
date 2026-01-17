lista_pesos = [] 

for p in range(1, 6):
    dado = float(input(f'Peso da {p}ª pessoa (kg): '))
    lista_pesos.append(dado)
    
maior = max(lista_pesos)
menor = min(lista_pesos)

print(f'O maior peso lido foi {maior}kg')
print(f'O menor peso lido foi {menor}kg')