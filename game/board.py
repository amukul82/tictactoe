class Board:
    def __init__(self, size):
        self.size = size
        self.mat = [[0] * size for _ in range(size)]

    def move(self, x, y, val):
        if 0 <= x < self.size and 0 <= y < self.size and not self.mat[x][y]:
            self.mat[x][y] = val
        else:
            raise Exception("invalid move")

    def is_solved(self):
        for i in range(self.size - 2):
            for j in range(self.size - 2):
                if self.mat[i][j] != 0 and self.mat[i][j] == self.mat[i][j+1] and self.mat[i][j] == self.mat[i][j+2] \
                    or self.mat[i][j] != 0 and self.mat[i][j] == self.mat[i+1][j] and self.mat[i][j] == self.mat[i+2][j] \
                    or self.mat[i][j] != 0 and self.mat[i][j] == self.mat[i+1][j+1] and self.mat[i][j] == self.mat[i+2][j+2]:
                    return True
        return False

    def draw(self):
        str1 = ""
        for i in range(self.size):
            str1 = ""
            for j in range(self.size):
                str1 = str1 + " ___"
            print(str1 + " ")
            str2 = ""
            for j in range(self.size):
                str2 = str2 + "| "
                if self.mat[i][j] != 0:
                    str2 = str2 + str(self.mat[i][j]) + " "
                else:
                    str2 = str2 + "  "
            print(str2 + "|")
        print(str1 + " ")

    def start_game(self, players):
        print("Let's play for ", players, " players")
        i = players % players
        moves = self.size * self.size
        solved = False
        while moves > 0 and not solved:
            print("Player ", i + 1, "'s move")
            try:
                d = input()
                move = d.split(" ")
                x, y = int(move[0]), int(move[1])
                print(x, y)
                self.move(x - 1, y - 1, i + 1)
            except Exception:
                print("move not allowed, try again")
                continue
            self.draw()
            solved = self.is_solved()
            i = (i + 1) % players
            moves = moves - 1
        if solved:
            print("Player ", ((i + 1) % players) + 1, "wins")
        else:
            print("Match drawn")
