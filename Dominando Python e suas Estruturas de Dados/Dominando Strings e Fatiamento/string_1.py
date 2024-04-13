#Exemplo 1

nome = "vinicius"

print(nome.upper()) # Isso seria um método de uma string em Python que transforma todas as letras em maiúsculas.
print(nome.lower()) # Isso seria um método de uma string em Python que transforma todas as letras em minúsculas.
print(nome.title()) # Isso seria um método de uma string em Python que transforma a primeira letra de cada palavra em maiúscula.



#Exemplo 2

texto = "   Olá Mundo!    "

print(texto + ".") # Isso seria um método de uma string em Python que remove os espaços em branco do início e do final da string.
print(texto.strip() + ".") # Isso seria um método de uma string em Python que remove os espaços em branco do início e do final da string.
print(texto.lstrip() + ".") # Isso seria um método de uma string em Python que remove os espaços em branco do início da string.
print(texto.rstrip() + ".") # Isso seria um método de uma string em Python que remove os espaços em branco do final da string.



#Exemplo 3

menu = "python"

print("####" + menu + "####") # Isso seria um método de uma string em Python que adiciona caracteres no início e no final da string.
print(menu.center(14)) # Isso seria um método de uma string em Python que adiciona caracteres no início e no final da string.
print(menu.center(14, "#")) # Isso seria um método de uma string em Python que adiciona caracteres no início e no final da string.
print("P-y-t-h-o-n") # Isso seria um método de uma string em Python que adiciona caracteres entre cada letra da string.
print("-".join(menu)) # Isso seria um método de uma string em Python que adiciona caracteres entre cada letra da string.