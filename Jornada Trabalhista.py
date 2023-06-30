#Variaveis a utilizar
semanasano = 365/7


hrd = str(input('Quantas horas você dorme por dia?\n\033[1;31mExemplo: "8:30"\033[m\n\033[1;30mINFORME:\033[m')).strip()
hrd = hrd.replace(':', '.')
horasdormindo = float(hrd)
l = str(input('Quantas horas passa se locomovendo?\n\033[1;31mExemplo: "2:30"\033[m\n\033[1;30mINFORME:\033[m')).strip()
l = l.replace(':', '.')
locomocao = float(l)
r = str(input('Quantas horas você tem de almoço?\n\033[1;31mExemplo: "1:30"\033[m\n\033[1;30mINFORME:\033[m')).strip()
r = r.replace(':', '.')
refeicoes = float(r)
t = str(input('Quantas horas você trabalha diariamente\n\033[1;31mExemplo: "8:00"\033[m\n\033[1;30mINFORME:\033[m')).strip()
t = t.replace(':', '.')
trabalho = float(t)
d = str(input('Quantos dias na semana você trabalha?\n\033[1;31mExemplo: 1 a 7 / Coloque somente o número\033[m\n\033[1;30mINFORME:\033[m')).strip()
diasdasemana = float(d)
a = str(input('Quantos anos você acha que viverá?\n\033[1;31mExemplo: 50 / Coloque somente o número\033[m\n\033[1;30mINFORME:\033[m')).strip()
anosmorte = float(a)
faixa = float(input('Quanto você recebe pelo tempo de trabalho?\n\033[1;31mExemplo: Liquido bancário\033[m\n\033[1;30mINFORME:\033[m'))



horasrest = 24.00 - (trabalho+refeicoes+locomocao+horasdormindo)
sobra_hora_ano = horasrest * (diasdasemana*semanasano)
temposobra = sobra_hora_ano * anosmorte
resultado1 = temposobra/24
resultadof = resultado1/365

horastrab =trabalho+locomocao
trab_hora_ano = horastrab * (diasdasemana*semanasano)
tempotrab = trab_hora_ano * anosmorte
resultado2 = tempotrab/24
resultadof2 = resultado2/365
horasmes = horastrab*(diasdasemana*4.34524)
faixasalarial = faixa/horasmes
horaspdia = horasmes/(diasdasemana*4.34524.__floor__())


salarialano = horasmes*trab_hora_ano
print(f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'\033[1;33mSobre o tempo restante livre, você tera um total de:\033[m\n'
      f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'\033[1;35m{sobra_hora_ano.__floor__():,.0f}Hrs LIVRES P/ANO\033[m\n'
      f'Total de tempo (Hrs) sobrando no total de anos vividos:\n\033[1;35m{temposobra.__floor__():,.0f}Hrs TOTAIS LIVRES\033[m\n'
      f'Dias livres na vida inteira durante esse período:\n\033[1;35m{resultado1.__floor__():,.0f} DIAS LIVRES\033[m \n'
      f'Quantidade de anos livres durante a vida:\n\033[1;35m{resultadof.__floor__():,.0f} ANOS LIVRES\033[m')
print('\033[1;31mOBS: O CALCULO CONSIDERA SOMENTE PARA OS DIAS TRABALHADOS!!\033[m')


print(f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'\033[1;33mSobre o tempo trabalho:\033[m\n'
      f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'\033[1;36mTrabalha {trab_hora_ano:,.0f}Hrs em um ano!!!\033[m\n'
      f'\033[1;35mTrabalha {trab_hora_ano/12:.0f} HRS em um mês...\033[m\n'
      f'\033[1;35mTrabalha {horaspdia:.0f} HRS por dia\033[m\n'
      f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'\033[1;33mSobre seu salário:\033[m\n'
      f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'Com uma faixa Salarial de:\n\033[1;35m{faixa:,.2f}R$...\033[m\n'
      f'Seu Salário por hora é de:\n\033[1;35m{faixasalarial:,.2f}R$...\033[m\n'
      f'Seu Salário por dia é de:\n\033[1;35m{horaspdia*faixasalarial:,.2f}R$...\033[m\n'
      f'Suas horas trabalhadas em um ano:\n\033[1;35m{trab_hora_ano:.0f} HRS ANO...\033[m\n'
      f'Recebendo um total de:\n\033[1;35m{faixasalarial*trab_hora_ano:,.2f}R$ no decorrer de um ano...\033[m')
