num = int(input('Informe um numero:'))
u = num // 1 % 10
d = num // 10 % 10
c = num // 100 % 10
m = num // 1000 % 10
print(f'Analisando o número {num}\n'
      f'Milhar {u}\n'
      f'Centena {c}\n'
      f'Dezena {d}\n'
      f'Unidade {u}\n')
