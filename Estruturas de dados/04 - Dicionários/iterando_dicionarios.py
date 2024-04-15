contatos = {
    "guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"},
    "giovanna@gmail.com": {"nome": "Giovanna", "telefone": "3443-2121"},
    "chappie@gmail.com": {"nome": "Chappie", "telefone": "3344-9871"},
    "melaine@gmail.com": {"nome": "Melaine", "telefone": "3333-7766"},
}

for chave in contatos:
    print(chave, contatos[chave])

print("=" * 100)

for chave, valor in contatos.items():
    print(chave, valor)

# Explicando detalhes: Podemos iterar sobre um dicionário utilizando um laço for. No primeiro exemplo, iteramos sobre as chaves do dicionário e imprimimos a chave e o valor associado a ela. No segundo exemplo, utilizamos o método items() para obter uma visão dos itens do dicionário e iteramos sobre essa visão, imprimindo a chave e o valor associado a ela.