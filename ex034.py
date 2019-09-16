#Reajuste salarial condicionado. Até R$ 1.250 = 10%; se não 15%
print('\033[1m========REAJUSTE SALARIAL========\033[m')
salario_atual = float(input('Digite o salário a ser reajustado: '))

base_minima = float(1250.00)

if salario_atual <= base_minima:
    print('O salário reajustado será de R$ {:.2f}'.format((base_minima * 0.10) + salario_atual))
else:
    print('O salário reajustado será de R$ {:.2f}.'.format((salario_atual * 0.15) + salario_atual))