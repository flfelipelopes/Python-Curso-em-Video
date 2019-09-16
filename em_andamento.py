print('==Essa é a nossa calculadora de IMC (Índice de Massa Corporal)==\n''')
print('Vamos cuidar da sua saúde? Preencha abaixo para obter o seu IMC*.')
print('='*65)
altura = float(input('Para começar digite a sua altura: '))
peso = float(input('Agora digite o seu peso: '))
imc = peso / (altura * altura)
print('O seu IMC* é igual a {:.2f}.'.format(imc))

if imc <= 18.50:
    print('Você está abaixo do peso!')
if imc > 18.51 <= 24.99:
    print('Parabéns! Continue assim!')
if imc > 25.00 <= 29.99:
    print('Atenção! Vamos controlar esse peso?')
if imc > 30.00 <= 34.99:
    print('Atenção! Você está no nível de Obesidade 1!')
if imc > 35.00 <= 39.99:
    print('Cuidado redobrado! Você está no nível de Obesidade 2!')
if imc > 40.00 <= 99.99:
    print('Atenção! Você está no nível de Obesidade 3!'
          ' Um acompanhamento médico é recomendado!')

