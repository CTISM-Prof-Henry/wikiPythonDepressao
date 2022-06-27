# wikiPythonDepressao

Wiki de Python do segundo ano de Técnico em Informática para Internet Integrado ao Ensino Médio do Colégio Técnico Industrial de Santa Maria. Turma de 2022.

![careca](images/careca.jpg)

# Descrição do trabalho

https://ead06.proj.ufsm.br/mod/assign/view.php?id=1649422

# Problemas resolvendo conflitos no git? 🤠

Tente este repositório: https://github.com/CTISM-Prof-Henry/gitEssentials

# Grupos & tópicos
| Grupo | Tópico |
|:------|:-------|
| Julia e Jhennifer | Números, expressões aritméticas, formatação de strings, comando pass |
| Kamilli e Nicolle | Controle de fluxo: if, else, elif |
| Augusto e Theo | Laços de repetição: while, for, função range, break, continue |
| Davi, Breno e Rhandres | [Estrutura de dados:](1-Introduçaozinha.md) listas, list comprehension, métodos da classe lista, operadores and, or, in, not in para listas |
| Miguel | Estrutura de dados: tuplas, sets, operadores and, or, in, not in para tuplas/sets     |
| Alexandre e Bernardo | Estrutura de dados: dicionáros, construção de dicionários, iteração sobre dicionários, operadores and, or, in, not in para dicionários     |
| Nicole, Thianna e João | Funções: definindo funções, funções com parâmetros padrão, argumentos nomeados, strings de documentação     |
| Stéfani e Valquíria | Funções: parâmetros especiais, funções anônimas, listas de argumentos arbitrárias     |
| Rafaela | Leitura e escrita de arquivos, método with, biblioteca csv, Gravando dados estruturados com json|
| Nathielly e Vanessa | Exceções     |
| Gabriela, Manuela e Mateus | Classes: sintaxe de definição de calsses, objetos de class, objetos instância, objetos método, variáveis de classe e instância, observações aleatórias     |


![careca](https://pm1.narvii.com/6727/31271b6a66c8f56f3a31f1f2734b85d28045170ev2_hq.jpg)







## Não atribuídos 
* Classes: herança múltipla, variáveis privadas, geradores
* Módulos
* Pacotes

1. [Introdução: Números e expessões aritiméticas](#Sumário:)
2. [Introdução: Listas](2-Introduçaozinha.md)
3. [Escrita arquivos](escrita_arquivos.md)
4. [If-Else](If,else,elif.md)
5. [Funções: definindo funções](funções.md)
6. [Funções com parâmetros padrão, argumentos nomeados, strings de documentação](quase_tudo_sobre_funções.md)
7. [Introdução: Laços de repetição](laços.md)
8. [Introdução: Tuplas](Tuplas.md)


# Juh e Jhenni
## Sumário:

1. [Números e expressões aritméticas](#números-e-expressões-aritméticas)
2. [Comando Pass](#comando-pass)
3. [Formatação de string](#formatação-de-string)


## Números e expessões aritiméticas:

### Resumo simplificado:
Os números em python são conceituados em dois tipos numéricos, os números inteiros e os números de ponto flutuante que são dados como (float) Funciona como uma calculadora simples, para isso você deve digitar uma expressão e o resultado será exibido.Expressões como operadores +, -, * e funcionam da mesma forma que em outras linguagens como: (pascal ou C).
O sinal de igual ('=') é usado para atribuir um valor de variável, se a variável não tiver um valor atribuído, constituirá um erro. No modo interativo a variável (' _ ') deve ser somente leitura pelo usuário, pois não especifica um valor, ela cria outra variável.

#### Resumo expandido:
O interpretador números funciona como uma calculadora, deve-se digitar uma expressão, com os operadores usuais ( +, -, * e / ), e o resultado será apresentado. Assim como nas linguagens tradicionais, os parênteses podem ser usados para agfrupar as expressões. 
Números inteiros, são do tipo int, enquanto números decimais são do tipo float. Divisão sempre retorna númetros do tipo float, para retornar números inteiros, é necessário usar o operador //; e para saber somente o resto da expressão é preciso usar o operador %.
Para exponenciação é possível usar o operador ** .
Para atribuir valor para uma variável é necessário usar o sinal de igual; caso uma variável não for atribuída, tentar utiliza-la gerará um erro.
A variável _ é usada para definir a quantidade de números após a vírgula; nun ca defina um valor, do contrário será criada outra variável independente que mascararia a variável especial.

## Exercícios:

### 1. Faça um código que converta reais em dólares.

## Resolução:
```python
dolar = float(input("Informe a quantidade de dólar para conversão: US$ "))
valor = float(input ("Informe o valor do dólar: R$ "))
conversao = dolar*valor
print('A quantidade de dólar em real é: R$', conversao)
```
### 2. Faça um código, onde, dado dois números, mostre o valor da divisão inteira, e o resto da divisão.

## Resolução:
```python
n1 = int(input("Digite um número:"))
n2 = int(input("Digite outro número:"))
DI = n1 // n2
RD = n1 % n2
print("O resultado da divisão inteira é igual a: {0} , e o resto da divisão é igual a: {1} ".format(DI, RD) )
```
### 3. Faça um código que pegue dois números, faça a multiplicação, e a divisão inteira entre eles, mostre o resultado na tela e depois eleve o resultado de ambos ao quadrado.

## Resolução:
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
