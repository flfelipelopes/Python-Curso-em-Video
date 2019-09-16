#Crie um programa que leia o nome completo de uma pessoa e mostre: - O nome com todas as letras maiúsculas e minúsculas.
# - Quantas letras ao todo (sem considerar espaços). - Quantas letras tem o primeiro nome.

nome = str(input('Digite o seu nome completo: ')).strip()
print('Seu nome em maiúsculas é: {}'.format(nome.upper()))
print('Seu nome em minúsculas é: {}'.format(nome.lower()))
print('Seu nome tem ao todo {} letras.'.format(len(nome) - nome.count('e') - nome.count(' ')))

nome_divido = nome.split()
print('O seu primeiro nome é {} e possui {} letras.'.format(nome_divido[0], len(nome_divido[0])))





