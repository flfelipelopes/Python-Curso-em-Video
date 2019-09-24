#Calculadora de IMC

print('==Essa é a nossa calculadora de IMC (Índice de Massa Corporal)==\n''')
print('Vamos cuidar da sua saúde? Preencha abaixo para obter o seu IMC*.')
print('='*65)
altura = float(input('Para começar digite a sua altura: '))
peso = float(input('Agora digite o seu peso: '))
imc = peso / (altura ** 2)
print('O seu IMC* é igual a {:.2f}.'.format(imc))

if imc < 18.50:
    print('Você está abaixo do peso!')
elif 18.51 <= imc < 24.99:
    print('Parabéns! Continue assim!')
elif 25.00 <= imc < 29.99:
    print('Atenção! Vamos controlar esse peso?')
elif 30.00 <= imc < 34.99:
    print('Atenção! Você está no nível de Obesidade 1!')
elif 35.00 <= imc < 39.99:
    print('Cuidado redobrado! Você está no nível de Obesidade 2!')
elif 40.00 <= imc < 99.99:
    print('Atenção! Você está no nível de Obesidade 3!\n'
          'Um acompanhamento médico é recomendado!')

print('')
print('Lembre-se que cuidar da sáude é fundamental!')

