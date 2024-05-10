# Gerenciamento de pacotes e Boas Práticas

## Objetivo Geral 

Aprender a trabalhar com gerenciamento de pacotes em Python, e boas práticas de codificação seguindo as convenções da PEP 8.

## O que são pacotes em Python?

Pacotes são módulos que podem ser instalados e utilizados em seus programas Python. Eles permitem que você utilize código que foi escrito por outras pessoas, economizando tempo e esforço.

## O papel do pip

Pip é o gerenciador de pacotes do Python. Eles nos permite instalar, atualizar e remover facilmente. Ele se ccomunica com o PyPl (Python Package Index), que é onde a maioria dos pacotes Python são armazenados.

### Exemplo de código:

``` Python

pip install numpy
pip uninstall numpy
pip list

```

## Uso de ambientes virtuais

Ambientes virtuais, como os criadores por venvs, nos permitem manter as dependências de diferentes projetos. Isso é importante para evitar conflitos entre versões de pacotes.

### Exemplo de código:

``` Python 

Python3 -m venv myenv
source myenv/bin/activate

```

## Comandos do pip

Como um programador que está aprendendo Python e deseja gerenciar os pacotes do seu projeto, é importante conhecer alguns dos principais comandos do pip.

``` Python

# Instalar um pacote
pip install nome_do_pacote

# Desinstalar um pacote
pip uninstall nome_do_pacote

# Listar pacotes instalados
pip list

# Atualizar um pacote
pip install --upgrade nome_do_pacote

# Procurar por pacotes
pip search termo_de_busca

``` 

## Introdução ao pipenv

Pipenv é uma ferramenta de gerenciamento de pacotes que combina a gestão de dependências com a criação de ambiente virtual para seus projetos e adiciona/remove pacotes automaticamente do arquivo Pipfile conforme você instala e desinstala pacotes.

### Comandos do pipenv

``` Python

pip install pipenv
pipenv install numpy
pipenv uninstall numpy
pipenv lock

``` 

## Introdução ao poetry

Poetry é outra ferramenta de gerenciamento de dependências para Python que permite declarar as bibliotecas de que seu projeto depende e gerencia (instala/atualiza/remove) essas bibliotecas para você. Ela também suporta o empacotamento e a publicação de projetos no PyPI.

### Comandos do poetry:

``` Python

pip install poetry
poetry new myproject 
cd myproject
poetry add numpy
poetry remove numpy

```

---
---
---

# Boas práticas em Python

## Introdução

Python tem uma série de convenções e melhores práticas codificadas em PEPs (Propostas de Melhoria do Python). A mais conhecida destas é provavelmente a PEP 8, que cobre o estilo de codificação.

## Principais recomendações da PEP 8 

Algumas das principais recomendações da PEP 8 incluem usar 4 espaços para a identificação. limitar as linhas a 79 caracteres, usar nomes de variáveis em snake_case para funções e variáveis, e CamelCase para classes.

### Exemplo de código:

``` Python

def somar(argumento_1, argumento_2):
    # Esta é uma função de exemplo seguindo a PEP 8
    pass

class ContaBancaria:
    # Esta é uma classe de exemplo seguindo a PEP 8
    pass

``` 

## Uso de ferramentas de checagem de estilo

Para nos ajudar a seguir as recomendações de PEP 8, podemos usar ferramentas de checagem de estilo como flake8. Essas ferramentas verificam nosso código e nos informam onde estamos desviando do guia de estilo.

### Exemplo de código:

``` Python

pip install flake8
flake8 meu_script.py

```

## Formatação automática de código

Black é uma ferramenta de formatação de código Python que segue a filosofia "formato único". Black reformata todo o seu arquivo em um estilo consistente, simplificando a tarefa de manter o código em conformidade com a PEP 8.

## Organização de imports com isort

Isort é uma ferramenta Python para classificar importações alfabeticamente e separá-las automaticamente em seções. Ele proporciona uma maneira rápida e fácil de ordenar e categorizar suas importações.

### Exemplo de código:

``` Python

pip install isort
isort meu_script.py

```


