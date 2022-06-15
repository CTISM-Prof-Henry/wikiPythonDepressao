# wikiPythonDepressao

Wiki de Python do segundo ano de Técnico em Informática para Internet Integrado ao Ensino Médio do Colégio Técnico Industrial de Santa Maria. Turma de 2022.


![careca](images/careca.jpg)

# Problemas resolvendo conflitos no git? 🤠

Tente este repositório: https://github.com/CTISM-Prof-Henry/gitEssentials

# Grupos & tópicos

| grupo | tópico |
|:------|:-------|
| julia e jhennifer | Números, expressões aritméticas, formatação de strings, comando pass |
| kamilli e nicolle | Controle de fluxo: if, else, elif |
| augusto e theo | Laços de repetição: while, for, função range, break, continue |
| davi, breno e rhandres | Estrutura de dados: listas, list comprehension, métodos da classe lista, operadores and, or, in, not in para listas |
| miguel | Estrutura de dados: tuplas, sets, operadores and, or, in, not in para tuplas/sets     |
| alexandre e bernardo | Estrutura de dados: dicionáros, construção de dicionários, iteração sobre dicionários, operadores and, or, in, not in para dicionários     |
| nicole, thianna e joão | Funções: definindo funções, funções com parâmetros padrão, argumentos nomeados, strings de documentação     |
| stéfani e valquíria | Funções: parâmetros especiais, funções anônimas, listas de argumentos arbitrárias     |
| rafaela | Leitura e escrita de arquivos, método with, biblioteca csv, Gravando dados estruturados com json|
| nathielly e vanessa | Exceções     |
| gabriela, manuela e mateus | Classes: sintaxe de definição de calsses, objetos de class, objetos instância, objetos método, variáveis de classe e instância, observações aleatórias     |


## Não atribuídos 

* Classes: herança múltipla, variáveis privadas, geradores
* Módulos
* Pacotes


## Exemplo de Wiki

### Sumário

1. [Introdução](#introdução)
2. [if-else](#if-else)
3. [Escrita de arquivos](#escrita-de-arquivos)

### Introdução

#### Resumo simplificado

Python é 🔝

#### Resumo expandido

Sério, Python é muito 🔝

#### Exercícios

1. Abra o console do Python.
2. Rode um programa Python pelo console.
3. Rode um script Python pelo console.

#### Resolução

1. Menu Iniciar > prompt de comando > digite `python` e dê Enter
2. Menu Iniciar > prompt de comando > digite `python` e dê Enter. Digite `print('olá mundo!')`. Feito!
3. Menu Iniciar > prompt de comando. Digite `python <nome do script>`, e dê Enter.

<<<<<<< HEAD
### If-Else
=======
### Implementação de listas :

#### List comprehension

### Métodos da classe lista :

##### list.**append**(x)

Adiciona um novo item ao fim da lista.
Ex :
```python
lista = [ ‘rhandres’ , ‘davi’ , ‘breno’ ]
lista.append('breno falta aula')

print(lista)
```
```python
['rhandres' , 'davi' , 'breno' , 'breno falta aula']
```
##### list.**remove**(x)
Remove um item da lista.
Ex :
```python
lista = [‘rhandres’ , ‘davi’ , ‘breno’ , 'breno falta aula']
lista.remove('breno')

print(lista)
```
```python
['rhandres' , 'davi' , 'breno falta aula']
```
##### list.**extend**(iterable)
Faz a junção de duas listas.
Ex :
```python
lista = [‘rhandres’ , ‘davi’ , ‘breno’]
lista2 = ['breno falta aula']
lista.extend(lista2)

print(lista)
```
```python
['rhandres' , 'davi' , 'breno' , 'breno falta aula']
```
##### list.**insert**(i,x)
Adiciona um item a lista, na posição determinada pelo usuário, iniciando a contagem a partir do 0.
Ex :

```python
lista = [‘rhandres’ , ‘davi’ , ‘breno’ , 'breno falta aula']
lista.insert(2,'o theo ta mal')

print(lista)
```
```python
['rhandres' , 'davi' , 'o theo ta mal' , 'breno' , 'breno falta aula']
```
##### list.**pop**([i])
Remove um item a lista, na posição determinada pelo usuário, iniciando a contagem a partir do 0. Ação opcional, se não dado um índice ele irá remover o último item da lista.
Ex :
```python
lista = [‘rhandres’ , ‘davi’ , 'o theo ta mal' , ‘breno’ , 'breno falta aula' ,]
lista.pop(2)

print(lista)
```
```python
['rhandres' , 'davi' , 'breno' , 'breno falta aula']
```

#### list.**clear**()
Remove todos itens da lista. Para esta ação também pode ser usado o `del lista[:]`
Ex :
```python
lista = [‘rhandres’ , ‘davi’ , 'o theo ta mal' , ‘breno’ , 'breno falta aula' ]
lista.clear()

print(lista)
```
```python
[]
```

### Operadores :

#### and

#### or

#### in 

#### not in


## Funções 

### Definindo Funções
>>>>>>> 2cf1e5c34f3a77d05bc32da3ec11b06593e215a8

#### Resumo simplificado

É if e é else.

#### Resumo expandido

Tem mais coisa, mas não tô afim de escrever agora.

#### Exercícios

Fiquei com preguiça de fazer.

#### Resolução

Depois eu faço.

#### Escrita de arquivos

#### Resumo simplificado 

É usada a função **open()** para abrir arquivos podemos acessar arquivos só para para leitura, só para escrita e para leitura e escrita

#### Resumo expandido

Abrindo arquivos:

Para isso usamos a função open().

Fechando arquivos