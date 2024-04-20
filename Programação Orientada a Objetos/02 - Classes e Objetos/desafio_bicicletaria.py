class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor
        self.marcha = 2

    def buzinar(self):
        print('BIBI')

    def parar(self):
        print('Freando...')
        print('Bicicleta parada')

    def correr(self):
        print('Pedalando...')
        print('Bicicleta em movimento')

    def trocar_marcha(self, nro_marcha):
        print('Trocando marcha...')

        def _trocar_marcha(nro_marcha):
            if nro_marcha > self.marcha:
                print("Marcha Trocada...")
            else:
                print("Não foi possível trocar a marcha...")

    def __str__(self):
        return f'Bicicleta {self.cor} {self.modelo} {self.ano} {self.valor}' #Retornar atributos da classe, porém a cada modificação no código, o retorno do método __str__ terá que ser modificado.
    
    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave} = {valor}' for chave, valor in self.__dict__])}" #Retornar atributos da classe indepensente de modificações feitas no código posteriormente. 


B1 = Bicicleta('vermelha', 'Caloi', 2020, 1000)
B1.buzinar()
B1.parar()
B1.correr()

print(B1.cor, B1.modelo, B1.ano, B1.valor) #Acessar atributos pelo print


B2 = Bicicleta('azul', 'Monark', 2021, 1500) #Instanciar outro objeto
Bicicleta.buzinar(B2) #Acessar método sem instanciar