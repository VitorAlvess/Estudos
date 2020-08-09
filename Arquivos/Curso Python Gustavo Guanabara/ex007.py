n1 = float(input("Digite A nota 1 do aluno: "))
n2 = float(input('Digite a nota 2 do aluno: '))
media = (n1 + n2) / 2

cores = { 'limpa':'\033[m',
    'vermelho':'\033[0;31m',
    'azul':'\033[0;34m',
    'amarelo':'\033[0;33m'

}
print('A media do aluno foi {}{}  '.format(cores['amarelo'], media))