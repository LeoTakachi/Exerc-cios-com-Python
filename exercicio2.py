# ENUNCIADO: Para uma seleção de produtos alimentícios, precisamos separar o conjunto de IDs dados por números inteiros
# sabendo que os produtos com ID par são doces e os com ID ímpar são amargos. Monte um código que colete 10 IDs.
# Depois, calcule e mostre a quantidade de produtos doces e amargos.

# RESOLUÇÃO:
lista_ids = []
doce = 0
amargo = 0

for i in range(0,10):
  lista_ids.append(int(input(f'Digite o {i+1}° ID: ')))


for id in lista_ids:
  if id % 2 == 0:
    doce += 1
  else:
    amargo += 1

# RESULTADO:
print(f'Quantidade de produtos doces: {doce}')
print(f'Quantidade de produtos amargos: {amargo}')