from time import sleep
r1 = int(input('Primeira segmento:'))
r2 = int(input('Segunda segmento:'))
r3 = int(input('Terceira segmento:'))
if r1 < r2+r3 and r2 < r1+r3 and r3 < r1+r2:
    print(f'O comprimento da 1º-"{r1}"')
    print(' ' * 16, f'2º-"{r2}"')
    print(' ' * 16, f'3º-"{r3}')
    print(' ' * 16, f'\033[1;35mLoading...\033[m')
    sleep(3)
    print('Pode formar um \033[1;32mTRIÂNGULO\033[m')
    sleep(2)
    print('\033[1;35mGemotria DASH!!\033[m')
    print('\033[1;31mRegra:\033[m A soma de dois segmentos menores tem de ser maior que o 3º segmento')
else:
    print(f'O comprimento da 1º-"{r1}"')
    print(' ' * 16, f'2º-"{r2}"')
    print(' ' * 16, f'3º-"{r3}"')
    print(' ' * 16, f'\033[1;35mLoading...\033[m')
    sleep(3)
    print(f'Os segmentos mencionados acima não pode formar um \033[1;32mTRIÂNGULO\033[m')
    print('\033[1;31mRegra:\033[m A soma de dois segmentos menores tem de ser maior que o 3º segmento')
