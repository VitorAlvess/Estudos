n1 = int(input('Digite os KM: '))

if n1 <= 200:
    n2 = n1 * 0.50
    print('O valor da passagem é de R${}'.format(n2))
    print('Boa Viagem')
else:
    n2 = n1 * 0.45
    print('O valor da passagem é de R${}'.format(n2))
    print('Boa Viagem')
