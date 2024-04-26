class Pessoa ():
    def __init__(self, nome, idade):
        self.nome = nome
        self.__idade = idade

    @property
    def idade(self):
        __ano_atual = 2024
        return self.__idade - self.__ano_atual
    

pessoa = Pessoa("João", 1995)
print(f"Nome: {pessoa.nome} \t Idade: {pessoa.data_nascimento} anos")
print(f"Nome: {pessoa.get_nome()} \t Idade: {pessoa.get_data_nascimento()} anos")




    