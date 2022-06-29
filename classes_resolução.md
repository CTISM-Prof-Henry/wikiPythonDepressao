### Resoluções:🔝

exercício 1:
```python
class Série:
 def __init__(self, nome, personagem_favorito, temporadas):
 self.nome = nome
 self.personagem_favorito = personagem_favorito
 self.temporadas = temporadas

 def ExibirInformacoesDaSerie(self):
 print(self.nome, self.personagem_favorito, self.temporadas)

série = Série('nome: You', 'personagem_favorito: Love', 'temporadas: 3')
série.ExibirInformacoesDaSerie()
```

exercício 2:
```python
class Filosofia:

    def __init__(self, nome, barba):
        self.nome = nome
        self.barba = barba
        
    def andardeskate(self):
        print('andou de skate!')
    

zolin = Filosofia('Zolin','da barba longa')
print(zolin.nome, zolin.barba) 
zolin.andardeskate()
```