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
