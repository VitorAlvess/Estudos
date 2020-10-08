
numeros = [[], []]
valor = 0


for c in range(0, 7):
    valor = int(input(f'Digite o valor {c + 1} '))
    if valor % 2 == 0:
        numeros[0].append(valor)
    else:
        numeros[1].append(valor)


print(f'Os valores pares digitados foram {sorted(numeros[0], key=int)}')
print(f'os valores imapres digitados foram {sorted(numeros[1],key=int)}')


