#Crie um programa que leia três números e mostre qual é o maior e o menor.

print('Escolha três números aleatórios.')
n1 = int(input('1º Número: '))
n2 = int(input('2º Número: '))
n3 = int(input('3º Número: '))

print('Dentre os números {}, {} e {}.'.format(n1, n2, n3))

#Achando o maior número
maior = n1
if n2>n1 and n2>n3:
    maior = n2
if n3>n1 and n3>n2:
    maior = n3

print('O Maior número é {}'.format(maior))

#Achando o menor número
menor = n1
if n2<n1 and n2<n3:
    menor = n2
if n3<n1 and n3<n2:
    menor = n3

print('O Menor número é {}.'.format(menor))