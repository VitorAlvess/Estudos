from random import randint
n1 = 0
n2 = 1
i = 0
while n1 != n2:
    n1 = int(input('digite um numero de 1 a 10 : '))

    n2 = randint(1, 10)
    print('Você escolheu {} e o computador {}'.format(n1, n2))
    i += 1
print('Foram necessarias {} tentativas'.format(i))


