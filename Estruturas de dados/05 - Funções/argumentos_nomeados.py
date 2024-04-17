def salvar_carro(marca, modelo, ano, placa):
    # salva carro no banco de dados...
    print(f"Carro inserido com sucesso! {marca}/{modelo}/{ano}/{placa}")


salvar_carro("Fiat", "Palio", 1999, "ABC-1234")
salvar_carro(marca="Fiat", modelo="Palio", ano=1999, placa="ABC-1234")
salvar_carro(**{"marca": "Fiat", "modelo": "Palio", "ano": 1999, "placa": "ABC-1234"})

# Explicando detalhes: A função salvar_carro recebe quatro argumentos obrigatórios: marca, modelo, ano e placa. Na primeira chamada, os argumentos são passados na ordem correta. Na segunda chamada, os argumentos são passados com seus respectivos nomes. Na terceira chamada, os argumentos são passados como um dicionário, e o operador ** é utilizado para desempacotar o dicionário e passar seus itens como argumentos nomeados.