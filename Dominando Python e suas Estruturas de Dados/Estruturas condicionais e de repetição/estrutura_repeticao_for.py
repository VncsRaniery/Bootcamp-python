texto = input('Digite um texto: ')
VOGAIS = 'aeiou'


#Exemplo utilizando um interável
for letra in texto:
    if letra.upper() in VOGAIS:
        print(letra, end="")


print() #Adiciona uma quebra de lnha

#===================================================================================================#

#Exemplo utilizando a função built-in range()
for numero in range(0, 51, 5):
    print(numero, end=" ")