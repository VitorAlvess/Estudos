# Lista principal, recebe das outras listas
# o nome do aluno, as notas dentro de uma lista e a média.
alunos = list()

dados = list()  # Guarda o nome e a nota média do aluno temporariamente.
notas = list()  # Guarda as duas notas de cada aluno temporariamente.
cont = ''
contator = 0
escolha = 0

while True:
    dados.append(str(input('\nNome: ').title()))
    notas.append(float(input('Nota 1: ')))
    notas.append(float(input('Nota 2: ')))
    dados.append(notas[:])
    dados.append((notas[0] + notas[1]) / 2)
    alunos.append(dados[:])
    contator += 1
    cont = input('Deseja continuar? [S/N]: ').upper()
    if cont == 'N':
        break
    notas.clear()
    dados.clear()
print(alunos[0])
print('*' * 30)
print(f'{"No.":<4}  {"Nome":<10}      {"Media":>8}')
for c in range(0, contator):
    print(f'{c:<4}  {alunos[c][0]:<10}      {alunos[c][2]:>8.1f}')
while True:
    escolha = int(input('Mostrar noda de qual aluno [999 EXIT]: '))
    if escolha == 999:
        break
    print(f'Notas de {alunos[escolha][0]} são {alunos[escolha][1]}')
    print('-' * 30)
print('OBRIGADO POR USAR O NOSSO PROGRAMA :)')
