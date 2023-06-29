nome = str(input('Digite seu nome completo:')).upper()
n = nome.split()
print(f'Seu nome completo é: {nome} !\n'
      f'Seu primeiro nome é :{n[0]}\n'
      f'Seu segundo nome é :{n[-1]}')