from random import randint
print('=-'*15)
print( 'VAMOS JOGAR PAR OU IMPAR ')
print('=-'*15)
c = 0
v = 0 #vitória
while True:
    comp = randint (0, 10)
    n = int(input('Digite um número: '))
    jogador = str(input('Escolha entre PAR ou Impar (P/I): ')).strip().upper()[0]
    s = n + comp
    
    if s % 2 == 0:
        r = 'PAR'
    else: 
        r = 'IMPAR'
    print(f'Você jogou {jogador} e o computador {comp}. Total deu {s}: DEU {r} ! ')
    
    if jogador == 'P' and r == 'PAR':
        print('VENCEU!')
        v += 1
    elif jogador == 'I' and r == 'IMPAR':
        print ('VENCEU!')
        v += 1
    else:
        print('PERDEU!')
        break
print('=-'*15)
print(f'GAME OVER! Você venceu {v} vezes.')
print('=-'*15)