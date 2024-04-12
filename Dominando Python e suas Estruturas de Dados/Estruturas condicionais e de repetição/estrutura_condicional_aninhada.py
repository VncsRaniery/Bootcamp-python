#Estrutura aninhada seria uma estrutura dentro de outra, como por exemplo, um if dentro de outro if. 

conta_normal = True
conta_universitaria = False

saldo = 500
saque = 100
cheque_especial = 450

if conta_normal:
    if saldo >= saque:
        print("Saque realizado com sucesso!")
    elif saldo <= (saldo + cheque_especial):
        print("Saque realizado com uso do cheque especial!")
    else:
        print("Não foi possível realizar o saque, Saldo insuficiente!")
elif conta_universitaria:
    if saldo >= saque:
        print("Saque realizado com sucesso!") 
    else:
        print("Saldo insuficiente para saque!")       