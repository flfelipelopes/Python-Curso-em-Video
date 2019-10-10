#validação de dados simples
sexo = str(input('Informe o seu sexo [M/F]: ').strip().upper())
while sexo not in 'MmFf':
    sexo = str(input('Dados inválidos. Por favor, informe seu sexo [M/F]: ')).strip().upper()
print('Sexo {} registrado com sucesso'.format(sexo))
