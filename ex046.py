#Contagem regressiva
from time import sleep
print('{:=^30}'.format('CONTAGEM REGRESSIVA'))
for c in range(10, -1, -1):
    print(c)
    sleep(1)
print('FELIZ ANO NOVO!')
