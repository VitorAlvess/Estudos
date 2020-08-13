numeros = (int(input('Digite um valor: ')), int(input('Digite um valor: ')),
           int(input('Digite um valor: ')), int(input('Digite um valor: ')))
print(f'Você digitou os valores {numeros}')

print(f'O valor 9 apareceu {numeros.count(9)} Vezes')
if 3 in numeros:
    print(f'O valor 3 foi digitado na primeira vez na posição {numeros.index(3) + 1}')
else:
    print('O valor 3 não foi encontrado')
print('Os valores pares são: ', end='')
for c in range (0,4):
    if numeros[c] % 2 == 0:
        print(numeros[c], end=' ')




