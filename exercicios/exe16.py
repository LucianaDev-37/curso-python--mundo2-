p_termo = int(input('Digite o primeiro termo: '))
razao = int(input('Digite a razão: '))
decimo_termo = p_termo + (10 - 1) * razao
for n in range(p_termo, decimo_termo + razao, razao):
    print(f'{n}', end = '->')
print('Fim')