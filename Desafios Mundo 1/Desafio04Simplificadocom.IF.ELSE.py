n = float(input('digite algo:'))
print(f'''
É Alpha númerico? {'Sim'if n.isalnum()else'Não'},
    É alpha? {'Sim'if n.isalpha()else'Não'},
    É Minuscula? {'Sim'if n.islower()else'Não'},
    É maiuscula? {'Sim'if n.isupper()else'Não'},
    Está capitalizada? {'Sim'if n.istitle()else'Não'},
    É Decimal? {'Sim'if n.isdecimal()else'Não'},
    É numérica? {'Sim'if n.isnumeric()else'Não'},
    É espaço? {'Sim'if n.isspace()else'Não'},
    Tipo: {type(n)}''')
