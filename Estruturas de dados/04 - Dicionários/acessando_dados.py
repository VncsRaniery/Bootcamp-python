dados = {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}

print(dados["nome"])  # "Guilherme"
print(dados["idade"])  # 28
print(dados["telefone"])  # "3333-1234"

dados["nome"] = "Maria"
dados["idade"] = 18
dados["telefone"] = "9988-1781"

print(dados)  # {"nome": "Maria", "idade": 18, "telefone": "9988-1781"}

# Explicando detalhes: Para acessar os dados de um dicionário, utilizamos a chave correspondente entre colchetes. Neste exemplo, acessamos os valores associados às chaves "nome", "idade" e "telefone" no dicionário de dados. Também é possível alterar os valores associados a essas chaves, como demonstrado na segunda parte do código.