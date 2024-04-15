conjunto_a = {1, 2, 3}
conjunto_b = {2, 3, 4}

resultado = conjunto_a.symmetric_difference(conjunto_b)
print(resultado)

# Explicando detalhes: O método symmetric_difference() retorna a diferença simétrica entre dois conjuntos, ou seja, um novo conjunto contendo os elementos que estão presentes em apenas um dos conjuntos. Neste exemplo, o conjunto resultado contém os elementos 1 e 4, que estão presentes apenas nos conjuntos A e B, respectivamente. O método symmetric_difference() não modifica os conjuntos originais, apenas retorna um novo conjunto com a diferença simétrica dos elementos.