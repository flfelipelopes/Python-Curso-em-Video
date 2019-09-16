#Conversor de moedas
#USD 1.00 = BRL $ 3.27

real = float(input("Quantos reais você deseja converter? R$ "))
dolar = (real / 4.1575)

print('Com R$ {}, você pode compar U$D {:.2f}.'.format(real, dolar))