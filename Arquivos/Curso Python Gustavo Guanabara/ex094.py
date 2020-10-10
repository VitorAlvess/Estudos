dados = list()
pessoa = dict()
mulher = list()
cont = ''
contator = media = 0
while True:
    pessoa['nome'] = str(input('Nome:'))
    pessoa['sexo'] = str(input('Sexo [M/F]: ')).upper()
    pessoa['idade'] = int(input('Idade:'))
    cont = str(input('Continuar? [S/N]')).upper()
    dados.append(pessoa.copy())
    contator += 1
    pessoa.clear()
    if cont == 'N':
        break
print(dados)
for c in range(0, len(dados)):
     media = media + dados[c]['idade']
     if dados[c]['sexo'] == 'F':
         mulher.append(dados[c]['nome'])
media = media / len(dados)
print(f'Foram cadastradas {contator} pessoas')
print(f'A media de idade é de {media:.2f} Anos')
print(f'As mulheres cadastradas foram: ', end=' ')
for c in mulher:
    print(c, end=' ')
print()
print('Lista de pessoas acima da media: ')
for c in range(0, len(dados)):
    if dados[c]['idade'] > media:
        print(dados[c])