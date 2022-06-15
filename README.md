# wikiPythonDepressao

Wiki de Python do segundo ano de Técnico em Informática para Internet Integrado ao Ensino Médio do Colégio Técnico Industrial de Santa Maria. Turma de 2022.


![careca](https://pm1.narvii.com/6727/31271b6a66c8f56f3a31f1f2734b85d28045170ev2_hq.jpg)


# Grupos & tópicos


| stéfani e valquíria | Funções: parâmetros especiais, funções anônimas, listas de argumentos arbitrárias     |



## Não atribuídos 

* Classes: herança múltipla, variáveis privadas, geradores
* Módulos
* Pacotes


## Exemplo de Wiki

### Sumário

1. [Introdução](#introdução)
<<<<<<< HEAD
2. [Exercícios](#exercicios)
3. [Resolução](#resolução)

=======
2. [if-else](#if-else)
3. [Escrita de arquivos](#escrita-de-arquivos)
>>>>>>> cde19e0824b19cde52b35084b135f4bd9db181f9

### Introdução

<<<<<<< HEAD
# If, Else, Elif. Nicolle Moreira E Kamilli Razera

#### Resumo simplificado

If, Else e elif são comandos de desvio de fluxo.
=======
#### Resumo simplificado de Funções ✨

Blocos de códigos que executam alguma tarefa e que tem um nome, ou manipulam algum dado e são capazes de receber (ou não) parâmetros e/ou argumentos, ou seja, processam informações e retornam valores. Dessa forma, são denominadas funções em python, que possuem alguns tipos, dentre eles: funções especiais, funções anônimas e listas de argumentos arbitrárias. 


#### Resumo expandido ✨

Funções são ..    a função inicia com "def" e um nome é atribuído, após isso um parâmetro é criado.
(exemplo)


• Evita repetição de código
• Deixa o código Menor
• Mais legível
• Mais modularizado
. def parâmetros são 

Funções especiais: são funções passadas por parâmetros que consistem em posições que são preenchidas por parâmetros

<<<<<<< HEAD

Python é 🔝
=======
>>>>>>> 48aa13fc8368026d7b88fd4bdb1bdf05688bcbc5

>>>>>>> d6e0f8517a43100b8ad6a27ff87e060e34b7b6b5


<<<<<<< HEAD
If(se) é uma condicional que permite avaliar se a expressão é afirmativa.
Else(se não) é a condicional que avalia se a condição é negativa.
Elif(se não se) é a junção de else + if, ele faz com que as condições sejam interligadas (se ele satisfizer uma condição ele não verifica as outras). 
=======
Por padrão, argumentos podem ser passadas para uma função Python tanto por posição quanto explicitamente pelo nome. Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados por posição, por posição e nome, ou por nome.
>>>>>>> d6e0f8517a43100b8ad6a27ff87e060e34b7b6b5

#### Exercícios

1. Abra o console do Python.
2. Rode um programa Python pelo console.
3. Rode um script Python pelo console.

#### Resolução

1. Menu Iniciar > prompt de comando > digite `python` e dê Enter
2. Menu Iniciar > prompt de comando > digite `python` e dê Enter. Digite `print('olá mundo!')`. Feito!
3. Menu Iniciar > prompt de comando. Digite `python <nome do script>`, e dê Enter.

### If-Else

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

#### Resolução


#### Exercícios

1. Abra o console do Python.
2. Rode um programa Python pelo console.
3. Rode um script Python pelo console.


### Juh e Jhenni
### Sumário

1. [Números e expressões aritméticas](#números-e-expressões-aritméticas)
2. [Comando Pass](#comando-pass)
3. [Escrita de arquivos](#escrita-de-arquivos)


### Números e expessões aritiméticas

#### Resumo simplificado


#### Resumo expandido
O interpretador números funciona como uma calculadora, deve-se digitar uma expressão, com os operadores usuais ( +, -, * e / ), e o resultado será apresentado. Assim como nas linguagens tradicionais, os parênteses podem ser usados para agfrupar as expressões. 
Números inteiros, são do tipo int, enquanto números decimais são do tipo float. Divisão sempre retorna númetros do tipo float, para retornar números inteiros, é necessário usar o operador //; e para saber somente o resto da expressão é preciso usar o operador %.
Para exponenciação é possível usar o operador ** .
Para atribuir valor para uma variável é necessário usar o sinal de igual; caso uma variável não for atribuída, tentar utiliza-la gerará um erro.
A variável _ é usada para definir a quantidade de números após a vírgula; nun ca defina um valor, do contrário será criada outra variável independente que mascararia a variável especial.

### Exercícios



### Resolução



### Comando Pass

#### Resumo simplificado

Python é 🔝




#### Resumo expandido

A instrução pass é usada em Python quando algum código é solicitado sintaticamente, mas o usuário não quer que o programa faça nada. Também podemos ignorar exceções em Python usando a instrução pass, uma instrução específica do Python usada como um espaço reservado quando o usuário deseja que o programa não faça nada.

#### Exercícios



<<<<<<< HEAD
Depois eu faço.


###Exceções 

###Resumo simplificado
Exceções são erros inesperados que acontecem na hora de executar o código. Elas não são fatais e podem ser resolvidas com intruções.

=======

### Resolução



### Formatação de strings

### Resumo simplificado


### Resumo expandido


### Exercícios


### Resolução
>>>>>>> fd64e6525cc036e388c4dc62aa5941ceda2bff9b
