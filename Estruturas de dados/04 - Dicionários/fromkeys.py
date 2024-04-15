resultado = dict.fromkeys(["nome", "telefone"])  # {"nome": None, "telefone": None}
print(resultado)

resultado = dict.fromkeys(["nome", "telefone"], "vazio")  # {"nome": "vazio", "telefone": "vazio"}
print(resultado)

# Explicando detalhes: O método fromkeys() é utilizado para criar um novo dicionário a partir de uma sequência de chaves. O primeiro argumento é a sequência de chaves que serão utilizadas no novo dicionário. O segundo argumento é o valor padrão que será associado a cada chave. Se o segundo argumento não for fornecido, o valor padrão será None. Neste exemplo, criamos um novo dicionário com as chaves "nome" e "telefone", associando o valor "vazio" a cada uma delas.