contato = {"nome": "Guilherme", "telefone": "3333-2221"}

contato.setdefault("nome", "Giovanna")  # "Guilherme"
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221'}

contato.setdefault("idade", 28)  # 28
print(contato)  # {'nome': 'Guilherme', 'telefone': '3333-2221', 'idade': 28}

# Explicando detalhes: O método setdefault() é utilizado para definir um valor padrão para uma chave em um dicionário. Se a chave já existir, o valor correspondente não será alterado. Caso contrário, um novo item será adicionado ao dicionário com o valor padrão especificado. Neste exemplo, definimos o valor padrão "Giovanna" para a chave "nome" e 28 para a chave "idade" no dicionário de contatos. Como a chave "nome" já existe, o valor correspondente não é alterado, mas a chave "idade" é adicionada com o valor 28.