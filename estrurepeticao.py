##DESAFIO 046 -- contagem regressiva
#ESTRUTURA DE REPETIÇÃO FOR
from time import sleep
for c in range(10, -1, -1 ):
     print(c)
     sleep(1)
print('POW POW')     

#DESAFIO 047 -- Crie um programa que mostre na tela todos os números pares que estão no intervalo entre 1 e 50.
num=int(input('Digite um numero e veja todos os pares dele: '))
for d in range(2, 51, 2):
     print(d)
print('acabou')    

#DESAFIO 48: Faça um programa que calcule a soma entre todos os números que são múltiplos de três e que se encontram no intervalo de 1 até 500.

soma=0
for e in range(1, 501, 2):
     if e % 3 == 0:
          soma = soma + e
print(f'a soma dos multiplos de 3 é: {soma} ')

#DESAFIO 49: Refaça o DESAFIO 9, mostrando a tabuada de um número que o usuário escolher, só que agora utilizando um laço for.

numero=int(input('Digite um valor: '))
for f in range(1, 11):
     print(f'A tabuada do numero: \n {numero}x{f} é: {numero*c}')
     
#while

r = 'S'
while r == 'S':
     n=int(input('Digite um valor: '))
     r=str(input('Quer continuar? [S/N] ')).upper()
print('fim')     
        
     
n=1
par=impar=0
while n != 0:
     n=int(input('digite um valor: '))
     if n % 2==0:
          par +=1
     else:
          impar+=1     
print('acabou')

#DESAFIO 057

sexo=str(input('Informe seu sexo: [F/M] ')).strip().upper()[0]
while sexo not in 'MmFf':
    sexo=str(input('inválido. Digite F ou M: ')) 
print(f'sexo {sexo} registrado com sucesso')  

#DESAFIO 059
#Crie um programa que leia dois valores e mostre um menu na tela:[ 1 ] somar[ 2 ] multiplicar[ 3 ] maioR[ 4 ] novos números[ 5 ] sair do programa
#Seu programa deverá realizar a operação solicitada em cada caso.         
          
v1=int(input('Primeiro valor: '))
v2=int(input('Segundo valor: '))
print(f'O valor foi {v1} e {v2}')
opçao=0
while opçao != 5:
     print('VOCE DESEJA \n [1] SOMAR \n [2] MULTIPLICAR \n [3] MAIOR \n [4] NOVOS NUMEROS \n [5] SAIR')
     opçao=int(input('Qual vai ser a opção?: '))
     if opçao ==1:
          soma=v1+v2
          print(f'A sua soma foi igual à: {soma}')
     elif opçao ==2:
          mult=v1*v2
          print(f'A sua multiplicação foi igual à: {mult}')
     elif opçao==3:
          if v1>v2:
               maior=v1
          else:
               maior=v2 
          print(f'O numero maior é: {maior}')
     elif opçao==4:
          print('informe novos valores: ')
          v1=int(input('Primeiro valor: '))
          v2=int(input('Segundo valor: '))     
print('FIM DO PROGRAMA') 
     
#Exercício Python 060: Faça um programa que leia um número qualquer e mostre o seu fatorial. Exemplo: 5! = 5 x 4 x 3 x 2 x 1 = 120     
n=int(input('Digite um numero para calcular o seu fatorial: '))
cont=n
#contador
f=1
#multiplicação sempre começa com 1 e soma com 0
while cont >0:
     print(f'{cont}',  end='')
     print('x' if cont > 1 else ' = ', end='')
     f*=cont
     cont -= 1
print(f'A multiplicação dos fatores é: {f}') 


n= cont = soma =0
n=int(input('Digite um numero [999 para parar]: '))
while n != 999:
     
     cont+=1
     soma+=n
     n=int(input('Digite um numero [999 para parar]: '))   
print(f'voce digitou {cont}. E a soma foi: {soma}')
print('Você parou o programa')

#DESAFIO 065
#Crie um programa que leia vários números inteiros pelo teclado. No final da execução, mostre a média entre todos os valores
r='S' 
media=quant=soma=0        
while r == 'S':
     n=int(input('Digite um numero: '))
     r=str(input('Quer continuar [S/N]')).upper().strip[0]
     soma=+n
     quant=+1   
media=soma/quant
print(f'A média foi: {media}')     
print('fim do programa')     
