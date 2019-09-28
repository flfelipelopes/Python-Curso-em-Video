#Soma entre números impares multiplos de três entre 1 e 500
soma = 0
print('{:=^40}'.format('Números Ímpares Multíplos de 3'))
for c in range(0, 500, 3):
    if (c / 2) % 1:
        soma += c
print('A soma total de números ímpares múltiplos'
      ' de 3 entre 1 e 500 é de {}.'.format(soma))
    