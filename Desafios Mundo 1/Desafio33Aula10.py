num1 = int(input('Primeiro Número:'))
num2 = int(input('Segundo Número:'))
num3 = int(input('Terceiro Número:'))
if num1 > num2 > num3:
    print(f'Maior número é o primeiro = {num1}\nE o menor número é o terceiro = {num3}')
elif num1 > num3 > num2:
    print(f'Maior número é o primeiro = {num1}\nE o menor número é o segundo = {num2}')
elif num2 > num1 > num3:
    print(f'Maior número é o segundo = {num2}\nE o menor número é o terceiro = {num3}')
elif num2 > num3 > num1:
    print(f'Maior número é o segundo = {num2}\nE o menor número é o primeiro = {num1}')
elif num3 > num1 > num2:
    print(f'Maior número é o terceiro = {num3}\nE o menor número é o segundo = {num2}')
elif num3 > num2 > num1:
    print(f'Maior número é o terceiro = {num3}\nE o menor número é o primeiro = {num1}')
else:
    print(f'Temos números iguais na parada aiii, verifica')


