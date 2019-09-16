#Faça um programa que leia um número de 0 a 9999 e mostre na tela cada um dos dígitos separados.

n1 = int(input('Insira um número: '))
print('A composição do número {} é: '.format(n1))
n2 = n1 // 1 % 10
n3 = n1 // 10 % 10
n4 = n1 // 100 % 10
n5 = n1 // 1000 % 10
print('Sendo:')
print('Unidade: {}'.format(n2))
print('Dezena: {}'.format(n3))
print('Centena: {}'.format(n4))
print('Milhar: {}'.format(n5))


