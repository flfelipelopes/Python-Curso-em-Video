#Tabuada com estrutura de repetição
from time import sleep
print('\033[1m{:=^40}\033[m'
      .format('TABUADA'))
n = int(input('{}Você deseja a tabuada de qual número?{} '
              .format('\033[1m', '\033[m')))
print('{}={}'.format('\033[1m', '\033[m') * 40)
for c in range(0, 11):
    print('{:2} x {:2} = {:2}'.format(n, c, (n * c)))
    sleep(0.7)
print('{}={}'.format('\033[1m', '\033[m') * 40)