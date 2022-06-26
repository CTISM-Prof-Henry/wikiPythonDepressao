### Sumário


1. [Argumento com valor padrão](#link)
2. [Argumentos nomeados](#link)
3. [Expressões Lambda](#expressões-lambda)
4. [Strings de documentação](#strings-de-documentação)
5. [Exercícios](#exercícios)


### Expressões Lambda
#### Resumo simplificado

- pequenas funções anônimas
- objetos (1 expressão) ou argumento (aninhamento)
- variáveis no escopo
- >função< = lambda >n<:>n/2<


#### Resumo expandido

“lambda” é a palavra-chave para definir pequenas funções anônimas em Python, é uma forma mais sucinta de definir uma função.

Podem ser usadas para representar objetos função, que ficam restritos a uma expressão;
Ou como argumento, onde uma função é um dos argumentos em uma fórmula com uma função (chamado de aninhamento). Aí podem referenciar variáveis contidas no escopo.
Exemplo: a função
```python
	def double(n):
		return n/2
	print(double(10))
```
pode ser reprentada pela seguinte Lambda:
```python
	double = lambda n:n/2
	print(double(10))
```
Resultando na mesma saída: 5.

Estrutura: (o que tá dentro >disso aqui< é o que será inserido/alterado)
função = nome da função
n = parâmetro necessário pela função (pode adicionar vários, separando cada um com ,)
n/2 = valor de retorno da função
```
	>função< = lambda >n<:>n/2<
```
no print(função(numero)), só é possível retornar 1 número.

 
Exemplo: pequena função como argumento:
```python
	pairs = [(1, 'um'), (2, 'dois'), (3, 'tres'), (4, 'quatro')] #pair é uma tupla, descobri agr
	pairs.sort(key=lambda pair: pair[1])
	print(pairs)
```
Saída:
```python
	[(4, 'quatro'), (1, 'um'), (3, 'tres'), (2, 'dois')]
```



### Strings de documentação
#### Resumo simplificado

- definição de função/método/classe/módulo - da maior parte do código
- __doc__ ou help() 


#### Resumo expandido

A docstring (string de documentação do Python) é uma string literal usada para definir classe, módulo, função ou método. São ideais para entender a funcionalidade, propósito, documentação, recursos da maior parte do código (código em geral).

Estrutura básica: é tipo um comentário de várias linhas mais chique, mas como tá escrito 2 linhas acima, não é só pra explicar uma parte específica e sim para o código/função em geral (propósito).
```python
	def my_function():
	"""Eh so isso, um comentario grande, na linha logo abaixo do q vai explicar, no caso uma função.
 				#linha em branco ta ok
		Eh pra entender funcionalidade em geral dai eh isso. 
		Não esquece de letra maiuscula e ponto final orgulho do saigon.
		Legal ne eu nao achei.
		"""
	pass
	print(my_function.__doc__)
```
Saída:
```
	Eh so isso, um comentario grande, na linha logo abaixo do q vai explicar, no caso uma função.
			#linha em branco ta ok
    Eh pra entender funcionalidade em geral dai eh isso.
    Não esquece da letra maiuscula e ponto final orgulho do saigon.
    Legal ne eu nao achei.
 ```

Uma docstring pode ser acessada pelo atributo __doc__:
-> Para colocar uma docstring de 1 linha: 
```python
	def função(a):
    '''Primeira linha com letra maiúscula e ponto final, orgulho do zolin.'''
	#isso é um comentário pra dizer pra não colocar linha em branco antes/depois da >docstring de 1 linha< ta ok
    return a**a
	print (função.__doc__)
```
Saída:
```
	Primeira linha com letra maiúscula e ponto final, orgulho do zolin.
```

```python
	help(função) 
	Help on function função in module __main__:

	função(a)
```
Saída:
```
	    Primeira linha com letra maiúscula e ponto final, orgulho do zolin.
```
 
Importante aqui: para um objeto, a constante de string vai na primeira instrução na definição. 

-> Docstring de várias linhas
Docstrings de várias linhas segue a estrutura de Docstrings de uma linha, mas é seguida por um único espaço em branco junto com o texto descritivo.
Então fica basicamente assim:
```python
def some_function(argument1):
    """Ta aqui seria tipo titulo bonitinho da explicacao
 
    Bota um parametro aqui so pra rir:
    argument1 (int): Pq eh o nome ne, ai explica aqui blz
 
    Aqui tipo retorno sla:
    int:Returning value

    Ou por exemplo nessa função tu pode usar a docstring pra dizer "ah essa função ela serve para retornar o argument1" tlg?
 
    Nao esquece das letra maiuscula eh isso flw
 
   """

    return argument1
 
print(some_function.__doc__)
```
Saída:
```
	Ta aqui seria tipo titulo bonitinho da explicacao
 
    Bota um parametro aqui so pra rir:
    argument1 (int): Pq eh o nome ne, ai explica aqui blz
 
    Aqui tipo retorno sla:
    int:Returning value

    Ou por exemplo nessa função tu pode usar a docstring pra dizer "ah essa função ela serve para retornar o argument1" tlg?
 
    Nao esquece das letra maiuscula eh isso flw
```
```python
help(some_function)
 
Help on function some_function in module __main__:
 
some_function(argument1)
```
Saída:
```
    Ta aqui seria tipo titulo bonitinho da explicacao
 
    Bota um parametro aqui so pra rir:
    argument1 (int): Pq eh o nome ne, ai explica aqui blz
 
    Aqui tipo retorno sla:
    int:Returning value

    Ou por exemplo nessa função tu pode usar a docstring pra dizer "ah essa função ela serve para retornar o argument1" tlg?
 
    Nao esquece das letra maiuscula eh isso flw
```
Uma coisa que eu achei interessante (foi mta mão achar isso ok) é que funciona também ao importar bibliotecas, segue o fio:
```python
	import math

	print(math.__doc__) #não coloca isso dentro do import pelamor quase se joguei na sanga pq dá erro, alias isso vale pra tudo aqui

	"""Também dá pra pegar uma função da biblioteca que ele explica

	Usando uma docstring pra ficar chique ta ok
	"""
	print(math.sqrt.__doc__) 
	"""aqui eu peço explicação da função sqrt"""
```
Saídas:
```
	This module provides access to the mathematical functions
	defined by the C standard.
	Return the square root of x.

	Process finished with exit code 0
```
- Ok mas, __doc__ ou help()?
__doc__ é usado no geral;
help(função) é usado nas associadas a vários objetos (por exemplo em classes).

### Exercícios
#### Lambda e Docstring:
Escreva um código que retorna 6 nomes em ordem, do menor ao maior (acho que nem preciso falar pra fazer isso com Lambda né). Utilizando docstrings, identifique o que cada parte dele está fazendo (do jeito certo ta ok, estuda ai filho).
Ps: tem que saber algumas funções peculiares de python

[Resolução: sugestão]
```py
	nomes = ["nico", "grandezolin", "jao", "henrynho", "thithi", "henrao"]
	nomes.sort(key = lambda x:len(x))
	print(nomes)
```
```py
	['jao', 'nico', 'thithi', 'henrao', 'henrynho', 'grandezolin']
```



