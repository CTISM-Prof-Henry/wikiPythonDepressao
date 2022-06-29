# 𝑭𝒖𝒏𝒄̧𝒐̃𝒆𝒔 𝒆𝒔𝒑𝒆𝒄𝒊𝒂𝒊𝒔, 𝒇𝒖𝒏𝒄̧𝒐̃𝒆𝒔 𝒂𝒏𝒐̂𝒏𝒊𝒎𝒂𝒔 𝒆 𝒍𝒊𝒔𝒕𝒂𝒔 𝒅𝒆 𝒂𝒓𝒈𝒖𝒎𝒆𝒏𝒕𝒐𝒔 𝒂𝒓𝒃𝒊𝒕𝒓𝒂́𝒓𝒊𝒂𝒔 -- Stéfani e Valquíria

### Sumário:
1. [Resumo simplificado de funções](#Resumo-simplificado)
2. [Resumo expandido](#Resumo-expandido)
3. [Parâmetros especiais](#Parâmetros-especiais)
4. [Funções anônimas](#Funções-anônimas)
5. [Listas de argumentos arbitárias](#Listas-de-argumentos-arbitárias)
6. [Exercícios](#Exercícios)

### Resumo simplificado de Funções ✨

Blocos de códigos que executam alguma tarefa e que tem um nome, ou manipulam algum dado e são capazes de receber (ou não) parâmetros e/ou argumentos, ou seja, processam informações e retornam valores. Dessa forma, são denominadas funções em python, que possuem alguns tipos, dentre eles: funções especiais, funções anônimas e listas de argumentos arbitrárias. 


### Resumo expandido ✨

Funções são sequências de comandos que exercem determinadas funções e que possuem um nome. A função inicia com "def" e um nome é atribuído, após isso um parâmetro é criado. Serve, também, para evitar repetição de código, deixar o código menor, mais compreensível, etc. 

#### Parâmetros especiais: 
São funções que consistem em parâmetros, que fazem referência à objetos, e são passados por valor. Assim, após passar uma variável a uma função, é passado a referência ao objeto que a variável se refere. Desse modo, os ítens são passados por posição, por posição e nome, ou por nome.
A definição de uma função pode parecer com:
```
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

#### Listas de argumentos arbitrárias:
 Neste os argumentos da função são agrupados e passados dentro de uma tupla.

 Agora, vendo este exemplo na prática:

``` 
def argumentos_arbitrarias (x, y=3, *args):
      return  [x + y * w for w in args]
```

#### Exercícios

1. Abra o console do Python.
2. Rode um programa Python pelo console.
3. Rode um script Python pelo console.

#### Resolução

1. Menu Iniciar > prompt de comando > digite `python` e dê Enter
2. Menu Iniciar > prompt de comando > digite `python` e dê Enter. Digite `print('olá mundo!')`. Feito!
3. Menu Iniciar > prompt de comando. Digite `python <nome do script>`, e dê Enter.