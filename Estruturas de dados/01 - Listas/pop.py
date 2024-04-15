linguagens = ["python", "js", "c", "java", "csharp"]

print(linguagens.pop())  # csharp
print(linguagens.pop())  # java
print(linguagens.pop())  # c
print(linguagens.pop(0))  # python

# Explicando em detalhes: A função pop() remove e retorna o último elemento da lista. Se um índice for passado como argumento, o elemento na posição especificada será removido e retornado. Se a lista estiver vazia, um erro será lançado.