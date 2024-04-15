numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(numeros)  # {1, 2, 3, 4, 5, 6, 7, 8, 9, 0}

numeros.discard(1)
numeros.discard(45)

print(numeros)  # {2, 3, 4, 5, 6, 7, 8, 9, 0}

# Explicando detalhes: O método discard() remove um elemento do conjunto, caso ele exista. Se o elemento não estiver presente, o conjunto permanece inalterado. Neste exemplo, o número 1 é removido do conjunto números, e o número 45 não é removido, pois não está presente. O conjunto resultante é {2, 3, 4, 5, 6, 7, 8, 9, 0}.