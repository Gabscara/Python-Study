s = float(input('Salário do funcionário:'))
acres = float(s*0.15)
sf = float(s+acres)
print(f'O Sálario inicial de R${s:.2f} ,com os 15% de acréscimo, '
      f'o valor do sálario final é de R${sf:.2F} \n Seu acréscimo de 15% é de R${acres:.2f}')
