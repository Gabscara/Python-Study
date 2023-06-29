sal = float(input('Digite seu salário para calcularmos o reajuste:'))
virg1 = (sal*0.10) + sal
virg2 = (sal*0.15) + sal
if sal > 1250:
    print(f'O salário de {sal:,.2f}R$ com aumento de 10% é de {(virg1):,.2f}R$!\nO seu valor de aumento é de {sal*0.10:,.2f}R$!')
else:
    print(f'O salário de {sal:,.2f}R$ com o aumento de 15% é de {(virg2):,.2f}R$!\nO seu valor de aumento é de {sal*0.15:,.2f}R$!')
