def exibir_mensagem():
    print("Olá mundo!")


def exibir_mensagem_2(nome):
    print(f"Seja bem vindo {nome}!")


def exibir_mensagem_3(nome="Anônimo"):
    print(f"Seja bem vindo {nome}!")


exibir_mensagem()
exibir_mensagem_2(nome="Guilherme")
exibir_mensagem_3()
exibir_mensagem_3(nome="Chappie")

# Explicando detalhes: A função exibir_mensagem não recebe argumentos e exibe a mensagem "Olá mundo!". A função exibir_mensagem_2 recebe um argumento nome e exibe a mensagem "Seja bem vindo" seguido do nome passado como argumento. A função exibir_mensagem_3 recebe um argumento nome com valor padrão "Anônimo" e exibe a mensagem "Seja bem vindo" seguido do nome passado como argumento ou "Anônimo" caso nenhum argumento seja passado.