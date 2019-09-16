#Descubra se o ano informado é bissexto ou não
import datetime
print('=====ESSE É UM ANO BISSEXTO?=====')
print('')
print('Vamos descobrir se um determinado ano é bissexto ou não?')
ano = int(input('Para isso, digite um ano aleatório ou 0 para utilizar o ano atual: '))


print('')
if ano == 0:
    ano = datetime.date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print('O ano de {} é um ano bissexto.'.format(ano))
else:
    print('O ano de {} não é um ano bissexto.'.format(ano))

