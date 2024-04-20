# Orientação a Objetos em Python

A **Orientação a Objetos** é um paradigma de programação que fornece meios de estruturar programas para que as propriedades e os comportamentos sejam agrupados em objetos individuais.

Por exemplo, um objeto pode representar uma pessoa com propriedades como nome, idade e endereço e comportamentos como andar, falar, respirar e correr. Ou um e-mail com propriedades como lista de destinatários, assunto, corpo e comportamentos como adicionar anexos e enviar.

## Classe

Uma **classe** é um código que especifica as propriedades e comportamentos de um objeto. É como um modelo ou plano para criar um objeto.

```python
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def falar(self, mensagem):
        print(f'{self.nome} diz: {mensagem}')
```

# Objeto
Um **objeto** é uma instância de uma classe. Um objeto tem um estado e comportamentos definidos pela sua classe.

```Python
pessoa1 = Pessoa('João', 30)
pessoa1.falar('Olá, mundo!')
```

# Herança
A **herança** é um mecanismo que permite que uma nova classe herde as propriedades e comportamentos de uma classe existente.

```Python
class Empregado(Pessoa):
    def __init__(self, nome, idade, salario):
        super().__init__(nome, idade)
        self.salario = salario

    def trabalhar(self):
        print(f'{self.nome} está trabalhando.')
```

# Encapsulamento
O **encapsulamento** é um mecanismo que restringe o acesso direto a alguns componentes do objeto e permite o acesso apenas através de métodos.

```Python
class Pessoa:
    def __init__(self, nome, idade):
        self.__nome = nome
        self.__idade = idade

    def get_nome(self):
        return self.__nome

    def get_idade(self):
        return self.__idade
```

# Polimorfismo
O **polimorfismo** é um princípio que permite que uma interface represente diferentes tipos de ações.

```Python
class Gato:
    def falar(self):
        return 'Miau!'

class Cachorro:
    def falar(self):
        return 'Au au!'

def fazer_falar(animal):
    print(animal.falar())

gato = Gato()
cachorro = Cachorro()

fazer_falar(gato)
fazer_falar(cachorro)
```