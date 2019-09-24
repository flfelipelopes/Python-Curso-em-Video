#Cálcule a média de duas notas mostrando uma mensagem de acordo com a média atingida.
# if média < 5 == reprovado; elif média > 5 and < 6.9 == recuperação, elif média => 7 == aprovado.

print('='*10, 'CÁLCULO DE MÉDIAS', '='*10)
print('')
nota1 = float(input('Nota 1ª Avaliação: '))
nota2 = float(input('Nota 2ª Avaliação: '))

media = (nota1 + nota2) / 2

print('Tirando {:.1f} e {:.1f}, a média do aluno é {:.1f}.'.format(nota1, nota2, media))

if media < 5:
    print('O aluno está REPROVADO.')
elif media > 5 and media < 6.9:
    print('O aluno está EM RECUPERAÇÃO.')
else:
    print('O aluno está APROVADO!')
