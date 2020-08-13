from random import randint

numeros = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))
menor = maior = 0
print(f'Os numeros sorteados foram {numeros}')
for c in range(0, 5):
    if c == 0:
        maior = numeros[0]
        menor = numeros[0]
    else:
        if numeros[c] < menor:
            menor = numeros[c]
        if numeros[c] > maior:
            maior = numeros[c]
print(f'O maior numero é {maior} e o menor numero é {menor}')
