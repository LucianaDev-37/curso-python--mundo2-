print('=-'*15)
print('LOJA SUPER'.center(30)) # centraliza
print('=-'*15)
total_gasto = 0
total1000 = 0
menor_preco = 0
cont = 0
barato = ' '
while True:
    p = str(input('Nome do Produto: ')).strip().upper()
    preco = float(input('Preço: R$ '))
    cont += 1
    total_gasto += preco

    if preco > 1000:
        total1000 += 1

    if cont == 1 or preco < menor_preco:
        menor_preco = preco
        barato = p
    r = str(input('Quer continuar? [S/N] ')).upper().strip()[0]
    if r == 'N':
        break
print(f'Valor total da sua compra: {total_gasto:.2f}')
print(f'Temos {total1000} produtos custando mais de R$ 1.000,00')
print(f'E o produto mais barato foi {barato} que custa R${menor_preco:.2f}')

