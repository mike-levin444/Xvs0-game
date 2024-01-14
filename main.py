game_matrix = [[None, None, None],
               [None, None, None],
               [None, None, None]]

game_is_on = True
def gameUI():
    print("-" * 6, "0", "-" * 3, "1", "-" * 3, "2", "-" * 3)
    n = 0
    for i in game_matrix:
        n += 1
        print(n-1, "|", i, "|")
    print("-" * 6, "0", "-" * 3, "1", "-" * 3, "2", "-" * 3)
gameUI()

step = 0
while game_is_on:
    move = input("Введите ход в формате: [*][*] = \"X\" Или [*][*] = \"0\":  ")
    print(move)
    exec("game_matrix" + move)
    gameUI()
    step += 1
    print("Ход: ", step)
    if step > 9:
        print("Конец игры")
        break