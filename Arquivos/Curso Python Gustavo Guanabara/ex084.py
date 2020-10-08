#
#galera = []
#dado = []
#for c in range(0,3):
 #   galera.append(str(input('Nome: ')))
  #  galera.append((int(input('Idade: '))))
   # dado.append(galera[:])
    #galera.clear()
#for c in dado:
# print(c[1]

dados = []
pessoas = []

continuar = ''
contagem = 0
maior = menor = 0
while True:
    dados.append(str(input('Nome:')))
    dados.append(float(input('Peso:')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]

    pessoas.append(dados[:])
    dados.clear()
    continuar = str(input('Continuar [S/N]')).upper()
    contagem += 1
    if continuar == 'N':
        break



print(f'Foram cadastradas {contagem} pessoas')
print(f'As pessoas mais pesadas são com {maior} kilos:', end=' ')
for p in pessoas:
    if p[1] == maior:
        print([p[0]], end='')

print(f'\nAs pessoas mais leves são com {menor} kilos:', end=' ')
for p in pessoas:
    if p[1] == menor:
        print([p[0]], end=' ')



