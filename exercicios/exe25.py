#from math import factorial
n = int(input('Digite um número para calcular seu Fatorial: '))
c = n 
fatorial = 1

print(f'Calculando {n}! = ', end='')

while c > 0:
    print(f'{c}', end='')
    if c > 1:
        print(' x ', end='')
    else:
        print(' = ', end='')
    fatorial *= c
    c -= 1
print(f'{fatorial}')