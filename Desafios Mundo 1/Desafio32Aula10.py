from datetime import date
numb = int(input('Digite qualquer ano sendo 0 o ano atual:\nInformarei se ele é um ano Bissexto ou não'))
if numb == 0:
    numb = date.today().year
if numb % 4 == 0 and numb % 100 != 0 or numb % 400 == 0:
    print(f'{numb} é um ano Bissexto!')
else:
    print(f'{numb} não é um ano Bissexto')





