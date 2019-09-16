#Conversor de metros em centimetros e milimetros
m = float(input('Quantos metros deseja converter? '))

cm = round(m*100)
mm = round(m*1000)

print('{0} metros, equivalem a {1} centimetros e {2} milimetros.'.format(m, cm, mm))
