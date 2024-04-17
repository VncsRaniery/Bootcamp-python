def somar(a, b):
    return a + b


def exibir_resultado(a, b, funcao):
    resultado = funcao(a, b)
    print(f"O resultado da operação {a} + {b} = {resultado}")


exibir_resultado(10, 10, somar)  # O resultado da operação 10 + 10 = 20

# Explicando detalhes: A função somar recebe dois argumentos a e b e retorna a soma dos dois valores. A função exibir_resultado recebe três argumentos a, b e funcao, onde funcao é uma função que será chamada com os argumentos a e b. A função exibir_resultado chama a função funcao com os argumentos a e b e exibe o resultado da operação.