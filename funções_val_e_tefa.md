# 🎭 𝑭𝒖𝒏𝒄̧𝒐̃𝒆𝒔 𝒆𝒔𝒑𝒆𝒄𝒊𝒂𝒊𝒔, 𝒇𝒖𝒏𝒄̧𝒐̃𝒆𝒔 𝒂𝒏𝒐̂𝒏𝒊𝒎𝒂𝒔 𝒆 𝒍𝒊𝒔𝒕𝒂𝒔 𝒅𝒆 𝒂𝒓𝒈𝒖𝒎𝒆𝒏𝒕𝒐𝒔 𝒂𝒓𝒃𝒊𝒕𝒓𝒂́𝒓𝒊𝒂𝒔  🎭-- Stéfani e Valquíria

### *Sumário:*
1. [Resumo simplificado de funções](#Resumo-simplificado-de-funções)
2. [Resumo expandido](#Resumo-expandido)
3. [Parâmetros especiais](#Parâmetros-especiais)
4. [Funções anônimas](#Funções-anônimas)
5. [Listas de argumentos arbitrárias](#Listas-de-argumentos-arbitrárias)
6. [Exercícios](#Exercícios)

### *Resumo simplificado de funções*

Blocos de códigos que executam alguma tarefa e que tem um nome, ou manipulam algum dado e são capazes de receber (ou não) parâmetros e/ou argumentos, ou seja, processam informações e retornam valores. Dessa forma, são denominadas funções em python, que possuem alguns tipos, dentre eles: funções especiais, funções anônimas e listas de argumentos arbitrárias. 


### *Resumo expandido*

Funções são sequências de comandos que exercem determinadas funções e que possuem um nome. A função inicia com "def" e um nome é atribuído, após isso um parâmetro é criado. Serve, também, para evitar repetição de código, deixar o código menor, mais compreensível, etc. 

#### Parâmetros especiais: 
São funções que consistem em parâmetros, que fazem referência à objetos, e são passados por valor. Assim, após passar uma variável a uma função, é passado a referência ao objeto que a variável se refere. Desse modo, os ítens são passados por posição, por posição e nome, ou por nome.
A definição de uma função pode parecer com:
```python
 def combined_example(pos_only, /, standard, *, kwd_only):
     print(pos_only, standard, kwd_only)
```

#### Funções anônimas: 
Funções anônimas ou também popularmente conhecida como
função Lambda; representa um nome que advém da matemática,
apresentado pelo matemático americano Alonzo Church em 1930, na qual era
orientador de Alan Turing. O cálculo lambda trata as funções como
valores, fazendo com que elas sejam entradas para outras funções, assim
como funções podem retornar funções como saída, ou seja, funções que
operam em funções (melhor no exemplo kkk).

Veja logo abaixo um exemplo de uma função normal:

```python
def funcao (arg,arg2):
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

#### Listas de argumentos arbitrárias:
 Neste os argumentos da função são agrupados e passados dentro de uma tupla.

 Agora, vendo este exemplo na prática:

``` python
def argumentos_arbitrarias (x, y=3, *args):
      return  [x + y * w for w in args]
```

### *Exercícios✨*

1. Defina uma funçao que dentro dela chame uma varivél que possa ser passado por mais de um valor (qualquer valor), essa função tem que retornar uma lista com vários itens dentro separado por "/", os itens desta lista tem que ser imutavel, mas a lista tem que ter a posibilidade de acresentar um novo item a ela (oque chamamos de lista tipo tupla). Por fim, defina uma variável que seja atribuída ao nome da função dada no inicio, e imprima na tela a lista. 

2. Passe uma função normal para uma função lambda, e dentro da fução crie uma variável que retorne no resultado o seu dobro.

3. Defina uma função e atribua os valores para as variáveis a, b e c:



### *Resolução✨*

1.
```python
  def qualquer_nome (*args, sep="/"):
  return sep.join(args)

  z = qualquer_nome ("minhas bandas do momento são:", "the smiths", "the verve" , "e matchbox twenty") 
  print(z)
  ```

  -Logo, definimos uma função com um nome "qualquer_nome", dentro dela definimos uma variável chamada "args" que vem do nome "argumentos", adjunto a ela observe-se o "*" que é usado para indicar que a variável args pode ser atribuída a qualquer valor e pode ser passada por infinitas casas, e o "sep= /" é o responsavel por colocar a barra para separar os elementos listados. Por fim, definimos uma nova variável chamada "z", na qual vai ser atribuída ao nome da função (qualquer_nome) e que vai printar a ista contida dentro da variável z.
  

2. 
```python
//Função normal :
def nome(b):
    return b*2
    nome(24)

//Passando para uma função Lambda: 
    praticando = lambda a: a*2
    praticando (45)
    print(praticando)
``` 

 -Na função normal definimos uma função chamada "nome" que é atribuída a uma variável (b), esta variável por sua vez vai retornar qualquer valor atribuído a ela, só que o seu dobro (*2). Passando para uma função lambda, temos que: nome = lambda argumentos (a): return (2 *a), na qual o nome da função lambda chama-se "praticando", e sua váriavel representa a letra "a"  como sendo o argumento da função, que por fim vai ser multiplicado por dois no retorno.


3. 
```python 
 def escolha_algum_nome (a=5, b=6, c=7):
  return  a + b + c
  ```