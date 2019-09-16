#Calculo de passagem por km. Se <= 199 km = R$ 0,50; Se >= 200 km = R$ 0,45
print('=======CÁLCULO DE PASSAGEM RODOVIÁRIA=======')
print('')
print('Bem-vindo ao nosso sistema de compras de passagem.')
km = float(input('Por gentileza, informe a distância do trecho a ser percorrido: '))
p1 = 0.50
p2 = 0.45
print('')

if km <= 200:
    print('O custo total da sua passagem será de R$ {:.2f} por pessoa.'.format(km * p1))
else:
    print('Essa passagem está com preço promocional.')
    print('E sairá por apenas R$ {:.2f} por pessoa.'.format(km * p2))
print('')
print('Tenha uma excelente viagem!')