pessoa = {"nome": "Guilherme", "idade": 28}
print(pessoa)

pessoa = dict(nome="Guilherme", idade=28)
print(pessoa)

pessoa["telefone"] = "3333-1234"  # {"nome": "Guilherme", "idade": 28, "telefone": "3333-1234"}
print(pessoa)

# Explicando detalhes: Dicionários são estruturas de dados que permitem armazenar pares de chave-valor. No Python, os dicionários são delimitados por chaves ({}) e os pares chave-valor são separados por vírgulas. Para criar um dicionário vazio, basta utilizar as chaves sem nenhum par de chave-valor. Também é possível utilizar a função dict() ou a sintaxe de dicionário literal para criar dicionários com valores iniciais. Neste exemplo, criamos um dicionário chamado pessoa com as chaves "nome" e "idade". Em seguida, adicionamos a chave "telefone" ao dicionário, associando o valor "3333-1234" a ela. O resultado final é um dicionário contendo as três chaves e seus respectivos valores.