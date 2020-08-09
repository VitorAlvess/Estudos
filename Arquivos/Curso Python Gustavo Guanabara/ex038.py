n1 = int(input('Digite o numero 1'))
n2 = int(input('Digite o numero 2'))

if n1 > n2:
    print('O numero {} é maior que o numero {}'.format(n1, n2))
elif n2 > n1:
    print('O numero {} é maior que o numero {}'.format(n2, n1))
else:
    print('os numeros são iguais')