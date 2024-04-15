contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.popitem()  # ('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})
print(resultado)

# contatos.popitem()  # KeyError

# Explicando detalhes: O método popitem() é utilizado para remover e retornar um item arbitrário de um dicionário. O item retornado é uma tupla contendo a chave e o valor removidos. Se o dicionário estiver vazio, um KeyError será lançado. Neste exemplo, removemos um item do dicionário de contatos.