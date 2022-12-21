#DESAFIO 005 
#um programa que leia o numero inteiro e mostre na tela o seu sucessor e o seu antecessor

n=int(input('Digite um numero inteiro: '))
print(f'O seu sucessor é igual a: {n} O seu antecessor é igual a: {n-1}')

#DESAFIO 006
# Crie um algoritimo que leia um numero e mostre o seu dobro, triplo e raiz quadrada

import math
f=int(input('Digite um numero: '))
print(f'o dobro do numero é: {f*2} \n O triplo do numero é: {f*3} \n A raiz quadrada do numero é: {math.sqrt(f)} ')

#DESAFIO 007
#Desenvolva um porgrama que leia as duas notas de um aluno, e calcule e  mostre a sua media

nota1=int(input('Aluno, Digite a sua nota de MATEMATICA: '))
nota2=int(input('Aluno, Digite a sua nota de PORTUGUÊS: '))
nota=nota1+nota2
media=nota/2
print(f'A sua média foi igual á: {media} ')

#DESAFIO 008
#Escreva um programa que leia o valor e o exiba convertido em cm e milimetros

valor=int(input('Insira o valor do chão em metros: '))
m=valor*100
print(f'Este é o valor convertido em cm: {m}')
mm=valor*1000
print(f'Este é o valor convertido em mm: {mm}')

#DESAFIO 009
#Faça um programa que leia um numero inteiro qualquer e mostre na tela a sua tabuada

numero=int(input('Digite um valor: '))
print(f'A tabuada do numero: \n {numero}x1 é: {numero*1} \n {numero}x2 é: {numero*2} \n {numero}x3 é: {numero*3} \n {numero}x4 é: {numero*4} \n {numero}x5 é: {numero*5} \n {numero}x6 é: {numero*6} \n {numero}x7 é: {numero*7} \n {numero}x8 é: {numero*8} \n {numero}x9 é: {numero*9} \n {numero}x10 é: {numero*10} ')

#DESAFIO 010
#Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar
#considerando  US$1,00 = 5,20 em 2022 e
# R$1,00 = 0,19


d=int(input('Digite quantos reais você tem na carteira: R$'))
conversao=d*0.19
print(f'Você pode comprar atualmente em dezembro de 2022: U${conversao} Dólares americanos')

#DESAFIO 011

l=int(input('Qual a largura da parede?: '))
a=int(input('Qual a alutra da parede?: '))
print(f'A área da parede é igual a: {l*a}')

#DESAFIO 012
#faça um algoritimo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto

p=float(input('Digite o valor do produto: '))
desc=p*5/100
desc1=p-desc
print(f'Este é o valor sem desconto: {p} \n Este é o valor com desconto de 5% {desc1}')

#DESAFIO 013
#Fala um algoritimo que leia o salario de um funcionario e mostre seu novo salario com 15% de aumento

s=int(input('Digite o seu salário: '))
sala=s*15/100
novosala=s+sala
print(f'O antigo salário é: {s} \n O seu novo salário agora é de {novosala}')