n1it = str(input('Coloque um número de 0 a 9999:'))
vazio = ('Não há')
print1 = (f'A sua milhar é : {n1it[0:1]}\n'              
          f'A sua centena é : {n1it[1:2]}\n'             
          f'A sua dezena é : {n1it[2:3]}\n'              
          f'A sua unidade é : {n1it[3:4]}\n')
print2 = (f'A sua milhar é : {vazio}\n'               
          f'A sua centena é : {n1it[0:1]}\n'             
          f'A sua dezena é : {n1it[1:2]}\n'              
          f'A sua unidade é : {n1it[2:3]}\n')
print3 = (f'A sua milhar é : {vazio}\n'                
          f'A sua centena é : {vazio}\n'               
          f'A sua dezena é : {n1it[0:1]}\n'              
          f'A sua unidade é : {n1it[1:2]}\n')
print4 = (f'A sua milhar é : {vazio}\n'
          f'A sua centena é : {vazio}\n'
          f'A sua dezena é : {vazio}\n'
          f'A sua unidade é : {n1it[0:1]}\n')

if int(n1it) >= 1000:
    str(print(print1))
elif int(n1it) >= 100:
    str(print(print2))
elif int(n1it) >= 10:
    str(print(print3))
elif int(n1it) < 10:
    str(print(print4))
else:
    print(print1)
