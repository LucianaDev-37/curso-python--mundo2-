frase = str(input('Digite uma frase: ' )).strip().upper()
palavra = frase.split()
junto = ''.join(palavra)
inverso = junto[::-1]#fatiamento
'''for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra]'''
print (inverso, junto)
if junto == inverso:
        print('Temos um palíndromo!')
else:
        print('A frase digitada não é um palíndromo!')
