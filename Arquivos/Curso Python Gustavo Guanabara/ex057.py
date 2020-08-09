sexo = str(input('Digite o sexo [M/F]')).strip().upper()
while sexo not in 'MF':
    sexo = str(input('Digite um sexo valido [M/F]')).upper().strip()
print('Fim')