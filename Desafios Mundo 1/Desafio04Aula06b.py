# Faça um programa que leia algo pelo teclado e mostre na tela o seu tipo primitivo e todas as informações possíveis sobre ele.
N = input('Digite algo?')
print('O tipo primitivo desse valor é', type(N))
print('Só tem espaços?', N.isspace())
print('É um número?',N.isnumeric())
print('É alfabético?',N.isalpha())
print('É alfanúmerico?',N.isalnum())
print('Está em maiúsculas?', N.isupper())
print('Está em minúsculas?', N.islower())
print('Está capitalizada?', N.istitle())




# print(N,'Está tudo em maisculo?'.isupper())
# print(N,'É um número alpha-número?'.isalnum())
# print(N,'É alfabetico?'.isalpha())
# print(N,'É númerico?'.format(N).isnumeric())
# print(N,'É um decimal?'.isdecimal())
# print(N,'É tudo escrito em letras minúsculas?'.islower())
# print(N,'É imprimivel?'.isprintable())
# print(N,'Com primeira letra Maiscula e o resto minuscula?'.istitle())
# print(N,'É um identificador?'.isidentifier())
# print(N,'É um digito?'.isdigit())