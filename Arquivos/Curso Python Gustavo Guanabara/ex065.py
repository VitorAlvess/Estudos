'''maior = 0
menor = 0

for c in range(1, 6):
    peso = float(input('Digite o valor {}: '.format(c)))
    if c == 1:
        maior = peso
        menor = peso
    else:
        if  peso > maior:
            maior = peso
        if peso < menor:
            menor = peso
print('O maior peso é {} e o menor é {}'.format(maior, menor))
'''
i = 0
media = maior = menor =0

n1 = int(input('Digite um valor: '))
val = n1
esc = input('Quer continuar? [S/N]').strip().upper()
maior = n1
menor = n1
while esc != 'N':
    i = i + 1





    n1 = int(input('Digite um valor: '))
    esc = input('Quer continuar? [S/N]').strip().upper()
    val = val + n1

    if n1 > maior:
        maior = n1
    if n1 < menor:
        menor = n1
media = val / (i + 1)
print(val)
print(i)
print('A media é {}'.format(media))
print('O Numero maior é {} e menor é {}'.format(maior, menor))


