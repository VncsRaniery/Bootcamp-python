contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

resultado = contatos.keys()  # dict_keys(['guilherme@gmail.com'])
print(resultado)

# Explicando detalhes: O método keys() retorna uma visão das chaves presentes em um dicionário. Neste exemplo, o resultado é um objeto dict_keys contendo as chaves do dicionário de contatos. Essa visão pode ser utilizada para acessar as chaves do dicionário, mas não permite alterá-las diretamente.