#Leia o salaário de um funcionário e mostre esse valor com 15% de reajuste

salario_atual = float(input('Qual o salário atual? R$ '))
salario_novo = ((salario_atual * 15 / 100) + salario_atual)

print('O salário reajustado com indice de 15% vai de $ {:.2f} para $ {:.2f}.'.format(salario_atual, salario_novo))