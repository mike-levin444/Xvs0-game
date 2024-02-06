game_is_on = True
game_matrix = [[None, None, None],
               [None, None, None],
               [None, None, None]]
def gameOver():
    print("Игра закончена!")
def gameUI():
    print("-" * 6, "0", "-" * 3, "1", "-" * 3, "2", "-" * 3)
    n = 0
    for i in game_matrix:
        n += 1
        print(n-1, "|", i, "|")
    print("-" * 6, "0", "-" * 3, "1", "-" * 3, "2", "-" * 3)
gameUI()
def checkWin():
    reference_matrix = [
        game_matrix[0],
        game_matrix[1],
        game_matrix[2],
        [i[0] for i in game_matrix],
        [i[1] for i in game_matrix],
        [i[2] for i in game_matrix],
        [game_matrix[0][0], game_matrix[1][1], game_matrix[2][2]],
        [game_matrix[0][2], game_matrix[1][1], game_matrix[2][0]]
    ]
    for item in reference_matrix:
        result = list(set(item))
        if len(result) == 1 and result[0] != None:
            print("Победил:", result[0])
            exit()

step = 0
while game_is_on:
    step += 1
    print("Ход: ", step)
    if step % 2 == 0:
        coord = input("Ход X в формате: 11 или 22:  ")
        print(coord)
        coordX = coord[0]
        coordY = coord[1]
        move = f"[{coordX}][{coordY}] = \"X\" "
        print(move)
        exec("game_matrix" + move)
    else:
        coord = input("Ход 0 в формате: 11 или 22:  ")
        print(coord)
        coordX = coord[0]
        coordY = coord[1]
        move = f"[{coordX}][{coordY}] = \"0\" "
        print(move)
        exec("game_matrix" + move)
    gameUI()
    checkWin()
    if step > 8:
        gameOver()
        break