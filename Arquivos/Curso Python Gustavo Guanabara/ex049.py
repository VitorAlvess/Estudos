
n1 = int(input('Digite o valor da tabuada que você deseja: '))
i = 1
for c in range(1, 11):
    print('{} X {:2} = {:2}'.format(n1, i, n1 * i))
    i = i + 1