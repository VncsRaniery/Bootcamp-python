class veiculo:
    def __init__(self, modelo, ano, cor):
        self.modelo = modelo
        self.placa = placa
        self.ano = ano
        self.cor = cor

    def ligar_motor(self):
        print("Motor ligado")
    pass

class motocicleta(veiculo):
    pass

class carro(veiculo):
    pass

class caminhao(veiculo):
    pass

moto = motocicleta("CG 125", "ABC-1234", 2018, "Vermelha")
moto.ligar_motor()

carro = carro("Gol", "DEF-5678", 2019, "Preto")
carro.ligar_motor()

caminhao = caminhao("Volvo", "GHI-9101", 2020, "Branco")
caminhao.ligar_motor()

