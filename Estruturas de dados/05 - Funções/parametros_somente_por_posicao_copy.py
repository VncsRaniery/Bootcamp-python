def criar_carro(modelo, ano, placa, /, marca, motor, combustivel):
    print(modelo, ano, placa, marca, motor, combustivel)


criar_carro("Palio", 1999, "ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")
criar_carro(modelo="Palio", ano=1999, placa="ABC-1234", marca="Fiat", motor="1.0", combustivel="Gasolina")  # inválido

# Explicando detalhes: A função criar_carro recebe três argumentos posicionais (modelo, ano e placa), um argumento somente por nome (marca) e dois argumentos somente por nome (motor e combustivel). Na chamada inválida, os argumentos modelo, ano e placa são passados como argumentos nomeados, o que não é permitido, pois eles são argumentos posicionais. Na chamada correta, os argumentos são passados na ordem correta, e os argumentos somente por nome são passados como argumentos nomeados.