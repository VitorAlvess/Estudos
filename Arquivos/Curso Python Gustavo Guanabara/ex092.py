from datetime import date

ano = date.today().year
pessoa = {
    'nome': str(input('Nome:')),
    'Idade': ano - int(input('Ano de nascimento:')),
    'Carteira de trabalho': int(input('Carteira de trabalho [0 = não tem]'))
}

if pessoa['Carteira de trabalho'] != 0:
    pessoa['contrataçao'] = int(input('Ano de contratação: '))
    pessoa['Salario'] = float(input('Salario:'))
    pessoa['Aposentadoria'] = (pessoa['contrataçao'] + 35) - (ano - pessoa['Idade'])

for k,v in pessoa.items():
    print(f'{k} tem o valor {v}')