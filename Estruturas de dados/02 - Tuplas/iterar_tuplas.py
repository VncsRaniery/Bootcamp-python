carros = (
    "gol",
    "celta",
    "palio",
)

for carro in carros:
    print(carro)


for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Explicando com detalhes: O laço for é utilizado para iterar sobre os elementos de uma tupla. No primeiro exemplo, cada elemento da tupla carros é impresso na tela. No segundo exemplo, a função enumerate() é utilizada para obter o índice e o valor de cada elemento da tupla. O índice é armazenado na variável indice e o valor na variável carro. Em seguida, esses valores são impressos na tela.