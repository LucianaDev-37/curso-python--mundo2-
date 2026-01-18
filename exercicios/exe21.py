soma_idade = 0
maior_idade_homem = 0
nome_velho = ''
tot_mulher_21 = 0
for p in range(1, 5):
    print(f'Digite o nome da {p}ª PESSOA ')
    nome = str(input('Nome: ')).strip()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()
    
    soma_idade += idade
    # Lógica do homem mais velho
    if p == 1 and sexo == 'M':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo == 'M' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
        
    if sexo == 'F' and idade < 21:
        tot_mulher_21 += 1
        print('menor de idade')
media = soma_idade / 4
print(f'A média de idade do grupo é de {media} anos.')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}.')
print(f'Ao todo são {tot_mulher_21} mulheres com menos de 21 anos.')