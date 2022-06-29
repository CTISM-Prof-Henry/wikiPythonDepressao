

# 1 
`print("Digite o respectivo número para escolher o seu shake [1] Banana + leite + aveia [2] Leite + Pasta de amendoim + aveia + morango [3] Leite + WheyProtein + aveia + banana")`

`shake = int(input('Escolha : '))`
`if shake == 1:`
    `print('Você escolheu o shake com Banana, leite e aveia')`
    `shake = {"banana":100, "Leite":120, "aveia":100}`

`elif shake == 2:`
    `print('Você escolheu o shake com Leite, pasta de amendoim, aveia e morango')`
    `shake = {"pasta de amendoim":100, "Leite":120, "aveia":100, "morango":30}`

`elif shake == 3:`
    `print("Você escolheu o shake com Leite, WheyProtein, aveia e banana")`
    `shake = {"Leite":120, "WheyProtein":130, "aveia":100, "banana":100}`

`for cada_ingrediente, calorias in shake.items():`
    `print(f"O ingrediente {cada_ingrediente}  tem {calorias} calorias")`

# 2 

`materiais = {'lapis':2, 'caneta':4, 'borracha':6, 'apontador':5, 'tesoura':10}`

`for cada_material, preco in materiais.items():`
`print(f'O preços do material {cada_material} é: {preco} reais')`
`print()`
`print()`
`for cada_material, preco in materiais.items():`

`quantidade = int(input(f'Digite a quantidade de {cada_material} que deseja: '))`
    `print(f'Você pagará: {preco*quantidade} reais em {cada_material} ')`

# 3 

    
`valor1 = int(input('Digite um primeiro número:'))
valor2 = int(input('Digite um segundo número:'))
valor3 = int(input('Digite um terceiro número:'))
dicionario = {'Primeiro Valor': valor1, 'Segundo Valor': valor2, 'Terceiro Valor': valor3}
for teste, valores in dicionario.items():
    if valores > 0:
        print(f'O {teste} {valores} é positivo')
    elif valores == 0:
        print(f"O {teste} {valores} é nulo (ZERO)")
    
    else:
        print(f'O {teste} {valores} é negativo')
        
     
        

