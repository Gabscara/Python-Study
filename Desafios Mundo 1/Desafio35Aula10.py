from time import sleep
r1 = int(input('Primeira reta:'))
r2 = int(input('Segunda reta:'))
r3 = int(input('Terceira reta:'))
rt = r1+r2
if rt >= r3:
    print(f'O comprimento da 1º-"{r1}"')
    print(' '*16, f'2º-"{r2}"')
    print(' '*16, f'3º-"{r3}')
    print(' '*16, f'Loading...')
    sleep(3)
    print(f'É um triângulo porque a soma do 1ºNúmero:"{r1}" E')
    print(' '*31, f'2ºNúmero:"{r2}" é maior que a 3º Reta = {r3} ')
    sleep(2)
    print(f'Gemotria DASH!!')

elif rt < r3:
    print(f'O comprimento da 1º-"{r1}"')
    print(' ' * 16, f'2º-"{r2}"')
    print(' ' * 16, f'3º-"{r3}"')
    print(' ' * 16, f'Loading...')
    sleep(3)
    print(f'Não é um triângulo porque a soma do 1ºNúmero:"{r1}" E')
    print(' ' * 35, f'2ºNúmero:"{r2}" não é maior que a 3º Reta = {r3} ')
