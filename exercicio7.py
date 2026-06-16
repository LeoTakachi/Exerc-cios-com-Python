# As pessoas colaboradoras de um setor da empresa que você trabalha vão receber um abono correspondente a 10% do salário devido ao ótimo desempenho do time.
# O setor financeiro solicitou sua ajuda para a verificação das consequências financeiras que esse abono irá gerar nos recursos.
# Assim, foi encaminhada para você uma lista com os salários que receberão o abono: [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903].
# O abono de cada colaborador(a) não pode ser inferior a 200. Em código, transforme cada um dos salários em chaves de um dicionário e o abono de cada salário no elemento.
# Depois, informe o total de gastos com o abono, quantos(as) colaboradores(as) receberam o abono mínimo e qual o maior valor de abono fornecido.

# RESOLUÇÃO:
salarios = [1172, 1644, 2617, 5130, 5532, 6341, 6650, 7238, 7685, 7782, 7903]
dic_abonos = {}
total_abono = 0
abonos_minimo = 0
maior_abono = 0

for salario in salarios:
    abono = salario * 0.1
    if abono < 200:
        abono = 200
    dic_abonos[salario] = abono

for abono in dic_abonos.values():
    if abono == 200:
        abonos_minimo += 1

    if abono > maior_abono:
        maior_abono = abono

    total_abono += abono

print(f'Abonos: {dic_abonos}')
print(f'Total de gasto com abonos: {total_abono}')
print(f'Número de funcionários que receberam o abono mínimo: {abonos_minimo}')
print(f'Maior valor de abono: {maior_abono}')
