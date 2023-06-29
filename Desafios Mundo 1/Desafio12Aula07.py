p = float(input('Preço do Produto:'))
d = float((p*0.05))
r = (p-d)
print(f'Com desconto de 5% no valor {p} o valor descontado (5%) é {d:.2f} o valor final é R${r:.2f}')
