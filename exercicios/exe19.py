from datetime import date

ano_atual = date.today().year
tot_maior = 0
tot_menor = 0

for pessoa in range(1, 8):
    nasc = int(input(f'Em que ano a {pessoa}ª pessoa nasceu? '))
    idade = ano_atual - nasc
    if idade >=21:
        tot_maior += 1
    else:
        tot_menor += 1
print (f'Atingiram a maioridade {tot_maior}. Ainda não atigiram a maioridade {tot_menor}.')