from random import randint
from time import sleep
itens = ('Pedra', 'papel', 'Tesoura')
print('Escolha:')
print('[ 0 ] Pedra')
print('[ 1 ] Papel')
print('[ 2 ] Tesoura')
n1 = int(input('Digite aqui :'))
n2 = randint(0, 2)
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
sleep(1)
print('-_-' * 11)
print('Você escolheu {}'.format(itens[n1]))
print('O computador escolheu {}'.format(itens[n2]))
print('-_-' * 11)

if n1 == n2:
    print('EMPATE')
elif n1 == 0 and n2 == 1:
    print('Computador venceu')
elif n1 == 0 and n2 == 2:
    print('Você venceu')
elif n1 == 1 and n2 == 2:
    print('Computador venceu')
elif n1 == 1 and n2 == 0:
    print('Você Venceu')
elif n1 == 2 and n2 == 0:
    print('Computador venceu')
elif n1 == 2 and n2 == 1:
    print('Você Venceu')

print('-_-' * 11)



