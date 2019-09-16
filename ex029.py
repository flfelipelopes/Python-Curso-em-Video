#Um programa que leia a velocidade de um carro. Se > 80km mensagem de multa. Multa = R$ 7,00/km acima do limite
import fsc.formatting
print('===========PROGRAMA PARA CONTROLE DE MULTA===========')
print('')
placa = str(input('Digite a placa do véiculo (7 digítos): ')).strip()
km = float(input('Qual foi a velocidade registrada para o veículo de placa {} ? '.format(placa)))
print('')
#Considerando o limite abaixo de velocidade e o seguinte valor de multa por km ultrapassado.
limite = 80
multa_km = 7.00

print('')
if km >= (limite + 1):
    print('O veículo de placa {} estava acima do limite de velocidade de {}km'.format(placa, limite))
    print('O valor total de multa será de R$ {:.2f}.'.format((km - limite) * multa_km))
else:
    print('Veículo de placa {}, encontra-se dentro do limite estabelecido em lei.'.format(placa))

