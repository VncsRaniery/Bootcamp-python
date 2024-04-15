lista = [1, "Python", [40, 30, 20]]

l2 = lista.copy()

print(lista) # => [1, 'Python', [40, 30, 20]]

print(id(l2), id(lista)) # => 140071036008448 140071036008320

l2[0] = 2

print(lista) # => [1, 'Python', [40, 30, 20]]
print(l2) # => [2, 'Python', [40, 30, 20]]

# Explicando com detalhes o código acima: Temos uma lista chamada lista que contém três elementos: um inteiro, uma string e outra lista. Em seguida, criamos uma cópia dessa lista chamada l2. A função copy() cria uma cópia rasa da lista, ou seja, ela copia apenas a referência dos elementos da lista original. Portanto, se alterarmos um elemento da lista l2, a lista original não será afetada.