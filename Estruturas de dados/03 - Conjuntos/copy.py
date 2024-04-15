sorteio = {1, 23}

print(sorteio)  # {1, 23}

sorteio.copy()

print(sorteio)  # {1, 23}

# Explicando detalhes: O método copy() é utilizado para criar uma cópia rasa de um conjunto. A cópia rasa é uma nova instância do conjunto original, contendo os mesmos elementos. Neste exemplo, o conjunto sorteio contém os elementos 1 e 23. Ao chamar o método copy(), uma cópia rasa do conjunto é criada, mas como não foi atribuída a uma variável, a cópia não é armazenada e o conjunto original não é modificado. Para armazenar a cópia, basta atribuí-la a uma nova variável, como por exemplo: novo_sorteio = sorteio.copy().