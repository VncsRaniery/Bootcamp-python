matriz = [
    [1, "a", 2],
    ["b", 3, 4],
    [6, 5, "c"]
]

print(matriz[0])  # [1, "a", 2]
print(matriz[0][0])  # 1
print(matriz[0][-1])  # 2
print(matriz[-1][-1])  # "c"

# Explicando em detalhes: Uma matriz é uma estrutura de dados bidimensional, ou seja, uma tabela com linhas e colunas. Em Python, uma matriz pode ser representada como uma lista de listas. No exemplo acima, temos uma matriz 3x3, onde cada elemento é acessado utilizando dois índices: o primeiro índice indica a linha e o segundo índice indica a coluna. Portanto, matriz[0] retorna a primeira linha da matriz, matriz[0][0] retorna o primeiro elemento da primeira linha, matriz[0][-1] retorna o último elemento da primeira linha, e matriz[-1][-1] retorna o último elemento da última linha.