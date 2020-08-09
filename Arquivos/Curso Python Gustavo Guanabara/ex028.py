from random import choice

n1 = int(input('digite um numero de 1 a 5 : '))

n2 = choice([1, 2, 3, 4, 5])

if n2 == n1:
    print('Parabens Você acertou o numero')
else:
    print('Você errou o numero. ele era {}'.format(n2))
