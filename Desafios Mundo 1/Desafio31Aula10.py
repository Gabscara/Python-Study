km = float(input('Qual é a distância você percorreu com seu carro de São Paulo até o seu destino?\nEm Km/h'))
kmu = float(0.5*km)
kma = float(0.45*km)
if km <= 200:
    print(f'Sendo 0.50R$ por Km/h.\nVocê pagará um total de {kmu:.2f} pelos {km:.2f}Km/h percorridos na viagem!')
else:
    print(f'Sendo 0.45R$ por Km/h.\nVocê pagará um total de {kma:.2f} pelos {km:.2f}Km/h percorridos na viagem!')