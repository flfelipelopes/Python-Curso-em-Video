#Leia o comprimento de 3 retas e diga se elas podem formar um triângulo ou não.
print('Vamos descobir se é possível formar um triângulo com os lados abaixo:')
l1 = float(input('Lado 1: '))
l2 = float(input('Lado 2: '))
l3 = float(input('Lado 3: '))

if l1 < l2 + l3 and l2 < l1 + l3 and l3 < l1 + l2:
    print('É possível construir um triângulo.')
else:
    print('Não é possível ober um triângulo.')
