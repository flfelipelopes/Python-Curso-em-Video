#classificação de atletas por idade.
#sendo até 9 anos = mirim; até 14 = infantil; até 19 = junior; até = 25 = sênior; acima = master.
from datetime import date
import emoji
atual = date.today().year

print('='*10, 'CLASSIFICAÇÃO DE ATLETAS', '='*10)
print('')
print('Para ajudarmos com a classificação dos atletas, insira abaixo o ano de nascimento: ')
nascimento = int(input('Ano de nascimento do atleta: '))
idade = (atual - nascimento)

print('')
print('O atleta nascido em {} e atualmente com {} anos. '
      'A categoria de competição é:'.format(nascimento, idade))

if idade <= 9:
    print('Esse atleta se enquadra na categoria MIRIM.')
elif idade <= 14:
    print('Esse atleta se enquadra na categiria INFANTIL.')
elif idade <= 19:
    print('Esse atleta se enquadra na categoria JUNIOR.')
elif idade <= 25:
    print('Esse atleta se enquadra na categoria SÊNIOR.')
else:
    print('Esse atleta se enquadra na categoria MASTER.')

print('')
print(emoji.emojize(('Tenha sempre uma competição saudável. Bom treino e boa sorte! :smile:'), use_aliases=True))