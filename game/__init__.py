from game.board import Board


def play():
    print("Enter size of board, a single number")
    i = input()
    n = int(i)
    # n = 4
    players = 2
    new_board = Board(n)
    new_board.draw()
    new_board.start_game(players)
