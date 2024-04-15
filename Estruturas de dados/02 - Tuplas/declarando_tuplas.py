frutas = (
    "laranja",
    "pera",
    "uva",
)
print(frutas)

letras = tuple("python")
print(letras)

numeros = tuple([1, 2, 3, 4])
print(numeros)

pais = ("Brasil",)
print(pais)

# Explicando em detalhes: Uma tupla é uma estrutura de dados semelhante a uma lista, mas imutável, ou seja, seus elementos não podem ser alterados após a criação da tupla. Em Python, uma tupla é representada por uma sequência de valores separados por vírgulas, e opcionalmente entre parênteses. No exemplo acima, temos quatro tuplas: frutas, letras, numeros e pais. A tupla frutas contém três elementos: laranja, pera e uva. A tupla letras contém seis elementos: p, y, t, h, o e n. A tupla numeros contém quatro elementos: 1, 2, 3 e 4. A tupla pais contém um único elemento: Brasil. Note que, para criar uma tupla com um único elemento, é necessário incluir uma vírgula após o valor, como em pais = ("Brasil",). Caso contrário, o Python interpretará o valor entre parênteses como um simples valor, e não como uma tupla.