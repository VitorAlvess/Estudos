a = float(input('Digite o valor da medida a'))
b = float(input('Digite o valor da medida b'))
c = float(input('Digite o valor da medida c'))

if (b - a) < a < b + c and (a - c) < b < a + c and (a- b) < c < a + b:
    print('Forma um triangulo')
else:
    print('não forma um tringulo')