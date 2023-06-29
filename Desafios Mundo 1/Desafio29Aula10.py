from time import sleep
velo = float(input(f'Seu amigo viu um radar e lhe perguntou qual era a sua velocidade atual.\n'
                   f'Indique em Km/h, sua velocidade:'))
multa = (velo-80)*7
if velo > 80:
    print(f'BASEADO NA VELOCIDADE, CALCULEI QUE...')
    sleep(3)
    print(f'MULTADO, Calculando a velocidade excedida...')
    sleep(1.5)
    print(f'Velocidade excedida de {velo-80:.2f}Km/h\nVocê pagará um total de {multa:.2f}R$')
else:
    print('BASEADO NA VELOCIDADE, CALCULEI QUE...')
    sleep(3)
    print('Não houve infrações portanto...\nContinuem seguros e tenham uma boa viagem!')
