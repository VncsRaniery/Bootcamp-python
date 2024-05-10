## Porque precisamos manipular arquivos?

Os arquivos são essenciais para qualquer tipo de programação, pois fornecem um meio de armazenar e recuperar dados. Através da manipulação de arquivos, podemos persistir os dados além da vida útil de um programa específico.

## Conceito de arquivo em informática

Um arquivo é um container no computador onde as informações são armazenadas em formato digital. Existem dois tipos de arquivos que podemos manipular em Python: arquivos de texto e arquivos binários.

## Porque precisamos manipular arquivos?

Para manipular arquivos em Python, primeiro precisamos abri-los. Usamos a função `Open()` para isso. Quando terminamos de trabalhar com o arquivo, usamos a função `close()` para liberar recursos

### Exemplo de Código

``` Python

file = open("exempla.txt", "r")
# ... fazemos aalgo com o arquivo ...
file.close()

```

## Modos de aberturas de arquivo

Existem diferentes modos para abrir um arquivo, como somente leitura ('r'), gravação ('w') e anexar ('a'). O modo de abertura deve ser escolhido de acordo com a operação que iremos realizar no mesmo.

### Exemplo de Código

``` Python

# Para ler um arquivo
file = open('example.txt', 'r')

# Para escrever em um arquivo
file = open('example.txt', 'w')

# Para anexar conteúdo a um arquivo existente
file = open('example.txt', 'a')

```
---
---
---

# Lendo um arquivo 

## Introdução

Python fornece várias maneiras de ler um arquivo. Podemos usar `read()`, `readline()` ou `readlines()` dependendo de nossas necessidades.

### Método read:

``` Python

# Ler todo o conteúdo do arquivo de uma vez
file = open('example.txt', 'r')
print(file.read())
file.close()

```

### Método readline e readlines

O método `readline()` lê uma linha por vez, enquanto `readlines()` retorna uma lista onde cada elemento é uma linha do arquivo. 

---
---
---

# Escrita

## Introdução 

Podemos usar `write()` ou `writelines()` para escrever em um arquivo. Lembre-se, no entanto, de abrir o arquivo no modo correto.

### Exemplo de Código

``` Python 

file = open('example.txt', 'w')
file.write("Olá, mundo!")
file.close

``` 

---
---
---

# Gerenciando arquivos e diretórios

## Introdução 

Python também foferece funções para gerenciar arquivos e diretórios. Podemos criar, renomear e excluir arquivos e diretórios usando os módulos `os` e `shutil`.

### Exemplo de Código:

``` Python

import os
import shutil

# Criar um diretório 
os.mkdir("exemplo")

# Renomear um arquivo
os.rename("old.txt", "new.txt")

# Remover um arquivo
os.remove("unwanted.txt")

# Mover um arquivo
shutil.move("source.txt", "destination.txt")

```

---
---
---

# Tratamento de exceções em mmanipulação de arquivos

## Introdução 

Tratar erros é uma parte importante da manipulação de arquivos. Python oferece uma variedade de exceções que nos permitem lidar com erros comuns.

## Exceções mais comuns

- **FileNotFoundError:** Lançada quando o arquivo que está sendo aberto não pode ser encontrado no diretório especificado. 
- **PermissionError:** Lançada quando ocorre uma tentativa de abrir um arquivo sem as permissões adequadas para leitura ou gravação.
- **IOError:** Lançada quando ocorre um erro geral de E/S (Entrada/Saída) aao trabalhar com o arquivo, como problemas de permissão, falta de espaço em disco, entre outros.
- **UnicodeDecodeError:** Lançada quando ocorre um erro ao tentar decodificar os dados de um arquivo de texto usando uma codificação inadequada.
- **UnicodeEncodeError:** Lançada quando ocorre um erro ao tentar codificar dados em uma determinada codificação ao gravar em um arquivo de texto.
- **IsADirectoryError:** Lançada quando é feita uma tentativa de abrir um diretório em vez de um arquivo de texto.

### Exemplo de Código;

``` Python

try:
    file = open('non_existent_file.txt', 'r')
except FileNotFoundError:
    print("Arquivo não encontrado.")

```

---
---
---

# Boas práticas na manipulação de arquivos

## Introdução

Ao manipular arquivos em Python existem algumas boas práticas que podemos seguir, vamos aordar as principais.

## Bloco With

Use o gerenciammento de contexto (context manager) com a declaração `with()`. O gerenciamento de contexto permite trabalhar com arquivos de forma segura, garantindo que eles sejam fechados corretamente, mesmo em caso de exceções.

### Exemplo de Código:

``` Python

with open('arquivo.txt', 'r') as arquivo:
    # Faça aoperações de leitura/gravação no arquivo

```

## Verifique se o arquivo foi aberto com sucesso

É recomendado verificar se o arquivo foi aberto corretamente antes de executar operações de leitura ou gravação nele.

### Exemplo de Código:

``` Python

try:
    with open('arquivo.txt', 'r') as arquivo:
        # Faça operações de leitura/gravação no arquivo
except IOError:
    print('Não foi possível abrir o arquivo.')

```

## Use a codificação correta

Certifique-se de usar a codificação correta ao ler ou gravar arquivos de texxto. O argumento `encoding()` da função `open()` permite especificar a codificação.

### Exemplo de Código:

``` Python 

with open('arquivo.txt', 'r', encoding='utf-8') as arquivo:
    # Operações de leitura com codificação UTF-8

with open('arquivo.txt', 'w', encoding='utf-8') as arquivo:
    # Operações de escrita com codificação UTF-8

```

---
---
---

# Trabalhando com arquivos CSV

## Introdução 

Vamos aprender sobre arquivos CSV, um formato de arquivo amplamente utilizado para armazenar dados tabulares. CSV é a sigla para 'Coma Separated Values'.

## Lendo arquivos CSV

Python fornece um módulo chamado 'csv' para lidar facilmente com arquivos CSV.

### Exemplo de código:

``` Python

import csv

eith open('example.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

```

``` Python

import csv

eith open('example.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["nome", "idade"])
    writer.writerow(["Ana", 30])
    writer.writerow(["João", 25])

```

## Práticas recomendadas

- Usar csv.reader e csv.writer para manipular arquivos CSV.
- Fazer o tratamento correto das exceções.
- Ao gravar arquivos CSV definir o argumento newline=" no método `open()`.
