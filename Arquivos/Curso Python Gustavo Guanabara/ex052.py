i = 0
n1 = int(input('Digite o numero'))
for c in range(1, n1+1):
    if n1 % c == 0:

        i = i + 1

if i == 2:
    print('O numero é primo')
else:
    print('O numero não é primo')