carros = {"gol", "celta", "palio"}

for carro in carros:
    print(carro)

for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}")

# Explicando detalhes: Para iterar sobre um conjunto, você pode usar um loop for. O loop for percorre cada elemento do conjunto, e você pode acessar o índice e o valor de cada elemento usando a função enumerate(). No exemplo acima, o primeiro loop for imprime cada carro do conjunto, e o segundo loop for imprime o índice e o carro do conjunto.