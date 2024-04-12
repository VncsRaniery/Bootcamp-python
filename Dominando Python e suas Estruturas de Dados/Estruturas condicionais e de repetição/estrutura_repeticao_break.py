# Exemplo 1 - Utilizado para interromper a execução de um laço de repetição
while True:
    numero = int(input("Informe um número: "))

    if numero == 10:
        break

print(numero)


#Exemplo 2 - Utilizando o break em um laço de repetição for
for numero in range(100):

    if numero == 12:
        break

    print(numero, end=" ")
