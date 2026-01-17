soma = 0
for n in range(1, 7):
    n_usuario = int(input('Digite um número par: '))
    if n_usuario % 2 == 0:
        soma += n_usuario
    else:
        print('Este número é ímpar e será ignorado')
print(f'O valor {soma}')
