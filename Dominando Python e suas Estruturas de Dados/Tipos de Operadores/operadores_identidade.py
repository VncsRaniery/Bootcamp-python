saldo = 1000
limite = 1000 

print(saldo is limite) # False
print(saldo is not limite) # True

# O operador is verifica se os dois operandos apontam para o mesmo objeto na memória. Isso acontece porque o Python armazena o valor 1000 em um objeto e ambos os operandos apontam para esse objeto.