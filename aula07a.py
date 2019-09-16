nome = input('Qual é o seu nome? ')
print('Prazer em te conhecer {:+^20}!'.format(nome))

print('==== Limitação de floating ====')

x = int(input('x: '))
y = int(input('y: '))
t = (x / y)
print(t)
print('{:.3f}'.format(t))
print('{:.2f}'.format(t))

print('===== Quebra e Junção de Linhas =====')

print('Quero que apareça')
print('tudo junto')

print('Quero que apareça', end=' ')
print('tudo junto')

print('Quero que apareça\n')
print('tudo separado')
