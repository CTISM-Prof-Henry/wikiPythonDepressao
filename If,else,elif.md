### Introdução

# Nicolle Moreira E Kamilli Razera

### Sumário

1. [Resumo simplificado](#Resumo-simplificado)
2. [Resumo expandido](#Resumo-expandido)
3. [Exercícios](#Exercícios)
4. [Resolução](#Resolução)

# if, else e elif

#### Resumo simplificado

If, Else e elif são comandos de desvio de fluxo.

### Resumo expandido 

If (se) é uma condicional que permite avaliar se a expressão é afirmativa.

## Exemplo de if
````python
if <condição_verdadeira>:
<faça_alguma_coisa>
````

Else (se não) é a condicional que avalia se a condição é negativa. (só pode existir o else se existir o if.)

## Exemplo de else
````python
if <condição_verdadeira>:
<faça_algo>
else:
<faça_outra_coisa>
````

Elif (se não se) é a junção de else + if, é utilizado para verificar a outra expressão caso a primeira seja falsa, ele faz com que as condições sejam interligadas (se ele satisfizer uma condição ele não verifica as outras). 

## Exemplo de elif
````python
if <condição_verdadeira>:
(rode_o_primeiro_código())
elif <segunda_condição_verdadeira>:
(rode_o_segundo_código())
````
### Exercícios

### Exercício 1:
1. Faça um programa que leia dois números e imprima o menor:

### Resolução
````python
 a = int(input('digite um numero'))
b = int(input('digite um numero'))
if a < b:
   print('o menor numero é', a)
else:
   print('o menor número é', b)
````
### Exercício 2: 

2. Faça um programa para ver se algo ou alguma coisa é novo ou velho, se a idade for maior que 4 é velho e menor ou igual a 4 é novo.

### Resolução
````python
idade = int(input("digite a idade:"))
if idade <= 4:
   print("Seu cachorro é novo")
else:
   print("seu cachorro é velho")
````

### Exercício 3: 

3. Faça um programa para determinar a situação escolar do aluno.(aprovado,reprovado,recuperação)

### Resolução 
````python
nota = int(input("Digite uma nota: "))
if nota < 70:
    print("Reprovado")
elif nota > 50:
    print("Aprovado")
else:
    print("Recuperação")

print("fim.")
````



