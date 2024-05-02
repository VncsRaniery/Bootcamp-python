from abc import ABC, abstractmethod

class controleRemoto(ABC):
    @abstractmethod
    def ligar(self):
        pass

    @abstractmethod
    def desligar(self):
        pass

class controleTV(controleRemoto):
    def ligar(self):
        print("Ligando a TV")
        print("Ligado")

    def desligar(self):
        print("Desligando a TV")
        print("Desligado")



class controleArCondicionado(controleRemoto):
    def ligar(self):
        print("Ligando o ar condicionado")
        print("Ligado")

    def desligar(self):
        print("Desligando o ar condicionado")
        print("Desligado")
        


controle = controleTV()
controle.ligar()
controle.desligar()

controle = controleArCondicionado()
controle.ligar()
controle.desligar()