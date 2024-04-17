def calcular_total(numeros):
    return sum(numeros)


def retorna_antecessor_e_sucessor(numero):
    antecessor = numero - 1
    sucessor = numero + 1

    return antecessor, sucessor


print(calcular_total([10, 20, 34]))  # 64
print(retorna_antecessor_e_sucessor(10))  # (9, 11)

# Explicando detalhes: A função calcular_total recebe uma lista de números e retorna a soma de todos os números. A função retorna_antecessor_e_sucessor recebe um número e retorna uma tupla contendo o antecessor e o sucessor do número passado como argumento.