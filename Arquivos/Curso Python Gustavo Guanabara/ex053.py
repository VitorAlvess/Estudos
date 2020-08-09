n1 = input('Digite a frase').replace(' ', '').lower()

n2 = n1[::-1]
if n1 == n2:
    print('é um palindromo')
else:
    print('não é um palindromo')