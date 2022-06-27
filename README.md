# wikiPythonDepressao

Wiki de Python do segundo ano de Técnico em Informática para Internet Integrado ao Ensino Médio do Colégio Técnico Industrial de Santa Maria. Turma de 2022.

![careca](images/careca.jpg)

# Descrição do trabalho

https://ead06.proj.ufsm.br/mod/assign/view.php?id=1649422

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
| stéfani e valquíria | Funções: parâmetros especiais, funções anônimas, listas de argumentos arbitrárias     |


![careca](https://pm1.narvii.com/6727/31271b6a66c8f56f3a31f1f2734b85d28045170ev2_hq.jpg)







## Não atribuídos 
* Classes: herança múltipla, variáveis privadas, geradores
* Módulos
* Pacotes


## Exemplo de Wiki

### Sumário

1. [Introdução](#introdução)
2. [Exercícios](#exercicios)
3. [Resolução](#resolução)
5. [Escrita arquivos](escrita_arquivos.md)
2. [if-else](#if-else)
6. [Introdução : Lista](Introduçaozinha.md)
7. [Funções: definindo funções](funções.md)
8. [Funções com parâmetros padrão, argumentos nomeados, strings de documentação](quase_tudo_sobre_funções.md)
7. [introdução : Laços de repetição](laços.md)

### Introdução

#### Resumo simplificado de Funções ✨

Blocos de códigos que executam alguma tarefa e que tem um nome, ou manipulam algum dado e são capazes de receber (ou não) parâmetros e/ou argumentos, ou seja, processam informações e retornam valores. Dessa forma, são denominadas funções em python, que possuem alguns tipos, dentre eles: funções especiais, funções anônimas e listas de argumentos arbitrárias. 


#### Resumo expandido ✨

Funções são ..    a função inicia com "def" e um nome é atribuído, após isso um parâmetro é criado.
(exemplo)


• Evita repetição de código
• Deixa o código Menor
• Mais legível
• Mais modularizado


Funções especiais: são funções passadas por parâmetros que consistem em posições que são preenchidas por parâmetros

Funções anônimas: Funções anônimas ou também popularmente conhecida como
função Lambda; representa um nome que advém da matemática,
apresentado pelo matemático americano Alonzo Church em 1930, na qual era
orientador de Alan Turing. O cálculo lambda trata as funções como
valores, fazendo com que elas sejam entradas para outras funções, assim
como funções podem retornar funções como saída, ou seja, funções que
operam em funções (melhor no exemplo kkk).

Veja logo abaixo um exemplo de uma função normal:

```def funcao (arg,arg2):
return arg*arg2
var = funcao (2,2)
print (var)
```
Aqui pode-se notar que definimos uma função, dentro dela atribuímos os
argumentos que queremos passar para a função e jogamos ela em uma
variável chamada var que guarda dois valores que vão ser multiplicados no
return. 

Agora vamos ver como esta função ficaria sendo lambda, logo temos que:

```python
a = lambda x , y: x*y
print (a(2,2))
```

Nesta função atribuímos o nome da função como lambda, que recebe uma
string (a) como uma variável que armazena dois números inteiros (x=2,y=2)
que vão ser multiplicados, mas desta vez sem utilizar o return.

listas de argumentos arbitrárias:











Python é 🔝


If(se) é uma condicional que permite avaliar se a expressão é afirmativa.
Else(se não) é a condicional que avalia se a condição é negativa.
Elif(se não se) é a junção de else + if, ele faz com que as condições sejam interligadas (se ele satisfizer uma condição ele não verifica as outras). 

Por padrão, argumentos podem ser passadas para uma função Python tanto por posição quanto explicitamente pelo nome. Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados por posição, por posição e nome, ou por nome.

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
<<<<<<< HEAD
##### 
=======
>>>>>>> 9e16e3ae1837a8e54b1a64dcff49b59e75296b0d
##### list.**pop**([i])
Remove um item a lista, na posição determinada pelo usuário, iniciando a contagem a partir do 0. Ação opcional, se não dado um índice ele irá remover o último item da lista.
Ex :
```python
lista = [‘rhandres’ , ‘davi’ , 'o theo ta mal' , ‘breno’ , 'breno falta aula' ,]
lista.pop(2)
<<<<<<< HEAD
=======

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


print(lista)
```
```python
['rhandres' , 'davi' , 'breno' , 'breno falta aula']
```

#### list.**clear**()
Remove todos itens da lista. Para esta ação também pode ser usado o `del lista[:]`
Ex :
```python
lista = ['rhandres' , 'davi' , 'o theo ta mal' , 'breno' , 'breno falta aula' ]
lista.clear()

print(lista)
```
```python
[]
```
#### list.**count**()
Conta a quantidade de vezes que o item aparece na lista.
Ex :
```python
lista = ['rhandres' , 'davi' , 'o theo ta mal' , 'breno' , 'breno falta aula' , 'breno' ]
lista.count('breno')

print(lista.count('breno'))
```
```python
2
```
#### list.**index**()
Informa o índice do item selecionado pelo usuário, podendo ser usado indices para determinar o inicio e o fim. Caso o valor não esteja presente na lista o programa irá retornar `ValueError` 
Ex :
```python
lista = ['rhandres' , 'davi' , 'o theo ta mal' , 'breno' , 'breno falta aula' , 'breno' ]
lista.index('breno', 0, 4)

<<<<<<< HEAD
print(lista.index('breno', 0, 4))
```
```python
3
```
#### list.**sort**()
Ordena os itens de uma lista de acordo com a informação passada pelo usuário.
Ex :
```python
lista = [1 , 3 , 8 , 5 , 7]
lista.sort()
=======
#### Resolução



print(lista)
```
```python
[1 , 3 , 5 , 7 , 8]
```
Ou
```python
lista = [1 , 3 , 8 , 5 , 7]
lista.sort(reverse=True)

print(lista)
```
```python
[8 , 7 , 5 , 3 , 1]
```
#### list.**reverse**()
Inverte a ordem da lista.
Ex :
```python
lista = ['rhandres' , 'davi' , 'o theo ta mal' , 'breno' , 'breno falta aula' , 'breno' ]
lista.reverse()

print(lista)
```
```python
['breno' , 'breno falta aula' , 'breno' , 'o theo ta mal' , 'davi' , 'rhandres']
```
#### list.**copy**()
Faz uma cópia rasa da lista. Podendo ser usado também o `a[:]`
Ex :
```python
lista = ['rhandres' , 'davi' , 'o theo ta mal' , 'breno' , 'breno falta aula' , 'breno' ]
lista.copy()

print(lista.copy())
```


### Operadores :

#### and
#### or
#### in 
#### not in
#### Exercícios
1. Abra o console do Python.
2. Rode um programa Python pelo console.
3. Rode um script Python pelo console.
<<<<<<< HEAD
#### Resolução
1. Menu Iniciar > prompt de comando > digite `python` e dê Enter
2. Menu Iniciar > prompt de comando > digite `python` e dê Enter. Digite `print('olá mundo!')`. Feito!
3. Menu Iniciar > prompt de comando. Digite `python <nome do script>`, e dê Enter.
=======
=======




# Juh e Jhenni
## Sumário

1. [Números e expressões aritméticas](#números-e-expressões-aritméticas)
2. [Comando Pass](#comando-pass)
3. [Formatação de string](#formatação-de-string)


## Números e expessões aritiméticas

### Resumo simplificado
Os números em python são conceituados em dois tipos numéricos, os números inteiros e os números de ponto flutuante que são dados como (float) Funciona como uma calculadora simples, para isso você deve digitar uma expressão e o resultado será exibido.Expressões como operadores +, -, * e funcionam da mesma forma que em outras linguagens como: (pascal ou C).
O sinal de igual ('=') é usado para atribuir um valor de variável, se a variável não tiver um valor atribuído, constituirá um erro. No modo interativo a variável (' _ ') deve ser somente leitura pelo usuário, pois não especifica um valor, ela cria outra variável.

#### Resumo expandido
O interpretador números funciona como uma calculadora, deve-se digitar uma expressão, com os operadores usuais ( +, -, * e / ), e o resultado será apresentado. Assim como nas linguagens tradicionais, os parênteses podem ser usados para agfrupar as expressões. 
Números inteiros, são do tipo int, enquanto números decimais são do tipo float. Divisão sempre retorna númetros do tipo float, para retornar números inteiros, é necessário usar o operador //; e para saber somente o resto da expressão é preciso usar o operador %.
Para exponenciação é possível usar o operador ** .
Para atribuir valor para uma variável é necessário usar o sinal de igual; caso uma variável não for atribuída, tentar utiliza-la gerará um erro.
A variável _ é usada para definir a quantidade de números após a vírgula; nun ca defina um valor, do contrário será criada outra variável independente que mascararia a variável especial.

## Exercícios

### 1. Faça um código que converta reais em dólares:

## Resolução
```python
dolar = float(input("Informe a quantidade de dólar para conversão: US$ "))
valor = float(input ("Informe o valor do dólar: R$ "))
conversao = dolar*valor
print('A quantidade de dólar em real é: R$', conversao)
```
### 2. Faça um código, onde, dado dois números, mostre o valor da divisão inteira, e o resto da divisão

## Resolução
```python
n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))
DI = n1 // n2
RD = n1 % n2
print("O resultado da divisão inteira é igual a: {0} , e o resto da divisão é igual a: {1} ".format(DI, RD) )
```
### 3. Faça um código que pegue dois números, faça a multiplicação, e a divisão inteira entre eles, mostre o resultado na tela e depois eleve o resultado de ambos ao quadrado

## Resolução
```python
n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))
divisao = n1 // n2
multiplicacao = n1 * n2
P1 = divisao ** 2
P2 = multiplicacao ** 2
print("o resultado da divisão inteira entre {0}, e {1}, é igual a {2}".format(n1, n2, divisao))
print("o resultado da multiplicação entre {0}, e {1}, é igual a {2}".format(n1, n2, multiplicacao))
print("o resultado de {0} ao quadrado é igual a {1}".format(multiplicacao, P2))
print("o resultado de {0} ao quadrado é igual a {1}".format(divisao, P1))
```

## Comando Pass

### Resumo simplificado
O git pass é usado para ignorar erros. 

#### Resumo expandido
A instrução pass é usada em Python quando algum código é solicitado sintaticamente, mas o usuário não quer que o programa faça nada. Também podemos ignorar exceções em Python usando a instrução pass, uma instrução específica do Python usada como um espaço reservado quando o usuário deseja que o programa não faça nada.

## Exercícios


## Resolução


## Formatação de string

### Resumo simplificado
Temos assim varias maneiras de formatar uma saída, as strings são basicamente um conjunto de caracteres de texto que também podem ser informações que estão escritas dentro de um código.

### Resumo expandido
Para usarmos strings literais que são formatadas devemos começar com uma string (f) ou podemos também com (F), podemos escrever também uma expressão mas ela deve ser antes de abrir as aspas ou aspas triplas, ( aspas triplas são usadas para as strings que usam varias linhas), (aspas simples são usadas para declarar uma string). 
Quando uma string for muito longa e não queremos quebra-la, podemos fazer algumas referencias dos valores que serão formatados por nome, podemos fazer isso usando os colchetes ‘[ ]’ (os colchetes sempre marcam o inicio e o fim da lista e os elementos que são separados da virgula. 
O ‘str.rjust()’ ele move uma stgring a direita, que tenha um campo de tamanho definido. 
O ‘str.ljust()’  ele move uma string a esquerda. 
O ‘str.center()’ é usado para centralizar, eles não escrevem nada, são usados apenas para retornar uma nova string. 
O ‘f.write()’ podem resultar a não serem completamente escritos nos discos, mesmo se acaso o programa for encerrado. Mas não podemos usar a palavra reservada (WITH) OU também “f.close()”. Logo depois que um arquivo é fechado com o ‘with’ não podemos usar o arquivo, ele basicamente ira falhar automaticamente. 



### Exercícios


### Resolução

### Rafaela
## Escrita de arquivos

### Resumo simplificado 

Existem dois tipos de arquivos que podem ser manipulados em python, **arquivos de texto** e **arquivos binários**. A função **open()** para abrir arquivos podemos acessar arquivos só para para leitura, só para escrita e para leitura e escrita.

### Resumo expandido

####Abrindo arquivos:

Abrir arquivos só para a escrita (write)

```python
arquivo = open('nome_arquivo', 'w')
```
####Fechando arquivos


* [Funções](Funções/funções.md) 

=======
## Funções 
### Definindo Funções

 #### Resumo simplificado

def - define;



#### Resumo Expandido

Para definir uma função em Python, utilizamos o comando `def`, que significa literalmente definir. Após `def`, o nome da função deve ser estabelecido, seguido pelos parâmetros formais entre parênteses.
	

#### Exercícios

#### Resolução












# nicole, thianna e joão



### Argumentos com valor padrão e Argumentos nomeados

#### Resumo Simplicado
In - Verifica se uma sequência contém ou não um determinado valor.



É possivel definir funções com um número variável de argumentos
// essas formas podem ser combinadas

#### Argumento com valor padrão

É utilizado para especificar um valor padrão para um ou mais argumentos.

Por exemplo  :
```python

def perguntar_ok(prompt, tentativas=4, relembrar='Porfavor Tente Denovo!'):
    while True:
        ok = input(prompt)
        if ok in ('sim', 'S', 'yes'):
            return True
        if ok in ('Não', 'Neh', 'nop', 'n'):
            return False
        tentativas = tentativas - 1
        if tentativas < 0:
            raise ValueError('invalid user response')
        print(relembrar)
```


Podemos chamar essa função com varias formas

Dando apenas o argumento Obrigatório :   perguntar_ok('voce quer realmente sair?')

Dando um argumento opcional :  perguntar_ok('Ok para sobrescrever o arquivo?', 2)

ou dando todos os argumentos : perguntar_ok('Ok para sobrescrever o arquivo??', 2, 'vamos, apenas sim ou não!)

Importante:  Valores padrões só são avaliados uma vez. veja que isso fará diferença quando um valor é um objeto mutável, lista, dicionário ou instâncias de classes. 

// Argumento posicional é o nome utilizado para a passagem de valores onde cada valor estara na ordem conforme implementado na função.

#### Argumentos nomeados
Essa função chama outros argumentos utilizando
 
‘’Chave’’ = ‘’valor’’
A chave seria o nome dado dentro da função

Exemplo:

def Moitinha ( perfeito, lindo, gostoso,pomposo):
  print('perfeito:{}/nlindo:{}/ngostoso{}/npomposo{}')

Moitinha("perfeitão", lindo="lindão", gostoso='gostoso', pomposo='pomposinho')



Importante : 
Nenhum argumento pode receber mais de um valor

### Exercícios
Exercicio - Argumento padrão
Crie uma função de argumento padrão pedindo a senha (12345), dando ate 5 tentativas,
chame esse argumento 



## Exceções (nathy e nessa)

## Resumo simplificado

Exceções são erros inesperados que acontecem na hora de executar o código. Elas não são fatais e podem ser resolvidas com instruções.


## Resumo expandido

As exceções, como outros erros, retornam mensagens de erro indicando o que está errado:


### EX1:
```python
6 - 9/num

//A mensagem de erro seria:

File "C:\Users\aluno\PycharmProjects\pythonProject\main.py", line 1, in <module>
    6-9/num
NameError: name 'num' is not defined
```

### EX2:
```python
n=9

while True:
print(n)

//A mensagem de erro seria:

File "C:\Users\aluno\PycharmProjects\pythonProject\main.py", line 4
    print(n)
    ^
IndentationError: expected an indented block
```

Exceções específicas podem ser tratadas por instruções dadas pelo usuário, usando comandos como `try`, `else` e `except`:

### EX:
```python
numero = int(input("Digite um numero "))
try:
    resultado = 45 / numero
except ZeroDivisionError:
    print("Não foi possivel calcular o resultado")
```

O código acima funciona assim:

-O comando try é executado.

-Se não houver nenhuma exceção, o comando except é ignorado e a execução do código acaba.

-Se por acaso alguma exceção acontecer e for a mesma que o usuário especificou, ela é executada. Se não for a mesma, a execeção é considerada não tratada e retorna uma mensagem de erro.



O conjunto `try … except` pode possuir uma cláusula `else`, que quando presente, deve ser colocada depois de todas as outras cláusulas. É útil quando você tem uma parte do código que precisa ser executada se nenhuma exceção for executada. 

#### EX:
```python
list = ['1','6','9','4','7']

try:
    print(list[8])
except IndexError:
        print('nem tem esse índice doido')
else:
        print('deu certo')

```



## Exercícios

### Exercício 1: trate a exceção do código abaixo:

numero=0

resultado = 234 / numero





## Resoluções

### Resolução exercício 1:

```python
numero = 0
try:
    resultado = 234 / numero
except ZeroDivisionError:
    print("Não foi possivel calcular o resultado")

```
