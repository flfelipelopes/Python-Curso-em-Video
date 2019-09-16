#Crie um programa que sorteie um número de 1 a 5 e faça o usuário descobrir esse número
import random
print('Você consegue adivinhar o número que eu vou escolher? Essa eu quero ver.')
n1 = int(input('Digite um número de 0 a 5: '))
n2 = random.randrange(0, 5)

if n1 == n2:
    print('PARABÉNS, você acertou!!!!')
else:
    print('Eu sabia que você não iria me vencer HAHAHA!')
    print('O número que eu escolhi foi {}'.format(n2))