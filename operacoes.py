# adição +
print(5+2);

# subtração -
print(5-2);

# multiplicação *
print(5*2);

# divisão /
print(5/2);

#  potência **
print(5**2);

# divisão inteira //
print(5//2);

# resto da divisão %
print(5%2);

#ordem de precedência
# 1 =    ()
# 2 =    ** potência
# 3 =    *  / // %
# 4 =    + e -

print(5+3*2);
print('O resultado é: ', 3*5+4**2);
print('O resultado é: ', 3*(5+4)**2);

# operadores de atribuição

#=	  x = 1	    x = 1
#+=   x += 1	x = x + 1
#-=	  x -= 1	x = x - 1
#*=	  x *= 1	x = x * 1
#/=	  x /= 1	x = x / 1
#%=	  x %= 1	x = x % 1

c = 5

c += 5
# x = x + 1

print(c) # O resultado será 10

#operadores de comparação
# >(Maior que)	        Verifica se um valor é maior que outro	         x > 5
# <(Menor que)	        Verifica se um valor é menor que outro	         x < 5
# == (Igual a)	        Verifica se um valor é igual a outro	         x == 5
# != (Diferente de)	    Verifica se um valor é diferente de outro	     x != 5
# >= (Maior ou igual a)	Verifica se um valor é maior ou igual a outro	 x >= 5
# <= (Menor ou igual a)	Verifica se um valor é menor ou igual a outro	 x <= 5

#programa de autorização por idade

# >=
idade=int(input('Digite a sua idade: '))

if idade >= 18:
    print('Você está autorizado, pode entrar!')
else:
    print('Não é permitido menores de 18 anos')

idade=int(input('Digite a sua idade: '))

# ==

if idade == 18:
    print('Você está autorizado pois sua idade é igual a 18 anos, pode entrar!')
else:
    print('sua idade não é igual a 18 anos')  

#operadores lógicos
#and	 Retorna True se todas as condições forem verdadeiras, caso contrário retorna          False	x > 1 and x < 5
#or	     Retorna True se uma das condições for verdadeiras, caso contrário retorna False	   x > 1 or x < 5
#not	 Inverte o resultado: se o resultado da expressão for True, o operador retorna false   not(x > 1 and x < 5)

#operador OR

idade1=int(input('Por Favor Cliente 1, Digite a sua idade: '))
idade2=int(input('Por Favor Cliente 2, Digite a sua idade: '))
if idade1 >=30 or idade2 >=30:
    print('um dos Clientes tem mais que 30 anos')
else:
    print('Nenhum dos Clientes tem mais do que 30 anos') 

#operador AND       

idade1=int(input('Por Favor Cliente 1, Digite a sua idade: '))
idade2=int(input('Por Favor Cliente 2, Digite a sua idade: '))
if idade1 >=30 and idade2 >=30:
    print('Todos os Clientes tem mais que 30 anos')
else:
    print('Um dos clientes não é maior do que 30 anos')  

#operador is e is not
     
tamlin='feyre'
rhysand='feyre'
cassian='nestha'

if tamlin is rhysand:
    print('rhysand - tamlin: Mesmo interesse')
else:
    print('rhysand - tamlin: Interesse diferente')

# retorna true se as variaveis comparadas forem o mesmo

if rhysand is cassian:
    print('rhysand - cassian: Mesmo interesse')
else:
    print('rhysand - cassian: Interesse diferente')   

#operador de associação      

#operador IN

cores_primarias=['azul','amarelo','vermelho']

cor1='amarelo'
cor2='verde'

print(cor1 in cores_primarias) #retorna TRUE pois 'amarelo' não existe na sequência
print(cor2 in cores_primarias) #retorna FALSE pois 'verde' não existe na sequência

#operador NOT IN


cores_primarias=['azul','amarelo','vermelho']

cor1='amarelo'
cor2='verde'

print(cor1 not in cores_primarias) #retorna FALSE pois 'amarelo' está na sequência
print(cor2 not in cores_primarias) #retorna TRUE pois 'verde' não existe na sequência