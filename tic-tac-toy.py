import random

X = 'X'
O = 'O'
EMPTY = " "
TIE = "Ничья"
NUMBER_FIELDS = 9

def instruction():
    """Выводит на экран инструкцию для игрока."""
    print("Это инструкция для игры в 'крестики-нолики':")
    print(
"""
Чтобы сделать ход введите число от 0 до 8. Число однозначно соответсвует полям
доски - так как показано ниже:
0 | 1 | 2
---------
3 | 4 | 5
---------
6 | 7 | 8\n"""
)

def random_selection():
    """Случайно выбирает игрока который будет первым совершать свой ход в игре и выводит результат"""
    number = random.randint(1,20)
    if number < 11:
        human = X
        computer = O
        print("Первый ход за тобой!")
        return human, computer
    else:
        human = O
        computer = X
        print("Первый ход за компьютером!")
        return human, computer

def ask_number(question, low, high):
    """Просит ввести число из диапазона"""
    responce = None
    while responce not in range(low, high):
        responce = int(input(question))
    return responce


def new_board():
    """Создает новую доску"""
    board = []
    for number in range(NUMBER_FIELDS):
        board.append(EMPTY)
    return board

def display_board(board):
    """Отображает игровую доску на экран"""
    print(board[0], "|", board[1], "|", board[2])
    print("---------")
    print(board[3], "|", board[4], "|", board[5])
    print("---------")
    print(board[6], "|", board[7], "|", board[8])

def legal_moves(board):
    """Создает список доступных ходов"""
    moves = []
    for number in range(NUMBER_FIELDS):
        if board[number] == EMPTY:
            moves.append(number)
    return moves

def winner(board):
    """Определяет победителя в игре"""
    WAYS_TO_WIN = ((0,1,2),
                   (3,4,5),
                   (6,7,8),
                   (0,3,6),
                   (1,4,7),
                   (2,5,8),
                   (2,4,6),
                   (0,4,8))

    for row in WAYS_TO_WIN:
        if board[row[0]] == board[row[1]] == board[row[2]] != EMPTY:
            winner = board[row[0]]
            return winner
        if EMPTY not in board:
            return TIE

def human_move(board, human):
    """Получает ход человека"""
    legal = legal_moves(board)
    move = None
    while move not in legal:
        move = ask_number("Выбери поле(0-8):", 0, NUMBER_FIELDS)
        if move not in legal:
            print("Это поле уже занято")
    return move

def computer_move(board, computer, human):
    """делает ход за компьютер"""
    board = board[:]
    BEST_MOVES = (4,0,2,6,8,1,3,5,7)
    print("Я выберу поле № ", end = " ")

    for move in legal_moves(board):
        board[move] = computer

        if winner(board) == computer:
            print(move)
            return move
        board[move] = EMPTY

    for move in legal_moves(board):
        board[move] = human

        if winner(board) == human:
            print(move)
            return move
        board[move] = EMPTY

    for move in BEST_MOVES:
        if move in legal_moves(board):
            print(move)
            return move

def next_turn(turn):
    """Осуществляет переход хода"""
    if turn == X:
        return O
    else:
        return X

def congrat_winner(the_winner, computer, human):
    """Поздравляет победителя игры"""

    if the_winner != TIE:
        print("Winner is", the_winner)
    else:
        print("Ничья")


def main():
    instruction()
    human, computer = random_selection()
    turn = X
    board = new_board()

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board,computer,human)
            board[move] = computer
        display_board(board)
        turn = next_turn(turn)
        the_winner = winner(board)
    congrat_winner(the_winner,computer,human)

main()


