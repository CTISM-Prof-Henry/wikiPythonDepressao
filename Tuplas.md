
# *Tuplas*

Tuplas é um tipo de coleção, semelhante às listas, mas a maior diferença entre elas é que uma tupla é imutável. Ou seja, após criada uma tupla com determinados valores, eles não podem mais ser alterados.
Os valores em uma tupla são arnazenados em  uma sequencia heterogênea, que podem ser acessados por desempacotamento ou índices.
As tuplas vazias são feitas por parênteses vazios:
```python
Tupla = ()
Desempacotamento:
Tupla = ('migloro', 'jesus', 'Henry')
Nome1, Nome2, Nome3 = Tupla

Caso você queira crirar uma TUPLA com apenas um valor atribuído, lembre-se que é necessário incluir uma virgula no final!

```python
Tupla = ('a',) – (Tupla)

	DIFERENTE

Tupla = ('a') – (STR)
```

As tuplas podem parecer inúteis, já que não é possível altrerar seus valores. Mas podem ser úteis para armazenar dados que não devem ser alterados nunca, como CPFs, por exemplo. Ou corrdenaddas, ou meses do ano, etc.
Caso tentemos mudar algum valor de uma tupla, o interpretador dára um aviso de erro.
PARA CRIAR UMA TUPLA:
```python

Tupla = (2, 3, 4, 5)

DIFERENCA ENTRE TUPLA E LISTAS:
Tupla = (2, 3, 4, 5)
Lista = [2, 3, 4, 5]
```

# *Exemplo de TUPLAS para realizar:*

### 1. Faca uma tupla com 5 valores e adicione essa tupla dentro de uma lista


### 2. Faca uma tupla com 5 valores e adicione essa tupla dentro de uma lista e mostre apenas os valores da tupla


# *Resolução*:

### 1. Faca uma tupla com 5 valores e adicione essa tupla dentro de uma lista:

```python
tupla = (1, 2, 3, 4, 5)
lista = []

lista.append(tupla)

print(lista)
```


### 2. Faca uma tupla com 5 valores e adicione essa tupla dentro de uma lista e mostre apenas os valores da tupla

```python
tupla = (1, 2, 3, 4, 5)
lista = ['artur', 'miguel']

lista.append(tupla)

print(lista[2])
```


# *CONJUNTOS (SETs)*


 ### Conjuntos são coleções desordenadas com elementos únicos – desordenada porque a cada vez que é “chamada” os elementos podem aparecer em uma ordem diferente, o que não permite selecionar itens por índices; e de elementos únicos porque, caso ocorra a repetição de algum elemento, as “cópias” serão apagadas, restando apenas um elemento que possui aquele valor, não havendo repetição dos elementos.
Um conjunto pode ser definido usando-se elementos entre chaves “{}”:
conj = {1,2,3,4}

Existem algumas funções que podem ser utilizadas com os conjuntos:
```python  
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
União:
print(a.union(b))
set([1, 2, 3, 4, 5, 6])
Interseção:
print(a.intersection(b))
set([3, 4])
```

Podemos utilizar essas funções com listas, desde que convertamos uma delas para conjuntos (sempre o primeiro da expressão:
```python
lista1 = [1, 2, 3]
lista2 = [2, 4, 3]
print(set(lista1).intersection(lista2))
set([2, 3])
```

# Diferença:
Retira os elemenntos comuns entre 2 conjuntos, deixando apenas os elementos do primeiro conjunto que não estão no segundo:
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.difference(b))
set([1, 2])
print(b.difference(a))
set([5, 6])
```

# Diferença Simétrica:
Semelhante a Diferença, mas mantém os elementos de ambos os conjuntos (primeiro e segundo) que não são comuns a ambos:
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
print(a.symmetric_difference(b))
set([1, 2, 5, 6])
```

Para verificar se um elemento pertence a um conjunto, podemos usar o operador “in”:
```python
a = {1, 2, 3, 4}
b = {3, 4, 5, 6}
1 in a:
True
5 in a:
False
```

 Verificar se um conjunto é um subconjunto de outro:
```python
a = {1, 2, 3, 4}
c = {1, 2}
c.issubset(a):
True
a.issubset(c):
False
```

 Verificar se um conjunto é superconjunto de outro:
```python
a.issuperset(c):
True

Podemos checar a disjunção entre dois conjuntos. Dois conjuntos são disjuntos se tiverem interseção nula:
c = {1, 2}
d = {3, 4}
c.isdisjoint(d):
True
```

# *Exemplo de SETS para realizar:*

### Use a funcao discard ou remove para retirar os numeros 2 do set.
```python
	nums = set([1, 2, 2, 3, 3, 3])
```

# *Resolução*
	
```python
	nums = set([1, 2, 2, 3, 3, 3])
	nums.remove(2)
	print("Números: ", nums)
```
	

