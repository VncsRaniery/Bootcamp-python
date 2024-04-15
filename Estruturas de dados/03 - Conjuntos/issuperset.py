conjunto_a = {1, 2, 3}
conjunto_b = {4, 1, 2, 5, 6, 3}

resultado = conjunto_a.issuperset(conjunto_b)  # False
print(resultado)

resultado = conjunto_b.issuperset(conjunto_a)  # True
print(resultado)

# Explicando detalhes: O método issuperset() verifica se um conjunto é superconjunto de outro, retornando True se todos os elementos do segundo conjunto estão presentes no primeiro, e False caso contrário. Neste exemplo, o primeiro resultado é False, pois o conjunto A não é superconjunto do conjunto B, já que B possui elementos que não estão presentes em A. O segundo resultado é True, pois o conjunto B é superconjunto do conjunto A, já que todos os elementos de A estão presentes em B. O método issuperset() não modifica os conjuntos originais, apenas verifica se um é superconjunto do outro.