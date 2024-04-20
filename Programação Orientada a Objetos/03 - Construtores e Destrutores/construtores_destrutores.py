class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        print("Inicializando a classe...")
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Destruindo a classe...")

    def falar(self):
        print("Au Au")


def criar_cachorro():
    c2 = Cachorro("T-Rex", "Branco", False)
    print(c.nome)


c = Cachorro("Rex", "Marrom")
c.falar()