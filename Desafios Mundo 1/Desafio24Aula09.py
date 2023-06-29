cidade = str(input(f'Nome da cidade')).lower().strip()
t = 'Tem Santo'
n = 'Não tem Santo'
santo = 'santo'

if santo in cidade:
    print(t)
else:
    print(n)
