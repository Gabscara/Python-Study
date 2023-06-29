from random import sample
nome1 = input('Nome do Primeiro Aluno:')
nome2 = input('Nome do Segundo Aluno:')
nome3 = input('Nome do Terceiro Aluno:')
nome4 = input('Nome do Quarto Aluno:')
nomes = [nome1, nome2, nome3, nome4]
sorteio = sample(nomes, k=len(nomes))
print(f'Os Alunos na sua respectiva sequência: {nomes} vão apresentar na ordem {sorteio} ')

#metodo utilizado pelo professor
'''from random import shuffle
n1 = str(input('Primeiro aluno:')
n2 = str(input('Segundo aluno:')
n3 = str(input('Terceiro aluno:')
n4 = str(input('Quarto aluno:')
Listalunos = [n1, n2, n3, n4]
shuffle(lista)
print(f'A ordem de apresentação será
      f'(lista)'''