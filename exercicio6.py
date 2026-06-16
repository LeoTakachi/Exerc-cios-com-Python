# Uma pesquisa de mercado foi feita para decidir qual design de marca infantil mais agrada as crianças.
# A pesquisa foi feita e o votos computados podem ser observados abaixo:
# '''
# Tabela de votos da marca
# Design 1 - 1334 votos
# Design 2 - 982 votos
# Design 3 - 1751 votos
# Design 4 - 210 votos
# Design 5 - 1811 votos
# '''
# Adapte os dados fornecidos para uma estrutura de dicionário. A partir dele, informe o design vencedor e a porcentagem de votos recebidos.

# RESOLUÇÃO:
designs = {'Desing 1': 1334
           , 'Desing 2': 982
           , 'Desing 3': 1751
           , 'Desing 4': 210
           , 'Desing 5': 1811}
total_votos = 0
design_vencedor = ''
unidade_design_vencedor = 0

for design in designs.keys():
    total_votos += designs[design]

    if designs[design] > unidade_design_vencedor:
        unidade_design_vencedor = designs[design]
        design_vencedor = design

porcentagem_votos_vencedor = unidade_design_vencedor / total_votos * 100

print(f'O design mais votado foi {design_vencedor} com {porcentagem_votos_vencedor}% dos votos.')

