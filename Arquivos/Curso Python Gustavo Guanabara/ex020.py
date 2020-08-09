#sortear e aparecer uma list
import random

nome1 = input('Digite o nome 1')
nome2 = input('Digite o nome 2')
nome3 = input('Digite o nome 3')
nome4 = input('Digite o nome 4')
ale = [nome1, nome2, nome3, nome4]
print('A ordem Dos alunos é {}'.format(random.sample(ale, k=4)))
