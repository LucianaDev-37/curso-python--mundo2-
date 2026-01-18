soma = 0
cont = 0
for n in range(1, 7):
    n_usuario = int(input('Digite um número par: '))
    if n_usuario % 2 == 0:
        soma += n_usuario
        cont += 1
    else:
        print('Este número é ímpar e será ignorado')
print(f'O valor da soma {soma}')
