p1 = int(input('Digite o primeiro termo'))
r = int(input('Digite a razão'))
i = 0
print(p1, end=' -> ')
while i < 9:
    i = i + 1
    p1 = p1 + r
    print('{} '.format(p1), end='-> ')
print('PAUSA')


mostrar = 1
print('Se não digite [0]')
while mostrar != 0:

    mostrar = int(input('Quer mostrar mais algum termo?'))
    c = 0
    while c < mostrar:
        i = i + 1
        p1 = p1 + r
        c = c + 1
        print('{} '.format(p1), end='-> ')
print('=-' * 25)
print('O programa foi finalizado com {} termos mostrados '.format(i+1))
print('=-' * 16)
print('OBRIGADO POR USAR O PROGRAMA')
print('=-' * 16)


