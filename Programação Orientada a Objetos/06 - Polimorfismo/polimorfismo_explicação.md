## O que é Polimorfismo

A palavra **polimorfismo** significa ter muitas formas. Na programação, polimorfismo significa o mesmo nome de funçãoc (mas assinaturas diferentes) sendo usado para tipos diferentes.

### Exemplo:

``` python

len ("Python)
len ([10, 20, 30])

```

---
---
---

## Mesmo método com comportamento diferente

Na herança, a  classe filha hherda os métodos da classe Pai. No entanto, é possível modificar um método em uma classe filha herdada da classe Pai. Isso particularmente útil nos casos em que o método herdado da classe pai não se encaixa perfeitamente na classe filha.

### Exemplo:

``` Python 

class Passaro:
    def voar(self): pass

class Pardal(Passaro):
    def voar(self):
        print("Pardal voa")

class Avestruz(Passaro):
    def voar(self):
        print("Avestruz não voa")

def plano_de_voo(passaro):
    passaro.voar()

plano_de_voo(Pardal())
plano_de_voo(Avestruz())

```
---
---
---