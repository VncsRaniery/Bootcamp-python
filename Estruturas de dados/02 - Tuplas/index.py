linguagens = ("python", "js", "c", "java", "csharp",)

print(linguagens.index("java"))  # 3
print(linguagens.index("python"))  # 0

# Explicando detalhes: A função index() retorna o índice do primeiro elemento encontrado na tupla. Se o elemento não existir, um erro será lançado.