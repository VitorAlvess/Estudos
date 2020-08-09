p1 = int(input('Digite o primeiro termo'))
r = int(input('Digite a razão'))

for c in range(p1, p1 + (10* r), r):
    print('{} '.format(c), end='-> ')
print('ACABOU')