print('='*30)
print('BANCO'.center(30))
print('='*30)

valor = int(input('Que valor você quer sacar? R$ '))
montante = valor
cedula_atual = 50
contador_notas =  0
while True:
    if montante >= cedula_atual:
        montante -= cedula_atual
        contador_notas +=1
    else:
        if contador_notas > 0: 
         print(f'Total de {contador_notas} cédulas de R$ {cedula_atual}')
    
        if cedula_atual == 50:
          cedula_atual = 20
        elif cedula_atual == 20:
         cedula_atual = 10
        elif cedula_atual == 10:
         cedula_atual = 1
        contador_notas = 0
        if montante == 0:
          break
print('='*30)
print('Volte sempre ao BANCO!')

