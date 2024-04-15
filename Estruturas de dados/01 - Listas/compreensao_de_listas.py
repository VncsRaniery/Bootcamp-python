# Filtrar lista
numeros = [1, 30, 21, 2, 9, 65, 34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)

# Modificar valores
numeros = [1, 30, 21, 2, 9, 65, 34]
quadrado = [numero**2 for numero in numeros]
print(quadrado)

# Explicando com detalhes: A compreensão de listas é uma forma concisa de criar listas em Python. Ela permite criar uma nova lista a partir de uma lista existente, aplicando uma expressão a cada elemento da lista original. No primeiro exemplo, a lista pares é criada a partir da lista numeros, contendo apenas os números pares. A expressão if numero % 2 == 0 verifica se o número é par. No segundo exemplo, a lista quadrado é criada a partir da lista numeros, contendo o quadrado de cada número. A expressão numero**2 calcula o quadrado de cada número.