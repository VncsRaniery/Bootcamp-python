linguagens = ['Python', 'Java', 'C#', 'JavaScript', 'Ruby']

print(sorted(linguagens, key=lambda x: len(x))) # => ['C#', 'Java', 'JavaScript', 'Python', 'Ruby']
print(sorted(linguagens, key=lambda x: len(x), reverse=True)) # => ['JavaScript', 'Python', 'Ruby', 'Java', 'C#']

# A fu nção sorted() retorna uma nova lista ordenada a partir dos elementos da lista original. O argumento key é uma função que será aplicada a cada elemento da lista para definir a ordem de classificação. O argumento reverse é um booleano que indica se a lista deve ser ordenada em ordem decrescente.