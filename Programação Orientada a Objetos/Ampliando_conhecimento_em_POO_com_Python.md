## Atributos do Objeto

Todos os objetos nascem com o mesmo número de atributos de classe e de instância. Atributos de instância são diferentespara cada obejto (cada objeto tem uma cópia), já os atributos de classe são compartilhados entre os objetos.

# Exemplo:

``` Python

class Estudante:
    escola = "DIO"

    def __init__(self, nome, numero):
        self.nome = nome
        self.numero = numero

    def __str__(self):
        return f"{self.nome} ({self.numero}) - {self.escola}"

gui = Estudante("Guilherme", 56451)
gi = Estudante("Giovana", 17323)

```

## Métodos de classe

Métodos de classes estão ligados à classe e não ao objeto. Eles têm acesso ao estado de classe, pois recebem um parâmetro que aponta para a classe e não para a instância do objeto.

## Métodos estáticos

Um método estático nãao recebe um primeiro argumento explícito. Ele também é um método vinculado à classe e não ao objeto da classe. Este método não pode acessar ou modificar o estado da classe. Ele está presente em uma classe porque faz sentindo que o método esteja presente na classe.

## Métodos de classe X Métodos estáticos

* Um método de classe recebe um primeiro parâmetro que aponta para a classe, enquanto um método estático não.
* Um método de classe pode acessar ou modificar o estado da classe enquanto um método estático não pode acessá-lo ou modificá-lo

## Quando utilizar método de classe ou estático 

* Geralmente usamos o método de classes para criar métodos de fábrica.
* Geralmente usamos método estáticos para criar funções utilitárias.

# O que são interfaces?

Obs: Interface definem o que uma classe deve fazer e não como.

# Python tem interface?

O conceito de interface é definir um contrato, onde são declarados os métodos (o que deve ser feito) e suas respectivas assinaturas. Em Python utilizamos classes abstratas para criar contratos. Classes abstratas não podem ser instanciadas.

# Criando Classes abstratas utilizando o módulo ABC

## ABC

Por padrão, o Python não fornece classes abstratas. O Python vem com um módulo que fornece a base para definir as classes abstratas, e o nome do módulo é ABC. O ABC funciona decorando os métodos da classe base como abstratos e, em seguida, registrando classes concretas como implementações de base abstrata. Um método se torna abstrato quando decorado com **@abstractmethod**.