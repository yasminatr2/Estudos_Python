import math
import random
import emoji



#DESAFIO 019 - SORTEAR UM NOME DA LISTA

no1=str(input('Primeiro nome: '))
no2=str(input('Segundo nome: '))
no3=str(input('Terceiro nome: '))
no4=str(input('Quarto nome: '))
lista=[no1, no2, no3, no4]
sortear=random.choice(lista)
print(f'O nome sorteado foi: {sortear}')

