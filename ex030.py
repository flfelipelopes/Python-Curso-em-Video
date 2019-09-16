#Crie um programa que leia um número e mostre se ele é par ou ímpar.

print('========JOGO DO PAR OU ÍMPAR=========')
print('')
print('Digite um número abaixo e vou te dizer se ele é par ou ímpar.')
n1 = int(input('Qual número você escolheu? '))

if (n1 % 2) == 0:
    print('{} é um número par.'.format(n1))
else:
    print('{} é um número ímpar.'.format(n1))
