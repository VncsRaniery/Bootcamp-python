contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.pop("guilherme@gmail.com")  # {'nome': 'Guilherme', 'telefone': '3333-2221'}
print(resultado)

resultado = contatos.pop("guilherme@gmail.com", {})  # {}
print(resultado)

# Explicando detalhes: O método pop() é utilizado para remover um item de um dicionário e retornar o valor correspondente. Se a chave não existir, é possível fornecer um valor padrão para ser retornado. Neste exemplo, removemos o contato de Guilherme do dicionário de contatos e retornamos o valor associado a essa chave. Como a chave não existe mais no dicionário, o valor padrão fornecido é retornado.