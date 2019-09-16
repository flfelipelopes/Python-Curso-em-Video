#Crie um programa que defina a ordem de apresentação do curso
import random
n1 = str(input('1º Nome: '))
n2 = str(input('2º Nome: '))
n3 = str(input('3º Nome: '))
n4 = str(input('4º Nome: '))
lista = [n1, n2, n3, n4]
random.shuffle(lista)
print('A ordem de apresentação será: ')
print(lista)