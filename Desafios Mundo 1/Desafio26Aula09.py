from itertools import count
p = str(input('Escreva uma frase qualquer:')).lower().strip()
p1 = p.count('a')
p2 = p.find('a')+1
p3 = p.rfind('a')+1
print(f'A letra A aparece {p1} vezes\n'
      f'A letra A aparece a primeira vez na casa {p2} da frase.\n'
      f'A letra A aparece a última vez na casa {p3} da frase.\n')
