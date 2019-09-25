#Sistema de Pagamento
#Considere seu preço normal e a condição de pagamento
#A vista: 10% desconto; A vista cartão: 5% desconto; 2x: preço normal; 3x ou +: 20% juros

print('\033[1m{:=^67}\033[m'.format(' SISTEMA DE REGISTRADORA '))

print('')
print('Insira o valor do produto e escolha qual será a forma de pagamento.')

print('')
produto = float(input('Valor do produto: R$ '))

print('')
pagamento = int(input('Qual será a forma de pagamento:'
      '\n[1] À vista em dinheiro'
      '\n[2] À vista no cartão de crédito\débito'
      '\n[3] 2x no cartão de crédito'
      '\n[4] 3x ou mais no cartão de crédito'
      '\n{}Opção escolhida: {}'.format('\033[1m', '\033[m')))
if pagamento == 4:
    parcela = int(input('Qual o número em parcelas: '))
    if parcela <= 2:
        print('Para a quantidade de parcelas informadas, '
              'utilize a forma de pagamento {}[3]{}'.format('\033[1m', '\033[m'))
    elif parcela > 12:
        print('O máximo de parcelas permitidas é {}12{}.'.format('\033[1m', '\033[m'))
    else:
        total = (((produto * 0.20) + produto) / parcela)
        print('{}{}{} parcelas iguais de R$ {}{:.2f}{} com juros de 20%.'
               .format('\033[1m', parcela, '\033[m', '\033[1m', total, '\033[m'))
elif pagamento == 1 or 2 or 3:
    print('')
    print('A compra de R$ {}{:.2f}{} com a opção de pagamento selecionada será de: '
        .format('\033[1m', produto, '\033[m'), end='')
else:
    print('')
if pagamento == 1:
    total = (produto - (produto * 0.10))
    print('R$ {}{:.2f}{}'.format('\033[1m', total, '\033[m'))
elif pagamento == 2:
    total = (produto - (produto * 0.05))
    print('R$ {}{:.2f}{}'.format('\033[1m', total, '\033[m'))
elif pagamento == 3:
    total = (produto / 2)
    print('2 parcelas iguais de R$ {}{:.2f}{} sem juros.'.format('\033[1m', total, '\033[m'))

print('')
print('Agradecemos pela preferência e confiança em nossos produtos!')

