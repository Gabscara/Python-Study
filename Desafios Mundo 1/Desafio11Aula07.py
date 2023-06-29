larg = float(input('Largura da Parede:'))
alt = float(input('Altura da Parede:'))
area = (alt*larg)
t = area/2
print(f'Sua parede tem a dimensão de {larg} x {alt} Obtendo a área de {area}M².\n '
      f'Para pintar essa parede temos que utilizar {t:.3f}l de tinta')
