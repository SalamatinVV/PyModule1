players = ['Вася', 'Ваня', 'Рома', 'Артём', 'Владик', 'Вовчик', 'Коля', 'Саня', 'Ваня2', 'Гоша']

amountPlayers = len(players)

firstTeam = players[:(amountPlayers//2)]

secondTeam = players[(amountPlayers//2):]

print(firstTeam)
print(secondTeam)