## Métodos da classe lista :
### list.**append**(x)

Adiciona um novo item ao fim da lista.
Ex :
```python
lista = [ ‘rhandres’ , ‘davi’ , ‘breno’ ]
lista.append('breno falta aula')

print(lista)
```
```python
['rhandres' , 'davi' , 'breno' , 'breno falta aula']
```
### list.**remove**(x)
Remove um item da lista.
Ex :
```python
lista = [‘rhandres’ , ‘davi’ , ‘breno’ , 'breno falta aula']
lista.remove('breno')

print(lista)
```
```python
['rhandres' , 'davi' , 'breno falta aula']
```
### list.**extend**(iterable)
Faz a junção de duas listas.
Ex :
```python
lista = [‘rhandres’ , ‘davi’ , ‘breno’]
lista2 = ['breno falta aula']
lista.extend(lista2)

print(lista)
```
```python
['rhandres' , 'davi' , 'breno' , 'breno falta aula']
```
### list.**insert**(i,x)
Adiciona um item a lista, na posição determinada pelo usuário, iniciando a contagem a partir do 0.
Ex :
```python
lista = [‘rhandres’ , ‘davi’ , ‘breno’ , 'breno falta aula']
lista.insert(2,'o theo ta mal')

print(lista)
```
```python
['rhandres' , 'davi' , 'o theo ta mal' , 'breno' , 'breno falta aula']
``` 

### list.**pop**([i])
Remove um item a lista, na posição determinada pelo usuário, iniciando a contagem a partir do 0. Ação opcional, se não dado um índice ele irá remover o último item da lista.
Ex :
```python
lista = [‘rhandres’ , ‘davi’ , 'o theo ta mal' , ‘breno’ , 'breno falta aula' ,]
lista.pop(2)

print(lista)
```
```python
['rhandres' , 'davi' , 'breno' , 'breno falta aula']
```

### list.**clear**()
Remove todos itens da lista. Para esta ação também pode ser usado o `del lista[:]`
Ex :
```python
lista = [‘rhandres’ , ‘davi’ , 'o theo ta mal' , ‘breno’ , 'breno falta aula' ]
lista.clear()

print(lista)
```
```python
[]
```

### list.**count**()
Conta a quantidade de vezes que o item aparece na lista.
Ex :
```python
lista = ['rhandres' , 'davi' , 'o theo ta mal' , 'breno' , 'breno falta aula' , 'breno' ]
lista.count('breno')

print(lista.count('breno'))
```
```python
2
```

### list.**index**()
Informa o índice do item selecionado pelo usuário, podendo ser usado indices para determinar o inicio e o fim. Caso o valor não esteja presente na lista o programa irá retornar `ValueError` 
Ex :
```python
lista = ['rhandres' , 'davi' , 'o theo ta mal' , 'breno' , 'breno falta aula' , 'breno' ]
lista.index('breno', 0, 4)

print(lista.index('breno', 0, 4))
```
```python
3
```

### list.**sort**()
Ordena os itens de uma lista de acordo com a informação passada pelo usuário.
Ex :
```python
lista = [1 , 3 , 8 , 5 , 7]
lista.sort()

print(lista)
```
```python
[1 , 3 , 5 , 7 , 8]
```
Ou
```python
lista = [1 , 3 , 8 , 5 , 7]
lista.sort(reverse=True)

print(lista)
```
```python
[8 , 7 , 5 , 3 , 1]
```

### list.**reverse**()
Inverte a ordem da lista.
Ex :
```python
lista = ['rhandres' , 'davi' , 'o theo ta mal' , 'breno' , 'breno falta aula' , 'breno' ]
lista.reverse()

print(lista)
```
```python
['breno' , 'breno falta aula' , 'breno' , 'o theo ta mal' , 'davi' , 'rhandres']
```

### list.**copy**()
Faz uma cópia rasa da lista. Podendo ser usado também o `a[:]`
Ex :
```python
lista = ['rhandres' , 'davi' , 'o theo ta mal' , 'breno' , 'breno falta aula' , 'breno' ]
lista.copy()

print(lista.copy())
```
```python
['rhandres' , 'davi' , 'o theo ta mal' , 'breno' , 'breno falta aula' , 'breno' ]
```

