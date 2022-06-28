### Sumário


1. [Definindo funções](#definindo-funções)
2. [Argumento com valor padrão](#argumento-com-valor-padrão)
3. [Argumentos nomeados](#argumentos-nomeados)
4. [Expressões Lambda](#expressões-lambda)
5. [Strings de documentação](#strings-de-documentação)
6. [Exercícios & resoluções](#exercícios-e-resoluções)

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




### Argumento com valor padrão
#### Resumo Simplicado
In - Verifica se uma sequência contém ou não um determinado valor.

#### Resumo expandido
É possivel definir funções com um número variável de argumentos
// essas formas podem ser combinadas

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

Dando apenas o argumento Obrigatório :   `perguntar_ok('voce quer realmente sair?')`

Dando um argumento opcional :  `perguntar_ok('Ok para sobrescrever o arquivo?', 2)`

ou dando todos os argumentos : `perguntar_ok('Ok para sobrescrever o arquivo??', 2, 'vamos, apenas sim ou não!)`

Importante:  Valores padrões só são avaliados uma vez. veja que isso fará diferença quando um valor é um objeto mutável, lista, dicionário ou instâncias de classes. 

-> Argumento posicional é o nome utilizado para a passagem de valores onde cada valor estara na ordem conforme implementado na função.


### Argumentos nomeados
#### Resumo simplificado
Essa função chama outros argumentos utilizando
 
`‘’Chave’’ = ‘’valor’’`
A chave seria o nome dado dentro da função

#### Resumo expandido
Exemplo:
```python
def Moitinha ( perfeito, lindo, gostoso,pomposo):
  print('perfeito:{}/nlindo:{}/ngostoso{}/npomposo{}')

Moitinha("perfeitão", lindo="lindão", gostoso='gostoso', pomposo='pomposinho')
```

Importante : 
Nenhum argumento pode receber mais de um valor




### Expressões Lambda
#### Resumo simplificado

- pequenas funções anônimas
- objetos (1 expressão) ou argumento (aninhamento)
- variáveis no escopo
- `>função< = lambda >n<:>n/2<`


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
`>função< = lambda >n<:>n/2<`
no print(função(numero)), só é possível retornar 1 número.

 
Exemplo: pequena função como argumento:
```python
	pairs = [(1, 'um'), (2, 'dois'), (3, 'tres'), (4, 'quatro')]
	#pair é uma tupla, descobri agr
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
- `__doc__` ou `help()`


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

Uma docstring pode ser acessada pelo atributo `__doc__`:
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

	print(math.__doc__) #não coloca isso dentro do import pelamor quase se
	#joguei na sanga pq dá erro, alias isso vale pra tudo aqui

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
- Ok mas, `__doc__` ou `help()`?
`__doc__` é usado no geral;
`help(função)` é usado nas associadas a vários objetos (por exemplo em classes).




### Exercícios e resoluções

#### Definindo funções:
1. Defina uma função que retorne o nome completo de a idade digitada pelo usuário.

2. Resolva a seguintes expressã0 ultilizando uma função: 
	–(–33) + √961 / 2.4

3. Defina uma função que peça 3 números e realize a soma deles.

##### Resolução

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



#### Argumento padrão
Crie uma função de argumento padrão pedindo a senha (12345), dando ate 5 tentativas, chame esse argumento 

##### Resolução:
```
AAAAAAAAAAAAAAAAAAAAAAAAAA
A
A
A

A
A
A

A
A

A
```



#### Lambda e Docstring:
Escreva um código que retorna 6 nomes em ordem, do menor ao maior (acho que nem preciso falar pra fazer isso com Lambda né). Utilizando docstrings, identifique o que cada parte dele está fazendo (do jeito certo ta ok, estuda ai filho).
Ps: tem que saber algumas funções peculiares de python

##### Resolução: sugestão
```py
	nomes = ["nico", "grandezolin", "jao", "henrynho", "thithi", "henrao"]
	nomes.sort(key = lambda x:len(x))
	print(nomes)
```
```py
	['jao', 'nico', 'thithi', 'henrao', 'henrynho', 'grandezolin']
```



