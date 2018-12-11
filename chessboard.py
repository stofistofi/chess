# initializes a chess board on a comand line interface (CLI)
import os
from move_alg import move_alg

class Chessboard():
    def create_board(self):
        self.__board = { 0:'R',  1:'N',  2:'B',  3:'Q',  4:'K',  5:'B',  6:'N',  7:'R', 
                         8:'P',  9:'P', 10:'P', 11:'P', 12:'P', 13:'P', 14:'P', 15:'P',
                        16:' ', 17:' ', 18:' ', 19:' ', 20:' ', 21:' ', 22:' ', 23:' ',
                        24:' ', 25:' ', 26:' ', 27:' ', 28:' ', 29:' ', 30:' ', 31:' ',
                        32:' ', 33:' ', 34:' ', 35:' ', 36:' ', 37:' ', 38:' ', 39:' ',
                        40:' ', 41:' ', 42:' ', 43:' ', 44:' ', 45:' ', 46:' ', 47:' ',
                        48:'p', 49:'p', 50:'p', 51:'p', 52:'p', 53:'p', 54:'p', 55:'p',
                        56:'r', 57:'n', 58:'b', 59:'q', 60:'k', 61:'b', 62:'n', 63:'r'}

    def __init__(self):
        self.create_board()
    
    def __str__(self):
        boardString = ""
        c = 8
        for b in self.__board:
            if (b % 8 == 0):
                boardString = boardString + '\n' + '(' + str(c) + ')  '
                c -= 1
            boardString = boardString + '[' + self.__board[b] + ']'
        boardString = boardString + '\n \n' + '     (A)(B)(C)(D)(E)(F)(G)(H)'
        return str(boardString)
    
    def move_piece(self, move, destination):
        self.__board[destination] = self.__board[move]
        self.__board[move] = " "

    # reveal_piece is useful for testing
    def reveal_piece(self, key):
        return self.__board[key]

def main():
    os.system('clear')
    c = Chessboard()
    print(str(c))
    lower = False            # 0: White, lower, 1: Black, UPPER
    status = 1               # 1: in game, 0: game over

    while (status == 1):
        # toggle player
        lower = not lower
        if (lower): print("lower:")
        else: print("UPPER:")

        print("Move:")
        move = input()
        print("Destination:")
        destination = input()
        os.system('clear')
        c.move_piece(move_alg(move), move_alg(destination))
        print(str(c))

main()

'''
CLI:

(8)  [R][N][B][Q][K][B][N][R]
(7)  [P][P][P][P][P][P][P][P]
(6)  [ ][ ][ ][ ][ ][ ][ ][ ]
(5)  [ ][ ][ ][ ][ ][ ][ ][ ]
(4)  [ ][ ][ ][ ][ ][ ][ ][ ]
(3)  [ ][ ][p][ ][ ][ ][ ][ ]
(2)  [p][p][ ][p][p][p][p][p]
(1)  [r][n][b][q][k][b][n][r]

     (A)(B)(C)(D)(E)(F)(G)(H)

$ lower: c2 c3

(1)  [r][n][b][q][k][b][n][r]
(2)  [p][p][ ][p][p][p][p][p]
(3)  [ ][ ][p][ ][ ][ ][ ][ ]
(4)  [ ][ ][ ][ ][ ][ ][ ][ ]
(5)  [ ][ ][ ][ ][ ][ ][ ][ ]
(6)  [ ][ ][ ][ ][ ][ ][ ][ ]
(7)  [P][P][P][P][P][P][P][P]
(8)  [R][N][B][Q][K][B][N][R]

     (H)(G)(F)(E)(D)(C)(B)(A)

$ UPPER:
'''

'''
move(i, b):
    c2: 'p'
'''