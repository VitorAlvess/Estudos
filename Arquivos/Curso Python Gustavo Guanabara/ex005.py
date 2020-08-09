n1 = int(input("Digite o numero"))
cores = { 'limpa':'\033[m',
    'vermelho':'\033[0;31m',
    'azul':'\033[0;34m',
    'amarelo':'\033[0;33m'

}

print('O antecessor desse numero é {}{}{} e o sucessor é {}{}{}'.format(cores['vermelho'], n1-1, cores['limpa'],cores['azul'], n1+1, cores['limpa']))
