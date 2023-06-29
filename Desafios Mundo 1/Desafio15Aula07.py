qtdekm = float(input(f'Quantos KMs foram percorridos com o carro alugado?'))
dias = int(input(f'Quantos dias o carro foi alugado?'))
pkm = (qtdekm*0.15)
preco = (dias*60)+pkm
print(f'O preço a se pagar pelos com o aluguel de {dias} dias e {qtdekm}KMs rodados é de R${preco:.2f}')