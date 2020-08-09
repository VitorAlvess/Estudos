from time import sleep
opc = 0
n1 = int(input('Digite o valor 1: '))
n2 = int(input('Digite o valor 2: '))

while opc != 5:

    print('-===== OPÇÔES =====-')
    print('[1] SOMAR')
    print('[2] MULTIPLICAR')
    print('[3] MAIOR')
    print('[4] NOVOS NÚMEROS')
    print('[5] SAIR DO PROGRAMA')
    opc = int(input('Digite a Opção: '))
    print('-=' * 20)
    if opc == 1:
        print('A Soma de {} + {} é {}'.format(n1, n2, n1 + n2))
        sleep(2)
    if opc == 2:
        print('A multiplicação de {} X {} é {}'.format(n1, n2, n1 * n2))
        sleep(2)
    if opc == 3:
        if n1 > n2:
            print('O maior numero é {}'.format(n1))
            sleep(2)
        elif n1 == n2:
            print('Os numeros são iguais')
            sleep(2)
        else:
            print('O maior numero é {}'.format(n2))
            sleep(2)
    if opc == 4:
        n1 = int(input('Digite o valor 1: '))
        n2 = int(input('Digite o valor 2: '))
        sleep(2)
    if opc > 5 or opc == 0:
        print('Opção invalida. Tente Novamente')
        sleep(2)
print('Finalizando....')
sleep(3)
print('FIM DO PROGRAMA')
print('-=' * 20)








