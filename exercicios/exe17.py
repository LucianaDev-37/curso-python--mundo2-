n = int(input('Digite um número: '))
contador = 0
for p in range(1, n + 1, 1):
    if n % p == 0:
        contador += 1
        print(p)
if contador == 2:
    print ('O numero digitado é PRIMO!')
else:
    print ('O número digitado NÃO É PRIMO!')


