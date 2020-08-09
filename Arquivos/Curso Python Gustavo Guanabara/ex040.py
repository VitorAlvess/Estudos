n1 = float(input('Digite a nota 1'))
n2 = float(input('Digite a nota 2'))

media = (n2 + n1) / 2

if media < 5:
    print('Sua media foi {}. Você foi reprovado'.format(media))
elif media >= 5 and media < 7:
    print('Sua media foi {}, Você esta de recuperação'.format(media))
else:
    print('Sua media foi {}, Você esta aprovado'.format(media))