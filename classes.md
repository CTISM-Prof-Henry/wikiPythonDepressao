## Classes:

### Sumário:
1. [Exercícios](classes_exercícios.md)
2. [Resolução](classes_resolução.md)

### RESUMO SIMPLIFICADO:
Classes, dentro da linguagem de programação Python, tem a função de otimizar o código e deixar ele mais legível, também servem para fazer um agrupamento de funções, funcionando como um, atributos de um objeto dentro da programação

### RESUMO EXPANDIDO:
Primeiramente vamos relembrar o que é Python?
 Python é uma das três linguagens de programação mais utilizadas no mundo por ser extremamente versátil, interativa e fácil de ser aprendida.
Ela é uma linguagem interpretada e fracamente tipada. Agora vamos estudar classes em python com mais detalhes:

#### Sintaxe de definição de classes:

   Criação de classes é bem simples e nos permite definir quais atributos e métodos uma classe
irá possuir, Mas como eu começo uma classe? como tranformo em código? Isso que vamos
descobrir agora!
   Vou usar um exemplo simples de uma caneta na qual os atributos vão ser cor e marca e o
método será exibir as informações sobre ela.
```python
class Caneta:#O Caneta será sua class. A palavra class seguida do nome da classe, por convenção a primeira letra se usa letra maiúscula
 def __init__(self, cor, marca): #Método montador, como todo método ele precisa receber self como argumento e esse método o nome dele é padrão que é "duas anderlaines init 2 anderlaines" e ele também recebe os atributos da classe que nesse exemplo é a cor e marca.
 self.cor = cor
 self.marca = marca
 #o self serve para que você acesse as propriedades de uma instância, sejam elas propriedades ou métodos

 def ExibirInformacoesDaCaneta(self): #aqui é o método (verá a explicação mais detalhada sobre ele mais em baixo)
 print(self.cor, self.marca)

caneta1 = Caneta('caneta1 - cor: rosa', 'marca: bic')
caneta1.ExibirInformacoesDaCaneta()
caneta2 = Caneta('caneta2 - cor: azul', 'marca: faber castell')
caneta2.ExibirInformacoesDaCaneta()
```
#### Objetos método
   Um método é uma função que é criada dentro de uma classe em python!
exemplo 1: Você quer definir a classe de um "cachorro" e os métodos (funções) vão ser: respirar, comer, beber, entre outros...
exemplo 2: uma classe com várias pessoas que os métodos seriam como por exemplo falar, andar, comer, entre outros... Todos essas ações são métodos de classes, e lembrando que métodos podem ou não retornar um valor.
Agora vamos trasformar o exemplo 1 em código?
```python
class Cachorro:

 def __init__(self): #método montador, para afim desse exemplo está vazio
 pass

 def respirar(self):
 print('respirou')
 def comer(self):
 print('comeu')
 def beber(self):
 print('bebeu')

def main():
 cachorro = Cachorro()
 cachorro.respirar()
 cachorro.comer()
 cachorro.beber()

main()
```
