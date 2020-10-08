from random import randint
from time import sleep

dado = []

quantjogos = numero = 0
quantjogos = int(input('Quantidade de jogos:'))
numero = randint(1, 60)

for c in range(0, quantjogos):
    jogos = []
    for n in range(0, 6):
        numero = randint(1, 60)
        while True:
            if numero not in jogos:
                jogos.append(numero)
                break
            numero = randint(1, 60)
    dado.append(jogos[:])
print('*-' * 15)
print(f'{"GERANDO NUMEROS":^30}')
for c in range(0, quantjogos):
    sleep(1)
    print(f'Jogo {c+1}: {sorted(dado[c])}')





