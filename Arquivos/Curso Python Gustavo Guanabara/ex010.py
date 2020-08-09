n1 = float(input("Digite quantos reais você possui: "))

cores = { 'limpa':'\033[m',
    'vermelho':'\033[0;31m',
    'azul':'\033[0;34m',
    'amarelo':'\033[0;33m'

}
print('Com esse dinheiro você consegue comprar {}{:.2f}{} Dolares '.format(cores['vermelho'], n1/3.27, cores['limpa']))