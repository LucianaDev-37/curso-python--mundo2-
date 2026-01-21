print ('----- TABUADA ----- ')
print (' = '*10)
n = 0
c = 0
r = 1
while True:
    n = int(input('Digite um número: '))
    if n < 0:
      break

    for c in range (1, 11):
      r = n * c
      print(f'{n} x {c} = {r}')     