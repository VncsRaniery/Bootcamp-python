contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.items()  # dict_items([('guilherme@gmail.com', {'nome': 'Guilherme', 'telefone': '3333-2221'})])
print(resultado)

# Explicando detalhes: O método items() é utilizado para retornar uma visão dos itens de um dicionário. Neste exemplo, obtemos uma visão dos itens do dicionário de contatos.