salario = 2000


def salario_bonus(bonus):
    global salario
    salario += bonus
    return salario


salario_bonus(500)  # 2500

# Explicando detalhes: A função salario_bonus recebe um argumento bonus e utiliza a palavra-chave global para acessar a variável salario definida fora da função. O valor do bônus é somado ao valor do salário, e o novo valor é retornado. A função é chamada com o argumento 500, e o valor do salário é atualizado para 2500.