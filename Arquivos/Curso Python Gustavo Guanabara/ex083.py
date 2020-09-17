exp = input('Digite a expresão').strip().replace('', ' ').split()
i = 0
for c in range(len(exp)):
    if exp[c] in '()':
        i = i + 1
if i % 2 == 0:
    print('Expresão Valida')
else:
    print('Expresão Invalida')

