p1 = int(input('Digite o primeiro termo'))
r = int(input('Digite a razão'))
i = 0
while i < 11:
    i = i + 1
    p1 = p1 + r
    print('{} '.format(p1), end='-> ')


'''for c in range(p1, p1 + (10* r), r):
    print('{} '.format(c), end='-> ')
print('ACABOU')'''