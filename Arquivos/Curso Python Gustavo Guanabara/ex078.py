numeros = []
maior = 0
menor = 0
for c in range(0, 5):
    numeros.append(int(input(f'Digite o valor para a posição {c}: ')))
    if c == 0:
        maior = numeros[c]
        menor = numeros[c]
    else:
        if numeros[c] > maior:
            maior = numeros[c]
        if numeros[c] < menor:
            menor = numeros[c]


print('=-'* 20)
print(numeros)
print(f'O maior valor é {maior} nas posiçoes', end='')
for v, c in enumerate(numeros):
    if c == maior:
        print(f' {v}', end=' ')

print()
print(f'O menor valor é {menor} nas posiçoes ', end='')
for v, c in enumerate(numeros):
    if c == menor:
        print(f'{v} ', end=' ')

