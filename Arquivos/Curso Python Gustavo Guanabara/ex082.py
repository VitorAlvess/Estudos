valores =  []
impar = []
par = []
while True:
    valores.append(int(input('Digite um valor')))
    con = input('Deseja Continua? [S/N]: ').upper()
    if con[0] == 'N':
        break
for c in range(len(valores)):
    if valores[c] % 2 == 0:
        par.append(valores[c])
    else:
        impar.append(valores[c])
print(f'A lista completa é {valores}')
print(f'A lista de pares é {par}')
print(f'A lista de impares é {impar}')