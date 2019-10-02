#Leia uma frase e diga se ela é uma palíndromo ou não.
print('{:=^70}'.format('VOCÊ SABE ESCREVER UM PALÍNDROMO ?'))
print('')
frase = str(input('DIGITE UMA FRASE: ')).strip().upper()
print('')

palavras = frase.split()
junto = ''.join(palavras)
inverso = ''
for letra in range(len(junto) -1, -1, -1):
    inverso += junto[letra] #versão com estrutura de repetição

print('O inverso de {} é {}'.format(frase, inverso))

if inverso == junto:
    print('Essa frase é um PALÍNDROMO!')
else:
    print('Essa frase não é um PALÍNDROMO!')