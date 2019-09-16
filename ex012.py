#Crie um algoritmo que leia o preço de um produto e mostre seu novo preço, como 5% de desconto

p1 = float(input('Digite o preço da mercadoria desejada: R$ '))
desc = 0.05

p2 = abs((desc * p1)-p1)

print('O novo preço a ser marcado, já incluso o desconto de 5% é de R$ {:.2f}.'.format(p2))

