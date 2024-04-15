contatos = {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}}

# contatos["chave"]  # KeyError

resultado = contatos.get("chave")  # None
print(resultado)

resultado = contatos.get("chave", {})  # {}
print(resultado)

resultado = contatos.get(
    "guilherme@gmail.com", {}
)  # {"guilherme@gmail.com": {"nome": "Guilherme", "telefone": "3333-2221"}
print(resultado)

# Explicando detalhes: O método get() é utilizado para acessar um valor em um dicionário a partir de uma chave. Se a chave não existir, o método retorna None. É possível fornecer um valor padrão para ser retornado caso a chave não exista. Neste exemplo, tentamos acessar um valor com a chave "chave", que não existe no dicionário de contatos. O método get() retorna None. Em seguida, tentamos acessar um valor com a chave "chave", fornecendo um valor padrão vazio. O método get() retorna o valor padrão. Por fim, acessamos um valor com a chave "