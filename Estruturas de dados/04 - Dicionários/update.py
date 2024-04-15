contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

contatos.update({"guilherme@gmail.com": {"nome": "Gui"}})
print(contatos)  # {'guilherme@gmail.com': {'nome': 'Gui'}}

contatos.update({"giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3322-8181"}})
# {'guilherme@gmail.com': {'nome': 'Gui'}, 'giovanna@gmail.com': {'nome': 'Giovanna', 'telefone': '3322-8181'}}
print(contatos)

# Explicando detalhes: O método update() é utilizado para adicionar ou atualizar itens em um dicionário. Se a chave já existir, o valor correspondente será atualizado. Caso contrário, um novo item será adicionado ao dicionário. Neste exemplo, o contato de Guilherme é atualizado com o nome "Gui" e um novo contato de Giovanna é adicionado ao dicionário.