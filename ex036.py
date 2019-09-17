#Aprovador de Empréstimo.
#Perguntar: valor da casa, salário, quantos anos para pagar.
#Calcule: valor da prestação
#Mostre: negado ou aprovado. Será negado, se prestação for maior que 30% do salário.
from math import ceil

print('=' * 10, 'CREDIFACIL: SISTEMA DE EMPRÉSTIMOS', '=' * 10)
print('')
print('Seja bem-vindo ao simulador de empréstimos {}CREDIFACIL{}.\n'
      'Você escolheu a opção de crédito {}RESIDENCIAL{}.\n'
      'Para prosseguir insira os dados abaixo:'.format('\033[1;32m', '\033[m', '\033[1m', '\033[m'))
print('')
casa = float(input('Qual o valor da casa que deseja comprar? R$ '))
salario = float(input('Qual o valor da sua renda mensal? R$ '))
anos = int(input('Em quantos anos você deseja quitar o seu financiamento? '))

parcela = int(anos * 12)
prestacao = (casa / parcela)

print('O valor da prestação em {} {} {} parcelas será de '
      'R$ {} {:.2f} {}.'.format('\033[1m', parcela, '\033[m', '\033[1m', prestacao, '\033[m'))

print('')

if parcela <= (salario * 0.30):
    print('Parabéns! O seu empréstimo já está {}PRÉ-APROVADO{}.'
          'Clique em CONTINUAR para os próximos passos.'.format('\033[1;32m', '\033[m'))
elif parcela >= (salario * 0.30):
    print('Infelizmente, a margem de empréstimo solicitado\n'
          'não é compatível com a sua renda atual.\n'
          '{}Que tal fazermos uma solicitação menor? {}'.format('\033[1;31m', '\033[m'))
else:
    print('Recebemos a sua solicitação e ela será analisada em até 48h úteis.\n'
          'Para maiores informações, entre em contato com a nossa central de atendimento\n'
          'através do número 0800-777-9999.')
print('')
print('Obrigado por contar com a {}CREDIFACIL{}'.format('\033[1;32m', '\033[m'))
#end