#JoKenPo
from time import sleep
from random import randrange

print('\033[1m{:=^70}\033[m'.format(' JOKENPO '))
print('')
print('Sou profissional em JOKENPO. Será que você consegue me vencer?')
print('')
print('Desafio aceito. Escolha a sua opção:')
usuario = int(input('{}[ 1 ]{} PEDRA'
                  '\n{}[ 2 ]{} PAPEL'
                  '\n{}[ 3 ]{} TESOURA'
                  '\nQual é a sua jogada? '
                  .format('\033[1;36m', '\033[m', '\033[1;35m', '\033[m', '\033[1;33m', '\033[m')))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')

#Jogada Computador
computador = randrange(1,3)
if computador == 1:
    computador = 'PEDRA'
elif computador == 2:
    computador = 'PAPEL'
elif computador == 3:
    computador = 'TESOURA'

#Jogada Usuário
if usuario == 1:
    usuario = 'PEDRA'
elif usuario == 2:
    usuario = 'PAPEL'
elif usuario == 3:
    usuario = 'TESOURA'

#Resultado
if computador == 1 and usuario == 3:
    resultado = 'JOGADOR PERDE'
elif computador == 2 and usuario == 1:
     resultado = 'JOGADOR PERDE'
elif computador == 3 and usuario == 2:
     resultado = 'JOGADOR PERDE'
elif computador == usuario:
    resultado = 'EMPATE'
else:
    resultado = 'JOGADOR VENCEU'

#Interface de Jogo
print('')
print('=' * 70)
print('Computador jogou {}{}{}'.format('\033[1m', computador, '\033[m'))
print('Jogador jogou {}{}{}'.format('\033[1m', usuario, '\033[m'))
print('=' * 70)
print('\033[1m', resultado, '\033[m')





