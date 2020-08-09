n1 = input('Digite Algo')

print('A frase em maisculo {} '.format(n1.upper()))

print('A frase em minusculo {}'.format((n1.lower())))

n2 = n1.replace(" ", "")
n3 = n1.split()



print('A frase sem espaços tem o tamanho de {} '.format(len(n2)))
print('a primeira palavra da frase é {}'.format(n3[0]))