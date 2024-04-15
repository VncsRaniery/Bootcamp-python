numeros = {1, 2, 3, 1, 2, 4, 5, 5, 6, 7, 8, 9, 0}

print(1 in numeros)  # True
print(10 in numeros)  # False

# Explicando detalhes: O operador in verifica se um elemento está presente em um conjunto. Se o elemento estiver presente, o operador retorna True, caso contrário, retorna False. Neste exemplo, o número 1 está presente no conjunto números, então o resultado é True. O número 10 não está presente, então o resultado é False. O operador in não modifica o conjunto original.