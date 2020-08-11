from random import randint
c = 0
print('=- '* 20)
print('VAMOS JOGAR PAR OU IMPAR')
print('=- '* 20)
while True:

    jogador = int(input('Digite um valor: '))
    computador = randint(1,10)
    n1 = jogador + computador
    escolha = str(input('Par ou Impar [P/I]: '))
    print(f'Vocé Jogou {jogador} e o computador {computador} , O total deu {n1} ', end='')
    if escolha == 'P':
        if n1 % 2 == 0:
            print('Você ganhou')
            c += 1

            print('=- ' * 20)
            print('Vamos jogar novamente')
            print('=-' *20)
        else:
            print('Você perdeu')
            break

    else:
        if n1 % 2 == 1:
            print('Você ganhou')
            c += 1
            print('Vamos jogar novamente')
            print('=-' * 20)
        else:
            print('Você perdeu')
            break

print('=- '* 20)
print(f'GAME OVER, Você ganhou {c} Vezes.')
