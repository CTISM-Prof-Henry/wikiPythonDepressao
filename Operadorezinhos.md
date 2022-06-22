### Operadores :
**and**	: Retorna True se ambas as afirmações forem verdadeiras. 
**or**	: Retorna True se uma das afirmações for verdadeira.
**not**	: Retorna False se o resultado for verdadeiro.
**in**	: Retorna True caso o valor seja encontrado na sequência.
**not in** : Retorna True caso o valor não seja encontrado na sequência.

### and
```python 
Numero = 4
Numero2 = 7
if Numero > 3 and Numero2 < 8:
    print("As Duas condições são verdadeiras")
```
```python
As Duas condições são verdadeiras
```
### or
```python
Numero = 3
Numero2 = 8
if Numero > 4 or Numero2 <= 8:
    print("Uma ou duas das condições são verdadeiras")
```
```python
Uma ou duas das condições são verdadeiras
```
### not
```python
Numero = 2
Numero2 = 9
if Numero > 3 and Numero2 < 8:
    print("As Duas condições são verdadeiras")
if not(Numero > 3 and Numero2 < 8):
    print("Nenhuma das duas estão corretas")
```
```python
Nenhuma das duas estão corretas
```
### in 
```python
Lista = [1 , 2 , 3 , 4 , 5]
if(4 in Lista):
    print("4 está na lista")
```
```python
4 está na lista
```
### not in
```python
Lista = [1 , 2 , 3 , 4 , 5]
if(6 in Lista):
    print("6 está na lista")
if(6 not in Lista):
    print("6 não está na lista")
```
```python
6 não está na lista
```
