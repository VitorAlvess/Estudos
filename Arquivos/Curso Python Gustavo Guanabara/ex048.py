soma = 0
i = 0
for c in range(1, 500, 1):
    if c % 2 != 0:
        if c % 3 == 0:
            i = i + 1
            soma = soma + c
print('A soma de todos os {} valores de 0 a 500 que são multiplos de 3 é {}'.format(i, soma))
