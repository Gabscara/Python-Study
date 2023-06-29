from random import choice
nome1 = input('Qual o nome do Primeiro aluno:')
nome2 = input('Qual o nome do Segundo aluno:')
nome3 = input('Qual o nome do Terceiro aluno:')
nome4 = input('Qual o nome do Quarto aluno:')
sorteio = [nome1, nome2, nome3, nome4]
select = choice(sorteio)
print(f'Os alunos selecionados para o sorteio foram eles: {sorteio}')
print(f'O Aluno esolhido foi {select.capitalize()}!')
