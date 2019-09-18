#Leia um número inteiro e peça ao usuário que escolha qual será a base de conversão. Sendo:
# 1 - binário; 2 - octal; 3 - hexadecimal

print('='*10, '{}CONVERSOR DE BASES CIENTÍFICAS{}'
      .format('\033[36;1m', '\033[m'), '='*10)
n1 = int(input('Digite um número qualquer: '))
print('')
print('Agora escolha para qual base deseja converter. Sendo:\n'
      '[{}1{}] para sistema {}BINÁRIO{}.\n'
      '[{}2{}] para sistema {}OCTAL{}.\n'
      '[{}3{}] para sistema {}HEXADECIMAL{}.\n'
      .format('\033[1;31m', '\033[m', '\033[1;31m', '\033[m',
              '\033[1;37m', '\033[m', '\033[1;37m', '\033[m',
              '\033[1;34m', '\033[m', '\033[1;34m', '\033[m'))

base = int(input('\033[1m' 'Insira a opção desejada: ' '\033[m'))
print('')

if base == 1:
    print('O número {}{}{} convertido para sistema BINÁRIO é igual a {}{}{}.'
          .format('\033[1m', n1, '\033[m', '\033[1m', bin(n1), '\033[m'))
elif base == 2:
    print('O número {}{}{} convertido para sistema OCTAL é igual a {}{}{}.'
          .format('\033[1m', n1, '\033[m', '\033[1m', oct(n1), '\033[m'))
elif base == 3:
    print('O número {}{}{} convertido para o sistema HEXADECIMAL é igual a {}{}{}.'
          .format('\033[1m', n1, '\033[m', '\033[1m', hex(n1), '\033[m'))
else:
    print('{}Opção inválida. Digite uma das opções acima.{}'.format('\033[1;31m', '\033[m'))
