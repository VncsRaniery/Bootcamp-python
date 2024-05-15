# Modelagem de Dados Relacionais - Tabelas, Colunas e Registros

## Tabelas

Ela é usada para armazenar dados de forma organizada. Cada tabela em um banco de dados relacional tem um nome único e é dividida em colunas e linhas.

## Colunas

Uma coluna é uma estrutura dentro de uma tabela que representa um atributo específico dos dados armazenados. Cada coluna tem um nome único e umm tipo de dados associado que define o tipo de informação que pode ser armazenado nela, como números, textos, datas, etc.

## Registros

Um registro, também conhecido como linha ou tupla, é uma instância individual de dados em uma tabela.

## Comando: CREATE TABLE

``` SQL

CREATE TABLE {{nome}}

    ({{coluna}} {{tipo}} {{opções}} COMMENT {{'COMENTARIO'}});

```
## Tipos de Dados

Os dados podem variar muito entre os diversos SGBD, os mais comuns são:
-- Inteiro (Integer)
-- Decimal/Numérico (Decimal/Numeric)
-- Caractere/Varchar (Character/Varchar)
-- Data/Hora (Date/Time)
-- Booleano (Boolean)
-- Texto longo (Text)

---
---
---

# Modelagem de Dados Relacionais - Alterando e Excluindo Tabelas

## Drop Table

O comando DROP TABLE é usado no SQL - para remover uma tabela existente de um banco de dados relacional.

Ele Exclui permanentemente a tabela

``` DROP TABLE {{tabela}} ```

## Alter Table

A cláusula ALTER TABLE é usada no SQL para modificar a estrutura de uma tabela existente em um banco de dados relacional.

Ela permite:
-- Adicionar, alterar ou excluir colunas
-- Modificar as restrições, índices
-- Renomear a tabela entre outras alterações

## Chaves Primárias

-- Identifica exclusiamente
-- Não pode conter valores nulos (NULL)
-- Uma tabela pode ter apenas uma chave primária 

## Chaves Estrangeira 

Ela é usada para estabelecer e manter a integridade dos dados entre tabelas relacionadas

-- Pode ser nula (NOT NULL); **Registro órfão**
-- É possível ter mais de uma (ou nenhuma) em uma tabela.

## Chaves estrageiras - Restrições

-- ```ON DELETE``` especifica o que acontece com os registros dependentes quando um registro pai é exxcluído.
-- ```ON UPDATE``` define o comportamento dos registros dependentes quando um registro pai é atualizado.
-- ```CASCADE```, ```SET NULL```, ```SET DEFAULT```, e ```RESTRICT```

---
---
---

# Consultas Avançadas - Consultas com junções e subconsultas

## Junções: JOINs

São usadas no SQL ppara combinar dados de duas ou mais tabelas relacionadas em uma única consulta.

## Junções: Tipos

-- INNER JOIN
-- LEFT JOIN ou LEFT OUTER JOIN
-- RIGHT JOIN ou RIGHT OUTER JOIN
-- FULL JOIN ou FULL OUTER JOIN

## INNER JOIN

Retorna apenas linhas que têm correspôndencia em ambas as tabelas envolvidas na junção. A junção é feita com base em uma condição de igualdade especificada na cláusula ON.

`SELECT *`

`FROM tabela1`

`INNER JOIN tabela2 ON tabela1.coluna = tabela2.coluna;`

## LEFT JOIN

Retorna todas as linhas da tabela à esquerda da junção e as linhas correspondentes da tabela à direita. Se não houver correspondência, os valores da tabela à direita serão NULL.

`SELECT *`

`FROM tabela1`

`LEFT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;`

## RIGHT JOIN

Retorna todas as linhas da tabela à direita da junção e as linhas correspondentes da tabela à esquerda. Se não houver correspôndencia, os valores da tabella à esquerda serão NULL.

`SELECT *`

`FROM tabela1`

`RIGHT JOIN tabela2 ON tabela1.coluna = tabela2.coluna;`

## FULL JOIN

Retorna todas as linhas de ambas as tabelas envolvidas na junção, combinando-as com base em uma condição de igualdade. Se não houver correspôndencia, os valores ausentes serão preenchidos com NULL.

`SELECT *`

`FROM tabela1`

`FULL JOIN tabela2 ON tabela1.coluna = tabela2.coluna;`

## Sub Consultas

Elas permitem realizar consultas mais complexas permitindo que você use o resultado de uma consulta como entrada para outra consulta.

As subconsultas podem ser usadas em várias partes de uma consulta:

-- SELECT
-- FROM
-- WHERE 
-- HAVING
-- JOIN

---
---
---

# Consultas Avançadas - Funções agregadas e Agrupamento de resultados

## Funções Agregadas

-- COUNT: Contra o número de registros.
-- SUM: Soma os valores de uma coluna numérica.
-- AVG: Calcula a média dos valores de uma coluna numérica.
-- MIN: Retorna o valor mínimo de uma coluna.
-- MAX: Retorna o valor máximo de uma coluna.

---
---
---

# Consulta Avançadas - Índices de Busca

## Análise do Plano de Execução

Ela nos permite examinar as operações realizadas, as tabelas acessadas, os índices utilizados e outras informações importantes para identificar possíveis melhorias de desempenho.

## Análise do Plano de Execução 

-- select_type:"SIMPLE","SUBQUERY","JOIN"
-- table.
-- Type:"ALL","INDEX" entre outros
-- possible_keys: Os índices possíveis que podem ser utilizados na operação.
-- key: O índice utilizado na operação, se aplicácel.
-- key_len: O comprimmento do índice utilizado.
-- ref: As colunas ou constantes usadas para acessar o índice rows.

## Índices de Busca

``` SQL

CREATE INDEX {{nome_index}}
ON {{tabela}} ({{coluna1, coluna2...}});

```

---
---
---