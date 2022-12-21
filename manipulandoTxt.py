
import emoji
#manipulando texto
# fatiamento
#frase[9]= 9 é a posição da letra do texto
#frase[9:20]= parte da letra 9 até o 20
#frase[9:21:2]= começa no 9, para no 21 e pula de 2 em 2
#frase[:5]= antes dos :, começa no 0 e termina no 5
#frase[5:]= começa no 5 e termina até o final
#frase[9::3]= começa no 9, termina até o final e pula de 3 em 3


#ANALISE
#len(frase)= conta os caracteres
#frase.count('o')= contar quantas vezes aparece a letra 'O'
#frase.count('o',0,13)= contar quantas vezes aparece a letra O do 0 até o 12
#frase.find('deo')= quantas vezes ele encontrou 'deo'
#'curso' IN frase =  existe a palavra curso em frase

#TRANSFORMAÇÃO
#frase.replace('python','android')= troca a primeira palavra pela segunda
#frase.upper()= transforma a string em maiusculo
#frase.lower()= transforma a string em minusculo
#frase.capitalize()= só a primeira letra da string fica em maiusculo
#frase.title()= transforma a primeira letra de cada palavra em maiusculo
#frase.strip()= remove os primeiro e ultimos espaços da string
#frase.rstrip()= remove os espaços somente do lado direito
#frase.lstrip()= remove os espaços somente do lado esquerdo

#DIVISÃO
#frase.split()=pega os espaços e cria uma divisão entre as palavras e coloca elas em outra lista

#JUNÇÃO
#'-'.join(frase)= junta os elementos da frase e coloca o '-'

frase='Jesus loves you '
print(emoji.emojize(' :red_heart:  '.join(frase)))


