### Sumário

1. [Definindo funções](#link)
2. [Argumento com valor padrão](#link)
3. [Argumentos nomeados](#link)
4. [Expressões Lambda](#expressões-lambda)
5. [Strings de documentação](#strings-de-documentação)
6. [Exercícios](#exercícios)
7. [Resoluções](#resolução)


### Expressões Lambda
#### Resumo simplificado

- pequenas funções anônimas
- objetos (1 expressão), argumento (aninhamento)
- variáveis no escopo
- “lambda” - a, b: a+b;


#### Resumo expandido

   “lambda” é a palavra-chave para definir pequenas funções anônimas em Python, é uma forma mais sucinta de definir uma função.
Uma função lambda retorna nada mais nada menos que a soma de seus 2 argumentos: 
```python
	lambda a, b: a+b;
```
Podem ser usadas para representar objetos função, que ficam restritos a uma expressão;
	Ou como argumento, onde uma função é um dos argumentos em uma fórmula com uma função (chamado de aninhamento). Aí podem referenciar variáveis contidas no escopo.
Exemplo: expressão lambda para retornar uma função:
```python
	def make_incrementor(n):
return lambda x: x + n
	f = make_incrementor(42)
	f(0) #saída = 42
	f(1) #saída = 43
```
 
Exemplo: pequena função como argumento:
```python
	pairs = [(1, 'um'), (2, 'dois'), (3, 'tres'), (4, 'quatro')] #pair é uma tupla, descobri agr
	pairs.sort(key=lambda pair: pair[1])
	pairs
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
texto pra caraio aqui, dps eu faço
[docs python](https://docs.python.org/pt-br/3.9/tutorial/controlflow.html#documentation-strings "docs.python.org") <br />
[datacamp](https://www.datacamp.com/tutorial/docstrings-python "datacamp.com") <br /> 
[programiz](https://www.programiz.com/python-programming/docstrings "programiz.com") <br />


Estrutura básica:
```python
	def my_function():
	"""Eh so isso, um comentario grande.
 				#linha em branco ta ok
		Eh pra entender funcionalidade em geral dai eh isso. 
		Não esquece de letra maiuscula e ponto final orgulho do saigon.
		Legal ne eu nao achei.
		"""
	pass
	print(my_function.__doc__)
```
Saída:
```python
	Eh so isso, um comentario grande.
			#linha em branco ta ok
    Eh pra entender funcionalidade em geral dai eh isso.
    Não esquece da letra maiuscula e ponto final orgulho do saigon.
    Legal ne eu nao achei.
 ```

   A docstring (string de documentação do Python) é uma string literal usada para definir classe, módulo, função ou método. São ideais para entender a funcionalidade, propósito, documentação, recursos da maior parte do código
Uma docstring é acessada pelo atributo __doc__:
 (para um objeto - constante de string na primeira instrução na definição) ou pelo help(função) (função integrada)
-> Para colocar uma docstring de 1 linha: 
```python
	def função(a):
    '''Primeira linha com letra maiúscula e ponto final, saco.'''
	#isso é um comentário pra dizer pra não colocar linha em branco antes/depois da >docstring de 1 linha< ta ok
    return a**a
	print (função.__doc__)
```
Saída:
```python
	Primeira linha com letra maiúscula e ponto final, saco.
```

```python
	help(função) #mais detalhada que __doc__
	Help on function função in module __main__:

	função(a)
```
Saída:
```python
	    Primeira linha com letra maiúscula e ponto final, saco.
```
 
-> Docstring de várias linhas
Docstrings de várias linhas também contém a mesma linha de literais de string que em Docstrings de uma linha, mas é seguida por um único espaço em branco junto com o texto descritivo.
O formato geral para escrever uma Docstring de várias linhas é o seguinte:
```python
def some_function(argument1):
    """Ta aqui seria tipo titulo bonitinho da explicacao
 
    Bota um parametro aqui so pra rir:
    argument1 (int): Pq eh o nome ne, ai explica aqui blz
 
    Aqui tipo retorno sla:
    int:Returning value
 
    Nao esquece das letra maiuscula eh isso flw
 
   """

    return argument1
 
print(some_function.__doc__)
```
Saída:
```python
	Ta aqui seria tipo titulo bonitinho da explicacao

    Bota um parametro aqui so pra rir:
    argument1 (int): Pq eh o nome ne, ai explica aqui blz
 
    Aqui tipo retorno sla:
    int:Returning value
 
    Nao esquece das letra maiuscula eh isso flw
 
help(some_function)
 
Help on function some_function in module __main__:
 
some_function(argument1)
    Ta aqui seria tipo titulo bonitinho da explicacao
 
    Bota um parametro aqui so pra rir:
    argument1 (int): Pq eh o nome ne, ai explica aqui blz
 
    Aqui tipo retorno sla:
    int:Returning value
 
    Nao esquece das letra maiuscula eh isso flw
```

### Exercícios
#### Docstring:
Identifique o que o codigo está fazendo, colocando strings (do jeito certo ta ok, estuda ai filho) no máximo de lugares possível (é pra ficar gigante mesmo tipo eu tlg)


### Resoluções

a

