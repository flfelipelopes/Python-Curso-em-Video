#Leia um número inteiro e diga se ele é primo ou não.
total = 0
n = int(input('Digite um número: '))
for c in range(1, n + 1):
    if n % c == 0:
        print('\033[33m', end='')
        total += 1
    else:
        print('\033[31m', end='')
    print('{} '.format(c), end='')
print('\n\033[mO número {} foi divisível {} vezes'.format(n, total))
if total == 2:
    print('O número {} é um número PRIMO.'.format(n))
else:
    print('O número {} não é um número PRIMO.'.format(n))
