#Escreva um programa que pergunte a quantidade de KM percorridos por um carro alugado e a quantidade de dias
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00/dia e R$ 0,15/KM rodado.

km = float(input('Qual a quantidade de KM rodados? '))
dias = int(input('E por quantos dias que o veículo foi alugado? '))

print('Considerando que o veículo foi alugado por {} dias'
      ' e andou {}KM. '
      'O total da fatura será de R${:.2f}'.format(dias, km, (dias * 60) + (km * 0.15 )))
