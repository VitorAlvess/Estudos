i = 1
soma = 0
for c in range(1, 7):
    n1 = int(input('Digite o numero {}: '.format(i)))
    i = i + 1
    if n1 % 2 == 0:
        soma = soma + n1
print('A soma de todos os numeros pares é {}'.format(soma))
