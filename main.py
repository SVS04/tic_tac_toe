# Функция, которая отображает матрицу
def show_board(board):
    for row in board:
        print(row)


# Функция, которая проверяет, выиграл ли один из игроков
def check_win(board, player):
    # Проверяем горизонтали
    for row in board:
        if row.count(player) == 3:
            return True

    # Проверяем вертикали
    for col in range(3):
        if board[0][col] == player and board[1][col] == player and board[2][col] == player:
            return True

    # Проверяем диагонали
    if board[0][0] == player and board[1][1] == player and board[2][2] == player:
        return True
    if board[0][2] == player and board[1][1] == player and board[2][0] == player:
        return True

    return False


# Функция, которая запрашивает у игрока номер ячейки и проверяет его корректность
def get_input(player):
    while True:
        try:
            move = int(input(f"Ход игрока {player}: "))
            if move < 1 or move > 9:
                print("Ошибка: выберите номер ячейки от 1 до 9!")
            else:
                return move
        except ValueError:
            print("Ошибка: введите число от 1 до 9!")


# Основной цикл игры
board = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
players = ["X", "O"]
current_player = 0
moves_left = 9

while True:
    # Отображаем текущее состояние игры
    show_board(board)

    # Запрашиваем номер ячейки у текущего игрока
    move = get_input(players[current_player])
    row = (move - 1) // 3
    col = (move - 1) % 3

    # Проверяем, что ячейка свободна
    if board[row][col] == "X" or board[row][col] == "O":
        print("Ошибка: ячейка занята!")
        continue

    # Помещаем символ на доску
    board[row][col] = players[current_player]

    # Проверяем, выиграл ли игрок
    if check_win(board, players[current_player]):
        show_board(board)
        print(f"Игрок {players[current_player]} победил!")
        break

    # Проверяем, закончилась ли игра вничью
    moves_left -= 1
    if moves_left == 0:
        show_board(board)
        print("Ничья!")
        break

    # Переключаемся к другому игроку
    current_player = (current_player + 1) % 2
