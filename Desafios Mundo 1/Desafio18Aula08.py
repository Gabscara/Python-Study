from math import cos, tan, sin, radians
an = float(input('Qual o anguloº: ?'))
an1 = radians(an)
print(f'o Valor do anguloº {an1:.2f} Cos vale {cos(an1):.2f},Seno {sin(an1):.2f},Tangente {tan(an1):.2f}')

#metodo feito pelo proff
'''from math import radians, sin, cos, tan
ângulo = float(input('Digite o ângulo que você deseja:')
seno = sin(radians(ângulo))
print('O ângulo de {ângulo} tem o SENO de {seno:.2f}')
cosseno = cos(radians(ângulo))
print('O ângulo de {ângulo} tem o COSSENO de {cosseno:.2f}')
tangente = tan(radians(ângulo))
print('O ângulo de {ângulo} tem a TANGENTE de {tangente:.2f}')'''