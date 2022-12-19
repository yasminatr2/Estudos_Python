n=input('digite algo: ');
print(n);

n=input('digite algo: ');
print(n.isupper());
# isupper = Se todas as letras são maiusculas.

n=input('digite algo: ');
print(n.isalpha());
# isalpha = Se o dado inserido é letra.

n=input('digite algo: ');
print(n.isalnum());
# isalnum = Se o dado inserido é letra e numero.

n=input('digite algo: ');
print(n.isnumeric());
# isnumeric = Se o dado inserido é apenas numérico.

n=input('digite algo: ');
print(n.islower());
# islower = Se todas as letras são minusculas.

#desafio

dado=input('Digite alguma coisa: ');
print(f'É um numero?:', dado.isnumeric(),'\n' 'É letra?:', dado.isalpha(), '\n' 'É maiscula?:', dado.isupper(), '\n' 'É minusculo?:', dado.islower(), '\n' 'É uma letra e um numero?:', dado.isalnum());