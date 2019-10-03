#Comparação de pesos mostrando o maior e o menor peso.
maior = 0
menor = 0
for c in range(1, 6):
    peso = float(input('Peso da {}ª pessoa: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso lido foi de {:.2f}Kg.'.format(maior))
print('O menor peso lido foi de {:.2f}Kg.'.format(menor))
