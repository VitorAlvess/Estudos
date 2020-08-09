n1 = float(input('Digite o numero 1'))
n2 = float(input('Digite o numero 2'))
n3 = float(input('Digite o numero 3'))

if n1 > n2 and n1 > n3:
    maior = n1

if n2 > n1 and n2 > n3:
    maior = n2
if n3 > n1 and n3 > n2:
    maior = n3

# Menor agr

if n1 < n2 and n1 < n3:
    menor = n1
if n2 < n1 and n2 < n3:
    menor = n2
if n3 < n1 and n3 < n2:
    menor = n3

print('O valor Maior é {} e o valor menor é {}'.format(maior, menor))

