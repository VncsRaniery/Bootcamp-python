# Na condição AND = Para ser True tudo tem que ser True
# Na condição OR = Para ser True basta um ser True

print(True and True) 
print(True and False)
print(False and False)
print(False and True) 
print(True or True)
print(True or False) 

saldo = 500
saque = 300
limite = 1000
conta_especial =  true

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saque # True
print(exp)

exp_2 = (saldo >= saque) and (saque <= limite) or (conta_especial and saldo >= saque) # True
print(exp_2)