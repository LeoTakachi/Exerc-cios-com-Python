# Uma equipe de cientistas de dados está estudando a diversidade biológica em uma floresta.
# A equipe fez a coleta de informações sobre o número de espécies de plantas e animais em cada área dessa floresta e armazenou essas informações em um dicionário.
# Nele, a chave descreve a área dos dados e os valores nas listas correspondem às espécies de plantas e animais nas áreas, respectivamente.
# {'Área Norte': [2819, 7236],
#  'Área Leste': [1440, 9492],
#  'Área Sul': [5969, 7496],
#  'Área Oeste': [14446, 49688],
#  'Área Centro': [22558, 45148]}
# Escreva um código para calcular a média de espécies por área e identificar a área com a maior diversidade biológica.

areas_floresta = {'Área Norte': [2819, 7236],
                  'Área Leste': [1440, 9492],
                  'Área Sul': [5969, 7496],
                  'Área Oeste': [14446, 49688],
                  'Área Centro': [22558, 45148]}

soma_medias = 0
area_mais_diversa = ''
maior_soma = 0


for area, especies in areas_floresta.items():
    soma_especies = sum(especies)
    media_especies = soma_especies / len(especies)
    print(f'{area} - média de {media_especies} espécies')
    if soma_especies > maior_soma:
        maior_soma = soma_especies
        area_mais_diversa = area
    soma_medias += media_especies

media_total = soma_medias / len(areas_floresta)
print(f'Média espécies por área: {media_total}')
print(f'A área com maior diversidade biológica é a {area_mais_diversa}')




