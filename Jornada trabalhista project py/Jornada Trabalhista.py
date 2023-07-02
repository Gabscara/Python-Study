#Variaveis a utilizar
semanasano = 365/7


hrd = str(input('Quantas horas você dorme por dia?\n\033[1;31mExemplo: "8:30"\033[m\n\033[1;30mINFORME:\033[m')).strip()
hrd = hrd.replace(':', '.')
horasdormindo = float(hrd)
loc = str(input('Quantas horas passa se locomovendo?\n\033[1;31mExemplo: "2:30"\033[m\n'
                '\033[1;30mINFORME:\033[m')).strip()
loc = loc.replace(':', '.')
locomocao = float(loc)
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
sobra_hora_ano = horasrest * (diasdasemana*52)
httf = 104*24
horaslivre = httf + sobra_hora_ano
temposobra = horaslivre * anosmorte
resultado1 = temposobra/24
resultadof = resultado1/365
horaslivrem = horaslivre/12
horaslivred = horaslivrem*0.0416667
#Variaveis de trabalho
horastrab = trabalho+locomocao
trab_hora_ano = horastrab * (diasdasemana*52)
tempotrab = trab_hora_ano * anosmorte
resultado2 = tempotrab/24
resultadof2 = resultado2/365
horasmes = horastrab*(diasdasemana*4)
#médias totais
media_sobra_rest = (horaslivre/8736) * 100
media_trab = (trab_hora_ano/8736) * 100
media_ali_dorm = 8736 - (horaslivre+trab_hora_ano)
media_rest = (media_ali_dorm/8736) * 100
media_livre = (horaslivre-media_ali_dorm)/8736
#Variaveis salarios
faixasalarial = faixa/horasmes
horaspdia = horasmes/(diasdasemana*4)
faixarest = faixa-gastm
faixaresta = (faixarest/horasmes)*trab_hora_ano


print(f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'\033[1;33mSobre o tempo restante livre, você tera um total de:\033[m\n'
      f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'\033[1;33mTEMPO,TIPO\033[m\n'
      f'\033[1;35m{resultadof.__ceil__():,.0f} '
      f'ANOS LIVRES\033[m em \033[1;35m{anosmorte:.0f} Anos Vividos\033[m\n'
      f'\033[1;35m{resultado1.__ceil__():,.0f} '
      f'DIAS LIVRES\033[m em \033[1;35m{anosmorte*365:,.0f} Dias Vividos\033[m\n'
      f'\033[1;35m{temposobra.__ceil__():,.0f} '
      f'HRS TOTAIS LIVRES\033[m em \033[1;35m{(anosmorte*365)*24:,.0f} Horas Vividas\033[m\n'
      f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'Nos \033[1;35m{diasdasemana:.0f} Dias da semana\033[m identifiquei \033[1;35m{horasrest} Hrs'
      f'\033[m livres em cada dia.\n as "horas livres restantes" + "horas livres finais de semana" '
      f'apresenta uma média de:\n'
      f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'\033[1;33mConvertendo as horas totais livres em um ANO...\033[m\n'
      f'\033[1;35mSão exatamente: "{horaslivre:,.0f}"\033[m HRS , \033[1;35m"{horaslivre/24:.0f}"\033[m DIAS e '
      f'\033[1;35m"{horaslivre*0.00136986:.0f}"\033[m MESES Livres '
      f'Média de \033[1;35m"{(horaslivrem/730)*100:,.1f}%"\033[m Dias livres a cada MÊS\n'
      f'Média de \033[1;35m{horaslivrem.__ceil__()/24:.0f} Dias\033[m Livres em cada MÊS durante um ANO\n'
      f'Média de \033[1;35m{horaslivrem:,.0f} HORAS\033[m LIVRES p/MÊS em um ANO\n'
      f'Média de \033[1;35m{horaslivrem/30:,.0f} HORAS\033[m LIVRES p/DIA em um ANO\n')

print(f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'\033[1;33mSobre o tempo trabalho:\033[m\n'
      f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'\033[1;35m{trab_hora_ano:,.0f} HRS em um ano!!!\033[m\n'
      f'\033[1;35m{horasmes:.0f} HRS em um mês...\033[m\n'
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

print(f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'\033[1;31mA Conclusão é que se um ano contém:\033[m \033[1;35m8,736 Hrs\033[m\nDessas horas:\n'
      f'\033[7;34;40m{"-=-"*20}\033[m\n'
      f'Você terá \033[1;35m{horaslivre:,.0f} HRS ou {media_sobra_rest:.1f}% de HORAS\033[m LIVRES por ANO\n'
      f'Você terá \033[1;35m{trab_hora_ano:,.0f} HRS ou {media_trab:.1f}% de HORAS\033[m TRABALHADAS por ANO'
      f'\n'
      f'Você terá \033[1;35m{media_ali_dorm:,.0f} HRS ou {media_rest:.1f}% de HORAS\033[m '
      f'DORMINDO e se ALIMENTANDO por ANO\n'
      f'Considerando que você dormir e se alimentar não entra em tempo livre:\n'
      f'Você terá \033[1;35m{horaslivre-media_ali_dorm:,.0f} HRS ou {(media_livre) * 100:.1f}% de HORAS por ANO')
