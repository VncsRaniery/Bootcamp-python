contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

telefone = contatos["giovanna@gmail.com"]["telefone"]  # "3443-2121"
print(telefone)

# Explicando detalhes: Dicionários aninhados são dicionários que possuem outros dicionários como valores. Neste exemplo, o dicionário de contatos possui e-mails como chaves e, para cada e-mail, um dicionário com informações de nome e telefone. Para acessar o telefone de Giovanna, utilizamos a chave "