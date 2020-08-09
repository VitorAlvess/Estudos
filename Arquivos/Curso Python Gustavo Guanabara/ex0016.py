# pulei 2 pq é tipo um extra tlgd

import math

n1 = float(input('Digite um numero'))
n2 = math.floor(n1)
cores = { 'limpa':'\033[m',
    'vermelho':'\033[0;31m',
    'azul':'\033[0;34m',
    'amarelo':'\033[0;33m'

}
print('O numero arredondando é igual a {}{}'.format(cores['amarelo'], n2))