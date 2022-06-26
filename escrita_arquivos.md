## Rafaela
### Escrita de arquivos

### Resumo simplificado 

Existem dois tipos de arquivos que podem ser manipulados em python, **arquivos de texto** e **arquivos binários**. A função **open()** para abrir arquivos podemos acessar arquivos só para para leitura, só para escrita e para leitura e escrita.

### Resumo expandido

#### Abrindo arquivos:

Abrir arquivos só para a escrita (write)

```python
arquivo = open('nome_arquivo', 'w')
```

Abrir arquivos só para leitura (read)

```python
arquivo = open('nome_arquivo', 'r')
```

Abrir arquivos para leitura e escrita 

```python
arquivo = open('nome_arquivo', 'r+')
```

Abrir arquivos para anexá-lo. Se o arquivo não existir, ele será criado para gravação.

```python
arquivo = open('nome_arquivo', 'a')
```

Abrir arquivos para leitura e adição.O arquivo é aberto no modo de acréscimo. Se o arquivo não existir, ele será criado para gravação.

```python
arquivo = open('nome_arquivo', 'a+')
```

#### Fechando arquivos:

Escrever **write()** em uma instrução **try**. Dessa forma, você pode lidar com quaisquer exceções e finalmente usá-lo para garantir que o arquivo seja fechado.

```python
arquivo = open('nome_arquivo', 'w')

try:
    arquivo.write('ola mundo!')
finally:
    arquivo.close()
```
#### Leitura de arquivos:

Existem duas maneiras para fazer a leitura de arquivos.

```python
with open('nome_arquivo', 'r') as arquivo:
	texto = arquivo.readlines()
	print(texto)
```

```python
arquivo = open('nome_arquivo', 'r')
texto = arquivo.readlines()
print(texto)
```

#### Leitura e escrita de arquivos json:

Para escrita usamos a função **dump()**.

```python
import json

dados = {

    'nome': 'rafaela',

    'idade': '17'
}
with open('dados.json', 'w') as json_file:
    json.dump(dados, json_file, indent=4)
```

Para leitura usamos a função **load()**.

```python
import json

with open('dados.json', 'r') as json_file:

    dados = json.load(json_file)

print(dados)

print(type(dados))
```

#### Exercícios

1. Faça um código que lê um arquivo JSON e imprime seu conteúdo na tela.
2. Faça um código em Python que leia o conteúdo de um arquivo txt, onde cada linha desse arquivo é um filme do Adam Sandler:

```
click
como se fosse a primeira vez
gente grande
esposa de mentirinha 
arremessando alto
```

3. Faça um código em Python que escreve as 5 melhores músicas do Jão em um arquivo txt.

#### Resolução 

1.

```python
import json

with open('arquivo.json', 'r') as json_file:

    arquivo = json.load(json_file)

print(arquivo)

print(type(arquivo))
```

2.

```python
with open('filmes.txt', 'r') as arquivo:
	texto = arquivo.readlines()
	print(texto)
```

3.

```python
with open('musicas.txt','w') as arquivo:
    for i in musicas_list:  
        arquivo.write('{}\n'.format(i))
```