#Soma entre números inteiros pares
soma = 0
print('{}{:#^30}{}'
      .format('\033[1m','Soma entre números pares inteiros', '\033[m'))
for c in range(0, 6):
    n = int(input('Digite um número: '))
if (n % 2) == 0:
    soma += n
print('A soma total entre os números pares é de {}{}{}'
      .format('\033[1m', soma, '\033[m'))