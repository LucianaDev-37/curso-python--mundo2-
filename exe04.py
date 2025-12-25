
from datetime import date
nascimento= int(input('Digite o ano do seu nascimento: '))
ano= date.today().year
idade= ano - nascimento
tempo_falta= 18 - idade
tempo_passou= idade - 18
if idade < 18:
        print ('Você tem {} anos em {}.Ainda não é hora de se alistar, faltam {} anos para completar 18anos. '.format (idade,ano,tempo_falta))
elif idade == 18:
    print ('Você tem {} anos em {}.Ja é exatamente a hora de se alistar '.format(idade,ano))
elif idade > 18:
    print ('Você tem {} anos em {}.Já passou do tempo do alistamento, passaram {} anos dos 18 anos. '.format(idade,ano,tempo_passou))


