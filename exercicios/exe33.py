print('=-'*15)
print('CADASTRE UMA PESSOA')
print('=-'*15)
maior_idade = 0
tol_homens = 0
tot_mulher_20 = 0
while True:
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip().upper()[0]

    if idade > 18:
        maior_idade += 1
    if sexo == 'M':
        tol_homens += 1
    if sexo == 'F' and idade < 20:
        tot_mulher_20 += 1
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r == 'N':
        break
print(f'Total de pessoas com mais de 18 anos: {maior_idade}')
print(f'Ao todo temos {tol_homens} homens cadastrados')
print(f'E temos {tot_mulher_20} mulheres com menos de 20 anos')

