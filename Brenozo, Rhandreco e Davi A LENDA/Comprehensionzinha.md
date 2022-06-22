### List Comprehension:

#### Resumo simplificado:
Método para criar listas mais precisas.

#### Resumo expandido:
Método mais pratico para a criação de listas, encurtando códigos de várias linhas para apenas uma.

Ex:

#### Lista Padrão:
```python
Lista = []
for x in range(10):
	Lista.append(x*1)

print(Lista)
```

```python
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

#### em List Comprehension:

```python
Lista = [x*1 for x in range(10)]

print(Lista)
```

```python
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```