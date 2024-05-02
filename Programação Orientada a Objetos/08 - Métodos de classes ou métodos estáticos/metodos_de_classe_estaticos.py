class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    @classmethod
    def criar_de_data_nascimento(cls, ano, mes, dia, nome):
        idade = 2024 - ano
        return cls(nome, idade)
    
    @staticmethod
    def maior_idade(idade):
        return idade >= 18 

p = Pessoa.criar_de_data_nascimento(1987, 10, 10, "Vinícius")
print(p.nome, p.idade)

print(Pessoa.maior_idade(17))
print(Pessoa.maior_idade(18))