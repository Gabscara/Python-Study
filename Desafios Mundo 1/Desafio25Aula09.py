nome = str(input('Qual é seu nome completo')).lower().strip()
t = 'Tem Silva em seu Nome'
n = 'Não tem Silva em seu nome'
r = 'silva'
if r in nome:
    print(t)
else:
    print(n)