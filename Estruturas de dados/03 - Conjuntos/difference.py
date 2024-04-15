conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.difference(conjunto_b)
print(resultado)

resultado = conjunto_b.difference(conjunto_a)
print(resultado)

# Explicando detalhes: O método difference() retorna a diferença entre dois conjuntos, ou seja, um novo conjunto contendo os elementos que estão presentes no primeiro conjunto, mas não no segundo. Neste exemplo, o primeiro resultado contém o elemento 1, que está presente no conjunto A, mas não no conjunto B. O segundo resultado contém o elemento 4, que está presente no conjunto B, mas não no conjunto A. O método difference() não modifica os conjuntos originais, apenas retorna um novo conjunto com a diferença dos elementos.