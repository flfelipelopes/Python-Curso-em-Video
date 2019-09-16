import math
#Hipotenusa == a² + b² = ²√c
a = float(input('Qual o comprimento do cateto oposto? '))
b = float(input('Qual o comprimento do cateto adjacente? '))
c = math.hypot(a, b)
print("A hipotenusa de {} e {} é {:.2f}".format(a, b, c))

