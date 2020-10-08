matris = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
pares = soma = maior = 0
for l in range(0,3):
    for c in range(0,3):
        matris[l][c] = int(input(f'Digite um valor: [{l}, {c}]'))
for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matris[l][c]:^5}]', end='')
    print()
for l in range(0,3):
    for c in range(0, 3):
        if matris[l][c] % 2 == 0:
            pares = pares + matris[l][c]
print(f'A soma de todos os valores pares são: {pares}')
for c in range(0, 3):
    soma = soma + matris[c][2]
print(f'A soma dos valores da terceira coluna é {soma}')

for c in range(0, 3):
    if c == 0:
        maior = matris[1][c]
    else:
        if matris[1][c] > maior:
            maior = matris[1][c]
print(f'O maior valor da segunda coluna é {maior}')



