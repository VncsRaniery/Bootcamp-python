tupla = ("p", "y", "t", "h", "o", "n")

print(tupla[2:]) # => ('t', 'h', 'o', 'n')
print(tupla[:2]) # => ('p', 'y')
print(tupla[1:3]) # => ('y', 't')
print(tupla[0:3:2]) # => ('p', 't')
print(tupla[::]) # => ('p', 'y', 't', 'h', 'o', 'n')
print(tupla[::-1]) # => ('n', 'o', 'h', 't', 'y', 'p')

# A tupla é uma estrutura de dados semelhante a lista, porém, imutável. Portanto, não é possível adicionar, remover ou alterar elementos de uma tupla. O fatiamento de tuplas funciona da mesma forma que o fatiamento de listas.