#Leia dois números inteiros e descubra qual o maior ou se os dois são iguais.
print('='*10, '{}QUAL É O MAIOR VALOR?{}'.format('\033[1;32m', '\033[m'), '='*10)
print('')
print('Digite dois números e descubra qual é o maior:')
n1 = int(input('1º Número: '))
n2 = int(input('2º Número: '))
print('')

maior = n1

if n2 > n1:
    maior = n2
    print('O maior valor é {}'.format(maior))
elif n2 < n1:
    maior = n1
    print('O maior valor é {}'.format(maior))
else:
    print('Não há maior. Os ambos os números são iguais!')
