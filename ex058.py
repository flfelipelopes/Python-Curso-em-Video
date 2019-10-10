#Jogo de adivinhação (usuário x computador)
import random
print('\033[1m{:=^70}\033[m'.format('JOGO DE ADIVINHAÇÃO'))
tentativas = 1
print('E aí...Afim de brincar?'
      '\nPensei em um número de 0 a 10.'
      '\nVocê consegue advinhar o número que eu estou pensando?')
print('=' * 70)
desafio = str(input('Você vai encarar esse desafio? [S/N]: ')).strip().upper()
print('=' * 70)
if desafio == 'S':
    print('Não esperava menos de você! Então vamos começar!!!')
    n_jogador = int(input('Digite um número de 0 a 10: '))
    n_computador = random.randint(0, 10)

    while n_jogador != n_computador:
        tentativas += 1
        if n_jogador > n_computador:
            n_jogador = int(input('Menos... Tente um novo número: '))
        if n_jogador < n_computador:
            n_jogador = int(input('Mais...Tente um novo número: '))
    print('Parabéns! Você acertou!'
          '\nE foram necessárias {} tentivas.'.format(tentativas))
else:
    print('Que pena! Quem sabe na próxima você não aceite.')