# Desenvolva um programa que informa a nota de um(a) aluno(a) de acordo com suas respostas.
# Ele deve pedir a resposta desse(a) aluno(a) para cada questão e é preciso verificar se a resposta foi igual ao gabarito.
# Cada questão vale um ponto e existem as alternativas A, B, C ou D.
# Gabarito da prova:
# 01 - D
# 02 - A
# 03 - C
# 04 - B
# 05 - A
# 06 - D
# 07 - C
# 08 - C
# 09 - A
# 10 - B

# RESOLUÇÃO:
respostas = []
gabarito = ['D', 'A', 'C', 'B', 'A', 'D', 'C', 'C', 'A', 'B']
nota = 0

for i in range(0, 10):
    respostas.append(input(f'Insira a respostas da questão {i + 1}:').upper())

for i in range(0, 10):
    if respostas[i] == gabarito[i]:
        nota += 1

print(f'Nota final: {nota}')
