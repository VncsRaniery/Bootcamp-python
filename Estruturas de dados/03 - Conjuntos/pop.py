numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {0, 1, 2, 3, 4, 5, 6, 7, 8, 9}
print(numeros.pop())  # 0
print(numeros.pop())  # 1
print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9}

# Explicando detalhes: O método pop() remove e retorna um elemento aleatório do conjunto. Como os conjuntos não possuem ordem, não é possível prever qual elemento será removido. Neste exemplo, os elementos 0 e 1 são removidos do conjunto números, e o conjunto resultante é {2, 3, 4, 5, 6, 7, 8, 9}. Se o conjunto estiver vazio, uma exceção do tipo KeyError será lançada.