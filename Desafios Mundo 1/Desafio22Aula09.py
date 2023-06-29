nome = str(input('Qual é seu nome completo?'))
nomesvaz = str(len(nome) - nome.count(' '))
nomel1 = nome.split()

print(f'O Nome com todas as letras maíusculas é {nome.upper()}')
print(f'O nome com letras minúsculas é {nome.lower()}')
print(f'Quantas letras ao todo (sem considerar espaços) {nomesvaz}')
print(f'Quantos letras tem o primeiro Nome: Primeiro nome {nomel1[0]} com a quantidade de letras {len(nomel1[0])}')
print('todas as infos: {}, {}, {},{}'.format(nome.upper(), nome.lower(), nomesvaz, len(nomel1[0])))
