n1 = int(input('Primeiro valor: '))
n2 = int(input('Segundo valor: '))
p = 0
while p != 5:
    print('''    [ 1 ] somar
    [ 2 ] multiplicar
    [ 3 ] maior
    [ 4 ] novos números
    [ 5 ] sair do programa''')
    p = int(input('>>>> Qual é a sua opção? '))
    if p == 1:
        soma = n1 + n2
        print(f'A soma entre {n1} e {n2} é {soma}')
    elif p == 2:
        mult = n1 * n2
        print(f'O resultado de {n1} x {n2} é {mult}')
    elif p == 3:
        if n1 > n2:
            maior = n1
        else:
            maior = n2
        print(f'Entre {n1} e {n2} o maior é {maior}')
    elif p == 4:
        print('Informe os números novamente:')
        n1 = int(input('Primeiro valor: '))
        n2 = int(input('Segundo valor: '))
    elif p == 5:
        print('Finalizando...')
    else:
        print('Opção inválida. Tente novamente.')