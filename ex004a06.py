print('===== DESAFIO 004 =====')
# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possívies
# sobre ele.
a3 = input('Digite qualquer coisa:')
print('É do tipo:',(type(a3)))
print('É alfa?', a3.isalpha())
print('É capitalizado?', a3.istitle())
print('É alfanumérico?', a3.isalnum())
print('É numérico?', a3.isnumeric())
print('É decimal?', a3.isdecimal())
print('Está em minúsculo?', a3.islower())
print('Está em maiúsculo?', a3.isupper())
print('É printable?', a3.isprintable())
print('É espaço?', a3.isspace())


