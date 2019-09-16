#Conversor de Temperaturas
temp = float(input('Qual a temperatura em °C a ser convertida? '))

fahrenheit = (temp * 9/5) + 32
kelvin = (temp + 273.15)

print('A conversão de {}°C em (°F) Fahrenheit é {}°F.'.format(temp, fahrenheit))
print('A mesma temperatura de {}°C para (K) Kelvin é de {}K.'.format(temp, kelvin))

