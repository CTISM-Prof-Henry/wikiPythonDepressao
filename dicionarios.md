# Dicionários - Python

## Versão Detalhada Dicionários:

Dicionários, (dict), também chamados de “memória associativa” ou “vetor associativo” em outras linguagens,  são estruturas de dados que já são embutidas no python,(*Não precisa importar de outra biblioteca*). Elas são estruturas de dados que servem para guardar valores dentro, assim como: Listas, Tuplas, Matrizes e conjuntos.

Uma das melhores definições de dicionários é de que eles são como listas, só que usam outros valores chave que você os atribuiu para chamar o valor dessa estrutura de dados, (como assim?), você vai criar o dicionário, e dar um nome que se refere ao valor que você atribuiu essa "*Chave*", e quando você for chamar esse valor, você vai dizer a chave dele, invés de chamar a posição dele em um número inteiro como faria em uma lista. Lembrando que os elementos de um dicionário são como conjuntos, são armazenados de forma não ordenada, ou seja, é como se fosse um saco, com objetos dentro tudo misturados, difere de uma lista por exemplo, que são como se fossem vagões de trem, com slots numerados e ordenados com elementos dentro. 

Para criar o dicionário em Python, primeiro damos o nome dele, como todas as estruturas de dados em Python, colocamos os elementos entre chaves "{}", e colocamos as chaves que são os nomes atribuídos aos valores, entre aspas " '' ", e colocamos dois pontos ":" logo no final dessa chave e em seguida colocamos o valor dela, e para colocar mais outras chaves com seus valores correspondentes no mesmo dicionário, basta colocar uma simples vírgula "," logo após o valor anterior.

Exemplo:

dicionario = {'valor1': 4139, 'valor2': 4127, 'valor3': 4098}
print(dict)

- {'valor1': 4139, 'valor2': 4127, 'valor3': 4098}

Os elementos das chaves podem ser de valores não mutáveis, como: string, int, float, bool, não podem ser aquelas estruturas que possuem outros valores dentro, como: listas, tuplas e até próprios dicionários, Já os formatos dos valores, podem sem até outros tipos mais diversos como: Os tipos numéricos, strings, lista, e até dicionários, daí teria dicionário dentro de dicionário.

Podemos fazer algumas operações com funções nos dicionários:

“get()” Esta função serve para acessar o valor de uma chave no dicionário pela chave, como usar em um print. Exemplo:

frutas = {'pera': 50, 'uva': 2, 'maçã':55, 'abacaxi': 25}
qtd_macas = frutas.get('maçã')
print('O Total de maçãs é: ',qtd_macas)

- O Total de maçãs é:  55
------------------------------------------------------------

"items()" Esta função quando usada, retorna uma lista de tuplas contendo as chaves e seus respectivos valores declarados no dicionário. Exemplo:

print(cesta_frutas.items())

- dict_items([('pera', 10), ('uva', 2), ('maça', 55), ('abacaxi', 25), ('laranja', 15)])

(ESSA NÃO É UMA FORMA MUITO APRESENTÁVEL DE MOSTRAR AS INFORMAÇÕES DE UM DICIONÁRIO, O MAIS LEGAL É PERCORRER COM FOR E IMPRIMIR:)

for fruta, qtd in cesta_frutas.items():
    print(fruta +": "+str(qtd))

- pera: 10
  uva: 2
  maça: 55
  abacaxi: 25
  laranja: 15
-------------------------------------------------------------

"keys()" Esta função retorna só as chaves do dicionário, sem os valores. Exemplo:

for fruta in cesta_frutas.keys():
    print(fruta)

- pera
  uva
  maça
  abacaxi
  laranja
-------------------------------------------------------------

"values()" Esta função, ao contrário da "keys()", retorna só os valores das chaves do dicionário. Exemplo:

for fruta in cesta_frutas.values():
    print(fruta)

- 10
  2
  55
  25
  15
-------------------------------------------------------------

"sorted()" Utilizado no laço de repetição, retorna os elementos em ordem alfabética: Exemplo:

for fruta in sorted(cesta_frutas.keys()):
    print(fruta)

- abacaxi
 laranja
 maça
 pera
 uva
-------------------------------------------------------------

"enumerate()" Usado no laço de repetição, retorna os valores em ordem numérica. Exemplo:

for i, fruta in enumerate(cesta_frutas):
    print(i, fruta)

- 0 pera
  1 uva
  2 maça
  3 abacaxi
  4 laranja 
------------------------------------------------------------

"len()" Serve para visualizar o tamanho, ou a quantidade de itens que um dicionário contém. Exemplo:

print(len(cesta_frutas))

- 5
------------------------------------------------------------

"append" Com este comando, podemos armazenar os valores do dicionário em uma lista. Exemplo:

compras = []
frutas = {
            'pera': 50, 
            'uva': 2, 
            'maçã': 55, 
            'abacaxi': 25
            }
compras.append(frutas)
print(compras)

- [{'pera': 50, 'uva': 2, 'maçã': 55, 'abacaxi': 25}]
-----------------------------------------------------------

Os dicionários são mutáveis, ou seja, podem ser alterados os valores deles por uma forma externa. Exemplos:

Adicionar itens:

frutas = {'pera': 50, 'uva': 2, 'maçã':55, 'abacaxi': 25}
frutas['laranja'] = 0
frutas['abacate'] = 33
print(frutas)

- {'pera': 50, 'uva': 2, 'maçã': 55, 'abacaxi': 25, 'laranja': 0, 'abacate': 33}

Se atribuir um valor a uma chave já existente no dicionário, ele substitui o valor pelo recentemente colocado, ou seja, altera um valor de um dicionário.

Remover itens: função "del"

frutas = {'pera': 50, 'uva': 2, 'maçã':55, 'abacaxi': 25, 'laranja' : 0, 'abacate' : 33}
del frutas['abacate']
print(frutas)

- {'pera': 50, 'uva': 2, 'maçã':55, 'abacaxi': 25, 'laranja' : 0}

Operadores and, or, in, not in para dicionários:

Podemos usar alguns operadores para analizar os dados elementos em dicionários. 

"in" Analiza se tem dentro:

frutas = {'pera': 50, 'uva': 2, 'maçã':55, 'abacaxi': 25, 'laranja' : 0, 'abacate' : 33}
if 'abacate' in frutas:
    print("tem abacate")

- tem abacate

Podemos usar a negação dele "not in", que analiza se são tem:

frutas = {'pera': 50, 'uva': 2, 'maçã':55, 'abacaxi': 25, 'laranja' : 0, 'abacate' : 33}
if 'melão' not in frutas:
    print("tem que comprar melão")

- tem que comprar melão

------------------------------------------------------------

"or" Analiza um valor (ou) outro:

frutas = {'pera': 50, 'uva': 2, 'maçã':55, 'abacaxi': 25, 'laranja' : 0, 'abacate' : 33}
if 'abacaxi' or 'laranja' in frutas:
    print("tem cítricas")

- tem cítricas
------------------------------------------------------------

"and" Analisa se um valor (e) outro:

frutas = {'pera': 50, 'uva': 2, 'maçã':55, 'abacaxi': 25, 'laranja' : 0, 'abacate' : 33}
if 'abacaxi' and 'laranja' in frutas:
    print("tá muito cítrico!!")

- tá muito cítrico!!
------------------------------------------------------------

Podemos utilizar esses comandos juntas em uma mesma função: Exemplo:

frutas = {'pera': 50, 'uva': 2, 'maçã':55, 'abacaxi': 25, 'laranja' : 0, 'abacate' : 33, 'bergamota' : 15}
if ('bergamota' and 'laranja') or ('pera' and 'maça') in frutas:
    print("tem duas frutas muito cítricas!")
elif ('limão' and 'laranja') or ('açaí' and 'guaraná') in frutas:
    print("tem duas frutas de fazer bebida!")

- tem duas frutas muito cítricas!
......................................................................


## Versão Simplificada Dicionários:

O que são dicionários? São estruturas de dados que já são embutidas no python, que servem para guardar valores dentro, assim como: Listas, Tuplas, Matrizes e conjuntos, Só que usam outros valores chave que você os atribuiu para chamar o valor desse dicionário. As chaves são os nomes das variáveis que contém o valor dela, o dicionário pode ter várias chaves.

Para que serve? É muito útil para quando você tem variáveis com seus valores mas que quer que estejam guardados numa variável, por exemplo um jogo que tem um dicionário que guarda informações do jogador, como vida, estamina e fome, e quando for atualizar algum valor, (como encostar em um inimigo baixar a vida), é só chamar a chave “vida”: jogador = {'vida': 89, 'estamina': 58, 'fome': 100}

Como se usa? Para criar o dicionário em Python, primeiro damos o nome dele, como todas as estruturas de dados em Python, colocamos os elementos entre chaves "{}", e colocamos as chaves que são os nomes atribuídos aos valores, entre aspas " '' ", e colocamos dois pontos ":" logo no final dessa chave e em seguida colocamos o valor dela, e para colocar mais outras chaves com seus valores correspondentes no mesmo dicionário, basta colocar uma simples vírgula "," logo após o valor anterior. 

Exemplo:

dicionario = {'valor1': 4139, 'valor2': 4127, 'valor3': 4098}
print(dict)

- {'valor1': 4139, 'valor2': 4127, 'valor3': 4098}

Podemos usar os dicionários percorrendo eles em um for, e usar os operadores and, (é verdadeiro se um informação E outra é verdade), or, (é verdadeiro se uma informação Ou outra for verdade), in, (analisa se aquela informação está dentro de outra), not in, (analisa se aquela informação não está dentro de outra).

Principais operações com os dicionários:

“get()” Esta função serve para acessar o valor de uma chave no dicionário pela chave, como usar em um print. Exemplo:

frutas = {'pera': 50, 'uva': 2, 'maçã':55, 'abacaxi': 25}
qtd_macas = frutas.get('maçã')
print('O Total de maçãs é: ',qtd_macas)

- O Total de maçãs é:  55
------------------------------------------------------------

"append" Com este comando, podemos armazenar os valores do dicionário em uma lista. Exemplo:

compras = []
frutas = {
            'pera': 50, 
            'uva': 2, 
            'maçã': 55, 
            'abacaxi': 25
            }
compras.append(frutas)
print(compras)

- [{'pera': 50, 'uva': 2, 'maçã': 55, 'abacaxi': 25}]
-----------------------------------------------------------

"enumerate()" Usado no laço de repetição, retorna os valores em ordem numérica. Exemplo:

for i, fruta in enumerate(cesta_frutas):
    print(i, fruta)

- 0 pera
  1 uva
  2 maça
  3 abacaxi
  4 laranja 
------------------------------------------------------------

"len()" Serve para visualizar o tamanho, ou a quantidade de itens que um dicionário contém. Exemplo:

print(len(cesta_frutas))

- 5
------------------------------------------------------------

"sorted()" Utilizado no laço de repetição, retorna os elementos em ordem alfabética: Exemplo:

for fruta in sorted(cesta_frutas.keys()):
    print(fruta)

- abacaxi
 laranja
 maça
 pera
 uva
-------------------------------------------------------------

Você pode retornar apenas o valor dos valores usando .values(),  “dicionario.values():”, e pode retornar só as chaves usando .keys(), “dicionario.keys():”

Os dicionários são mutáveis, ou seja, podem ser alterados os valores deles por uma forma externa. Exemplos:

Adicionar itens:

frutas = {'pera': 50, 'uva': 2, 'maçã':55, 'abacaxi': 25}
frutas['laranja'] = 0
frutas['abacate'] = 33
print(frutas)

- {'pera': 50, 'uva': 2, 'maçã': 55, 'abacaxi': 25, 'laranja': 0, 'abacate': 33}

Se atribuir um valor a uma chave já existente no dicionário, ele substitui o valor pelo recentemente colocado, ou seja, altera um valor de um dicionário.

Remover itens: função "del"

frutas = {'pera': 50, 'uva': 2, 'maçã':55, 'abacaxi': 25, 'laranja' : 0, 'abacate' : 33}
del frutas['abacate']
print(frutas)

- {'pera': 50, 'uva': 2, 'maçã':55, 'abacaxi': 25, 'laranja' : 0}

......................................................................



# [exercicios](exerciciosdicionario.md)
