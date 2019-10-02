#Contador de pessoas maiores e menores de 21 anos
print('{:=^50}'.format('MAIOR OU MENOR DE IDADE? '))
from datetime import date
atual = date.today().year
totalmaior = 0
totalmenor = 0
for c in range(1, 8):
    ano = int(input(('Em que ano a {}ª pessoa naseceu? '.format(c))))
    idade = atual - ano
    if idade >= 21:
        totalmaior += 1
    else:
        totalmenor += 1
print('=' * 50)
print('A quantidade de pessoas de maior idade é de {}.'.format(totalmaior))
print('A quantidade de pessoas de menor idade é de {}.'.format(totalmenor))
