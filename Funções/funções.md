## Funções 

### Definindo Funções

#### Resumo simplificado

```python
def nome(arg, arg, ... arg):
	comando
	...
	comando
```

`def` - define;
`nome` - é o nome da função;
`arg` - especificação de argumento da função, que podem ser nenhum ou vários;
`comandos` - é onde contém o que deve ser executado quando essa função é chamada.


#### Resumo Expandido

Para definir uma função em Python, utilizamos o comando `def`, que significa literalmente definir. Após `def`, o nome da função deve ser estabelecido, seguido pelos parâmetros formais, os argumentos, entre parênteses.
Uma função normalmente computa um ou mais valores. Como sempre há um específico a ser retornado no final, usa-se o comando `print` ou `return`, seguido pelo valor a ser retornado. A função termina e retorna ao ponto onde a mesma foi chamada. Observe o exemplo a seguir.

```python
def parabens():
	print('parabens pra voce \n nessa data querida \n muitas felicidades \n muitos anos de vida \n')

parabens()
```
```python
parabens pra voce 
nessa data querida  
muitas felicidades 
muitos anos de vida
```

Para verificar se algo digitad por um usuário possui algo pré definido no código, usarem `if` e `else`, seguido, nesse caso, pela letra que queremos identificar e pelo comando `in`, que irá percorrer a variável definida após até encontrar o que foi pedido na frase digitada pelo usuário. 

```python
def temLetrau():
	frase = input('Digite uma frase: ')
	if 'u' in frase:
		print('Voce utilizou a letra u.')
	else:
		print('Voce nao utilizou a letra u.')

```
```python
Digite uma frase: o dia esta bonito
Voce nao utilizou a letra u.
```
```python
Digite uma frase: o dia esta nublado
Voce utilizou a letra u.
```

Agora, definindo uma função com números.

```python
def somaQuadrado(a,b):
	somaQ = a**2 + b**2
	return somaQ

somaQuadrado(2,3)
```
```python
13
```
Repare que os parâmetros `a` e `b` não foram definidos, deixando para fazê-lo no momento de chamar a função.


#### Exercícios
1. Defina uma função que retorne o nome completo de a idade digitada pelo usuário.

2. Resolva a seguintes expressã0 ultilizando uma função: 
	–(–33) + √961 / 2.4

3. Defina uma função que peça 3 números e realize a soma deles.

#### Resolução

1. 
```python
def dados():
	nome = input('Digite seu nome completo: ')
	frase = input('Digite sua idade: ')

dados()
```
```python
Digite seu nome completo: Thianna Lara Kovalesky Hartmann
Digite sua idade: 16
```

2. 
```python
def expressao(a,b,c,d):
	a = -33
	b = 961
	c = 2
	d = 4
	raiz = math.sqrt(b)
	- a + raiz / c * d

expressao()
```
```python
8
```

3. 
```python
def soma(a,b,c):
	a = input('Digite um numero: ')
	b = input('Digite outro numero: ')
	c = input('Digite mais um numero: ')
	resultado = a + b + c
	print('A soma desses tres numeros eh' resultado)

soma()
```
```python
Digite um numero: 10
Digite outro numero: 45
Digite mais um numero:18
A soma desses tres numeros eh 73
```
