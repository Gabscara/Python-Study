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
t = str(input('Quantas horas você trabalha diariamente\n\033[1;31mExemplo: "8:00"\033[m\n\033[1;30m'
              'INFORME:\033[m')).strip()
t = t.replace(':', '.')
trabalho = float(t)
d = str(input('Quantos dias na semana você trabalha?\n\033[1;31mExemplo: 1 a 7 / Coloque somente o número\033[m\n'
              '\033[1;30mINFORME:\033[m')).strip()
diasdasemana = float(d)
a = str(input('Quantos anos você acha que viverá?\n\033[1;31mExemplo: 50 / Coloque somente o número\033[m\n'
              '\033[1;30mINFORME:\033[m')).strip()
anosmorte = float(a)
faixa = float(input('Quanto você recebe pelo tempo de trabalho?\n\033[1;31mExemplo: Liquido bancário\033[m\n'
                    '\033[1;30mINFORME:\033[m'))
gast = str(input('Quanto você gasta em média no mês\n\033[1;31mExemplo: 800 / Coloque somente o número\033[m\n'
                 '\033[1;30mINFORME:\033[m')).strip()
gastm = float(gast)

#Variaveis de tempo livre na jornada
horasrest = 24.00 - (trabalho+refeicoes+locomocao+horasdormindo)
sobra_hora_ano = horasrest * (diasdasemana*semanasano)
diasfrest = 365 - (diasdasemana*semanasano)
httf = diasfrest*24
horaslivre = httf+sobra_hora_ano
temposobra = horaslivre * anosmorte
resultado1 = temposobra/24
resultadof = resultado1/365
horaslivrem = horaslivre/12
horaslivred = horaslivrem/24

#Variaveis de trabalho
horastrab = trabalho+locomocao
trab_hora_ano = horastrab * (diasdasemana*semanasano)
tempotrab = trab_hora_ano * anosmorte
resultado2 = tempotrab/24
resultadof2 = resultado2/365
horasmes = horastrab*(diasdasemana*4.34524)

#Variaveis salarios
faixasalarial = faixa/horasmes
horaspdia = horasmes/(diasdasemana*4.34524)
faixarest = faixa-gastm
faixaresta = (faixarest/horasmes)*trab_hora_ano


print(f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'\033[1;33mSobre o tempo restante livre, você tera um total de:\033[m\n'
      f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'\033[1;33mTEMPO,TIPO\033[m\n'
      f'\033[1;35m{int(resultadof.__ceil__()):,.0f} '
      f'ANOS LIVRES\033[m em \033[1;35m{anosmorte:.0f} Anos Vividos\033[m\n'
      f'\033[1;35m{int(resultado1.__ceil__()):,.0f} '
      f'DIAS LIVRES\033[m em \033[1;35m{anosmorte*365:,.0f} Dias Vividos\033[m\n'
      f'\033[1;35m{int(temposobra.__ceil__()):,.0f} '
      f'HRS TOTAIS LIVRES\033[m em \033[1;35m{(anosmorte*365)*24:,.0f} Horas Vividas\033[m\n'
      f'\033[1;35m{int(horaslivre/24):,.0f}\033[m Dias livres em um ANO\n'
      f'\033[1;35m{int(horaslivrem/24):,.0f}\033[m Dias livres em um MÊS\n'
      f'\033[1;35m{(horaslivred/24):,.2f}\033[m Média de DIA livre contando finais de semana\n'
      f'\033[1;35m{int(horaslivre.__ceil__()):,.0f}\033[m '
      f'HORAS LIVRES\033[m em um ANO\n'
      f'\033[1;35m{int(horaslivrem.__ceil__()):,.0f} '
      f'HORAS LIVRES\033[m em um MÊS\n'
      f'\033[1;35m{int(horaslivred.__ceil__()):,.0f} '
      f'HORAS LIVRES\033[m em um DIA')

print('\033[1;31mAVISO: O CALCULO CONSIDERA SOMENTE PARA OS DIAS TRABALHADOS!!\033[m')


print(f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'\033[1;33mSobre o tempo trabalho:\033[m\n'
      f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'\033[1;35m{trab_hora_ano:,.0f} HRS em um ano!!!\033[m\n'
      f'\033[1;35m{trab_hora_ano/12:.0f} HRS em um mês...\033[m\n'
      f'\033[1;35m{horaspdia:.0f} HRS por dia\033[m\n'
      f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'\033[1;33mSobre seu salário:\033[m\n'
      f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'Faixa Salarial:\n\033[1;35m{faixa:,.2f}R$...\033[m\n'
      f'Salário por hora:\n\033[1;35m{faixasalarial:,.2f}R$...\033[m\n'
      f'Salário por dia:\n\033[1;35m{horaspdia*faixasalarial:,.2f}R$...\033[m\n'
      f'Recebendo um total de:\n\033[1;35m{faixaresta:,.2f}R$ no decorrer de um ano considerando seu gasto'
      f' mensal...\033[m\n'
      f'Se guardar 10% desse valor no decorrer de um ano receberá:\n'
      f'\033[1;35m{faixaresta*0.10:,.2f}R$\033[m')
