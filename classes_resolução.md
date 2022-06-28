### Resoluções:

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