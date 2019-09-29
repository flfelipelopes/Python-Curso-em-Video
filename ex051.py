#Leia o 1º termo e a razão de uma PA. Mostre os 10 primeiros termos dessa progressão.
print('=' * 40)
print('{:^}'.format('10 TERMOS DE UMA P.A.'))
print('=' * 40)
termo = int(input('Primeiro termo: '))
razao = int(input('Razão: '))
decimo = termo + (10 - 1) * razao
for c in range(termo, decimo + razao, razao):
    print('{} '.format(c), end=' → ')
print('FIM')
