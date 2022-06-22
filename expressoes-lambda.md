#####nico

###Expressões Lambda
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
	```python
	[(4, 'quatro'), (1, 'um'), (3, 'tres'), (2, 'dois')]
```


#### Exercícios

a

#### Resolução

a