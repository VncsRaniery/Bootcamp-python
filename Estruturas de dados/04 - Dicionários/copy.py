contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

copia = contatos.copy()
copia["guilherme@gmail.com"] = {"nome": "Gui"}

print(contatos["guilherme@gmail.com"])  # {"nome": "Guilherme", "telefone": "3333-2221"}

print(copia["guilherme@gmail.com"])  # {"nome": "Gui"}

# Explicando detalhes: O método copy() é utilizado para criar uma cópia rasa de um dicionário. Isso significa que os valores do dicionário original são copiados para o novo dicionário, mas as referências aos objetos internos são mantidas. Neste exemplo, criamos uma cópia do dicionário de contatos e alteramos o nome de Guilherme na cópia, sem afetar o dicionário original.