# Valquíria e Stéfani|funções especiais, funções anônimas e listas de argumentos arbitrárias. 

###Sumário:
1. [Resumo simplificado de funções](#Resumo-simplificado)
2. [Resumo expandido](#Resumo-expandido)
3. [Funções especiais](#Funções-especiais)
4. [Funções anônimas](#Funções-anônimas)
4. [Listas de argumentos arbitárias](#Listas-de-argumentos-arbitárias)

#### Resumo simplificado de Funções ✨

Blocos de códigos que executam alguma tarefa e que tem um nome, ou manipulam algum dado e são capazes de receber (ou não) parâmetros e/ou argumentos, ou seja, processam informações e retornam valores. Dessa forma, são denominadas funções em python, que possuem alguns tipos, dentre eles: funções especiais, funções anônimas e listas de argumentos arbitrárias. 


#### Resumo expandido ✨

Funções são ..    a função inicia com "def" e um nome é atribuído, após isso um parâmetro é criado.
(exemplo)


• Evita repetição de código
• Deixa o código Menor
• Mais legível
• Mais modularizado


#Funções especiais: são funções passadas por parâmetros que consistem em posições que são preenchidas por parâmetros

#Funções anônimas: 
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

#Listas de argumentos arbitrárias:
 Neste os argumentos da função são agrupados e passados dentro de uma tupla.

 Agora, vendo este exemplo na prática:

```def argumentos_arbitrarias (x, y=3, *args):
      return  [x + y * w for w in args]
```












Python é 🔝

Por padrão, argumentos podem ser passadas para uma função Python tanto por posição quanto explicitamente pelo nome. Para uma melhor legibilidade e desempenho, faz sentido restringir a maneira pelo qual argumentos possam ser passados, assim um desenvolvedor precisa apenas olhar para a definição da função para determinar se os itens são passados por posição, por posição e nome, ou por nome.

#### Exercícios

1. Abra o console do Python.
2. Rode um programa Python pelo console.
3. Rode um script Python pelo console.

#### Resolução

1. Menu Iniciar > prompt de comando > digite `python` e dê Enter
2. Menu Iniciar > prompt de comando > digite `python` e dê Enter. Digite `print('olá mundo!')`. Feito!
3. Menu Iniciar > prompt de comando. Digite `python <nome do script>`, e dê Enter.