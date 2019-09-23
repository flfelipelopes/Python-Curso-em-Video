#Um programa que leia se uma pessoa está na idade de alistamento militar ou não,
#se já está em tempo de se alistar ou se já passou da época de alistamento.
from datetime import date
atual = date.today().year

print('X'*10, '{}ANALISADOR DE ALISTAMENTO MILITAR{}'
      .format('\033[1m', '\033[m'), 'X'*10)
print('')

print('Para fazer a análise do candidato, insira o ano de nascimento abaixo.')
nascimento = int(input('Ano de nascimento: '))
idade = (atual - nascimento)
print('')
print('Quem nasceu em {} tem {} anos em {}'.format(nascimento, idade, atual))
print('')
print('Considerando a informação acima: ')

if idade == 18:
    print('Você já está na idade de se alistar! Procure a junta mauis próxima de sua residência.')

elif idade < 18:
    print('Não se preocupe, você ainda não está na idade de se alistar.\n'
          'Mas, deverá fazê-lo daqui a {} anos'.format(18 - idade))

elif idade > 18:
    verificacao = input('Você já se apresentou em uma junta militar? (S/N)').lower()
    print('')
    if verificacao == 's' or 'sim':
        print('Então não se preocupe. Você está em dia com a sua obrigação militar.')
    elif verificacao != 's' or 'sim':
        print('Você já passou da idade de se alistar e deverá fazê-lo imediatamente.\n'
              'Procure a junta militar mais próximo de sua residência.')

else:
    print('Dados incorretos. Tente novamente.')

print('')
print('Obrigado por colaborar com o Exército Brasileiro. Tenha um ótimo dia!')




