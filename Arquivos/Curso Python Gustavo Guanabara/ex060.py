'5! = 5*4*3*2*1'
print('===== Calculador de Fatorial ======')
i = 1
n1 = int(input('Digite o Numero'))
fato = 1
c = n1
print('{}! = '.format(n1), end='')
while n1 != i:

    i = i + 1
    fato = fato * i
    print('{}'.format(c), end='')
    print(' X ' if c > 1 else ' = ', end='')

    c = c - 1




print('1 = {}'.format(fato))
