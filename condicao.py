

import random     
opcoes=['pedra', 'papel', 'tesoura']
jogador=['pedra', 'papel', 'tesoura']          
print('Escolha, pedra papel ou tesoura')
computador=random.choice(opcoes)

if jogador==opcoes and computador=='papel':
    print('Você perdeu') 
elif jogador=='pedra' and computador=='pedra':
    print('Empate!')
elif jogador=='pedra' and computador=='tesoura':
    print('Você ganhou')

                   