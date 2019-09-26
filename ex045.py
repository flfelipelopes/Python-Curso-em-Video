#JoKenPo
from time import sleep
from random import randint
items = ('PEDRA', 'PAPEL', 'TESOURA')
print('\033[1m{:=^70}\033[m'.format(' JOKENPO '))
print('')
print('Sou profissional em JOKENPO. Será que você consegue me vencer?')
print('')
print('Desafio aceito. Escolha a sua opção:')
usuario = int(input('{}[ 0 ]{} PEDRA'
                  '\n{}[ 1 ]{} PAPEL'
                  '\n{}[ 2 ]{} TESOURA'
                  '\nQual é a sua jogada? '
                  .format('\033[1;36m', '\033[m', '\033[1;35m', '\033[m', '\033[1;33m', '\033[m')))
sleep(1)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO !!!')

#Jogada Computador
computador = randint(0, 2)

#Interface de Jogo
print('')
print('=' * 70)
print('Computador jogou {}{}{}'.format('\033[1m', items[computador], '\033[m'))
print('Jogador jogou {}{}{}'.format('\033[1m', items[usuario], '\033[m'))
print('=' * 70)

#Resultado
if computador == 0: #compuatdor jogou PEDRA
    if usuario == 0:
        print('EMPATE!')
    elif usuario == 1:
        print('JOGADOR VENCEU')
    elif usuario == 2:
        print('COMPUTADOR VENCEU')
    elif usuario > 2:
        print('JOAGADA INVÁLIDA!')
elif computador == 1: #compuatdor jogou PAPEL
    if usuario == 0:
        print('COMPUTADOR VENCEU')
    elif usuario == 1:
        print('EMPATE!')
    elif usuario == 2:
        print('JOGADOR VENCEU')
    elif usuario > 2:
        print('JOAGADA INVÁLIDA!')
elif computador == 2: #compuatdor jogou TESOURA
    if usuario == 0:
        print('JOGADOR VENCEU')
    elif usuario == 1:
        print('COMPUTADOR VENCEU')
    elif usuario == 2:
        print('EMPATE!')
    elif usuario > 2:
        print('JOAGADA INVÁLIDA!')
