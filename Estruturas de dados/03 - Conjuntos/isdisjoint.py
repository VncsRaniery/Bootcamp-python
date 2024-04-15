conjunto_a = {1, 2, 3, 4, 5}
conjunto_b = {6, 7, 8, 9}
conjunto_c = {1, 0}

resultado = conjunto_a.isdisjoint(conjunto_b)  # True
print(resultado)

resultado = conjunto_a.isdisjoint(conjunto_c)  # False
print(resultado)

# Explicando detalhes: O método isdisjoint() verifica se dois conjuntos são disjuntos, ou seja, se não possuem elementos em comum. Se os conjuntos não tiverem elementos em comum, o método retorna True, caso contrário, retorna False. Neste exemplo, o primeiro resultado é True, pois os conjuntos A e B são disjuntos, não possuindo elementos em comum. O segundo resultado é False, pois os conjuntos A e C possuem o elemento 1 em comum. O método isdisjoint() não modifica os conjuntos originais, apenas verifica se eles são disjuntos. 