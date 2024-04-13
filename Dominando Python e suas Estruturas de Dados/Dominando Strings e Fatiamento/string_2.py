nome = "Vinícius"
idade = 18
profissao = "Programador"
linguagem = "Python"

dados = {"nome" : "Vinícius", "idade" : 18, "profissao" : "Programador", "linguagem" : "Python"}


# Exemplo 1
print("Nome: %s Idade: %d" % (nome, idade)) 
# Explicando o código: O %s é um marcador de posição para strings e o %d é um marcador de posição para números inteiros. O % é um operador de formatação de string que permite que você insira valores em strings. O % (nome, idade) é uma tupla que contém os valores que você deseja inserir na string. O % é um operador de formatação de string que permite que você insira valores em strings. O % (nome, idade) é uma tupla que contém os valores que você deseja inserir na string.



#Exemplo 2
print("Nome: {} Idade: {}" .format(nome, idade)) 
# Explicando o código: As chaves {} são marcadores de posição para strings. O .format(nome, idade) é um método de formatação de string que permite que você insira valores em strings. O .format(nome, idade) é uma tupla que contém os valores que você deseja inserir na string.



#Exemplo 3
print("Nome: {1} Idade: {0} Nome: {1} {1}" .format(idade, nome)) 
# Explicando o código: As chaves {} são marcadores de posição para strings. O .format(idade, nome) é um método de formatação de string que permite que você insira valores em strings. O .format(idade, nome) é uma tupla que contém os valores que você deseja inserir na string. O {1} e o {0} são índices que indicam a posição dos valores na tupla. O {1} e o {0} são índices que indicam a posição dos valores na tupla.



#Exemplo 4
print("Nome: {nome} Idade: {idade}" .format(nome=nome, idade=idade)) 
# Explicando o código: As chaves {} são marcadores de posição para strings. O .format(nome=nome, idade=idade) é um método de formatação de string que permite que você insira valores em strings. O .format(nome=nome, idade=idade) é um dicionário que contém os valores que você deseja inserir na string. O {nome} e o {idade} são chaves que indicam os valores no dicionário.
print("Nome: {name} Idade: {age}" .format(age=idade, name=nome)) 
# Explicando o código: As chaves {} são marcadores de posição para strings. O .format(age=idade, name=nome) é um método de formatação de string que permite que você insira valores em strings. O .format(age=idade, name=nome) é um dicionário que contém os valores que você deseja inserir na string. O {name} e o {age} são chaves que indicam os valores no dicionário.



#Exemplo 5
print("Nome: {nome} Idade: {idade}" .format(**dados)) 
# Explicando o código: As chaves {} são marcadores de posição para strings. O .format(**dados) é um método de formatação de string que permite que você insira valores em strings. O .format(**dados) é um dicionário que contém os valores que você deseja inserir na string. O {nome} e o {idade} são chaves que indicam os valores no dicionário.



#Exemplo 6
print(f"nome: {nome} Idade: {idade}") 
# Explicando o código: As chaves {} são marcadores de posição para strings. O f é um prefixo que indica que a string é uma f-string