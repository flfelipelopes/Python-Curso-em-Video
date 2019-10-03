soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_mais_velho = ''
mulheres_menos_vinte = 0
for c in range(1, 5):
    print('----- {} ª PESSOA ------'.format(c))
    nome = str(input('Nome: ')).strip().capitalize()
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    print('')
    soma_idade += idade
    if c == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_mais_velho = nome
    if sexo in 'Ff' and idade < 20:
        mulheres_menos_vinte += 1
media_idade = soma_idade / 4
print('A média de idade do grupo é de {} anos.'.format(media_idade))

if maior_idade_homem > 0:
    print('O homem mais velho tem {} anos e se chama {}'.format(maior_idade_homem, nome_mais_velho))
else:
    print('Não temos nenhum homem nessa relação.')

if mulheres_menos_vinte == 1:
    print('Neste caso temos apenas {} mulher com menos de 20 anos.'.format(mulheres_menos_vinte))
else:
    print('A quantidade de mulheres com menos de 20 anos é de {} mulheres.'.format(mulheres_menos_vinte))
