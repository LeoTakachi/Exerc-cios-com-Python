# Um instituto de meteorologia deseja fazer um estudo de temperatura média de cada mês do ano. Para isso,
# você precisa fazer um código que colete e armazene essas temperaturas médias em uma lista.
# Depois, calcule a média anual das temperaturas e mostre todas as temperaturas acima da média anual e em que mês elas ocorreram,
# mostrando os meses por extenso (Janeiro, Fevereiro, etc.).

# RESOLUÇÃO:
lista_medias_temperatura_mes = []
lista_meses = ['Janeiro', 'Fevereiro', 'Março', 'Abril', 'Maio', 'Junho', 'Julho', 'Agosto', 'Setembro', 'Outubro', 'Novembro', 'Dezembro']

for i in range(0, len(lista_meses)):
    lista_medias_temperatura_mes.append(float(input(f'Digite a temperatura média do mês {lista_meses[i]}: ')))
print()

media_anual = sum(lista_medias_temperatura_mes) / len(lista_medias_temperatura_mes)

print('Temperaturas acima da média em:')
for i in range(0, len(lista_meses)):
    if lista_medias_temperatura_mes[i] > media_anual:
        print(lista_meses[i])