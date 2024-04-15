sorteio = {1, 23}

sorteio.add(25)  # {1, 23, 25}
print(sorteio)

sorteio.add(42)  # {1, 23, 25, 42}
print(sorteio)

sorteio.add(25)  # {1, 23, 25, 42}
print(sorteio)

# Explicando detalhes: O método add() é utilizado para adicionar um novo elemento a um conjunto. Se o elemento já estiver presente no conjunto, ele não será adicionado novamente. Neste exemplo, o conjunto sorteio contém os elementos 1 e 23. Ao adicionar o elemento 25, o conjunto passa a conter os elementos 1, 23 e 25. Em seguida, o elemento 42 é adicionado, resultando no conjunto {1, 23, 25, 42}. Por fim, ao tentar adicionar novamente o elemento 25, como ele já está presente no conjunto, não ocorre nenhuma alteração no conjunto final.