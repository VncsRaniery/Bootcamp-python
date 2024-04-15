conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issubset(conjunto_b)  # True
print(resultado)

resultado = conjunto_b.issubset(conjunto_a)  # False
print(resultado)

# Explicando detalhes: O método issubset() verifica se um conjunto é subconjunto de outro, retornando True se todos os elementos do primeiro conjunto estão presentes no segundo, e False caso contrário. Neste exemplo, o primeiro resultado é True, pois o conjunto A é subconjunto do conjunto B, já que todos os elementos de A estão presentes em B. O segundo resultado é False, pois o conjunto B não é subconjunto do conjunto A, já que B possui elementos que não estão presentes em A. O método issubset() não modifica os conjuntos originais, apenas verifica se um é subconjunto do outro.