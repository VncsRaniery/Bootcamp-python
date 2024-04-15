lista = ["p", "y", "t", "h", "o", "n"]

print(lista[2:])  # ["t", "h", "o", "n"]
print(lista[:2])  # ["p", "y"]
print(lista[1:3])  # ["y", "t"]
print(lista[0:3:2])  # ["p", "t"]
print(lista[::])  # ["p", "y", "t", "h", "o", "n"]
print(lista[::-1])  # ["n", "o", "h", "t", "y", "p"]

# Explicando em detalhes: O fatiamento de listas é uma operação que permite extrair uma parte da lista original, criando uma nova lista com os elementos desejados. O fatiamento é feito utilizando dois pontos (:) e aceita até três argumentos: início, fim e passo. O início indica a posição inicial da fatia, o fim indica a posição final (não inclusiva) e o passo indica o intervalo entre os elementos. Se algum dos argumentos for omitido, o valor padrão é utilizado: início = 0, fim = tamanho da lista e passo = 1. Além disso, é possível utilizar índices negativos para contar a partir do final da lista. No exemplo acima, lista[2:] retorna os elementos a partir da posição 2 até o final, lista[:2] retorna os elementos até a posição 2 (não inclusiva), lista[1:3] retorna os elementos das posições 1 e 2, lista[0:3:2] retorna os elementos nas posições 0 e 2, lista[::] retorna todos os elementos da lista, e lista[::-1] retorna todos os elementos em ordem reversa.