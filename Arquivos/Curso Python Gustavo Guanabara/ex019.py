#escolher um aluno de forma aleatoria

import random

nome1 = input('Digite o nome do aluno 1')
nome2 = input('Digite o nome do aluno 2')
nome3 = input('Digite o nome do aluno 3')
nome4 = input('Digite o nome do aluno 4')


print('O nome do aluno sorteado é {} '.format(random.choice([nome1, nome2, nome3, nome4])))
