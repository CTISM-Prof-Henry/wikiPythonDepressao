### Resolução:
1.
```python
list = [1,2,3,4,5,6,7,8]
	list.append(9)

print(list)

	list.remove(9)

print(list)
```

```python
[1, 2, 3, 4, 5, 6, 7, 8, 9]
[1, 2, 3, 4, 5, 6, 7, 8]
```

2.
```python
lista = [9,7,3,5,0,1,2,3]
lista.sort()

print(lista)
```

```python
[0, 1, 2, 3, 3, 5, 7, 9]
```

```python
lista = [6,5,3,9,1,4,7,8]
lista.sort()

print(lista)
```

```python
[1, 3, 4, 5, 6, 7, 8, 9]
```

3. 
```python
lista = [1,2,3,4,5,6,12,7,8,9,0]
lista2 = [190, 12, 192, 191, 12, 9]

lista.extend(lista2)

print(lista)

lista.count(12)

print(lista.count(12))
```

```python
[1, 2, 3, 4, 5, 6, 12, 7, 8, 9, 0, 190, 12, 192, 191, 12, 9]
3
```

4.
```python
Numero = 5
Numero = 7
if Numero > 4 or Numero2 < 8:
	print("Estes são maiores que 4 e menores que 8")


```

```python
Estes são maiores que 4 e menores que 8
```

5.
```python
Lista = [x*1 for x in range(0, 50, 5)]

print(Lista)
```

```python
[0, 5, 10, 15, 20, 25, 30, 35, 40, 45]
```