# O setor de RH da sua empresa te pediu uma ajuda para analisar as idades de colaboradores(as) de 4 setores da empresa.
# Para isso, foram fornecidos os seguintes dados:
# {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
#  'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
#  'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
#  'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}
# Sabendo que cada setor tem 10 colaboradores(as), construa um código que calcule a média de idade de cada setor,
# a idade média geral entre todos os setores e quantas pessoas estão acima da idade média geral.

# RESOLUÇÃO:
soma_idades = 0
media_setor = 0
soma_setores = 0
media_geral = 0
quant_acima_media = 0

idades_setores = {'Setor A': [22, 26, 30, 30, 35, 38, 40, 56, 57, 65],
                  'Setor B': [22, 24, 26, 33, 41, 49, 50, 54, 60, 64],
                  'Setor C': [23, 26, 26, 29, 34, 35, 36, 41, 52, 56],
                  'Setor D': [19, 20, 25, 27, 34, 39, 42, 44, 50, 65]}

for setor, idades in idades_setores.items():
    media_setor = sum(idades) / len(idades)
    print(f'{setor}: média de {media_setor} anos')
    soma_setores += sum(idades)

media_geral = soma_setores / (len(idades) * len(idades_setores))
print(f'A média geral de idade é {media_geral} anos')

for setor, idades in idades_setores.items():
    for id in idades:
        if id > media_geral:
            quant_acima_media += 1
print(f'{quant_acima_media} pessoas estão acima da média geral de idade')

