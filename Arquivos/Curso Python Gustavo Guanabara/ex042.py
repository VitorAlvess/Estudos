a = float(input('Digite o valor da medida a'))
b = float(input('Digite o valor da medida b'))
c = float(input('Digite o valor da medida c'))

if (b - a) < a < b + c and (a - c) < b < a + c and (a- b) < c < a + b:
    print('Forma um triangulo')
    if a == b and b == a and b == c:
        print('O triangulo é um equilatero')
    elif a == b or b == c or c == a:
        print('O triangulo é um isósceles')
    else:
        print('O triangulo é um escaleno')
else:
    print('não forma um tringulo')