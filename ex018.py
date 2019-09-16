#Encontro o seno, cosseno e tangente de um número
import math

n1 = float(input('Digite o ângulo a ser calculado: '))

print('O seno de {} é {:.2f}'.format(n1, math.sin(math.radians(n1))))
print('O cosseno de {} é {:.2f}'.format(n1, math.cos(math.radians(n1))))
print('A tangente de {} é {:.2f}'.format(n1, math.tan(math.radians(n1))))