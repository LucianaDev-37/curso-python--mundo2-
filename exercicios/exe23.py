from random import randint
tentativa = 0
jogador = int(input('Digite um número de 0 a 10: '))
comp = randint (0, 10)
while comp != jogador:
    tentativa += 1
    jogador = int(input('Digite um número de 0 a 10: '))
    if jogador < comp:
        print ('Mais... tente novamente!')
    else:
        print ('Menos... tente novamente!')
print (f'Acertou com {tentativa +1} tentativas')   
    

