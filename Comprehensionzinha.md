### List Comprehension:

#### Resumo Expandido:
Método para criar listas mais precisas, sendo mais pratico, encurtando códigos de várias linhas para apenas uma. `List Comprehension` consiste em um par de colchetes que dentro dele, ira armazenar uma expressão seguida de um for. 


Ex:

#### Lista Padrão:
```python
Lista = []
for x in range(0, 10, 2):
	Lista.append(x*1)

print(Lista)
```

```python
[0, 2, 4, 6, 8]
```

#### em List Comprehension:

```python
Lista = [x*1 for x in range(0, 10, 2)]

print(Lista)
```

```python
[0, 2, 4, 6, 8]
```
