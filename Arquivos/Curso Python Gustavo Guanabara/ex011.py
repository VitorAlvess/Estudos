n1 = float(input('Digite a altura da parede: '))
n2 = float(input('Digite a largura da parede'))
area = n1 * n2
cores = { 'limpa':'\033[m',
    'vermelho':'\033[0;31m',
    'azul':'\033[0;34m',
    'amarelo':'\033[0;33m'

}
print('A quantidade de tinta necessaria para pintar a parede é de {}{}{} litros '.format(cores['azul'], area/2, cores['limpa']))