#Faça um programa que leia a LARGURA e a ALTURA de uma parede em metros, calcule a sua ÁREA e a quantidade de tinta
#necessária para pintá-la. Sendo 1 LITRO de tinta pinta uma área de 2m².

largura = float(input('Qual a largura da parede? '))
altura = float(input('Qual a altura da parede? '))
area = (largura * altura)

print('Se você tem uma parede de dimensão {} x {}.'
      'A sua área total é igual a {} m²'.format(largura, altura, area))

tinta = (area / 2.00)

print('A quantidade de tinta necessária para pintar esse parede é de {:.2f} litros.'.format(tinta))

