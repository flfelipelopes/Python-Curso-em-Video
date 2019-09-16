#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.

nome = str(input('Digite o seu nome completo: ')).strip()
split_name = nome.split()
#print(split_name)
print('O seu primeiro nome é {}.'.format(split_name[0]))
print('O seu último nome é {}.'.format(split_name[-1]))

