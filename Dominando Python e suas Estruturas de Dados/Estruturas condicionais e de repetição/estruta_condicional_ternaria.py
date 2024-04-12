#   Estrutura condional ternária é uma forma simplificada de escrever uma estrutura condicional. 

saldo = 2000
saque = 500

status = "Sucesso" if saldo >= saque else "Falha"

print(f"{status} ao realizar o saque!")