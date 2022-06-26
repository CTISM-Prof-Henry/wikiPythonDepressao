# Laços de repetição:
#### **Sumário**
1- [For e While](#**for**)
2- Função range
3- [Break](#break)
4- Continue
5- Exercícios
## Introdução

### Resumo simplificado

**Laços de repetição**: são estruturas que têm o controle do programa, que se utiliza para repetir a execução de um bloco de código quando a sua condição for verdadeira.

### Resumo expandido

O laço mais conhecido como **for**, é utilizado para realizar um número fixo de iterações, e o laço que é indeterminado **while**, ele é usado quando não se sabe quantas iterações serão necessárias antes do início do laço. Para o **for** se repetir, é necessário a coleção iterada deve conter mais itens. Quanto ao laço **while**, a condição lógica é verificada antes de cada iteração, e o laço continua somente se esta condição for avaliada como true.
Em alguns casos, muitas vezes é necessário executar a mesma instrução (ou grupo de instruções) executada várias vezes seguidas. Nesses casos, geralmente usamos um loop (ou laço de repetição), que permite que um bloco de código seja executado repetidamente quando uma determinada condição for atendida.
Em Python, os loops são codificados usando instruções **for** e **while**. A primeira nos permite iterar sobre os itens da coleção e executar um bloco de código para cada item. Por outro lado, **while** executa um conjunto de instruções várias vezes quando uma condição é atendida.

**Exemplo do uso do comando for**:
```python 
Nomes = ['Jorge da Borracharia', 'Jucelina Kubistschek', 'Zezin du Pineu'] 
for n in Nomes: 
print(n)
```

**Exemplo do uso do comando while**:
```python
Contador = 0 
while Contador < 10: 
    print(Contador) 
    Contador = Contador + 2
```

A função de nome **range**, é a função que volta uma série numérica em um intervalo de tempo enviando como argumento. A série que retorna é iterável tipo range e os elementos que são contidos são gerados sob demanda.

**Exemplo de range**:
```python
for X in range(20): 
    print(X)
```

A instrução **break** oferece a possibilidade de sair do loop quando a condição externa é acionada. A instrução break será colocada dentro do bloco de código abaixo da instrução loop, normalmente após a instrução if condicional. Neste mini programa, o número da sua variável é iniciado em 0.

**Exemplo de break**:
```python
x = 0 
while(x<40): 
    x+=4
    if(x==10): 
        print("Interrompendo a execução da repetição.") 
        break 
    print(x)
```
 
O laço de repetição **continue** impedir a execução do ciclo sem impedir a execução do laço. A instrução continue assim como a instrução break são instrumentos das estruturas de repetição deixando a interrupção de um ciclo ou de um laço de repetição.

**Exemplo de continue**: 
```python
numero = 1 
for numero in range(20): 
    if numero == 0: 
        continue 
    print('Numero é ' + str(numero)) 
print('Fora do seu alcance')
```
 
Exercícios
 
Resolução
 

